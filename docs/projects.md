# How to Manage Projects in Hi, Moose

## What This Helps You Do

Projects are organizational containers in Hi, Moose where each one holds your competitors, comparisons, content briefs, brand voice settings, and platform integrations (Webflow, WordPress, CSV).

### By creating projects, you can:

- **Organize by website**: One project per client or website.
- **Separate campaigns**: Different projects for different products or services.
- **Isolate competitors**: Each project has its own competitor set.
- **Connect platforms**: Link projects to Webflow sites or WordPress installations.

Projects keep your workspace tidy and ensure content generation uses the right context (brand voice, competitors, domain).

---

## When to Use This

- **Agency work**: Create one project per website, domain, or client (e.g., "Client A Website," "Client B Blog").
- **Multiple brands**: Separate projects for each brand you manage.
- **Testing**: Create a test project to experiment with features before applying them to production.
- **Platform-specific workflows**: One project for Webflow sites, another for WordPress, another for CSV exports.
- **Team collaboration**: Share specific projects with team members (all plans support team members).

Create a new project whenever you're working on a distinct website, brand, or campaign that needs its own competitor analysis and content strategy.

---

## Before You Start

### What You Need

1. **Active Hi, Moose account**: You must be logged in.

2. **Subscription limits**: Your plan determines how many projects you can create:
   - **Free**: 1 project
   - **Standard**: 10 projects
   - **Professional**: 20 projects
   - **Premium**: 30 projects

3. **For platform integrations** (optional):
   - **Webflow**: API key from Webflow.
   - **WordPress**: Domain name (to generate API key for WordPress plugin).

### Important Notes

- You must have **at least 1 project** at all times—you can't delete your last project.
- Only **team owners** can delete projects or manage platform integrations.
- **Switching projects** changes the context for all AI features (competitors, brand voice, etc.).

---

## Step-by-Step (in Hi, Moose)

### 1. View Your Projects

1. In the left sidebar, click **Projects** (folder icon).
2. You'll see the **Manage Projects** page with:
   - **Project Capacity**: Shows how many projects you've used vs. your plan limit (e.g., "3 of 10 projects used").
   - **Your Projects**: A grid of project cards.

Each project card shows:
- **Project name**: e.g., "Acme Corp Website."
- **Platform**: Webflow, CSV, or WordPress.
- **Slug**: URL-friendly identifier (e.g., "acme-corp").
- **Webflow site** (if linked): e.g., "Acme Website."
- **Current Project badge**: Shows which project is currently active.

---

### 2. Create a New Project

#### Check Your Project Limit

- In the **Project Capacity** section, see if you can add more projects.
- If you're at the limit, you'll see: "Project limit reached (X)". Click **Upgrade Now** to increase your limit.

#### Add a Project

1. Click **Add Project** (top-right) or click the **Add New Project** card (if under your limit).

2. A modal opens with these fields:
   - **Project Name** (required): Enter your website or brand name (e.g., "Acme Corp Website").
   - **Slug** (required): A URL-friendly identifier (e.g., "acme-corp"). Auto-generated from the name, but you can edit it.
   - **Domain Name** (optional): Your website domain (e.g., "acmecorp.com"). Required for WordPress integration.
   - **Platform** (required): Choose:
     - **Webflow**: For Webflow CMS sites.
     - **CSV**: For CSV and HTML exports (works for most CMS).
     - **WordPress**: For WordPress sites with Hi, Moose plugin.

3. Click **Create Project**.

4. The project is created and **automatically selected** as your current project.

**What happens next?**
- If you chose **Webflow**: You'll need to add your Webflow API key (see Step 4).
- If you chose **WordPress**: You'll need to generate an API key (see Step 5).
- If you chose **CSV**: You're ready to use the project—no extra setup needed.

---

### 3. Select a Project

**What this does**: Switching projects changes the context for all features—competitors, brand voice, content briefs, etc.

#### How to Switch

1. On the **Manage Projects** page, find the project you want to work on.
2. Click **Select Project** (blue arrow button).
3. The project is now active. You'll see **Current Project** (purple border) on the card.

You can also select your project from the Projects drop-down select menu in the top left corner on the left side navigation.

---

### 4. Edit a Project

**Why edit?** To change the name, slug, platform, domain, or add/regenerate your Hi, Moose API key for that project.

#### How to Edit

1. On the project card, click the **pen icon** (Edit Project).
2. The card expands to show editable fields:
   - **Project Name**: Change the name.
   - **Slug**: Change the URL-friendly identifier.
   - **Domain Name**: Add or update your website domain (required for WordPress).
   - **Platform**: Switch between Webflow, CSV, or WordPress.

3. Make your changes.
4. Click **Save**.

