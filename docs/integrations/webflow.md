# How to Use the Webflow Content Manager

## What This Helps You Do

The Webflow Content Manager lets you edit your Webflow CMS collections and page metadata directly in Hi, Moose—without opening the Webflow Designer. 

You get AI-powered suggestions for titles, descriptions, and content fields, so you can optimize for SEO and AI Overviews faster. This is especially useful if you're managing dozens (or hundreds) of blog posts, products, or landing pages.

Unlike the Webflow Designer, you see **Draft** and **Live** versions side-by-side, so you can edit staged content or directly update published pages. When you're ready, you can **Publish Site** to push all changes live at once.

---

## When to Use This

- **Bulk editing collection items**: Update meta descriptions, tags, or content fields across multiple blog posts, products, or team bios without logging into Webflow.
- **AI-assisted metadata**: Generate SEO titles, meta descriptions, or Open Graph tags using your page content—Hi, Moose analyzes the page and suggests optimized copy.
- **Page-level SEO updates**: Edit page titles, meta descriptions, and Open Graph tags for static pages (Home, About, Contact) or collection template pages.
- **Team collaboration**: Let content writers and marketers update Webflow content without giving them full Designer access.

This tool is **not** for visual design changes (layouts, styling, components). For that, you still need the Webflow Designer.

---

## Before You Start

### What You Need

