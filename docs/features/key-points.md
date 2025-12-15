# How to Generate Key Points in Hi, Moose

## What this helps you do

Extract the most important points from articles and content as clean, scannable bullet points. This improves content accessibility, helps readers quickly grasp main ideas, and boosts SEO with structured content.

Hi, Moose uses **semantic compression** — AI that understands meaning and context to identify what's truly important, not just what appears frequently. This means your key points capture the essence of your content, not just surface-level summaries.

Key points appear at the beginning of your content, giving busy readers instant value and encouraging them to read the full article.

## When to use this

- **Long-form articles** — Help readers scan before committing to read
- **Technical content** — Simplify complex topics into digestible takeaways
- **News and updates** — Highlight the most critical information upfront
- **Product documentation** — Surface key features and benefits
- **Educational content** — Provide study aids and quick reference points

Best for articles over 500 words. Shorter content may not have enough substance for meaningful key points.

## Before you start (requirements)

### Required
- A project selected in Hi, Moose
- Either:
  - A published article URL (publicly accessible), OR
  - Content ready to paste manually

### Optional
- Webflow API key (if you want automatic updates to Webflow CMS)

### Note on API keys
- **Free & Standard plans**: Use Hi, Moose's API keys automatically
- **BYOK plans**: Your OpenAI API key must be saved in Settings

## Step-by-step (in Hi, Moose)

### Method 1: From URL

#### 1. Select input mode
- Click the **From URL** tab (should be selected by default)
- The globe icon indicates URL input mode

#### 2. Enter article URL
- Paste your article's full URL in the text field
- Example: `https://yourwebsite.com/blog/article-title`
- The URL must be publicly accessible (not behind a login)

#### 3. Generate key points
- Click **Generate Key Points** (or **Extract Key Points** in Marketer Mode)
- Hi, Moose will:
  - Extract content from the URL
  - Generate bullet-point key points using AI
  - Display results in an editable preview

**Status indicators**:
- "Extracting..." — Hi, Moose is fetching your content
- "Generating..." — AI is creating key points
- Success — Green preview box appears with results

#### 4. Review extracted content
- After extraction, you'll see your content in a gray box
- Character count displays (e.g., "Content (5,234 chars)")
- Verify the content looks complete and accurate

#### 5. Edit key points (optional)
- Use the rich text editor to modify generated points
- Format text: **bold**, *italic*
- Add or remove bullet points
- Reorganize content as needed

#### 6. Save changes
- If you edited: Click **Save Changes** button (top right)
- This saves your edits for future reference
- Button shows "Saving..." while processing

#### 7. Copy to your CMS
- Click **Copy** button (purple) to copy HTML with proper wrapper
- Paste at the beginning of your article in WordPress, Webflow, etc.
- The HTML includes `<div id="key-points-paeo">` wrapper for styling

### Method 2: Paste Content

#### 1. Select input mode
- Click the **Paste Content** tab
- Document icon indicates manual input mode

#### 2. Paste your content
- Copy content from your article/document
- Paste into the large text area
- No formatting is preserved — plain text only

#### 3. Generate key points
- Click **Generate Key Points** (green button)
- AI processes your pasted content
- Results appear in the editable preview

#### 4. Follow steps 5-7 from Method 1
- Edit, save, and copy as described above

### Additional features

#### Export CSV
- Click **Export CSV** button (yellow)
- Downloads a CSV file with URL and key points
- Useful for batch processing records or audits

#### Update in Webflow (if configured)
- **Update in Webflow** button appears if:
  - Your project platform is set to Webflow
  - Webflow API key exists in settings
- Click the button to choose a collection and update items
- Only available if you've saved changes (button disabled if unsaved edits)

## What you get (outputs)

### Key points list
- Formatted as HTML bullet points
- Typically 3-7 key points depending on content length
- Each point is concise (1-2 sentences)
- **Semantically compressed** — captures core meaning, not just surface-level summaries
- Focuses on the most valuable insights from your content
- Wrapped in `<div id="key-points-paeo">` for easy styling

### HTML structure
```html
<div id="key-points-paeo">
  <h2>Key Points</h2>
  <ul>
    <li>First key point...</li>
    <li>Second key point...</li>
    <li>Third key point...</li>
  </ul>
</div>
```

### Editable format
- Rich text editor with formatting controls
- Bold, italic, lists, headings
- Live preview of changes
- Saved to your project history

