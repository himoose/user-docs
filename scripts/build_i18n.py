"""Build the docs site once per locale.

We deliberately do NOT use mkdocs-static-i18n. See DOCS_I18N_PLAN.md section 1:
it is frozen upstream, it merges every language into one search index, and its
theme integration is Material-only (we are on mkdocs-shadcn).

Instead: for each locale, overlay the translations on top of the English docs,
generate a config, and run a normal `mkdocs build`. Each build writes its own
search index, so search never bleeds across languages.

Usage:
    DOCS_BASE_URL=http://localhost:8000 python scripts/build_i18n.py
    DOCS_BASE_URL=http://localhost:8000 python scripts/build_i18n.py --only en,es

The default base URL is the production one, so a bare run produces exactly what
launch day should publish.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"
BUILD = ROOT / "build"
SITE = ROOT / "site"

PROD_BASE_URL = "https://himoose.com/docs"

# Past this much drift between the English source at translation time and the
# English source now, the translated page is not merely stale but likely wrong,
# so we stop search engines indexing it. Starting value, tune once we have real
# drift data -- see DOCS_I18N_PLAN.md section 8.
NOINDEX_DRIFT_THRESHOLD = 0.25

# lunr stemmer languages. All five of our non-English locales are supported.
LUNR_LANGS = {"en", "es", "fr", "de", "it", "pt"}

FRONT_MATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


# --------------------------------------------------------------------------
# front matter


def split_front_matter(text: str) -> tuple[dict, str]:
    """Return (front_matter_dict, body). Absent front matter yields ({}, text)."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    meta = yaml.safe_load(match.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("front matter is not a mapping")
    return meta, text[match.end():]


def join_front_matter(meta: dict, body: str) -> str:
    if not meta:
        return body
    dumped = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{dumped}\n---\n{body}"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def md_to_url(rel_posix: str) -> str:
    """docs-relative markdown path -> mkdocs page.url (use_directory_urls)."""
    stem = rel_posix.removesuffix(".md")
    if stem == "index":
        return ""
    if stem.endswith("/index"):
        stem = stem.removesuffix("/index")
    return f"{stem}/"


# --------------------------------------------------------------------------
# config


