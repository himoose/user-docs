!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Audio

## What this helps you do

Turn an article into a two-voice conversation, then download the MP3 or embed the player on your site. The player ships with a transcript, which puts real, crawlable first-hand text on the page — content an answer engine can retrieve.

Audio lives in the desktop app under **Audio** in the sidebar, split into three tabs: **Generate**, **History**, and **Analytics**.

!!! note "Audio moved out of the legacy web app"
    Audio generation used to live at `app.himoose.com` as "Listen to this Article." It's now fully part of the desktop app, with project scoping, listening analytics, and player customization that the web version didn't have.

## Before you start

Set the project's website first. Playback is locked to your project domain plus `himoose.com`, so Hi, Moose needs to know the domain before it will generate anything. If it isn't set, the Generate tab shows a **Set website** prompt instead of the composer.

Audio availability depends on your [plan](../getting-started/account-modes.md): BYOK Premium and BYOK Agency include 15 generations per month, managed plans are unlimited, and the free plans don't include audio.

## Choosing a source

Three ways to get content in:

- **Article URL** — paste a published URL and click **Fetch**. Hi, Moose extracts the content and shows the domain, word count, and estimated read time. The article has to be publicly reachable, not behind a login or paywall.
- **Paste text** — give the episode a title and paste the script or article text directly.
- **Upload file** — drop in a `.txt`, `.md`, `.docx`, `.doc`, or `.pdf`. The file is read on your device and its text drops into the paste flow.

## Shaping the conversation

**Focus** (optional) steers what the conversation digs into. There are quick suggestions for common angles: key takeaways, explain it to a beginner, push back on the argument, who should care.

**Length** sets the target runtime:

| Length | Runtime | Approximate script |
|---|---|---|
| Short | 4–5 min | ~700 words |
| Standard | 8–10 min | ~1,400 words |
| Deep dive | 15–18 min | ~2,600 words |

**Language** defaults to matching the article. Override it to change both the script and the voices.

**Voices** come as host and guest pairings, with three presets — warm + curious, calm + analytical, bright + skeptical — or a custom pairing you pick yourself.

## Advanced direction

Optional, and everything left blank follows the article and the voice pairing. Seven fields are available: host direction, guest direction, scene, style, pace, accent, and extra context.

- **Scene**: studio interview, fireside chat, panel discussion, phone-in, walk-and-talk
- **Style**: explanatory, debate, storytelling, interview, casual
- **Pace**: slower, natural, faster
- **Accent**: American (neutral), British, Australian, Irish, Indian, or neutral international

Any of these can be replaced with a custom description in your own words.

**Extra context** is for what the article doesn't say — how to pronounce a product name, claims to avoid, who the audience is.

!!! warning "Context steers tone, not facts"
    Hi, Moose won't invent facts to fill a direction. Extra context changes framing and delivery; it doesn't add evidence that isn't in the source.

Once you've got settings you like, **Save as project default** reuses them for the next episode in this project.

## Generating

Click **Generate audio**. The composer shows an estimated render time before you start. Generation runs in the background, so you can leave the screen and keep working — the finished episode appears in the sidebar **Recents** list, and clicking it opens that episode directly.

When it's done you get:

- A player with seek, 15-second skip back and forward, and playback speed
- **Download MP3**
- **Share** to copy the audio link
- The full **transcript**, with turn and word counts, and a copy button
- **Embed on your site**, covered in [Player & Embed](player-and-embed.md)
- **Regenerate with edits** and **Edit settings**, to adjust direction and run it again

## History

The **History** tab lists every episode in the current project with its length, creation date, and status. Episodes are scoped per project, so switching projects changes what you see.

- Search episodes by name
- Filter by **All**, **Ready**, or **Needs attention**
- Play, download, open the embed options, or open the full episode
- **Retry** a failed episode

Statuses are Ready, Processing, Playing, Failed, and Canceled.

## Where to go from here

- **[Player & Embed](player-and-embed.md)** — theme, layout, accent color, and the embed code.
- **[Listening Analytics](analytics.md)** — what happens after the player is on a page.