1. **Webflow API Key** with these permissions:
   - **Sites** → Read and Write
   - **CMS** → Read and Write (required for Collections)
   - **Pages** → Read and Write (required for page metadata)
   - **Assets** → Read and Write

   To create an API key: Go to your [Webflow Dashboard](https://webflow.com/dashboard/workspace/sites) → Workspace Settings → Integrations → API Access → Create New Token.

2. **Webflow Site ID**: You can find this in your Webflow site settings URL (e.g., `https://webflow.com/dashboard/sites/YOUR_SITE_ID/general`).

3. **Hi, Moose project**: Create or open a project where you want to connect Webflow.

4. **Subscription tier**:
   - **Free**: View collections and pages only.
   - **Starter, Growth, Enterprise**: Full editing + AI suggestions.

### Important Notes

- Changes you make are **staged** (draft) by default. You must click **Publish Site** to make them live.
- Publishing affects your **entire site**, not just the items you edited. Any staged changes in Webflow Designer will also go live.
- If your API key is missing permissions, you'll see an error with instructions to fix it.

---

## Step-by-Step (in Hi, Moose)

### 1. Connect Your Webflow Site

**First time only**: If you haven't connected Webflow to this project yet, you'll see a setup screen.

1. Go to **Projects** → click your project name.
2. Click the **Edit Project** icon (pen icon) next to the project name.
3. Scroll to the **Webflow Configuration** section.
4. Paste your **Webflow API Key** and **Webflow Site ID**.
5. Click **Save**.

The platform field will automatically be set to "Webflow" so the Webflow menu item appears.

Once saved, return to your project and click **Webflow Content Manager** in the left menu.

---

### 2. Edit Collection Items (Blog Posts, Products, etc.)

**What are collections?** Collections are your CMS content types in Webflow—like blog posts, products, team members, or case studies.

#### View and Filter Collections

1. On the **Collections** tab, you'll see all your Webflow collections with item counts.
2. Use the **search bar** to filter collections by name or slug.
3. Click **Refresh** (top-right) to reload the list from Webflow. This uses cached data by default for speed.

**If you see a permission error**: Your API key is missing the **CMS → Read and Write** scope. Follow the instructions on-screen to regenerate your key with the correct permissions.

#### Edit an Item

1. Click a collection name to see all items in that collection.
2. Find the item you want to edit and click **Edit** (pen icon).
3. A modal opens showing:
   - **Draft** tab: Staged changes (not yet live)
   - **Live** tab: Currently published version

**To edit Draft (recommended)**:
1. Select the **Draft** tab.
2. Edit any field: plain text, rich text, images, etc.
3. Click **Save Draft**. Your changes are staged but not live yet.

**To edit Live directly**:
1. Select the **Live** tab.
2. Edit fields.
3. Click **Save Live**. Changes go live **immediately** for this item.

#### Use AI to Generate Field Content

1. While editing an item, click the **sparkle icon** (✨) next to any text field.
2. Hi, Moose analyzes the item (title, existing content, etc.) and suggests optimized copy.
3. Review the suggestion and click **Accept** to use it, or keep typing to adjust.
4. The field will show a blue "AI-modified" indicator. You can click **Undo** to revert.

**Note**: AI suggestions require a paid plan (Starter+). Free users can edit manually.

#### Create a New Item

1. On the collection items page, click **New Item** (top-right).
2. Fill in all required fields (marked with *).
3. Click **Create Item**. The new item is created as a draft.
4. Edit it further if needed, then publish the site to make it live.

---

### 3. Edit Page Metadata (Titles, SEO, Open Graph)

**What are pages?** Pages are your static pages (Home, About, Contact) and collection template pages (like Blog Post or Product templates).

#### View and Filter Pages

1. On the **Pages** tab, you'll see all pages in your site.
2. Use the **search bar** to filter by page name or slug.
3. Sort by **Name**, **Slug**, or **Created On** using column headers.
4. Use **pagination** (bottom) to browse if you have many pages.
5. Click **Refresh** to reload from Webflow.

#### Edit Page Metadata

1. Click **Edit Metadata** (pen icon) next to any page.
2. A modal opens with these fields:
   - **SEO Title**: The `<title>` tag for search engines.
   - **Meta Description**: The meta description shown in search results.
   - **Open Graph Title**: Title shown when shared on social media.
   - **Open Graph Description**: Description shown on social shares.
   - **Open Graph Image**: URL for the social share image (paste a URL).

3. Edit any field manually, or use **AI Suggest** (sparkle icon) to generate optimized copy based on page content.

**For static pages**: Hi, Moose can read your page content to generate suggestions.  
**For collection template pages**: Suggestions are based on the template structure (e.g., `{post-title}` variable).

4. Click **Save Metadata**. Changes are staged (draft).
5. Click **Publish Site** later to make them live.

#### About Webflow Variables

If your page uses Webflow dynamic fields (like `{post-title}` or `{name}`), Hi, Moose shows them in simplified form: `{post-title}`.

**Do not rename or delete these variables**. You can edit the text around them, but keep the variable names intact. If you accidentally modify one, you'll see an error when saving.

#### Publish vs. Save

- **Save Metadata**: Saves to the **staged/draft** version in Webflow. Not live yet.
- **Publish & Save**: Saves metadata and **publishes the entire site** in one step. All staged changes go live.

---

### 4. Publish Your Site

When you're done editing collection items and page metadata, it's time to push everything live.

1. Click the **Publish** tab.
2. You'll see a warning: "Publishing affects your entire site."
3. Click **Publish Site**.
4. Confirm in the modal: **Yes, Publish Site**.
5. Hi, Moose sends a publish request to Webflow. This takes a few seconds.

**What gets published**:
- All staged collection items
- All page metadata changes
- Any other changes in your Webflow site (even if you made them in Webflow Designer)

**Important**: There's no undo for publishing. Make sure everything is ready before you click Publish.

---

## What You Get (Outputs)

- **Updated collection items**: Changed fields are saved to Webflow (draft or live).
- **Optimized metadata**: SEO titles, meta descriptions, and Open Graph tags for better search visibility and social shares.
- **AI-generated suggestions**: Contextually relevant copy based on your page or item content.
- **Published site**: All changes live on your Webflow site (after you click Publish).

Changes appear in Webflow immediately after saving/publishing—no need to re-export or rebuild.

---

## Tips for Best Results

1. **Edit drafts, then publish**: Always edit the **Draft** version first so you can review changes before they go live. Use the **Live** tab only for urgent fixes.

2. **Use AI for bulk optimization**: If you're updating 50 blog posts, let AI suggest meta descriptions—it's faster than writing them manually. Review each one, then save.

3. **Check variables before saving**: On collection template pages, make sure you don't accidentally delete Webflow variables like `{post-title}`. Hi, Moose will warn you if you do.

4. **Refresh when needed**: If you (or a teammate) made changes in Webflow Designer, click **Refresh** in Hi, Moose to sync the latest data.

5. **Publish at the end**: Edit multiple items/pages, then publish once. This is faster and safer than publishing after every change.

6. **Use search and filters**: If you have hundreds of items, use the search bar to find specific ones. You can also sort by name or date.

7. **Team permissions**: If you're a team member (not the project owner), you'll inherit the owner's subscription tier for AI features. Admins can edit; viewers can only view.

---

## Troubleshooting

### 1. "Webflow Configuration Required" screen appears

**Why**: Your project doesn't have a Webflow API key or Site ID saved yet.

**Fix**:
- Click **Go to Project Settings**.
- Enter your Webflow API Key and Site ID.
- Save the project.
- Return to Webflow Content Manager.

---

### 2. "Your Webflow API key is missing required permissions" error

**Why**: Your API key doesn't have all the necessary scopes.

**Fix**:
1. Go to [Webflow Dashboard](https://webflow.com/dashboard/workspace/sites) → Workspace Settings → Integrations → API Access.
2. Delete your old token.
3. Create a new token with these permissions:
   - **Sites** → Read and Write
   - **CMS** → Read and Write
   - **Pages** → Read and Write
   - **Assets** → Read and Write
4. Copy the new token.
5. Update your project settings in Hi, Moose with the new API key.

---

### 3. Collection or page not found

**Why**: The collection or page may have been deleted in Webflow, or the Site ID is incorrect.

**Fix**:
- Verify your **Site ID** in project settings.
- Click **Refresh** to reload the latest data from Webflow.
- If the item was deleted in Webflow, it won't appear here.

---

### 4. "Failed to save item" or "Failed to update metadata"

**Why**: Network issue, invalid data, or Webflow API rate limit.

**Fix**:
- Check your internet connection.
- Make sure all required fields are filled in (look for * markers).
- If you're making many rapid changes, wait 10–20 seconds and try again (Webflow rate limits apply).
- Check the browser console for detailed error messages.

---

### 5. AI suggestions not working ("Upgrade to use AI features")

**Why**: You're on the Free plan, or you're a team member and the project owner is on Free.

**Fix**:
- Upgrade to **Starter, Growth, or Enterprise** to unlock AI features.
- If you're a team member, ask the project owner to upgrade.

---

### 6. Changes saved but not appearing on live site

**Why**: You saved to **Draft**, but didn't click **Publish Site** yet.

**Fix**:
- Go to the **Publish** tab.
- Click **Publish Site**.
- Wait a few seconds for Webflow to rebuild your site.
- Refresh your live site in a browser.

---

### 7. "Please don't modify variable names" error

**Why**: You edited or deleted a Webflow dynamic field variable (like `{post-title}`) in a page metadata field.

**Fix**:
- Look for the simplified variable in your text (e.g., `{post-title}`).
- Make sure the variable name is exactly as it was originally.
- You can edit text *around* the variable, but don't rename or delete the variable itself.
- Click **Undo** if you see the button to revert your changes.

---

### 8. "Publishing..." takes a long time

**Why**: Webflow's publish process can take 30–60 seconds for large sites (especially if you have many pages or CMS items).

**Fix**:
- Wait patiently. Don't close the modal or refresh the page.
- If it takes longer than 2 minutes, check [Webflow's status page](https://status.webflow.com/) for outages.
- Try publishing directly in Webflow Designer to confirm the issue isn't site-specific.

---

### 9. Modal won't close after saving

**Why**: This is intentional—the modal stays open so you can make multiple edits without reopening it each time.

**Fix**:
- Click the **X** or **Cancel** button to close manually when you're done.

---

### 10. Slow performance when loading collections or pages

**Why**: Hi, Moose caches data to speed up loading. If the cache is stale, the first load may be slow.

**Fix**:
- Click **Refresh** (with the spinning icon) to force a fresh fetch from Webflow.
- Subsequent loads will be faster as the cache updates.
- If it's still slow, check your Webflow site—sites with 1,000+ pages may take longer to load.

---

## Frequently Asked Questions

### What's the difference between Collections and Pages?

**Collections** are CMS content types (blog posts, products, team members, etc.). Each collection contains multiple items.

**Pages** are individual static pages (Home, About, Contact) or collection template pages (the blog post template, product template, etc.). You edit **metadata** (titles, descriptions) for pages, not the actual content/layout.

---

### What's the difference between Draft and Live?

**Draft**: Staged changes in Webflow. Not visible on your live site yet. This is where you should make edits so you can review before publishing.

**Live**: The currently published version on your live site. Editing the Live version directly pushes changes live **immediately** for that item (but you still need to publish the site for other changes).

**Best practice**: Edit Draft, review, then publish.

---

### Does "Publish Site" only publish my Hi, Moose edits?

No. **Publish Site** publishes **everything** that's staged in Webflow—including:
- Hi, Moose edits (collection items, page metadata)
- Changes made in Webflow Designer
- Any unpublished changes from other integrations

It's a site-wide publish, not a selective publish.

---

### How are AI suggestions generated?

For **collection items**: Hi, Moose analyzes the item's existing fields (title, content, description) and generates contextually relevant copy.

For **static pages**: Hi, Moose fetches the page HTML, extracts headings and text, and suggests metadata based on that content.

For **collection template pages**: Suggestions are based on the template structure and dynamic fields (like `{post-title}`).

AI uses your page context to generate copy optimized for search engines and AI Overviews—not generic templates.

---

### Is my Webflow API key secure?

Yes. Your API key is **encrypted** before being stored in Firestore. Hi, Moose decrypts it only when making requests to Webflow on your behalf. It's never exposed in the browser or shared with third parties.

You can rotate your API key anytime in Webflow, then update it in Hi, Moose project settings.

---

### Can I edit multiple items at once?

Not yet. Currently, you edit one item or page at a time. Bulk editing is planned for a future release.

**Workaround**: Use AI suggestions to speed up optimization. Click **AI Suggest** for each field, review, save, move to next item.

---

### Can I create new collections or pages?

You can **create new collection items** (e.g., add a new blog post to your Blog collection), but you **cannot create new collections or pages** from Hi, Moose.

To create new collections or static pages, use the Webflow Designer.

---

### What happens if I delete an item in Webflow?

If you delete a collection item or page in Webflow, it will disappear from Hi, Moose the next time you refresh the list. You won't be able to edit deleted items.

---

### Can I use this for multi-language sites?

Hi, Moose connects to one Webflow Site ID at a time. If you have separate Webflow sites for different languages, you'd need separate Hi, Moose projects for each site.

Webflow's native localization (multiple locales in one site) is **not fully supported yet**. The tool will use the default locale.

---

### Does this work with Webflow's eCommerce products?

Yes, if your products are in a **CMS collection**. You can edit product fields (name, description, price, images) just like any other collection item.

**Note**: Inventory and fulfillment are managed in Webflow, not Hi, Moose.

---

### Why do I see "Last refresh: X minutes ago"?

Hi, Moose caches collection and page data to speed up loading. The timestamp shows when the cache was last updated.

Click **Refresh** to fetch fresh data from Webflow. This bypasses the cache.

---

### Can team members use the Webflow Content Manager?

Yes. Team members inherit the project owner's subscription tier:
- **Free tier**: Team members can view collections/pages but not edit.
- **Paid tiers**: Team members can edit and use AI features.

**Note**: Only the project owner can update the Webflow API key in project settings. Team members (including admins) cannot see or change the API key.

---

### What if I make a mistake?

- **Before publishing**: Just edit the Draft again and fix the mistake. Then publish.
- **After publishing**: Edit the Live version to fix the mistake, save, then publish again.

There's no "version history" in Hi, Moose. For safety, consider taking screenshots before big changes, or use Webflow's backup feature.

---

### Can I schedule publishes?

Not yet. You have to manually click **Publish Site** when you're ready. Scheduled publishing is planned for a future update.

---

### Why are some fields read-only?

Some fields in Webflow are system-managed (like **Created On**, **ID**, **Slug**). You can't edit these—even in Webflow Designer.

If a custom field appears read-only, check its field settings in Webflow. It may be set to "Generated" or "Read-only."

---

### Does this replace the Webflow Designer?

No. The Webflow Content Manager is for **content and metadata editing only**. You still need the Webflow Designer for:
- Visual design and layout changes
- Adding/removing page sections
- Creating new collections, fields, or pages
- Configuring CMS field settings
- Managing forms, interactions, or custom code

Think of Hi, Moose as a **content management layer** on top of Webflow—optimized for bulk SEO updates and AI-assisted optimization.

---

### I'm getting rate-limited by Webflow. What do I do?

Webflow's API has rate limits (60 requests per minute for most endpoints). If you're editing many items rapidly, you may hit this limit.

**Fix**:
- Wait 60 seconds, then try again.
- Slow down your editing pace.
- If you need to update hundreds of items, spread the work over multiple sessions.

Hi, Moose automatically retries failed requests with exponential backoff, so most rate limit issues are temporary.

---

## Related Features

- **AEO Tools**: After editing your content in Webflow, use [AEO Tools](../features/aeo-optimization.md) to analyze how AI engines interpret your pages.
- **LLM Beacon**: Monitor if your Webflow content gets cited in AI platforms. See [LLM Beacon](../features/llm-beacon.md).
- **Content Brief Creator**: Generate data-driven content briefs for new Webflow blog posts. See [SEO Content Briefs](../features/content-briefs.md).

---

**Still stuck?** Check the [Support](https://www.himoose.com/contact) page or email support@himoose.com. Include your project ID and a screenshot of the error for faster help.