### Export options
- **Copy button**: Copies formatted HTML to clipboard
- **Export CSV**: Downloads CSV file for record-keeping
- **Webflow integration**: Direct CMS updates (if configured)

## Tips for best results

### Content preparation
- **Use complete articles** — Full content produces better key points than excerpts
- **Clean URLs work best** — Avoid URLs with `?preview=true` or login requirements
- **Well-structured content** — Articles with clear paragraphs and headings yield better results
- **Optimal length**: 800-3000 words gets 4-6 strong key points

### When to use manual paste
- URL extraction fails (Cloudflare protection, JavaScript-heavy sites)
- Content is in a Google Doc or Word document
- You want to generate points from draft content
- Behind a paywall or login
- Complex page layouts that confuse the extractor

### Editing best practices
- **Keep points concise** — Aim for 1-2 sentences per point
- **Action-oriented language** — "Learn how..." or "Discover why..."
- **Front-load value** — Most important points first
- **Maintain parallel structure** — All points should follow similar format
- **Test with your audience** — What seems valuable to them?

### CMS implementation
- **WordPress**: Paste in "Text" or "HTML" editor mode, not Visual
- **Webflow**: Use Rich Text or Embed element
- **Shopify**: Use HTML content blocks
- **Custom sites**: Place near the top of article content
- **CSS styling**: Target `#key-points-paeo` for custom styles

### Token management
- Single URL generation uses approximately 200-1000 tokens
- Longer articles use more tokens
- Editing and re-saving doesn't use additional tokens
- Track usage in Settings → Usage to avoid hitting limits

## Troubleshooting

### ❌ "Could not extract enough content" error
**Problem**: URL extraction failed or returned insufficient text.

**Fix**:
- Check the URL is correct and publicly accessible
- Try opening the URL in an incognito browser window
- Remove any tracking parameters (`?utm_source=...`)
- Switch to **Paste Content** tab and paste manually
- If site uses JavaScript for content, manual paste is required
- Check for Cloudflare protection or bot detection

---

### ❌ "Select a project first" error
**Problem**: No project is currently selected in Hi, Moose.

**Fix**:
- Look at the top of the page for the project dropdown
- Select your project from the dropdown menu
- If you have no projects, create one first in Settings
- Refresh the page if project selector isn't responding

---

### ❌ Empty or incomplete key points
**Problem**: Generated points are generic, missing details, or too short.

**Fix**:
- Verify the extracted content (check gray "Content" box)
- Ensure article has substantial content (500+ words minimum)
- Try manual paste if extraction missed key sections
- Regenerate — click input field and **Generate Key Points** again
- Edit manually using the rich text editor
- Check that article has clear structure (not just navigation/boilerplate)

---

### ❌ "Auth required" or "Permission denied"
**Problem**: Authentication or authorization issue.

**Fix**:
- Refresh the page and log in again
- Check you have access to the selected project
- Verify your subscription is active (check Settings)
- If using BYOK plan, ensure OpenAI API key is saved in Settings
- Try logging out completely and logging back in
- Clear browser cache and cookies if issue persists

---

### ❌ "Save Changes" button doesn't work
**Problem**: Edits aren't saving when clicking the Save Changes button.

**Fix**:
- Check your internet connection
- Look for error messages in a red toast notification
- Verify you made actual changes (button only appears if edited)
- Try copying the content and regenerating
- Check browser console for errors (F12 → Console tab)
- If using old browser, update to latest version

---

### ❌ Formatting lost when pasting in CMS
**Problem**: Key points lose formatting when pasted into WordPress/Webflow.

