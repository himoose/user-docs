# Docs Site Localization Plan

Bring `docs-site` to the same six languages as `marketing-site` and the desktop app:
`en`, `es`, `fr`, `de`, `it`, `pt`.

## Goal: launch-day is one button

Everything gets built and verified **locally**. Nothing is deployed until launch day,
when the docs go live alongside the new desktop app and marketing site.

On launch day Sam runs the deploy and the Worker cutover and otherwise ignores this repo.
Every decision below is made now so that nothing needs deciding then. The deploy steps
live in `LAUNCH_CHECKLIST.md`, not in this plan.

**Not in scope tonight:** `firebase deploy`, the Cloudflare Worker, the
`docs.himoose.com` 301, Search Console. All of it is Phase 6, all of it is launch day.

Consequence for verification: local builds must set `DOCS_BASE_URL=http://localhost:8000`.
The theme's `main.html` bakes `const base_url = "{{ config.site_url }}"` into every page,
and the search JS uses it to resolve result links. Build locally with the production URL
and every local search result links to a site that isn't live yet.

---

## 1. Decision: do not use `mkdocs-static-i18n`

The standard plugin is the wrong fit here. Three findings, all verified against the
installed packages and the plugin's source:

1. **It is frozen.** The upstream repo states: "Due to the core MkDocs upstream being
   unmaintained and uncertain, this project is frozen."
2. **It produces one shared search index for all languages.** `reconfigure.py` stacks
   every language's entries via `extend_search_entries()` into a single
   `search_index.json`, then only de-duplicates fallback pages. A Spanish reader would
   get English, French, and German hits back from the search dialog.
3. **Its theme integration is Material-only.** It sets `theme.locale` for the
   `mkdocs`/`readthedocs` themes and `theme.language` for Material. We are on
   `mkdocs-shadcn` 0.9.8, which gets neither. Its `main.html` hardcodes
   `<html lang="en">`. The language switcher is a Material feature (`extra.alternate`).

The plugin would give us file resolution and English fallback. We would still hand-build
the switcher, the `hreflang` cluster, and the `lang` attribute, and we would inherit a
broken search index.

**Instead: generate one MkDocs config per locale and build the site six times.**
Each build writes its own `search_index.json`, so search is correctly scoped for free.

---

## 2. Decisions

All settled 2026-07-09.

| # | Decision | Resolution | Why |
|---|---|---|---|
| D1 | Locale set | `en, es, fr, de, it, pt` | Matches `marketing-site/src/_data/locales.js` and `desktop-app/src/renderer/services/i18n/locales/` exactly. |
| D2 | URL shape | `<base>/es/getting-started/projects` | Mirrors the marketing site's `/es` prefix. Default language stays unprefixed at `<base>/`. |
| D3 | Canonical base URL | **`https://himoose.com/docs`**, `docs.himoose.com` retired with a 301 | One canonical URL, and docs inherit the marketing domain's authority. See §3. |
| D4 | Slugs | Keep English, untranslated | Keeps `firebase.json` redirects tractable, keeps cross-locale switching a pure prefix swap, avoids a slug-translation map. |
| D5 | Scope | All 41 pages, `docs/legacy/**` included but frozen | No English islands. Legacy English is never updated again, so those pages are translated once and exempted from drift checks (§8). |
| D6 | Stale translations | Ship with a banner; add `noindex` past a drift threshold | Fails soft on small edits, stops search engines indexing materially wrong content. See §8. |
| D7 | Sequencing | Localize first, then cut over to the Worker | Locale URLs are built once against the final base URL. No re-crawl. See §10. |

---

## 3. The canonical base URL (resolved: `himoose.com/docs`)

`mkdocs.yml` sets:

```yaml
site_url: https://himoose.com/docs/
```

But per `README-SAM.md`, the site is **live today at `docs.himoose.com`** via Firebase
Hosting, and the Cloudflare Worker that would reverse-proxy `himoose.com/docs/*` has
never been deployed. So every page currently emits a `<link rel="canonical">` pointing at
a URL that is not served.

This matters more once we add `hreflang`, because a `hreflang` cluster with URLs that
404 or that disagree with `canonical` is worse than no cluster at all. Search engines
drop the whole cluster.

