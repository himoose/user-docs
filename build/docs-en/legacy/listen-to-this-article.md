# Listen to this Article (Audio Generation)

!!! note "This feature lives in the legacy web app"
    As Hi, Moose moves to a desktop-first product, most features have moved into the desktop app. **Audio generation is one of two features that remain in the legacy web app** (`app.himoose.com`) for now — the other is [Versus Pages](versus-pages.md). If you're a desktop app user, you can reach this feature from the account menu without creating a separate login.

## What this helps you do

Turn any public article URL into a two-voice conversational audio experience, with a customizable embeddable player and transcript for your website.

## How it works

1. Enter a published article URL. Hi, Moose extracts the content automatically.
2. Choose a host voice and a guest voice, and an audio length (short or standard).
3. Optionally add conversation guidance — basic instructions, or advanced direction for tone, pacing, and accent.
4. Customize the player's colors and title.
5. Generate. Audio generation typically takes 5–10 minutes and continues in the background.
6. Once ready, copy the embed code and paste it into your site.

## Embedding

- **WordPress**: use the [Listen to This Article plugin](https://wordpress.org/plugins/listen-to-this-article/), or paste the embed code directly into your post's HTML/code view.
- **Webflow**: paste the embed code into an Embed element on your page.

## Requirements

- Your website domain must be set and whitelisted so only your site can play the generated audio.
- The source article must be publicly accessible (not behind a login or paywall).

## Why it helps AEO

The player's transcript adds crawlable, structured, first-hand text content to the page, which can support extractability and comprehensiveness in an [AEO Audit](../features/aeo-audits.md) — the transcript is additional real content an answer engine can retrieve, not a scored "media" factor on its own.
