# How to Generate and Embed Podcasts in Hi, Moose

## What this helps you do

Turn any blog article or webpage into a two-person conversational podcast that your visitors can listen to. This increases content accessibility, improves engagement, and gives busy readers an audio alternative to reading.

The podcast features natural conversation between two AI voices discussing your content, and you get a customizable player that matches your brand.

## When to use this

- **Long-form blog posts** — Give readers an audio option for in-depth articles
- **News and updates** — Let busy audiences consume your content on-the-go
- **Educational content** — Make learning material more accessible
- **Product announcements** — Reach audio-first audiences
- **SEO content** — Add structured data and increase time-on-page metrics

Best for articles between 800-3000 words. Shorter content may feel rushed; longer content should be split into multiple podcasts.

## Before you start (requirements)

### Required
- Your website domain must be set in Hi, Moose (e.g., `yoursite.com`)
- A published article with a public URL
- The article must be accessible (not behind a login or paywall)

### Recommended
- Article should be well-formatted with clear paragraphs
- Content should be in one of the 24+ supported languages
- Have a sense of what tone/style you want for the conversation

## Step-by-step (in Hi, Moose)

### 1. Set your domain (first time only)

If you see "Domain Required" warning:
- Click **Set Domain Now**
- Enter your website domain (e.g., `yoursite.com`)
- Click **Save**

This whitelists your domain so only your website can play the audio files.

### 2. Enter article URL

- Paste your article's full URL in the **Article URL** field
- Example: `https://yourwebsite.com/blog/article-title`
- Hi, Moose will extract the content automatically

### 3. Choose voices

**Host Voice** and **Guest Voice**:
- Select different voices from the dropdown menus
- Click the play button (▶) next to each dropdown to preview voices
- Host and Guest must use different voices
- Default: Sulafat (Host) and Fenrir (Guest)

**Voice selection tip**: Choose contrasting voices (e.g., one deeper, one higher) for better listener experience.

### 4. Set podcast length

**Podcast Length** dropdown:
- **Short (4-5 minutes)** — Best for news, quick updates, summaries
- **Standard (8-10 minutes)** — Best for full articles, detailed content

Actual length depends on your article's word count.

### 5. Choose language (SEO Mode only)

**Language** dropdown:
- **Auto-detect from article (recommended)** — Hi, Moose detects the article's language
- Or select a specific language from 24+ options

The generated script and audio will match the selected language. Speaker labels ("Host:" and "Guest:") remain in English.

### 6. Add conversation guidance (optional)

Choose between **Basic Customization** or **Advanced Customization**:

#### Basic Customization
- **Basic Instructions** field: Provide simple directions for the conversation
- Example: _"Focus on the key benefits for small businesses"_
- Example: _"Emphasize the technical aspects and implementation details"_

#### Advanced Customization
More granular control over the conversation:

- **Host Direction**: How the host should sound (e.g., _"Friendly, confident, and curious"_)
- **Guest Direction**: How the guest should sound (e.g., _"More analytical and detail-oriented"_)
- **The Scene**: Set the recording environment (e.g., _"A quiet studio recording with a calm, focused vibe"_)
- **Conversation Style**: Overall tone (e.g., _"warm"_, _"professional"_, _"casual"_)
- **Conversation Pace**: Speaking speed (e.g., _"medium"_, _"fast"_, _"relaxed"_)
- **Accent**: Voice accent preference (e.g., _"neutral US"_, _"British"_)
- **More Context**: Additional audience context (e.g., _"The listener is a busy founder who wants the key takeaways"_)

All advanced fields are optional. Only fill in what you need.

### 7. Customize the player

**Player Customization** section:

