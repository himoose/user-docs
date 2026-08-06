# Grav

## What this helps you do

Connect a live [Grav](https://getgrav.org) site through the Hi, Moose Grav plugin, so the desktop app can inspect Grav content and run remote create, update, publish, and rollback actions directly.

## Installing the plugin

1. From **Connections → Grav** in the desktop app, open the plugin download link and download the Hi, Moose plugin ZIP. The current version is **0.1.1** and it requires Grav 1.7.0 or newer.
2. In your Grav Admin, open **Plugins**, upload the ZIP, and complete the install.
3. Enable the plugin, then open its settings in Grav Admin.
4. Copy the connection bundle shown there — you'll paste it into Hi, Moose in the next step.

## Connecting in Hi, Moose

1. Open **Connections** in the desktop app and choose Grav.
2. Enter your Grav site URL.
3. Leave the connector route blank unless your Grav plugin uses a non-default route — Hi, Moose otherwise uses the route from the connection bundle or falls back to `/himoose-connector`.
4. Paste the connection bundle copied from the plugin, then save.
5. Click **Test connector** to validate the connection against your live Grav site.

## Connection readiness

After testing, Hi, Moose reports one of a few states: the connector isn't fully set up yet, it's saved but not yet validated, it responded but remote write actions aren't fully enabled (read-only), it's fully ready for read and remote write actions, or the last validation failed and the site settings or plugin secrets need attention.

## What the connection can do

Once ready, the Grav connector can list content, read raw content, and create, update, and publish content directly — the same staged, reviewable path used by [Drafts, Preview & Publishing](../features/drafts-and-publishing.md) for other connections.

## Security

Your Grav site URL and connection bundle are stored locally, only accessible to the desktop app's background process — never exposed to the renderer UI.