**Resolution: `https://himoose.com/docs` is canonical. `docs.himoose.com` gets retired
with a 301 to it.** This settles the open question in `README-SAM.md`.

Consequence for sequencing (D7): the Worker that serves `himoose.com/docs/*` must exist
before we can honestly emit `hreflang` against those URLs, but we do not want to build
the locale URLs twice. So we build against the final base URL from day one and cut the
Worker over before the localized site goes public. Concretely, `hreflang` ships in Phase 2
but is only ever *served* from the final host.

Make the base URL a single build-time variable regardless:

```
DOCS_BASE_URL=https://himoose.com/docs     # canonical, per D3
```

Everything downstream (per-locale `site_url`, `hreflang`, switcher hrefs, sitemaps)
derives from it, so preview channels can point it elsewhere without editing configs.

Two things this now blocks on, both already scoped in `README-SAM.md`:

- The Worker `../platform/.workers-cloudflare/user-docs.js` must be deployed as a
  **zone-scoped Route**, not a Custom Domain. `wrangler.toml` in this folder is unwired
  boilerplate and must not be deployed as-is.
- The Worker's regex link-rewriting (`href="/..."` / `src="/..."`) needs re-checking
  against `/es/` paths. Setting `site_url` per locale means MkDocs bakes the correct
  prefix into canonical, sitemap, and search output at build time, so the rewrite should
  only ever be a fallback for plain root-relative links.

The 301 from `docs.himoose.com` needs to preserve the path, so
`docs.himoose.com/es/visibility/overview` lands on `himoose.com/docs/es/visibility/overview`.

---

## 4. Repo layout

```
docs-site/
  mkdocs.yml                  # base config, English, unchanged as the source of truth
  docs/                       # English markdown, unchanged (41 files, ~15,800 words)
  i18n/
    ui/
      en.yml                  # theme chrome strings ("Menu", "On This Page", ...)
      es.yml  fr.yml  de.yml  it.yml  pt.yml
    nav/
      es.yml  fr.yml  de.yml  it.yml  pt.yml     # nav title translations
    glossary/
      es.json fr.json de.json it.json pt.json    # generated from the desktop app
    es/                       # translated markdown, mirrors docs/ tree
      index.md
      getting-started/projects.md
      ...                     # only pages that have been translated
    fr/  de/  it/  pt/
  overrides/
    main.html                 # NEW: html lang attribute
    templates/
      seo.html                # NEW: hreflang cluster + og:locale
      header.html             # EXISTING: add language switcher, localize chrome
      search.html             # NEW: localize placeholder strings
      toc.html                # NEW: localize "On This Page"
      copy_button.html        # existing, untouched
      speculation_rules.html  # existing, untouched
  scripts/
    build_i18n.py             # generates configs, runs the six builds
    translate.py              # Claude-API translation with drift detection
    gen_glossary.py           # extracts UI nouns from the desktop app catalogs
    gen_redirects.py          # expands firebase.json redirects across locales
  build/                      # gitignored scratch
    docs-es/                  # English overlaid with i18n/es
    mkdocs.es.yml             # generated, never committed
  site/                       # published to Firebase
    index.html                # English at the root
    search/search_index.json
    es/index.html
    es/search/search_index.json
    fr/  de/  it/  pt/
```

`docs/` and `mkdocs.yml` stay exactly as they are. English authors never learn a new
workflow, which is the main reason to prefer this over restructuring into
`docs/en/`, `docs/es/`.

---

## 5. The build

`scripts/build_i18n.py` does four things per locale:

**Step 1 — Overlay for English fallback.**
Copy `docs/` to `build/docs-<lang>/`, then copy `i18n/<lang>/` over the top. Any page
not yet translated ships in English at the correct localized URL. This is the same
en-fallback pattern the marketing site uses in `src.11tydata.js`.

**Step 2 — Generate the config.** Read `mkdocs.yml`, then override:

```yaml
docs_dir: build/docs-es
site_dir: site/es
site_url: ${DOCS_BASE_URL}/es/
plugins:
  - search:
      lang: [es]              # lunr stemmer; es/fr/de/it/pt are all supported
      separator: '...'        # keep the existing custom separator
  - minify:
      minify_html: true
extra:
  locale: {code: es, tag: es, label: Español}
  languages: [ ... all six, with code/tag/label/prefix ... ]
  ui: { ...contents of i18n/ui/es.yml... }
nav: # base nav with titles replaced from i18n/nav/es.yml
```

Generate the whole config rather than using MkDocs `INHERIT:`. Inheritance merges
`plugins` and `nav` in ways that are easy to get subtly wrong, and the generated file is
trivial to inspect when something breaks.

**Step 3 — Build.**

```
python -m mkdocs build -f build/mkdocs.es.yml
```

**Step 4 — Order matters.** MkDocs cleans `site_dir` before writing.
The English build's `site_dir` is `site/`, so it would wipe `site/es/`.

> **Build English first, then the five locales.** Any other order silently deletes work.

Six sequential builds of a 41-page site is a few seconds. Not worth parallelizing.

---

## 6. Template overrides

`mkdocs-shadcn` has no locale support, so four templates need overriding. `custom_dir`
replaces a template by its relative path, so these are copy-then-edit, not `{% extends %}`.
That couples us to the theme version, which is already pinned at `mkdocs-shadcn==0.9.8`
in `requirements.txt`. **Leave it pinned**, and re-diff these four files on any upgrade.

| File | Change |
|---|---|
| `overrides/main.html` | `<html lang="en">` becomes `<html lang="{{ config.extra.locale.tag }}">`. This is the only place the attribute exists. |
| `overrides/templates/seo.html` | Append the `hreflang` cluster and `og:locale`. The existing `canonical` emission via `page.canonical_url` is already correct once `site_url` is per-locale. |
| `overrides/templates/header.html` | Add the language switcher. Localize `Menu`, `Toggle Menu`, `Toggle theme`, `Toggle layout` from `config.extra.ui`. |
| `overrides/templates/search.html` | Localize `Search documentation...` (twice: label and `placeholder`) and `Search...`. |
| `overrides/templates/toc.html` | Localize `On This Page`. |

That is the complete inventory of hardcoded English chrome in the theme. Eleven strings.

### hreflang cluster

Mirror `marketing-site/src/_includes/partials/head.njk`: self-referential (every page
lists every language including itself), plus `x-default` pointing at English.

Because of the fallback overlay in Step 1, **every page exists in every locale**, so the
cluster is always complete and the switcher never dead-ends. This is the quiet payoff of
the overlay approach.

In Jinja, the alternate for a given language is `${DOCS_BASE_URL}/<prefix>/{{ page.url }}`,
where `page.url` is the language-independent page path (`''` for the index). That is the
direct analogue of the marketing site's `basePermalink`.

### Language switcher

Port the markup semantics from `marketing-site/src/_includes/partials/nav.njk`: a
dropdown of links, each carrying `lang` and `hreflang` attributes, the current one marked
active with a visually-hidden status label, and an `aria-label` on the trigger. Style it
with the theme's existing shadcn button/popover classes so it matches the header.

Because slugs are untranslated (D4), the switcher href is a prefix swap on the current
page path. The reader stays on the page they were reading.

---

## 7. Search

Each locale build emits its own `site/<lang>/search/search_index.json`. No cross-language
result bleed.

Two details:

- The theme's `main.html` sets `const base_url = "{{ config.site_url }}"`, which the
  search JS uses to resolve result links. Per-locale `site_url` therefore makes search
  results resolve correctly inside each locale, with no JS changes. This is the second
  reason separate builds beat the single-build plugin.
- The built-in `search` plugin accepts a `lang` list mapping to lunr stemmers.
  `es`, `fr`, `de`, `it`, `pt` are all supported. Set it per locale for correct stemming.
  Keep the existing custom `separator` from `mkdocs.yml`.

---

## 8. Translation pipeline and drift

This is the real cost. Not the plumbing, which is roughly a day.

**41 files, ~15,800 words, times five languages, is ~79,000 words** to translate and then
keep from drifting. The marketing site has no translation script; those
`src/_data/i18n/*` modules were written by hand. We should not repeat that by hand at
four times the volume.

### `scripts/gen_glossary.py`