def load_locales() -> dict:
    with open(I18N / "locales.yml", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_base_config() -> dict:
    with open(ROOT / "mkdocs.yml", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_yaml_if_exists(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def deep_merge(base: dict, override: dict) -> dict:
    """Override wins. Used to fall back to English UI strings."""
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def missing_ui_keys(english: dict, localized: dict, prefix: str = "") -> list[str]:
    missing = []
    for key, value in english.items():
        path = f"{prefix}{key}"
        if key not in localized:
            missing.append(path)
        elif isinstance(value, dict) and isinstance(localized[key], dict):
            missing.extend(missing_ui_keys(value, localized[key], f"{path}."))
    return missing


# --------------------------------------------------------------------------
# nav


def translate_nav(nav, titles: dict):
    """Walk the mkdocs nav, replacing English section/page titles via `titles`."""
    if isinstance(nav, list):
        return [translate_nav(item, titles) for item in nav]
    if isinstance(nav, dict):
        return {
            titles.get(key, key): translate_nav(value, titles)
            for key, value in nav.items()
        }
    return nav


def nav_titles(nav, found: set) -> set:
    """Collect every title in the nav, so we can report untranslated ones."""
    if isinstance(nav, list):
        for item in nav:
            nav_titles(item, found)
    elif isinstance(nav, dict):
        for key, value in nav.items():
            found.add(key)
            nav_titles(value, found)
    return found


# --------------------------------------------------------------------------
# overlay


def drift_ratio(old_source: str, new_source: str) -> float:
    """1.0 means totally rewritten, 0.0 means identical."""
    matcher = difflib.SequenceMatcher(None, old_source, new_source, autojunk=False)
    return 1.0 - matcher.ratio()


def stale_banner(ui: dict, english_url: str) -> str:
    stale = ui.get("stale", {})
    title = stale.get("title", "This page may be out of date")
    body = stale.get("body", "")
    link_label = stale.get("linkLabel", "View in English")
    return (
        f'!!! warning "{title}"\n'
        f"    {body}\n\n"
        f"    [{link_label}]({english_url})\n\n"
    )


def machine_translated_notice(ui: dict, english_url: str) -> str:
    """Shown on every page that actually has a translation."""
    notice = ui.get("machineTranslated", {})
    title = notice.get("title", "Machine translated")
    body = notice.get("body", "")
    link_label = notice.get("linkLabel", "Read it in English")
    return (
        f'!!! note "{title}"\n'
        f"    {body}\n\n"
        f"    [{link_label}]({english_url})\n\n"
    )


def not_translated_notice(ui: dict) -> str:
    """Shown when a page falls back to English inside a localized section.

    Such a page is NOT machine-translated, so it must not carry the
    machine-translation notice. Saying "translated by AI" above untouched English
    prose would be a lie, and the reader would have no idea which claim to trust.
    """
    notice = ui.get("notTranslated", {})
    title = notice.get("title", "Not translated yet")
    body = notice.get("body", "")
    return f'!!! info "{title}"\n    {body}\n\n'


def build_overlay(lang: str, ui: dict, frozen: set[str], base_url: str, is_default: bool) -> dict:
    """Copy English docs into build/docs-<lang>, then overlay translations.

    Untranslated pages ship in English at the localized URL. Stale translations
    ship with a banner, and are marked noindex once drift crosses the threshold.

    Returns a report: {"translated": n, "english": n, "stale": [...], "noindex": [...]}
    """
    target = BUILD / f"docs-{lang}"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(DOCS, target)

    report = {"translated": 0, "english": 0, "stale": [], "noindex": [], "orphans": []}

    locale_dir = I18N / lang
    translated_paths: set[str] = set()

    if locale_dir.exists():
        translated_paths = {
            str(p.relative_to(locale_dir)).replace("\\", "/")
            for p in locale_dir.rglob("*.md")
            if p.relative_to(locale_dir).parts[:1] != ("_sources",)
        }

    def mark_english_fallbacks() -> None:
        """Label every page in a localized section that is still English."""
        if is_default:
            return
        for english_path in sorted(DOCS.rglob("*.md")):
            rel_posix = str(english_path.relative_to(DOCS)).replace("\\", "/")
            if rel_posix in translated_paths:
                continue
            copied = target / english_path.relative_to(DOCS)
            meta, body = split_front_matter(copied.read_text(encoding="utf-8"))
            copied.write_text(join_front_matter(meta, not_translated_notice(ui) + body), encoding="utf-8")

    if not locale_dir.exists():
        mark_english_fallbacks()
        report["english"] = len(list(DOCS.rglob("*.md")))
        return report

    snapshots = locale_dir / "_sources"

    for translated in sorted(locale_dir.rglob("*.md")):
        rel = translated.relative_to(locale_dir)
        if rel.parts and rel.parts[0] == "_sources":
            continue

        english_path = DOCS / rel
        if not english_path.exists():
            # A translation whose English source was deleted or renamed. Do not
            # ship it: it would be an orphan page reachable by URL but absent
            # from the nav and from every other locale.
            report["orphans"].append(str(rel).replace("\\", "/"))
            continue

        english_source = english_path.read_text(encoding="utf-8")
        meta, body = split_front_matter(translated.read_text(encoding="utf-8"))

        rel_posix = str(rel).replace("\\", "/")
        is_frozen = rel_posix in frozen
        recorded = meta.get("source_hash")
        current = sha256(english_source)

        # Absolute, not root-relative: the docs are served from a subpath
        # (himoose.com/docs/), so "/inbox/overview" would escape the site.
        english_url = f"{base_url}/{md_to_url(rel_posix)}"
        notices = ""

        if recorded and recorded != current and not is_frozen:
            report["stale"].append(rel_posix)

            snapshot = snapshots / rel
            if snapshot.exists():
                ratio = drift_ratio(snapshot.read_text(encoding="utf-8"), english_source)
                if ratio >= NOINDEX_DRIFT_THRESHOLD:
                    meta["noindex"] = True
                    report["noindex"].append(rel_posix)

            notices += stale_banner(ui, english_url)

        # Every genuinely translated page says so, per the machine-translation
        # disclosure decision. English-fallback pages get a different notice, in
        # mark_english_fallbacks() -- they were never translated.
        if not is_default:
            notices += machine_translated_notice(ui, english_url)

        (target / rel).write_text(join_front_matter(meta, notices + body), encoding="utf-8")
        report["translated"] += 1

    mark_english_fallbacks()
    report["english"] = len(list(DOCS.rglob("*.md"))) - report["translated"]
    return report


# --------------------------------------------------------------------------
# per-locale config


def generate_config(
    lang: str,
    locales: dict,
    base: dict,
    base_url: str,
    ui: dict,
    noindex_pages: dict[str, list[str]],
) -> Path:
    language = next(l for l in locales["languages"] if l["code"] == lang)
    is_default = lang == locales["default"]

    config = dict(base)
    config["docs_dir"] = str((BUILD / f"docs-{lang}").resolve())
    config["site_dir"] = str((SITE if is_default else SITE / lang).resolve())
    config["site_url"] = f"{base_url}{language['prefix']}/"
    config["theme"] = dict(base["theme"])
    config["theme"]["custom_dir"] = str((ROOT / "overrides").resolve())

    site_meta = ui.get("site", {})
    if site_meta.get("name"):
        config["site_name"] = site_meta["name"]
    if site_meta.get("description"):
        config["site_description"] = site_meta["description"]

    if not is_default:
        titles = load_yaml_if_exists(I18N / "nav" / f"{lang}.yml")
        config["nav"] = translate_nav(base["nav"], titles)

    # Rebuild the plugin list so search gets this locale's stemmer. The base
    # config's custom `separator` is preserved.
    plugins = []
    for plugin in base.get("plugins", []):
        if isinstance(plugin, dict) and "search" in plugin:
            search = dict(plugin["search"] or {})
            if lang in LUNR_LANGS:
                search["lang"] = [lang]
            plugins.append({"search": search})
        else:
            plugins.append(plugin)
    config["plugins"] = plugins

    extra = dict(base.get("extra", {}))
    extra["base_url"] = base_url
    extra["locale"] = language
    extra["languages"] = locales["languages"]
    extra["default_language"] = locales["default"]
    extra["ui"] = ui
    # Every locale's noindex set, not just this one. A page that is noindexed in
    # Spanish must not be advertised as the Spanish alternate from the English
    # page either, or we tell crawlers to both follow and ignore the same URL.
    # Only the full cross-locale map makes that possible, which is why overlays
    # for every locale run before any build does.
    extra["noindex_pages"] = noindex_pages
    config["extra"] = extra

    BUILD.mkdir(parents=True, exist_ok=True)
    path = BUILD / f"mkdocs.{lang}.yml"
    with open(path, "w", encoding="utf-8") as handle:
        yaml.safe_dump(config, handle, allow_unicode=True, sort_keys=False)
    return path


# --------------------------------------------------------------------------
# main


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="comma-separated locale codes, e.g. en,es")
    parser.add_argument("--strict", action="store_true", help="fail on any warning")
    parser.add_argument(
        "--partial",
        action="store_true",
        help="allow --only to omit locales, accepting that hreflang will advertise "
        "locales that were not built. Never use for a deploy.",
    )
    args = parser.parse_args()

    base_url = os.environ.get("DOCS_BASE_URL", PROD_BASE_URL).rstrip("/")
    locales = load_locales()
    base = load_base_config()
    frozen = set(locales.get("frozen", []))

    codes = [l["code"] for l in locales["languages"]]
    if args.only:
        requested = [c.strip() for c in args.only.split(",")]
        unknown = set(requested) - set(codes)
        if unknown:
            print(f"error: unknown locale(s): {', '.join(sorted(unknown))}", file=sys.stderr)
            return 1
        codes = [c for c in codes if c in requested]

    # The hreflang cluster is rendered from locales.yml, not from the set of
    # locales this run happens to build. So a partial build emits alternates
    # pointing at directories that do not exist. Fine for iterating, fatal if
    # deployed.
    omitted = [l["code"] for l in locales["languages"] if l["code"] not in codes]
    if omitted and not args.partial:
        print(
            f"error: --only omits {', '.join(omitted)}, but every page's hreflang cluster "
            f"still advertises them. Deploying this would advertise URLs that 404.\n"
            f"       Pass --partial if you are iterating locally and know this.",
            file=sys.stderr,
        )
        return 1

    default = locales["default"]
    if default not in codes:
        # The default build owns site/ and cleans it, so it cannot be skipped
        # when other locales are being written into site/<lang>.
        print(f"error: the default locale '{default}' must be included in --only", file=sys.stderr)
        return 1

    # CRITICAL: the default locale builds into site/, and mkdocs cleans site_dir
    # before writing. Building it after the others would delete site/es, site/fr,
    # and so on. Default first, always.
    codes = [default] + [c for c in codes if c != default]

    english_ui = load_yaml_if_exists(I18N / "ui" / "en.yml")
    warnings: list[str] = []

    print(f"base url: {base_url}")
    print(f"locales:  {', '.join(codes)}\n")

    # Pass 1: overlay every locale, so we know the full cross-locale noindex map
    # before any hreflang cluster gets rendered.
    uis: dict[str, dict] = {}
    reports: dict[str, dict] = {}
    noindex_pages: dict[str, list[str]] = {}

    for lang in codes:
        ui = english_ui
        if lang != "en":
            localized = load_yaml_if_exists(I18N / "ui" / f"{lang}.yml")
            missing = missing_ui_keys(english_ui, localized)
            if missing:
                warnings.append(f"[{lang}] untranslated UI strings: {', '.join(missing)}")
            ui = deep_merge(english_ui, localized)

        uis[lang] = ui
        report = build_overlay(lang, ui, frozen, base_url, lang == default)
        reports[lang] = report
        noindex_pages[lang] = [md_to_url(p) for p in report["noindex"]]

        if lang != "en":
            titles = load_yaml_if_exists(I18N / "nav" / f"{lang}.yml")
            untranslated = sorted(nav_titles(base["nav"], set()) - set(titles))
            if untranslated:
                warnings.append(f"[{lang}] untranslated nav titles: {len(untranslated)}")

        for orphan in report["orphans"]:
            warnings.append(f"[{lang}] orphan translation, no English source: {orphan}")
        for stale in report["stale"]:
            warnings.append(f"[{lang}] stale, banner shown: {stale}")
        for page in report["noindex"]:
            warnings.append(f"[{lang}] drift past threshold, noindex: {page}")

    # Pass 2: build. Default locale first -- see the ordering note above.
    for lang in codes:
        config_path = generate_config(lang, locales, base, base_url, uis[lang], noindex_pages)

        result = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "-f", str(config_path)],
            cwd=ROOT,
        )
        if result.returncode != 0:
            print(f"\nerror: mkdocs build failed for '{lang}'", file=sys.stderr)
            return result.returncode

        site_dir = SITE if lang == default else SITE / lang
        if not (site_dir / "index.html").exists():
            print(f"\nerror: '{lang}' produced no index.html in {site_dir}", file=sys.stderr)
            return 1

        report = reports[lang]
        print(
            f"  {lang}: {report['translated']} translated, "
            f"{report['english']} English fallback, "
            f"{len(report['stale'])} stale\n"
        )

    # Guard against the build-order bug above ever regressing silently.
    for lang in codes:
        if lang == default:
            continue
        if not (SITE / lang / "index.html").exists():
            print(
                f"error: site/{lang}/index.html is missing after the full run. "
                f"The default locale build cleaned site/ and wiped it.",
                file=sys.stderr,
            )
            return 1

    # Sitemap index referencing every locale's sitemap (see DOCS_I18N_PLAN §9).
    # Each locale build emits its own sitemap.xml; nothing ties them together
    # for Search Console without this. The index needs a name other than
    # sitemap.xml because the default locale build owns site/sitemap.xml.
    # No leading whitespace before the XML declaration -- it must be the
    # first bytes of the file or strict parsers reject the document.
    index_entries = []
    for lang in codes:
        prefix = "" if lang == default else f"/{lang}"
        sitemap_file = (SITE if lang == default else SITE / lang) / "sitemap.xml"
        if not sitemap_file.exists():
            print(f"error: {sitemap_file} missing, sitemap index would 404", file=sys.stderr)
            return 1
        index_entries.append(
            f"    <sitemap>\n"
            f"        <loc>{base_url}{prefix}/sitemap.xml</loc>\n"
            f"    </sitemap>"
        )
    (SITE / "sitemap_index.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(index_entries)
        + "\n</sitemapindex>\n",
        encoding="utf-8",
    )
    print(f"sitemap index: {len(index_entries)} locale sitemap(s) in site/sitemap_index.xml")

    # Real <lastmod> dates and the IndexNow queue (see scripts/stamp-lastmod.cjs).
    # MkDocs stamps every page with the build time, so without this every deploy
    # claims the whole manual changed. Skipped on partial or non-production
    # builds: the manifest tracks the full production site, and stamping a
    # subset would drop the missing locales and resubmit them on the next full
    # build.
    if args.only:
        print("lastmod: skipped, --only builds a subset of the site")
    elif base_url != PROD_BASE_URL:
        print(f"lastmod: skipped, base URL is {base_url}")
    else:
        stamp = subprocess.run(
            ["node", str(ROOT / "scripts" / "stamp-lastmod.cjs")],
            cwd=ROOT,
        )
        if stamp.returncode != 0:
            print("error: lastmod stamping failed", file=sys.stderr)
            return 1

    if warnings:
        print("warnings:")
        for warning in warnings:
            print(f"  {warning}")
        if args.strict:
            print("\nerror: --strict and there were warnings", file=sys.stderr)
            return 1

    print(f"\nbuilt {len(codes)} locale(s) into {SITE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
