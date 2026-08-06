const fs = require('node:fs');
const path = require('node:path');

const docsRoot = path.join(__dirname, '..');
const manifestPath = path.join(docsRoot, 'sitemap-lastmod.json');
const pendingPath = path.join(docsRoot, '.indexnow-pending.json');

const config = require(path.join(docsRoot, 'indexnow.json'));
const baseUrl = config.baseUrl.replace(/\/+$/, '');
const key = config.key;
const keyLocation = config.keyLocation;
const host = new URL(baseUrl).host;
const endpoint = 'https://api.indexnow.org/indexnow';
const batchSize = 10000;

const submitAll = process.argv.includes('--all');
const dryRun = process.argv.includes('--dry-run');
const FAILED = '__reported__';

function readJson(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch {
    return null;
  }
}

function urlsToSubmit() {
  if (submitAll) {
    const manifest = readJson(manifestPath);
    return Object.keys((manifest && manifest.pages) || {}).sort();
  }
  const pending = readJson(pendingPath);
  return ((pending && pending.urls) || []).slice().sort();
}

async function main() {
  if (!key || !/^[A-Za-z0-9-]{8,128}$/.test(key)) {
    console.error('ping-indexnow: indexnow.json is missing a valid key');
    throw new Error(FAILED);
  }

  const urls = urlsToSubmit();
  if (urls.length === 0) {
    console.log('ping-indexnow: no docs pages changed since the last successful ping');
    return;
  }

  const offSite = urls.filter((url) => !url.startsWith(`${baseUrl}/`) && url !== baseUrl);
  if (offSite.length > 0) {
    console.error(`ping-indexnow: refusing to submit URLs outside ${baseUrl}:\n  ${offSite.slice(0, 5).join('\n  ')}`);
    throw new Error(FAILED);
  }

  if (dryRun) {
    console.log(`ping-indexnow: would submit ${urls.length} docs URL(s) to ${endpoint}`);
    for (const url of urls.slice(0, 20)) {
      console.log(`  ${url}`);
    }
    if (urls.length > 20) {
      console.log(`  ... and ${urls.length - 20} more`);
    }
    return;
  }

  const keyCheck = await fetch(keyLocation).catch(() => null);
  if (!keyCheck || !keyCheck.ok) {
    console.error(`ping-indexnow: key file is not reachable at ${keyLocation}`);
    throw new Error(FAILED);
  }
  const hosted = (await keyCheck.text()).trim();
  if (hosted !== key) {
    console.error(`ping-indexnow: ${keyLocation} does not contain the key from indexnow.json`);
    throw new Error(FAILED);
  }

  for (let start = 0; start < urls.length; start += batchSize) {
    const urlList = urls.slice(start, start + batchSize);
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({ host, key, keyLocation, urlList }),
    });

    if (response.status !== 200 && response.status !== 202) {
      const body = await response.text().catch(() => '');
      console.error(
        `ping-indexnow: ${endpoint} returned ${response.status} ${response.statusText}\n${body.slice(0, 500)}`,
      );
      console.error('ping-indexnow: the queue was kept — rerun `npm run indexnow` to retry');
      throw new Error(FAILED);
    }

    console.log(`ping-indexnow: submitted ${urlList.length} docs URL(s), got ${response.status}`);
  }

  if (!submitAll) {
    fs.rmSync(pendingPath, { force: true });
  }
}

main().catch((error) => {
  if (error.message !== FAILED) {
    console.error(`ping-indexnow: ${error.message}`);
  }
  process.exitCode = 1;
});