Run first, once. The desktop app already ships full catalogs for exactly our six
languages at `desktop-app/src/renderer/services/i18n/locales/*.json` (228KB for `es.json`).
Extract the UI nouns the docs refer to (Inbox is `Bandeja` in Spanish, not `Buzón`;
Visibility, Library, Prompt Manager, Brand Voice, and so on) into
`i18n/glossary/<lang>.json`.

Feed that glossary to the translator as a hard constraint. **A docs translation that
names a button differently from the button's actual label in the app is worse than no
translation.** This is the single highest-risk quality item in the plan.

Never translate: `Hi, Moose`, `Moose`, model names, code blocks, link targets, image
paths, `attr_list` braces, snippet includes. Translate the label text only inside
`=== "Tab"` markers and `!!! note "Title"` admonitions.

### `scripts/translate.py`

For each `docs/**/*.md` and each locale:

1. `source_hash = sha256(english_source)`.
2. If `i18n/<lang>/<path>` exists and its front-matter `source_hash` matches, skip.
3. Otherwise translate via the Claude API and write the file with front matter:
   `source_hash`, `translated_at`, `translator: claude-opus-4-8`.

Idempotent, resumable, and only re-translates what actually changed. Run it in CI on a
schedule or as a pre-release step, not on every commit.

### Drift (D6)

When `source_hash` no longer matches the English source, the translation is stale.
Resolution per D6: **ship it with a banner, and add `noindex` once drift is large.**

`build_i18n.py` knows the hash mismatch at overlay time, so it:

1. Injects an admonition at the top of the page: "This page may be out of date.
   View in English." The link points at the English page, not the English site root.
2. Computes a drift ratio (changed lines over total lines of the English source).
   Past a threshold, add `<meta name="robots" content="noindex">` to that page so search
   engines do not index materially wrong content. **Start the threshold at 0.25 and tune
   it once we see real drift**, since a guessed number here is not worth defending.

Note the interaction with `hreflang`: a `noindex`ed page should be dropped from the
cluster and from that locale's `sitemap.xml`, otherwise we are advertising a page we are
simultaneously telling crawlers to ignore. `check_i18n.py` (§11) must assert this.

`build_i18n.py` prints a staleness report on every run. CI fails if any page exceeds the
`noindex` threshold, since that means a translation has been neglected long enough to be
actively misleading.

Both the banner text and the "View in English" label are themselves localized, so they
belong in `i18n/ui/<lang>.yml` alongside the theme chrome strings.

---

## 9. Firebase and redirects

`site/` is already the published directory with `cleanUrls: true`, so nested `site/es/`
serves at `<base>/es/...` with **no hosting configuration change.**

The problem: the **24 redirects in `firebase.json` are English-path-only.** After this
change, `/es/features/podcast-generator` is a 404 rather than a redirect to
`/es/legacy/listen-to-this-article`.

`scripts/gen_redirects.py` should expand each rule across the five prefixes, keeping the
English rules as-is. Prefer explicit enumeration over Firebase's `:segment` capture: a
`/:lang/features/...` pattern matches *any* first segment and would silently produce
redirects into locales that do not exist. 24 rules becomes 144, generated, never
hand-edited. There is precedent for this in
`marketing-site/scripts/sync-download-redirects.cjs`.

**Sitemaps.** Each locale build emits its own `site/<lang>/sitemap.xml`. Add a post-build
step that writes a sitemap index at the site root referencing all six, and point Search
Console at that. Careful: the English build owns `site/sitemap.xml`, so the index needs a
distinct name (`sitemap_index.xml`) or it gets clobbered.

---

## 10. Sequencing

Each phase is independently verifiable and independently shippable. Per D7 the Worker
cutover lands late, but every build from Phase 1 onward already targets
`https://himoose.com/docs`, so no URL is ever built twice.

- **Phase 0 — Decisions.** DONE. D1-D7 settled 2026-07-09.
- **Phase 1 — Pipeline, no translations.** DONE. `scripts/build_i18n.py` builds all six
  locales; `scripts/check_i18n.py` verifies the output. 246 pages, 246 valid hreflang
  clusters, six independent search indexes. Every page currently English.