**Fix**:
- Use **Copy** button (don't select and copy manually)
- In WordPress: Switch to "Text" or "Code" view before pasting
- In Webflow: Use Rich Text element, not plain text
- Don't paste into visual/WYSIWYG editors
- HTML must be pasted in HTML/code mode
- Check your CMS allows custom HTML (some block editors restrict it)

---

### ❌ "Team information required" error
**Problem**: Team/subscription data is missing.

**Fix**:
- This usually resolves automatically after a few seconds
- Refresh the page to reload subscription data
- Check your subscription status in Settings
- Contact support if error persists (rare)

---

### ❌ Token limit exceeded
**Problem**: "Your monthly usage limit has been reached" error.

**Fix**:
- Check current usage in Settings → Usage tab
- Wait until the next billing cycle (resets monthly)
- Upgrade your plan for higher token limits
- For BYOK plans, verify your OpenAI account has credits
- Consider using batch processing for multiple URLs (more efficient)

---

### ❌ Webflow button is grayed out
**Problem**: "Update in Webflow" button is disabled or shows "Save Changes First".

**Fix**:
- **If unsaved edits**: Click **Save Changes** first, then try Webflow button
- **If grayed out**: Webflow API key may be missing
  - Go to Project Settings
  - Add your Webflow API key
  - Return to Key Points generator
- **If wrong platform**: Change project platform to "Webflow" in Settings
- Refresh page after adding API key

---

### 🔄 Stuck on "Extracting..." or "Generating..."
**Problem**: Generation process taking longer than 60 seconds.

**Fix**:
- Wait up to 2 minutes for very long articles
- Check internet connection is stable
- Refresh the page and try again
- Try a different article to test if it's URL-specific
- Use manual paste method as alternative
- Very long content (10,000+ words) may timeout — split into sections

---

### 📱 Editor not working on mobile
**Problem**: Can't edit key points on phone or tablet.

**Fix**:
- Rich text editor works best on desktop browsers
- Use laptop/desktop for editing
- Mobile users: generate on desktop, copy to CMS from mobile
- Alternatively, export CSV and edit offline
- Consider using mobile browser's "Desktop site" mode

## FAQs

### How accurate are the generated key points?
Key points use semantic compression to identify the most important ideas in your content. They're typically 85-95% accurate for well-structured content, capturing core meaning rather than just summarizing text. Always review and edit before publishing to ensure accuracy and tone match your brand.

### Can I generate multiple key points for different articles?
Yes, there's no limit to single URL processing (within your token quota). For bulk processing of many URLs, use the Batch Sitemap Processor feature.

### Do the key points update if I change my article?
No. Key points are generated once from a snapshot of your content. If you update your article, regenerate key points by entering the URL again.

### How many key points should I aim for?
Typically 4-6 points is ideal. Fewer than 3 may not provide enough value; more than 8 becomes overwhelming. It depends on article length and complexity.

### Can I customize the format or style?
Yes, edit directly in the rich text editor. You can change bullet styles, add bold/italic, adjust wording, or completely rewrite points. The `#key-points-paeo` wrapper allows custom CSS styling on your site.

### What's the difference between "From URL" and "Paste Content"?
- **From URL**: Hi, Moose automatically extracts content from a live webpage
- **Paste Content**: You manually copy/paste content (useful for drafts, protected content, or when extraction fails)

Both methods produce identical results once content is processed.

### Does this work with non-English content?
Yes, Hi, Moose supports 100+ languages. The AI will generate key points in the same language as your input content.

### What is semantic compression?
Semantic compression is an AI technique that understands the meaning and context of your content to identify what's truly important. Unlike simple text summarization (which just shortens text), semantic compression analyzes relationships between ideas, identifies core concepts, and extracts insights that represent the essence of your content. This results in key points that capture real value, not just frequently mentioned topics.

### Can I use this for video transcripts or podcasts?
Yes, if you have a text transcript. Paste the transcript using the **Paste Content** tab. Key points work well for long-form transcripts.

### Where should I place key points on my webpage?
Best practice: Place immediately after the title/intro paragraph, before the main content begins. This gives readers an instant preview of what they'll learn.

### What HTML tags are included in the output?
Common tags: `<div>`, `<h2>`, `<ul>`, `<li>`, `<p>`, `<strong>`, `<em>`. The output is sanitized HTML safe for all CMS platforms.

### Can I export key points for multiple URLs at once?
For single URLs, use the Export CSV button. For batch processing and exports, use the Batch Sitemap Processor (separate feature).

### Will this work with password-protected pages?
No. The URL extractor can only access publicly available pages. For password-protected or draft content, use the **Paste Content** method.

### How do I style the key points on my website?
Use CSS to target `#key-points-paeo`. Example:
```css
#key-points-paeo {
  background: #f5f5f5;
  padding: 20px;
  border-left: 4px solid #0066cc;
}
```

### Can I regenerate if I don't like the results?
Yes, simply click the URL input field (to reset) and click **Generate Key Points** again. Each generation uses tokens, so edit existing results when possible.

### What happens to my edit history?
Saved changes are stored in your project's key points history. Access history from the main Key Points page to view previous generations.

### Does the "Manual" label affect the output?
No, the "Manual" label just indicates content source. Manual and URL-extracted content are processed identically by the AI.
