const fs = require('node:fs');
const path = require('node:path');
const zlib = require('node:zlib');
const crypto = require('node:crypto');

const docsRoot = path.join(__dirname, '..');
const siteDir = path.join(docsRoot, 'site');
const indexPath = path.join(siteDir, 'sitemap_index.xml');
const manifestPath = path.join(docsRoot, 'sitemap-lastmod.json');
const pendingPath = path.join(docsRoot, '.indexnow-pending.json');

const config = require(path.join(docsRoot, 'indexnow.json'));
const baseUrl = config.baseUrl.replace(/\/+$/, '');

function today() {
  return new Date().toISOString().slice(0, 10);
}

function localFileFor(url, suffix) {
  if (!url.startsWith(`${baseUrl}/`) && url !== baseUrl) {
    return null;
  }
  const rel = url.slice(baseUrl.length).replace(/^\/+/, '');
  return suffix ? path.join(siteDir, rel) : path.join(siteDir, rel, 'index.html');
}

function readManifest() {
  try {
    const parsed = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
    if (parsed && typeof parsed === 'object' && parsed.pages) {
      return parsed.pages;
    }
  } catch {
    /* first run */
  }
  return null;
}

function writeManifest(pages) {
  const sorted = {};
  for (const key of Object.keys(pages).sort()) {
    sorted[key] = pages[key];
  }
  fs.writeFileSync(
    manifestPath,
    `${JSON.stringify({ version: 1, pages: sorted }, null, 2)}\n`,
    'utf8',
  );
}

function fail(message) {
  console.error(`stamp-lastmod: ${message}`);
  process.exit(1);
}

if (!fs.existsSync(indexPath)) {
  fail(`no sitemap index at ${path.relative(docsRoot, indexPath)} — build the docs first`);
}

const indexXml = fs.readFileSync(indexPath, 'utf8');

const localeYml = fs.readFileSync(path.join(docsRoot, 'i18n', 'locales.yml'), 'utf8');
const expectedLocales = [...localeYml.matchAll(/^ {2}- code:\s*(\S+)/gm)].map((m) => m[1]);
if (expectedLocales.length === 0) {
  fail('could not read the locale list from i18n/locales.yml');
}
if (([...indexXml.matchAll(/<loc>/g)]).length !== expectedLocales.length) {
  console.log(
    `stamp-lastmod: the sitemap index lists ${[...indexXml.matchAll(/<loc>/g)].length} of ${expectedLocales.length} locales — this is a partial build, skipping so the manifest keeps tracking the full site`,
  );
  process.exit(0);
}

const sitemapFiles = [];
for (const match of indexXml.matchAll(/<loc>([^<]+)<\/loc>/g)) {
  const file = localFileFor(match[1], true);
  if (!file) {
    console.log(
      `stamp-lastmod: sitemap index points at ${match[1]}, which is not under ${baseUrl} — this looks like a non-production build, skipping`,
    );
    process.exit(0);
  }
  if (!fs.existsSync(file)) {
    fail(`sitemap index lists ${match[1]} but ${path.relative(docsRoot, file)} is missing`);
  }
  sitemapFiles.push(file);
}

const previous = readManifest();
const isFirstRun = previous === null;
const known = previous || {};
const buildDate = today();

const pages = {};
const changed = [];
const missing = [];

for (const sitemapFile of sitemapFiles) {
  const original = fs.readFileSync(sitemapFile, 'utf8');

  const stamped = original.replace(/<url>[\s\S]*?<\/url>/g, (block) => {
    const locMatch = block.match(/<loc>([^<]+)<\/loc>/);
    if (!locMatch) {
      return block;
    }
    const loc = locMatch[1];
    const file = localFileFor(loc, false);
    if (!file || !fs.existsSync(file)) {
      missing.push(loc);
      return block;
    }

    const hash = crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
    const prior = known[loc];

    let lastmod;
    if (!prior) {
      lastmod = buildDate;
      changed.push(loc);
    } else if (prior.hash !== hash) {
      lastmod = buildDate;
      changed.push(loc);
    } else {
      lastmod = prior.lastmod;
    }

    pages[loc] = { hash, lastmod };

    return block.replace(/<lastmod>[^<]*<\/lastmod>/, `<lastmod>${lastmod}</lastmod>`);
  });

  if (stamped !== original) {
    fs.writeFileSync(sitemapFile, stamped, 'utf8');
  }
  fs.writeFileSync(`${sitemapFile}.gz`, zlib.gzipSync(Buffer.from(stamped, 'utf8')));
}

const dropped = Object.keys(known).filter((loc) => !(loc in pages));

writeManifest(pages);

if (changed.length > 0) {
  const queued = new Set(changed);
  try {
    const carried = JSON.parse(fs.readFileSync(pendingPath, 'utf8'));
    for (const loc of carried.urls || []) {
      if (loc in pages) {
        queued.add(loc);
      }
    }
  } catch {
    /* nothing queued from an earlier build */
  }
  fs.writeFileSync(
    pendingPath,
    `${JSON.stringify({ generatedAt: new Date().toISOString(), urls: [...queued].sort() }, null, 2)}\n`,
    'utf8',
  );
}

const total = Object.keys(pages).length;
if (isFirstRun) {
  console.log(`stamp-lastmod: first run, seeded ${total} docs pages across ${sitemapFiles.length} sitemap(s)`);
} else {
  console.log(`stamp-lastmod: ${total} docs pages, ${changed.length} changed since last build`);
}
if (dropped.length > 0) {
  console.log(`stamp-lastmod: ${dropped.length} page(s) no longer built, removed from the manifest`);
}
if (missing.length > 0) {
  console.warn(
    `stamp-lastmod: ${missing.length} sitemap URL(s) had no built page and were left unstamped:\n  ${missing.slice(0, 10).join('\n  ')}`,
  );
}
