# Docs Site Launch Checklist

Everything below is deliberately deferred to launch day. Nothing here has been run.

Read `DOCS_I18N_PLAN.md` first if you need the reasoning. This file is just the buttons.

---

## Before launch day

- [ ] Translations exist for `es`, `fr`, `de`, `it`, `pt` (Phase 3-4 of the plan)
- [ ] `python scripts/build_i18n.py --strict` passes with no warnings
- [ ] `python scripts/check_i18n.py` passes
- [ ] `firebase.json` redirects expanded across locales (`scripts/gen_redirects.py`, Phase 5)
- [ ] Sitemap index generated (Phase 5)

## Launch day

### 1. Build against the production URL

The default base URL is already production, so no environment variable is needed.

```bash
cd docs-site
python scripts/build_i18n.py --strict
python scripts/check_i18n.py
```

`--strict` fails on untranslated nav titles, untranslated UI strings, orphaned
translations, and stale pages. Do not deploy past a failure.

Both commands must pass before anything below runs.

### 2. Deploy Firebase Hosting

```bash
cd docs-site
firebase deploy --only hosting --project himoose-user-docs
```

At this point the localized site is live at `himoose-user-docs.web.app` and at
`docs.himoose.com`, but **not** yet at `himoose.com/docs/`. The `hreflang` and
`canonical` tags all point at `himoose.com/docs/`, which does not resolve yet.
That is expected and lasts only until step 3. Do not leave it in this state.

### 3. Cut the Cloudflare Worker over

Per `README-SAM.md`:

- [ ] Copy `../platform/.workers-cloudflare/user-docs.js` into the Cloudflare Worker editor.
      Do **not** deploy this folder's `wrangler.toml`: placeholder `account_id`, a
      `main` that does not exist, and `custom_domain = true` where a zone-scoped
      Route is required.
- [ ] Set the Worker's `FIREBASE_HOSTING_URL` env var to `https://himoose-user-docs.web.app`
- [ ] In the `himoose.com` Cloudflare zone, add a **Route** (not a Custom Domain) for
      `himoose.com/docs` and `himoose.com/docs/*`
- [ ] Re-check the Worker's regex link-rewriting against `/es/` paths. It rewrites only
      `href="/..."` and `src="/..."`. Canonical, `og:url`, sitemap, and the search index
      are already correct because `site_url` is baked in per locale at build time.

Verify before moving on:

```bash
curl -sI https://himoose.com/docs/es/visibility/overview | head -1   # expect 200
curl -s  https://himoose.com/docs/es/ | grep -o '<html lang=[^ >]*'  # expect es
```

### 4. Retire the subdomain

- [ ] 301 `docs.himoose.com/*` to `himoose.com/docs/*`, **preserving the path**

A path-dropping redirect that dumps every deep link on the docs index is the easy
mistake here. Check a localized deep link specifically:

```bash
curl -sI https://docs.himoose.com/es/visibility/overview | grep -i location
# expect: https://himoose.com/docs/es/visibility/overview
```

### 5. Search Console

- [ ] Submit `https://himoose.com/docs/sitemap_index.xml`
- [ ] Confirm the `hreflang` cluster is picked up (International Targeting report)
- [ ] Leave `docs.himoose.com` verified for long enough to watch the 301s drain

---

## Rollback

Firebase Hosting keeps prior releases. To roll back the docs content:

```bash
firebase hosting:rollback --project himoose-user-docs
```

To roll back the URL move, delete the Cloudflare Route and remove the
`docs.himoose.com` 301. The site returns to serving from the subdomain, but every page
still emits `canonical`/`hreflang` pointing at `himoose.com/docs/`. Rebuild with
`DOCS_BASE_URL=https://docs.himoose.com` if the rollback is going to last more than a
few hours, or search engines will start dropping pages.

---

## Notes

- **Sam runs the deploys.** These commands are here to be copied, not automated.
- The `OS-specific separator '\'` warnings during the build are a pre-existing
  `mkdocs-shadcn` bug on Windows (`raw_markdown_url` is built with `os.sep`). They are
  harmless: mkdocs normalizes the path. They appear with zero overrides applied.
