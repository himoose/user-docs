# Hi, Moose Documentation Site

Public user documentation for Hi, Moose - the desktop-first AI visibility operations platform.

This documentation site is built with **MkDocs** using the `shadcn` theme, and deployed to **Firebase Hosting**, served at `himoose.com/docs/`.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+ (for the Firebase CLI)
- Firebase account with access to this project

### Local Development

1. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

2. **Serve documentation locally:**

```bash
mkdocs serve
```

The site will be available at `http://localhost:8000`. On Windows, use `python -m mkdocs serve` if `mkdocs` isn't on your `PATH`.

3. **Build static site:**

```bash
mkdocs build
```

This generates static files in the `site/` directory.

## 📁 Project Structure

```
user-docs/
├── docs/                          # Markdown documentation files
│   ├── index.md                  # Homepage
│   ├── getting-started/          # Install, account modes, projects, settings, team, Context
│   │   └── context/
│   ├── inbox/                    # Inbox and notification preferences
│   ├── visibility/                # Visibility dashboard, Prompt Manager, settings
│   ├── workflows/                 # Saved workflow recipes
│   ├── chat/                      # Chat, specialists, model selection, chat history
│   ├── library/                   # Library
│   ├── features/                  # Agent worksteams (audits, briefs, FAQs, key points, drafts, etc.)
│   ├── integrations/              # Grav, WordPress, Webflow, Google Search Console
│   ├── legacy/                    # Legacy web app-only features
│   ├── assets/                    # Logos, favicon, and other static assets
│   ├── stylesheets/
│   │   └── extra.css             # Theme customizations
│   └── javascripts/
│       └── custom.js             # Header/logo/sidebar behavior tweaks
├── overrides/                     # Theme template overrides (shadcn theme)
├── mkdocs.yml                     # MkDocs configuration and nav structure
├── requirements.txt                # Python dependencies
├── firebase.json                   # Firebase Hosting config (includes URL redirects)
├── .firebaserc                     # Firebase project config
└── README.md                       # This file
```

## 🎨 Customization

### Update Navigation

Edit [mkdocs.yml](mkdocs.yml) to modify the navigation structure:

```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Installing & Signing In: getting-started/install-and-sign-in.md
  # Add more sections...
```

Any new page must be added here or it will not appear in the site's navigation.

### Theme Configuration

The site uses the `shadcn` theme for MkDocs, with local overrides in `overrides/`. Customize colors and features in [mkdocs.yml](mkdocs.yml):

```yaml
theme:
  name: shadcn
  custom_dir: overrides
  palette:
    primary: indigo
    accent: indigo
```

### Add New Pages

1. Create a new `.md` file in the matching `docs/` subfolder.
2. Add it to the navigation in `mkdocs.yml`.
3. Preview changes with `mkdocs serve`.

## 🔥 Firebase Deployment

### Initial Setup

1. **Install Firebase CLI:**

```bash
npm install -g firebase-tools
```

2. **Login to Firebase:**

```bash
firebase login
```

3. **Confirm the project in `.firebaserc`** matches the Firebase Hosting project this site deploys to.

### Deploy to Firebase

1. **Build the documentation:**

```bash
mkdocs build
```

2. **Deploy to Firebase Hosting:**

```bash
firebase deploy --only hosting
```

The site is served from the `himoose.com/docs/`.

## 📝 Content Guidelines

### Writing Documentation

- Use clear, concise language.
- Include examples where appropriate.
- Add code blocks with syntax highlighting.
- Use admonitions for tips, warnings, and notes.
- Keep paragraphs short (3-4 sentences).
- Use bullet points for lists.
- Include screenshots when helpful.

### Markdown Tips

**Admonitions:**

```markdown
!!! tip "Pro Tip"
    This is a helpful tip for users.

!!! warning "Important"
    This is something users should be careful about.

!!! note
    This is additional information.
```

**Code Blocks:**

````markdown
```python
# Python code example
def hello_world():
    print("Hello, World!")
```
````

**Links:**

```markdown
[Link text](page-name.md)
[External link](https://example.com)
```

## 🧪 Testing

### Test Locally

```bash
# Serve and test
mkdocs serve

# Build and check for errors
mkdocs build --strict
```

### Check for Broken Links

Install and use linkchecker:

```bash
pip install linkchecker
mkdocs serve &
linkchecker http://localhost:8000
```

## 🐛 Troubleshooting

### MkDocs Issues

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**Theme not loading:**
```bash
pip install --upgrade mkdocs-shadcn
```

### Firebase Issues

**Authentication error:**
```bash
firebase login --reauth
```

**Wrong project:**
```bash
firebase use your-project-id
```

## 📚 Additional Resources

### MkDocs Documentation
- [MkDocs](https://www.mkdocs.org/)
- [mkdocs-shadcn](https://github.com/asiffer/mkdocs-shadcn)
- [Python Markdown Extensions](https://python-markdown.github.io/extensions/)

### Firebase Hosting
- [Firebase Hosting Docs](https://firebase.google.com/docs/hosting)
- [Firebase CLI Reference](https://firebase.google.com/docs/cli)

## 🤝 Contributing

### Making Updates

1. Create a new branch for your changes.
2. Update markdown files in `docs/`.
3. Test locally with `mkdocs serve`.
4. Build and verify: `mkdocs build --strict`.
5. Commit and push changes.
6. Deploy to Firebase Hosting.

### Content Review Process

1. Technical accuracy check against the desktop app.
2. Grammar and spelling review.
3. Link verification.
4. Screenshot updates (if needed).
5. Final preview before deployment.

## 📞 Support

For questions or issues:

- **Documentation Issues**: Open an issue in the repository.
- **Technical Support**: support@himoose.com

## 📄 License

Copyright © 2026 Hi, Moose. All rights reserved.

---

## Quick Reference Commands

```bash
# Local development
mkdocs serve                  # Serve locally
mkdocs build                  # Build static site
mkdocs build --strict         # Build with strict error checking

# Firebase
firebase login                # Login to Firebase
firebase deploy --only hosting  # Deploy to Firebase Hosting

# Useful development commands
pip install -r requirements.txt    # Install Python dependencies
pip list                           # List installed packages
python -m http.server 8000         # Simple HTTP server for the built site/ directory
```

---

Made in Austin, TX by the Hi, Moose team