**Platform changes**:
- **Switching to Webflow**: You'll see a prompt to add your Webflow API key after saving.
- **Switching from Webflow**: Any existing Webflow integration settings are removed.
- **Switching to WordPress**: You'll need to enter a domain name and generate an API key (see Step 5).

---

### 5. Connect Webflow (Optional)

**When to do this**: If you selected "Webflow" as your platform and want to sync content to Webflow CMS.

#### Webflow Setup

1. After creating or editing a project with platform = "Webflow," you'll see a **Webflow Configuration** prompt.
2. Click **Set Up Webflow** (or edit the project and add Webflow details).

3. A modal opens: **Connect Webflow API Key**.
4. Enter your **Webflow API Key** (get one at [Webflow Dashboard](https://webflow.com/dashboard/workspace/sites) → Workspace Settings → Integrations → API Access).

5. Click **Test Connection**.
   - Hi, Moose verifies the key and fetches your Webflow sites.
   - You'll see a list of sites tied to your API key.

6. Select a site from the **Site** dropdown.
7. Click **Save Webflow Settings**.

**What this does**:
- Links this project to a specific Webflow site.
- Enables Webflow Content Manager and Versus Content Wizard export to Webflow.

**Security note**: Your Webflow API key is **encrypted** before storage and is no longer accessible from the frontend. 

---

### 6. Connect WordPress (Optional)

**When to do this**: If you selected "WordPress" as your platform and want to connect the Hi, Moose WordPress plugin.

#### WordPress Setup

**Requirement**: You must first add a **Domain Name** and save the project before generating a WordPress API key.

1. Edit the project (pen icon).
2. Enter your **Domain Name** (e.g., "acmecorp.com") in the Domain Name field.
3. Click **Save**.

4. Once saved, the **WordPress Configuration** section appears.
5. You'll see a read-only input field (masked if a key exists: `••••••••••••••••••••••••••••••••`).

#### Generate a Key

1. Click **Generate Key** (or **Regenerate** if a key already exists).
2. A confirmation modal appears (if regenerating): "This will invalidate the current key. Update your WordPress plugin after regeneration."
3. Click **Regenerate Key**.
4. A new API key is generated and displayed in the input field (e.g., `sk_wpkey_abc123...`).

5. Click **Copy Key**.
6. Paste the key into your **Hi, Moose WordPress Plugin** settings.

**Where to use the key**:
- Install the Hi, Moose WordPress plugin on your WordPress site.
- Go to **Settings → Hi, Moose** in WordPress admin.
- Paste the API key and save.

**Reveal an existing key**:
- If you lost your key, click **Reveal Key** to see it again.

**Regenerate a key**:
- If your key is compromised, click **Regenerate** to create a new one.
- **Warning**: The old key will stop working immediately—update your WordPress plugin.

---

### 7. Delete a Project

**Who can delete**: Only **team owners** can delete projects (not team members).

**Restrictions**: You cannot delete your last remaining project—you must always have at least 1 project.

#### How to Delete

1. On the project card, click the **trash icon** (Delete Project).
2. A modal opens: **Delete Project**.
3. You'll see a warning:
   - "This will permanently delete the project [Project Name], including all of its matrices and competitors. This action cannot be undone."

4. Read what will be deleted:
   - All competitor data and logos.
   - All comparison matrices and content.
   - All associated files and configurations.
   - All generated podcasts and analytics data.

5. **Type the project name** exactly as shown (e.g., "Acme Corp Website") in the confirmation field.
6. Click **Delete Project**.

The project is permanently deleted—this **cannot be undone**.

---

## What You Get (Outputs)

After managing your projects, you have:

- **Organized workspace**: Each website/brand has its own project with separate competitors, content, and settings.
- **Context-aware AI**: Switching projects changes the AI's context (brand voice, competitors, domain).
- **Platform integrations**: Webflow or WordPress connected for seamless content publishing.
- **Team collaboration**: Share specific projects with team members (team plans only).
- **Scalable workflows**: Manage multiple clients or brands without mixing data.

---

## Tips for Best Results

1. **One project per website**: Don't mix multiple websites in one project—create separate projects for better organization.

2. **Use descriptive names**: Instead of "Project 1," use "Acme Corp Blog" or "Client X Landing Pages." This makes it easier to find the right project.

3. **Add domain names early**: If you're using WordPress, add the domain name when creating the project—it's required for API key generation.

4. **Test projects first**: Create a test project to experiment with features before applying them to production. Delete it when done.

5. **Link Webflow sites correctly**: Make sure you select the right Webflow site when setting up the integration—Hi, Moose pulls data from that site only.

6. **Regenerate WordPress keys carefully**: If you regenerate a WordPress API key, update your WordPress plugin immediately—the old key stops working.

7. **Check project limits before scaling**: If you're approaching your limit (e.g., 8/10 projects), consider upgrading **before** you hit the cap.

8. **Use CSV for flexibility**: If you don't use Webflow or WordPress, choose CSV—you can export data and import it nearly anywhere.

9. **Delete unused projects**: If a client project is complete, delete it to free up space for new projects (team owners only).

10. **Switch projects intentionally**: Always check which project is active before generating content—AI features use the active project's context.

---

## Troubleshooting

### 1. "Project limit reached" message appears

**Why**: You've used all available projects for your subscription tier (e.g., 3/3 on Starter plan).

**Fix**:
- **Upgrade**: Click **Upgrade Now** to increase your project limit (Starter → Growth = 3 → 10 projects).
- **Delete old projects**: Delete unused projects to free up space (team owners only).
- **Archive workflow**: If you need temporary projects, create, use, and delete them as needed.

---

### 2. "You must enter a Domain Name before generating an API key"

**Why**: WordPress API keys require a domain name (to validate WordPress plugin requests).

**Fix**:
1. Click **Edit** (pen icon) on the project card.
2. Fill in the **Domain Name** field (e.g., "acmecorp.com").
3. Click **Save**.
4. Now you can click **Generate Key** in the WordPress Configuration section.

---

### 3. Webflow connection test fails—"Invalid API key"

**Why**: Your Webflow API key is incorrect, expired, or lacks permissions.

**Fix**:
1. Go to [Webflow Dashboard](https://webflow.com/dashboard/workspace/sites) → Workspace Settings → Integrations → API Access.
2. Verify the key is active (not revoked).
3. Make sure the key has these permissions:
   - **Sites** → Read and Write
   - **CMS** → Read and Write
   - **Pages** → Read and Write
   - **Assets** → Read and Write
4. Copy the key and paste it again in Hi, Moose.
5. Click **Test Connection**.

---

### 4. Can't delete a project—trash icon is grayed out

**Why**: You only have 1 project left, or you're a team member (not the owner).

**Fix**:
- **Last project**: You cannot delete your only project. Create a new project first, then delete the old one.
- **Team member**: Only the **team owner** can delete projects. Ask your team owner to delete it.

---

### 5. WordPress API key doesn't work in plugin

**Why**: The key was regenerated, there's a typo, or the domain was saved incorrectly.

**Fix**:
1. In Hi, Moose, click **Reveal Key** to see the current key.
2. Copy the key.
3. Go to your WordPress site → **Settings → Hi, Moose**.
4. Paste the key **exactly** (no spaces or line breaks).
5. Save and test the connection.
6. Make sure the domain matches the domain of your production domain where you will use audio player

If it still fails:
- Regenerate the key in Hi, Moose.
- Update it in WordPress immediately.

---

### 6. Changing platform removes my Webflow settings

**Why**: Switching from "Webflow" to "CSV" or "WordPress" removes Webflow-specific settings (API key, site ID).

**Fix**:
- This is intentional—Webflow settings are platform-specific.
- If you switch back to "Webflow," you'll need to re-enter your API key and site.

---

### 7. Project name change doesn't update everywhere

**Why**: Project names are displayed in the Projects page only—not in URLs or slugs.

**Fix**:
- **Project Name**: Displayed in the UI only (project cards, headers).
- **Slug**: Used in URLs (e.g., `/projects/acme-corp`). Edit the slug separately if you want to change it.
- Changing the name doesn't affect existing data. All competitors, comparisons, and settings remain intact.

---

### 8. "Failed to save project" error

**Why**: Network issue, missing required fields, or duplicate slug.

**Fix**:
- Check your internet connection.
- Make sure **Project Name** and **Slug** are filled in.
- Make sure the **Slug** is unique (not used by another project).
- Try saving again. If it fails, refresh the page and try once more.

---

### 9. Can't see new project after creating it

**Why**: The project was created but not automatically selected, or there's a UI refresh issue.

**Fix**:
- Refresh the page (Ctrl+R or Cmd+R).
- Look for the new project card in the grid.
- Click **Select Project** to activate it.
- If it's still missing, check your subscription limit—you may have hit the cap.

---

### 10. Switching projects doesn't update feature context

**Why**: You need to refresh or reload the feature page for the new project context to apply.

**Fix**:
1. Switch projects on the **Manage Projects** page.
2. **Refresh the page** (Ctrl+R or Cmd+R).
3. Navigate to the feature you want (e.g., Content Brief Creator).
4. The new project's context (competitors, brand voice) should now be active.

---

## Frequently Asked Questions

### What's the difference between "Project Name" and "Slug"?

- **Project Name**: The display name (e.g., "Acme Corp Website").
- **Slug**: A URL-friendly identifier (e.g., "acme-corp"). Used in URLs and API calls.

Both can be edited, but **slugs must be unique** across your projects.

---

### Can I rename a project?

Yes. Click **Edit** (pen icon) on the project card, change the **Project Name**, and click **Save**.

---

### What happens when I delete a project?

**Permanently deleted**:
- All competitor data and logos.
- All comparison matrices and content.
- All brand voice settings and documents.
- All generated podcasts and analytics.
- All platform integrations (Webflow, WordPress).

**Not deleted**:
- Your Hi, Moose account.
- Other projects.
- Your subscription.

---

### Can I recover a deleted project?

No. Deletion is **permanent** and **cannot be undone**. Make sure you export any data (CSV, Webflow) before deleting.

---

### What's the "Current Project" badge?

The **Current Project** badge (highlighted in purple) shows which project is currently active. This is the context used by all AI features:
- Content Brief Creator uses this project's competitors.
- AEO Tools references this project's brand voice.
- Versus Content Wizard generates comparisons for this project.

Switching projects changes the AI's context.

---

### Can I have multiple projects for the same website?

Yes, but it's not recommended. You'd have separate competitor sets, brand voice settings, and content—which defeats the purpose of organization.

**Better approach**: Use one project per website, and create separate **comparison sets** or **content briefs** within that project.

---

### Do team members see all projects?

Yes. All team members with access to the team workspace see all projects.

**Editing permissions**:
- **Team Owner**: Full edit/delete access.
- **Members**: Full edit access (cannot delete projects).

---

### What's the difference between "Webflow," "CSV," and "WordPress" platforms?

**Webflow**:
- Syncs data directly to Webflow CMS.
- Requires Webflow API key and Site ID.
- Enables Webflow Content Manager and Versus Content Wizard export.

**CSV**:
- Exports data as CSV files and HTML.
- No platform integration required.
- Most flexible. Import CSV or HTML manually nearly anywhere.

**WordPress**:
- Connects to Hi, Moose Text-to-Speech WordPress plugin.
- Requires domain name and API key generation.
- Enables WordPress content sync (on the roadmap).

---

### Can I change a project's platform after creating it?

Yes. Edit the project and change the **Platform** dropdown. But:
- **Switching to Webflow**: You'll need to set up Webflow API key.
- **Switching from Webflow**: Existing Webflow settings are removed.
- **Switching to WordPress**: You'll need to add a domain and generate an API key.

---

### Why do I need a domain name for WordPress?

The domain name is used to **validate** API requests from your WordPress site. It ensures only your WordPress installation can use the API key and the audio player—not someone else who got your key.

---

### Can I use the same Webflow API key for multiple projects?

Yes. If you have multiple Webflow sites under one workspace, you can use the same API key. Just select a different **Site** for each project.

---

### What happens if I regenerate my WordPress API key?

The old key **stops working immediately**. You must update your WordPress plugin with the new key, or content sync will fail.

**Steps after regeneration**:
1. Copy the new key in Hi, Moose.
2. Go to your WordPress site → **Settings → Hi, Moose**.
3. Paste the new key and save.

---

### Can I export project data before deleting?

In most cases you can, but not for all features. Before deleting:
- **Versus Content Wizard**: Go to Step 7 (Export) and download CSV files.
- **Webflow users**: Content is already in Webflow CMS—no export needed.
- **Content Briefs**: Export each into the desired file format.
- **AEO analyses**: Export each as PDF.
- **Key Points**: Export each as CSV.
- **FAQs**: Export each as CSV.

At the time of this writing, the following features do not currently have export capabilities:
- **Podcasts**
- **LLM Beacon**
- **Topical Authority Audits**

---

### Why can't I see the "Add Project" button?

**Reason 1**: You're at your project limit (e.g., 3/3 on Starter plan).  
**Fix**: Upgrade or delete an unused project.

**Reason 2**: You're a team member (not the owner).  
**Fix**: Only team owners can add projects. Ask your team owner to add more.

---

### Do projects share brand voice settings?

No. **Brand voice settings are project-specific**. Each project has its own:
- Brand tone, style, audience.
- Uploaded brand documents.
- Preferred terminology.

If you want the same brand voice in multiple projects, you'll need to set it up separately for each one (or copy/paste the text fields).

---

## Related Features

- **Brand Voice Settings**: Customize AI output for each project. See [Brand Voice Settings](brand-voice.md).
- **Webflow Content Manager**: Manage Webflow CMS collections. See [Webflow Integration](integrations/webflow.md).
- **Versus Content Wizard**: Create comparison pages at scale. See [Versus Pages](features/versus-pages.md).

---

**Still stuck?** Check the [Support](https://www.himoose.com/contact) page or email support@himoose.com. Include your project name and a screenshot for faster help.