- **Phase 2 — Overrides.** DONE. `lang` attribute, hreflang cluster, language switcher,
  eleven chrome strings, stale banner, `noindex` + sitemap exclusion. Verified in a
  browser: switching locale on a deep page holds the path, and search inside `/de/`
  returns only that locale's index.
- **Phase 3 — NEXT.** Glossary and pilot locale.

Original phase descriptions follow.

- **Phase 1 (orig) — Pipeline, no translations.** `build_i18n.py` with English plus Spanish,
  where `i18n/es/` is empty so every Spanish page falls back to English. Proves URLs,
  build order, per-locale search, and the Firebase layout without a single word
  translated. This is the cheapest possible test of the riskiest structural assumptions.
- **Phase 2 — Overrides.** `lang` attribute, `hreflang`, switcher, eleven chrome strings.
  Still zero translated content. At the end of this phase the site is structurally
  multilingual and serving English everywhere.
- **Phase 3 — Glossary and pilot locale.** `gen_glossary.py`, then translate Spanish
  only, all 41 pages including `legacy/` per D5. Review it properly. Spanish is the right
  pilot: it is the largest audience and the easiest for us to sanity-check.
- **Phase 4 — Remaining four locales.** `fr`, `de`, `it`, `pt`.
- **Phase 5 — Redirects and sitemaps.** `gen_redirects.py`, sitemap index, Search Console.
- **Phase 6 — Worker cutover.** Deploy `../platform/.workers-cloudflare/user-docs.js` as a
  zone-scoped Route for `himoose.com/docs` and `himoose.com/docs/*`. Re-check its regex
  link-rewriting against `/es/` paths. Then 301 `docs.himoose.com/*` to
  `himoose.com/docs/*`, preserving the path. Only after this does the localized site go
  public.

Phases 1 and 2 are the day of plumbing. Phase 3 is where the real work and the real cost
sit. Phase 6 is the only phase that touches live serving infrastructure, and it is
deliberately last.

---

## 11. Verification

Per phase, before deploying:

```bash
# Full build, all six locales
DOCS_BASE_URL=https://himoose.com/docs python scripts/build_i18n.py

# Structural checks
python scripts/check_i18n.py     # hreflang reciprocity, lang attr, no 404 alternates
```

`check_i18n.py` should assert, over the built `site/`:

- every page emits `<html lang="...">` matching its locale
- every page's `hreflang` cluster is self-referential and reciprocal
- every `hreflang` href resolves to a file that exists on disk
- exactly one `x-default`, pointing at English
- `canonical` agrees with `site_url` for that locale
- `site/<lang>/search/search_index.json` exists and contains only that locale's pages
- switcher hrefs preserve the current page path
- any `noindex`ed stale page is absent from both the `hreflang` cluster and its
  locale's `sitemap.xml` (§8)

Then a preview deploy. **I will not run `firebase deploy`.** The command for Sam:

```bash
cd docs-site
firebase hosting:channel:deploy i18n-preview --project himoose-user-docs --expires 7d
```

Check on the preview URL: switch language on a deep page and confirm you land on the same
page; search inside `/es/` and confirm no English results; view source and confirm the
`hreflang` cluster and `lang` attribute.

---

## 12. Risks

| Risk | Mitigation |
|---|---|
| Glossary drift between docs and app UI labels | Generate the glossary from the app's own catalogs; regenerate whenever the app's `locales/*.json` change. |
| Theme upgrade breaks the four overridden templates | `mkdocs-shadcn` is pinned at `0.9.8`. Re-diff the overrides on any bump. |
| Wrong build order silently wipes locales | English first. Assert in `build_i18n.py` that `site/<lang>/` is non-empty after the full run. |
| Localized site goes public before the Worker route exists | D7 puts the cutover last. `hreflang` is built against `himoose.com/docs` from Phase 1, but nothing is announced until Phase 6. |
| `docs.himoose.com` 301 drops the path and dumps everyone on the docs index | Assert path preservation on a localized deep link before retiring the subdomain. |
| Translation cost and drift accumulate unmanaged | `source_hash` drift report in CI; stale-page banner; `noindex` past a threshold; scheduled re-translation. |
| The plugin looks easier and someone reaches for it later | This document. See §1. |