**Colors**:
- **Primary Color**: Main player color (click color picker or enter hex code)
- **Secondary Color (Gradient)**: Creates gradient effect with primary color
- Default colors: Purple gradient (#667eea to #764ba2)

**Title settings**:
- Toggle **Show title above player** on/off
- When enabled, optionally enter **Custom Title** (or leave blank to use article title)
- Example custom title: _"Listen to this article as a podcast"_

**Player Preview** updates in real-time as you adjust settings.

### 8. Generate podcast

Click **Generate Podcast** button.

**What happens next**:
- Status shows: ⏳ **Pending** → ⚙️ **Processing** → ✅ **Ready**
- Processing typically takes 5-10 minutes
- You'll see estimated token cost breakdown
- You can leave the page — generation continues in background

### 9. Get your embed code

When status shows ✅ **Ready**:

1. Preview your podcast using the player that appears
2. Click **Copy Embed Code** button
3. Paste the HTML code into your article (see installation steps below)

### 10. Embed on your website

**WordPress**:
1. We highly recommend using the WordPress plugin at https://wordpress.org/plugins/listen-to-this-article/, but it's optional
2. When not using the WordPress plugin, edit your article in WordPress
3. Switch to "HTML" or "Code" view
4. Paste the embed code where you want the player
5. Update/Publish the article

**Webflow**:
1. Add a "Code Embed" element to your page
2. Paste the embed code
3. Publish your site

**Other platforms**:
- Look for "Custom HTML" or "Embed Code" blocks
- Paste the full embed code (including script tags)
- Save and publish

## What you get (outputs)

### Audio file
- MP3 format, high-quality (128kbps)
- Hosted on CDN (fast loading worldwide)
- Domain-whitelisted (only plays on your website and himoose.com)

### Embed code
- Fully functional audio player with controls
- Transcript included (collapsible "View Transcript" section)
- Responsive design (works on mobile, tablet, desktop)
- SEO-friendly with JSON-LD structured data markup
- "Powered by Hi, Moose" attribution

### Player features
- Play/Pause controls
- Seek bar with progress indicator
- Playback speed control (0.5x to 2.0x)
- Volume control with mute
- Displays current time and total duration
- Shows buffered/loaded sections

## Tips for best results

### Content preparation
- **Use well-structured articles** with clear headings and paragraphs
- **Irrelevant sections** Hi, Moose automatically focuses on the body of your content and attempts to ignore navigation, ads, and sidebars. Worst case scenario, you can give a URL version of your content that excludes the non-core content and our crawler should pick it up.
- **Ensure content is public** — Hi, Moose can't access password-protected pages
- **Keep it focused** — 800-3000 words is the sweet spot

### Voice selection
- **Test multiple voice combinations** — preview voices before generating
- **Match voices to brand** — formal content = professional voices; casual content = relaxed voices
- **Consider your audience** — regional preferences may matter for accent direction

### Customization strategy
- **Start with Basic Customization** for most articles
- **Use Advanced Customization** when you need specific tone/style control
- **Be specific in directions** — _"enthusiastic and upbeat"_ is better than _"good"_
- **Test with one article first** before generating in bulk

### Player placement
- **Place player near the top** of articles for maximum visibility
- **Test on mobile** — ensure player doesn't break responsive layout
- **Keep default colors** if unsure — they work well on most sites
- **Use custom title** to add context (e.g., "Listen while you work")

### Token management
- **Shorter podcasts use fewer tokens** — use "Short" length when appropriate
- **Preview estimated tokens** before generating
- Each podcast shows token breakdown: base fee + script + audio generation
- Free plan: Limited lifetime podcasts
- Paid plans: Token-based usage
- BYOK plan: The BYOK plan has a hard limit since the TTS model is using Hi, Moose keys for generation

## Troubleshooting

### ❌ "Domain Required" error
**Problem**: You haven't set your website domain yet.

**Fix**:
1. Click **Set Domain Now** button
2. Enter your domain without `https://` (e.g., `yoursite.com`)
3. Save and try generating again

---

### ❌ "Failed to extract content" error
**Problem**: Hi, Moose couldn't access or parse your article.

**Fix**:
- Check the URL is correct and publicly accessible
- Try the URL in an incognito browser window
- Remove any `?preview=true` or draft parameters from the URL
- If site has Cloudflare or bot protection, content may not be accessible
- For sites with heavy JavaScript, ensure content loads without JS

---

### ❌ "Host and Guest voices must be different"
**Problem**: You selected the same voice for both speakers.

**Fix**:
- Choose different voices from the dropdown menus
- Preview voices with the play button to find good combinations

---

### ❌ Player not showing on website
**Problem**: Embed code pasted incorrectly or blocked by platform.

**Fix**:
- Make sure you pasted the FULL embed code (including `<script>` tags)
- Confirm your CMS did not strip anything out. WordPress may do this if you toggle between "Visual" and "Code" tabs in the Classic Editor. We highly recommend using the WordPress plugin in this case.
- Switch to HTML/Code view (not visual editor) when pasting
- Check your platform allows custom HTML/scripts
- Clear browser cache and hard refresh (Ctrl+Shift+R)
- Check browser console for JavaScript errors (F12)

---

### ❌ "Content is too large" error
**Problem**: Article exceeds token limits (very long content).

**Fix**:
- Split long articles into multiple shorter podcasts
- Remove unnecessary sections (footnotes, references, author bios)
- Use the "Short" length option
- Typical limit: ~75,000 characters or ~100,000 tokens (most podcasts cost 10,000 to 20,000 tokens)

---

### ❌ Podcast sounds robotic or unnatural
**Problem**: Generated audio doesn't sound conversational.

**Fix**:
- Use **Advanced Customization** to guide the conversation style
- Add Host/Guest Direction (e.g., _"Speak naturally with casual enthusiasm"_)
- Set Conversation Style to _"warm"_ or _"conversational"_
- Check your article — very formal or technical writing may need rewriting
- Try different voice combinations

---

### ⏳ Generation taking too long
**Problem**: Status stuck on "Processing" for 15+ minutes.

**Fix**:
- Wait up to 20 minutes for long articles
- Check "Estimated Token Cost" — very high tokens = longer processing
- Refresh the page to check current status
- If stuck 30+ minutes, generate a new podcast (click **Create a New Podcast**)
- Contact Support if issue persists

---

### 🔊 Audio not playing on website
**Problem**: Player loads but won't play audio.

**Fix**:
- Check your domain is correctly set in Hi, Moose
- Verify domain in embed code matches your actual website domain
- Audio files are domain-whitelisted and won't play on different domains
- Test on your live website (not localhost during development)
- Check your browser console for CORS or 403 errors

---

### 🎨 Player colors don't match preview
**Problem**: Colors look different on your website.

**Fix**:
- Check you copied the embed code AFTER customizing colors
- Regenerate embed code if you changed colors after initial generation
- Your website's CSS may override player styles — check for conflicts
- Test in incognito mode to rule out browser extensions

---

### 📱 Player breaks on mobile
**Problem**: Player doesn't display correctly on phones/tablets.

**Fix**:
- Player is responsive by default — check for CSS conflicts on your site
- Don't wrap player in narrow containers (<300px width)
- Test on actual devices, not just browser dev tools
- Check your theme's mobile CSS isn't overriding player styles

## FAQs

### How long does podcast generation take?
Typically 5-10 minutes. Longer articles with more complex customization may take up to 10-15 minutes. You can leave the page and generation continues in background. Podcasts are available to access from the History tab.

### Can I edit the podcast after it's generated?
No, but you can regenerate with different instructions and settings. Click **Create a New Podcast** when generation completes.

### How many podcasts can I generate?
- **Free plan**: Limited lifetime podcasts (check your plan details)
- **Paid plans**: Unlimited but based on token usage allowance per plan
- **BYOK plans**: Monthly podcast limit (check Settings)

### What languages are supported?
24+ languages including English, Spanish, French, German, Japanese, Chinese, Arabic, Hindi, and more. See the Language dropdown for full list.

### Can I use custom voices?
Currently, you must use the provided voice options. We offer 30 AI voices with different characteristics.

### Do I need to credit Hi, Moose?
The embed code includes "Podcast generated by Hi, Moose" attribution. This is greatly appreciated to leave in, but not required.

### Can I download the MP3 file?
Not directly through the UI. The audio is hosted on our CDN for optimal performance and includes domain whitelisting.

### What if my article is behind a paywall?
Hi, Moose likely won't be able access password-protected or paywalled content. Make the article public temporarily during generation. You can optionally use a temporary URL the generator can use to fetch the content.

### Can I customize the transcript?
To an extent you can. The transcript is auto-generated from the content, however, you can direct what you want the podcast script to exlucde/include before generating. To to make updates or changes, you will need to regenerate the podcast with different instructions.

### Does the player work on all browsers?
Yes, modern browsers support the player. Minimum requirements: Chrome 60+, Firefox 55+, Safari 11+, Edge 79+.

### How do I remove an old podcast?
Embed codes remain functional until you remove them from your website. Simply delete the embed code from your article's HTML. If you're using the WordPress plugin, you can click the "Remove podcast" under the drop down select field.

### Can I use this for videos or social media?
The embed player is designed for web articles and pages. For other uses, contact Hi, Moose support about custom solutions.

### What happens if I change my domain?
First, update your domain in Hi, Moose Settings for the project. The final step is to contact Hi, Moose so we can update the domain whitelisting.

### How are tokens calculated?
Tokens = base processing fee + script generation (based on article length) + audio generation (based on podcast length). An estimate is shown before generation.

### Can I generate podcasts in bulk?
Currently, podcasts are generated one at a time. Webflow, WordPress, and by sitemap.xml is on the roadmap. Please contact us if you need bulk generation for multiple articles.
