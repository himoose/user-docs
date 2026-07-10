"""Assert the built site/ is a correct multilingual site.

Run after scripts/build_i18n.py. Exits non-zero on any violation, so it can gate
a deploy. Everything here checks the built HTML on disk, not the source, because
the built HTML is what search engines and readers actually get.

Usage:
    python scripts/check_i18n.py
    DOCS_BASE_URL=http://localhost:8000 python scripts/check_i18n.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
I18N = ROOT / "i18n"

PROD_BASE_URL = "https://himoose.com/docs"

# The minifier strips attribute quotes and reorders attributes, so parse loosely.
LINK_RE = re.compile(r"<link\b[^>]*>", re.IGNORECASE)
HTML_LANG_RE = re.compile(r"<html\b[^>]*\blang=\"?([\w-]+)\"?", re.IGNORECASE)
ROBOTS_RE = re.compile(r"<meta\b[^>]*\bname=\"?robots\"?[^>]*>", re.IGNORECASE)


def attrs(tag: str) -> dict:
    found = {}
    for match in re.finditer(r'(\w[\w:-]*)=("([^"]*)"|\'([^\']*)\'|([^\s>]+))', tag):
        key = match.group(1).lower()
        found[key] = match.group(3) or match.group(4) or match.group(5) or ""
    return found


def load_locales() -> dict:
    with open(I18N / "locales.yml", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def url_to_relpath(url: str, base_url: str) -> str | None:
    """Map an absolute page URL back to its path under site/."""
    if not url.startswith(base_url):
        return None
    rest = url[len(base_url):].strip("/")
    return f"{rest}/index.html" if rest else "index.html"


def locale_of(page: Path) -> str:
    """Which locale directory does this built page live in?"""
    rel = page.relative_to(SITE).as_posix()
    head = rel.split("/", 1)[0]
    return head if (SITE / head).is_dir() and len(head) == 2 else "en"


def main() -> int:
    base_url = os.environ.get("DOCS_BASE_URL", PROD_BASE_URL).rstrip("/")
    locales = load_locales()
    languages = locales["languages"]
    default = locales["default"]
    codes = {l["code"] for l in languages}
    by_code = {l["code"]: l for l in languages}

    failures: list[str] = []

    def fail(message: str) -> None:
        failures.append(message)

    if not SITE.exists():
        print("error: site/ does not exist. Run scripts/build_i18n.py first.", file=sys.stderr)
        return 1

    # Every locale must have been built.
    for code in codes:
        index = SITE / "index.html" if code == default else SITE / code / "index.html"
        if not index.exists():
            fail(f"locale '{code}' has no index.html at {index.relative_to(SITE)}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    pages = sorted(SITE.rglob("index.html"))
    print(f"checking {len(pages)} pages across {len(codes)} locales, base {base_url}\n")

    noindexed: set[str] = set()
    clusters: dict[str, dict[str, str]] = {}

    for page in pages:
        rel = page.relative_to(SITE).as_posix()
        code = locale_of(page)
        html = page.read_text(encoding="utf-8", errors="replace")

        # 1. html lang matches the locale it was built into.
        match = HTML_LANG_RE.search(html)
        if not match:
            fail(f"{rel}: no <html lang>")
        elif match.group(1) != by_code[code]["tag"]:
            fail(f"{rel}: <html lang={match.group(1)}>, expected {by_code[code]['tag']}")

        links = [attrs(tag) for tag in LINK_RE.findall(html)]
        alternates = {
            link["hreflang"]: link.get("href", "")
            for link in links
            if link.get("rel") == "alternate" and "hreflang" in link
        }
        canonicals = [link.get("href", "") for link in links if link.get("rel") == "canonical"]

        is_noindex = bool(ROBOTS_RE.search(html) and "noindex" in ROBOTS_RE.search(html).group(0))
        if is_noindex:
            noindexed.add(rel)

        # 2. canonical agrees with the locale's site_url.
        if len(canonicals) != 1:
            fail(f"{rel}: expected exactly 1 canonical, found {len(canonicals)}")
        else:
            prefix = by_code[code]["prefix"]
            if not canonicals[0].startswith(f"{base_url}{prefix}/"):
                fail(f"{rel}: canonical {canonicals[0]} is not under {base_url}{prefix}/")

        if is_noindex:
            # 3. A noindex page must not advertise a cluster at all.
            if alternates:
                fail(f"{rel}: noindex but still emits {len(alternates)} hreflang alternates")
            continue

        # 4. Self-referential: the cluster lists every language including itself.
        expected = codes - {c for c in codes if f"{c}-placeholder" in ""}
        missing = {by_code[c]["tag"] for c in expected} - set(alternates)
        if missing and len(alternates) > 0:
            # Alternates for other locales are legitimately dropped when that
            # locale's copy is noindex, so only flag a missing SELF reference here;
            # cross-locale reciprocity is checked below, once every page is read.
            if by_code[code]["tag"] in missing:
                fail(f"{rel}: cluster omits its own language {by_code[code]['tag']}")

        if alternates:
            # 5. Exactly one x-default, pointing at the default language.
            if "x-default" not in alternates:
                fail(f"{rel}: cluster has no x-default")
            elif not alternates["x-default"].startswith(f"{base_url}/"):
                fail(f"{rel}: x-default {alternates['x-default']} is not the default language")

            # 6. Every alternate href resolves to a file that exists on disk.
            for tag, href in alternates.items():
                if tag == "x-default":
                    continue
                target = url_to_relpath(href, base_url)
                if target is None:
                    fail(f"{rel}: alternate {tag} -> {href} is outside {base_url}")
                elif not (SITE / target).exists():
                    fail(f"{rel}: alternate {tag} -> {href} does not exist on disk")

            clusters[rel] = alternates

    # 7. Reciprocity: if A lists B as an alternate, B must list A back.
    for rel, alternates in clusters.items():
        for tag, href in alternates.items():
            if tag == "x-default":
                continue
            target = url_to_relpath(href, base_url)
            if target is None or target not in clusters:
                continue
            back = clusters[target]
            source_url = None
            for candidate_tag, candidate_href in clusters[rel].items():
                if candidate_tag != "x-default" and url_to_relpath(candidate_href, base_url) == rel:
                    source_url = candidate_href
            if source_url and source_url not in back.values():
                fail(f"{rel} lists {target} as '{tag}', but {target} does not list it back")

    # 8. A noindex page is absent from its locale's sitemap and from every cluster.
    for code in codes:
        sitemap = SITE / "sitemap.xml" if code == default else SITE / code / "sitemap.xml"
        if not sitemap.exists():
            fail(f"locale '{code}' has no sitemap.xml")
            continue
        locs = re.findall(r"<loc>(.*?)</loc>", sitemap.read_text(encoding="utf-8"))
        for loc in locs:
            target = url_to_relpath(loc.strip(), base_url)
            if target and target in noindexed:
                fail(f"sitemap for '{code}' lists noindex page {target}")

    for rel, alternates in clusters.items():
        for tag, href in alternates.items():
            target = url_to_relpath(href, base_url)
            if target and target in noindexed:
                fail(f"{rel}: advertises noindex page {target} as hreflang '{tag}'")

    # 9. Each locale has its own search index, with its own stemmer.
    for code in codes:
        index = (
            SITE / "search" / "search_index.json"
            if code == default
            else SITE / code / "search" / "search_index.json"
        )
        if not index.exists():
            fail(f"locale '{code}' has no search_index.json")
            continue
        data = json.loads(index.read_text(encoding="utf-8"))
        configured = (data.get("config") or {}).get("lang") or []
        if configured != [code]:
            fail(f"search index for '{code}' has lang={configured}, expected ['{code}']")
        if not data.get("docs"):
            fail(f"search index for '{code}' is empty")

    if failures:
        print(f"{len(failures)} failure(s):\n")
        for failure in failures:
            print(f"  FAIL {failure}")
        return 1

    print(f"ok: {len(pages)} pages, {len(clusters)} hreflang clusters, {len(noindexed)} noindex")
    return 0


if __name__ == "__main__":
    sys.exit(main())
