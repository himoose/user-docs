# Player & Embed

## What this helps you do

Style the embedded audio player to match the page it's going on, then copy the embed code. Open it from a finished episode with **Customize player**, or from the **History** tab's embed action.

## Player options

- **Theme** — Dark, Light, or Auto. Auto follows each visitor's device setting.
- **Layout** — Full or Compact.
- **Accent color** — any 6-digit hex value, for example `#5688b0`.
- **Show the title** — turn it off when the embed sits under your own headline.
- **Custom title** — leave blank to use the episode title.
- **Transcript button** — show or hide the transcript toggle on the player.

A live preview updates as you change settings. If the player script isn't reachable when you're previewing, the preview falls back to plain markup — the copied embed code is still correct.

## Copying the embed code

Click **Copy embed code** and paste it into your page.

- **WordPress** — paste into the post's HTML or code block, or use the [Listen to This Article plugin](https://wordpress.org/plugins/listen-to-this-article/).
- **Webflow** — paste into an Embed element.
- **Grav** — paste into the page content where raw HTML is allowed.

## Playback is domain-locked

Generated audio only plays on your project's website domain and on `himoose.com`. This is set from the project's website field, and it's why that field has to be filled in before you can generate. If you embed the player on a domain that isn't whitelisted, playback will be refused.

## Agency attribution

On plans with [white-label branding](../agency/white-label.md), the embedded player can carry your agency's attribution instead of Hi, Moose's. Set it in **Settings → Branding**:

- **Audio embed attribution** — the text shown on the player. Leave it empty to use "Audio by" plus your agency name.
- **Attribution link** — a full `https://` address. Leave it empty to reuse your main branding link.

The attribution is a real link back to your site from every client page carrying the player, which is the point of it for agencies.

!!! warning "Attribution applies to embed code copied after saving"
    Changing branding doesn't rewrite embeds you've already placed. Copy the embed code again after saving to pick up new attribution.

## Why this helps AEO

The transcript adds crawlable, structured, first-hand text to the page. That's additional real content an answer engine can retrieve and quote, and it can support the extractability and comprehensiveness signals in an [AEO Audit](../features/aeo-audits.md). It isn't a scored "has media" factor on its own — the value is in the text the player brings with it.
