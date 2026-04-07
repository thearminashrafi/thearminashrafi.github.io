# thearminashrafi.github.io

Personal academic website for Armin Ashrafi — hosted on GitHub Pages, no build step, no framework, no server required.

---

## Table of Contents

- [Site Structure](#site-structure)
- [Design System](#design-system)
- [Pages](#pages)
  - [Home](#home-indexhtml)
  - [Research](#research-researchhtml)
  - [Blog](#blog-blogsindexhtml)
  - [Wiki](#wiki-wikiindexhtml)
  - [Learning](#learning-learninghtml)
  - [Tutoring](#tutoring-tutoringhtml)
- [Wiki — Full Guide](#wiki--full-guide)
  - [Opening the Vault in Obsidian](#opening-the-vault-in-obsidian)
  - [Writing Notes](#writing-notes)
  - [Math](#math)
  - [Wikilinks](#wikilinks)
  - [Callouts](#callouts)
  - [Frontmatter Reference](#frontmatter-reference)
  - [Rebuilding the Manifest](#rebuilding-the-manifest)
- [Blog — Full Guide](#blog--full-guide)
  - [Creating a Post](#creating-a-post)
  - [Writing in Markdown](#writing-in-markdown)
  - [Registering the Post](#registering-the-post)
- [Deploying to GitHub Pages](#deploying-to-github-pages)
- [Automatic Wiki Updates (GitHub Action)](#automatic-wiki-updates-github-action)
- [Local Development](#local-development)
- [Adding / Editing Content Cheatsheet](#adding--editing-content-cheatsheet)

---

## Site Structure

```
thearminashrafi.github.io/
│
├── index.html              # Home / profile page
├── research.html           # Research, publications, experiments, projects
├── learning.html           # Learning materials you have created
├── tutoring.html           # Tutoring services + contact form
├── styles.css              # Shared design system (tokens, nav, footer, components)
│
├── blogs/
│   ├── index.html          # Blog post listing (search + tag filter)
│   ├── template.html       # Copy this to create a new post
│   └── my-post.html        # Example finished post
│
├── wiki/
│   ├── index.html          # Wiki homepage (note index, tag filter, search)
│   ├── page.html           # Generic note renderer (loads any .md from manifest)
│   ├── manifest.json       # Auto-generated note index (metadata only)
│   ├── manifest.js         # Same data as a JS file — loaded by the browser
│   ├── build-manifest.py   # Run locally to regenerate manifest after adding notes
│   ├── home.md             # Example note
│   ├── reinforcement-learning-basics.md  # Example note with math
│   ├── templates/
│   │   └── note.md         # Obsidian template for new notes
│   └── .obsidian/          # Obsidian vault config (committed to repo)
│
├── assets/
│   ├── armin.jpg           # Profile photo
│   └── *.pdf               # CV, paper drafts, etc.
│
└── .github/
    └── workflows/
        └── wiki-manifest.yml  # GitHub Action: regenerates manifest on push
```

---

## Design System

All visual styling lives in `styles.css`. Every page links to it and inherits the same tokens, components, and layout utilities. You should never need to duplicate CSS across pages.

### Color Tokens

| Token | Light | Dark | Used for |
|---|---|---|---|
| `--bg` | `#faf8f4` | `#141009` | Page background |
| `--bg-2` | `#f2ece0` | `#1e1810` | Cards, code blocks, inputs |
| `--text` | `#1c1510` | `#ede8e0` | Headings, primary text |
| `--text-2` | `#5a4e42` | `#a89880` | Body copy, descriptions |
| `--muted` | `#9a8d7f` | `#756050` | Timestamps, labels |
| `--accent` | `#c75d20` | `#f07530` | Links, buttons, highlights |
| `--border` | `#e6ddd0` | `#2e2418` | Borders, dividers |

To change the color scheme site-wide, edit only the `:root` and `:root.dark` blocks at the top of `styles.css`.

### Dark Mode

Dark mode is toggled by the `🌙` button in the navigation bar. The preference is saved in `localStorage` and respects the OS setting on first visit. No extra work needed — all pages inherit this behavior from the shared JS snippet at the bottom of each `<body>`.

### Typography

- **Body:** Inter (sans-serif) — loaded from Google Fonts
- **Headings:** Lora (serif) — loaded from Google Fonts

---

## Pages

### Home (`index.html`)

Single-purpose: introduces you. Contains:
- Profile photo, name, role, short bio
- Links to GitHub, LinkedIn, email (click-to-reveal), CV
- Four navigation cards pointing to the other sections

**To update your bio or links:** open `index.html` and edit the `.hero` section directly.

**To update your photo:** replace `assets/armin.jpg` with a new image (keep the same filename), or change the `src` attribute on the `<img class="avatar">` tag.

---

### Research (`research.html`)

Contains five sections:

1. **Research Statement** — a short paragraph about your work
2. **Education Timeline** — degree entries using `.tl-item` components
3. **Publications** — list of papers with links
4. **Experiments** — a filterable, tag-based lab notebook (see below)
5. **Projects** — card grid for selected projects
6. **Talks** — chronological list of talks

#### Adding an Experiment

Find the `experiments` array in the `<script>` block at the bottom of `research.html` and add an entry:

```js
{
  title: "Your experiment title",
  date: "Nov 2025",
  status: "active",       // "active" | "done" | "planned"
  tags: ["rl", "jax"],    // used for the filter buttons
  desc: "One paragraph describing what you tried and what you found.",
  links: [
    { label: "Paper draft", href: "assets/draft.pdf" }
  ]
}
```

The filter buttons at the top of the section are built automatically from all unique tags in the array. To add a new tag, just use it in an entry — no other changes needed.

---

### Blog (`blogs/index.html`)

A searchable, filterable list of posts. Posts are plain HTML files in the `blogs/` folder.

See [Blog — Full Guide](#blog--full-guide) below.

---

### Wiki (`wiki/index.html`)

A personal knowledge base powered by Obsidian-authored Markdown files. The index is auto-generated; notes support full LaTeX math, wikilinks, and Obsidian callouts.

See [Wiki — Full Guide](#wiki--full-guide) below.

---

### Learning (`learning.html`)

Two sections — Mathematics and Machine Learning & RL — each listing resources you have created. Each resource uses the `.resource` component (icon + title + description + link).

**To add a resource:** copy an existing `.resource` block in the HTML and edit the content. The two sections are separated by a `<div class="page">` boundary.

---

### Tutoring (`tutoring.html`)

Contains:
- A subject grid (emoji + subject name)
- A three-step "how it works" section
- A contact form that opens the visitor's email client with a pre-filled subject and body (no backend required)

**To change your email address:** find `const to = 'armin.ashrafi@ualberta.ca'` in the `<script>` block and update it.

**To add a subject:** add a `<div class="subject-card">` entry to the subjects grid.

---

## Wiki — Full Guide

The wiki is built on a simple idea: you write `.md` files in Obsidian, run one script to bundle them, and the website renders them with full math and wikilink support.

### Opening the Vault in Obsidian

1. Open Obsidian.
2. Click **"Open folder as vault"**.
3. Select the `wiki/` folder inside this repository.

Obsidian will pick up the `.obsidian/` config already committed to the repo. The file explorer, backlinks panel, graph view, and Templates plugin are all pre-configured.

> The `.obsidian/` folder is committed intentionally so the vault settings travel with the repo. If you install community plugins, their config will also live here and be committed on the next push.

---

### Writing Notes

Create a new file in Obsidian (`Cmd+N`) or use the template:

1. `Cmd+P` → **"Insert template"** → select `note`
2. Fill in the frontmatter at the top of the file (see [Frontmatter Reference](#frontmatter-reference))
3. Write your note in normal Markdown

Files can be named with spaces (`My Note.md`) or hyphens (`my-note.md`) — both work. The site resolves wikilinks case-insensitively.

Subdirectories are also supported. A note at `wiki/rl/policy-gradients.md` will appear in the index with path `rl/policy-gradients.md`.

---

### Math

Math is rendered using [KaTeX](https://katex.org/). Use standard LaTeX syntax.

**Inline math** — wrap in single dollar signs:

```
The discount factor $\gamma \in [0, 1)$ controls how much future rewards matter.
```

**Display math** — wrap in double dollar signs on their own line:

```
$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s \right]
$$
```

KaTeX supports most common LaTeX commands: `\frac`, `\sum`, `\int`, `\mathbb`, `\mathcal`, `\text`, `\begin{align}`, matrices, etc. For a full reference see [katex.org/docs/supported](https://katex.org/docs/supported.html).

---

### Wikilinks

Link between notes using Obsidian's double-bracket syntax:

```
[[Note Name]]                  → links to Note Name.md, displays "Note Name"
[[Note Name|Custom Display]]   → links to Note Name.md, displays "Custom Display"
[[rl/Policy Gradients]]        → links to rl/Policy Gradients.md in a subfolder
```

The site resolves links by matching the target stem against all notes in the manifest, normalising case and treating spaces, hyphens, and underscores as equivalent. If a note is renamed, update the links pointing to it (Obsidian's built-in rename will do this automatically within the vault).

---

### Callouts

Obsidian callouts render as styled boxes on the website:

```markdown
> [!NOTE]
> This is a note callout.

> [!WARNING]
> This is a warning callout.

> [!TIP]
> This is a tip callout.
```

Any word after `[!` is accepted as the callout type and displayed as the box title.

---

### Frontmatter Reference

Every note should begin with a YAML frontmatter block:

```yaml
---
title: Human-Readable Title
tags: [rl, math, notes]     # or multi-line format below
date: 2025-11-01             # ISO format YYYY-MM-DD
---
```

Multi-line tags format also works:

```yaml
---
title: My Note
tags:
  - rl
  - math
date: 2025-11-01
---
```

| Field | Required | Purpose |
|---|---|---|
| `title` | Recommended | Shown as the page heading and in the index. Falls back to the filename stem. |
| `tags` | Optional | Used for tag filter buttons on the wiki index. |
| `date` | Optional | Shown in the note header and used for sorting (newest first). |

---

### Rebuilding the Manifest

The website reads from `manifest.js` — a bundled file containing all note metadata and content. You must regenerate it every time you add, rename, or delete a note.

**Run from the repo root:**

```bash
python3 wiki/build-manifest.py
```

This updates both `wiki/manifest.json` and `wiki/manifest.js`. Commit both files along with your new `.md` files.

> On GitHub Pages, the manifest is regenerated automatically by a GitHub Action every time you push a commit that touches a file in `wiki/`. You only need to run the script manually for local previewing.

**Quick workflow:**

```bash
# 1. Write your note in Obsidian
# 2. Rebuild the manifest
python3 wiki/build-manifest.py

# 3. Commit and push
git add wiki/
git commit -m "wiki: add note on policy gradients"
git push
```

---

## Blog — Full Guide

### Creating a Post

1. Copy `blogs/template.html` to a new file, e.g. `blogs/my-post.html`
2. Edit the metadata at the top:

```html
<title>My Post Title — Armin Ashrafi</title>
<meta name="description" content="One sentence description." />
```

3. Update the post header inside `<main>`:

```html
<div class="post-tags">
  <span class="tag tag-accent">rl</span>
  <span class="tag">math</span>
</div>
<h1 class="post-title">My Post Title</h1>
<div class="post-meta">
  <span>Armin Ashrafi</span>
  <span>·</span>
  <span>November 1, 2025</span>
  <span>·</span>
  <span>8 min read</span>
</div>
```

### Writing in Markdown

The template supports two writing modes:

**Option A — Plain HTML** (default): write directly inside `<article id="prose-content" class="prose">`:

```html
<article id="prose-content" class="prose">
  <p>Your content here...</p>
  <h2>A Section</h2>
  <p>More content...</p>
</article>
```

**Option B — Markdown** (recommended for longer posts): uncomment the Markdown script block in `template.html` and write inside it:

```html
<script id="md-content" type="text/markdown">

## Introduction

Write your post in **Markdown** here. Math works too: $E = mc^2$.

$$
\nabla_\theta J(\theta) = \mathbb{E}_\pi \left[ \nabla_\theta \log \pi_\theta(a|s) \, Q^\pi(s,a) \right]
$$

</script>
```

The `marked.js` library parses this and injects the HTML into `#prose-content` automatically.

### Registering the Post

After writing the post, add it to the `posts` array in `blogs/index.html` so it appears in the listing:

```js
const posts = [
  {
    title:   "My Post Title",
    date:    "2025-11-01",       // ISO format for sorting
    display: "Nov 1, 2025",      // shown in the UI
    tags:    ["rl", "math"],
    excerpt: "One sentence teaser shown in the listing.",
    href:    "my-post.html"
  },
  // ... existing posts
];
```

The search and tag filter on the index page work automatically once the entry is in the array.

---

## Deploying to GitHub Pages

The site deploys automatically on every push to `main`. No build step required.

**Initial setup** (one time only):

1. Go to your repository on GitHub → **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Set branch to `main`, folder to `/ (root)`
4. Click **Save**

Your site will be live at `https://thearminashrafi.github.io` within a minute or two.

**Every subsequent push** to `main` deploys automatically. The wiki manifest Action also runs on push, so new wiki notes are live without any extra steps.

---

## Automatic Wiki Updates (GitHub Action)

The file `.github/workflows/wiki-manifest.yml` runs automatically when you push any `.md` file inside `wiki/`. It:

1. Scans all `.md` files in `wiki/` (excluding `templates/` and `.obsidian/`)
2. Parses YAML frontmatter for title, tags, and date
3. Embeds the full note content into the manifest
4. Writes `wiki/manifest.json` and `wiki/manifest.js`
5. Commits them back to the branch with the message `chore: update wiki manifest [skip ci]`

You do not need to run `build-manifest.py` yourself when deploying — only when you want to preview locally before pushing.

**If the Action fails:** go to the **Actions** tab on GitHub, find the failed run, and read the error. The most common causes are a malformed frontmatter block in a `.md` file (e.g. an unmatched quote or colon in the title).

---

## Local Development

No build server is required for most editing. Open any `.html` file directly in your browser.

**One exception:** `wiki/index.html` and `wiki/page.html` load `manifest.js` via a `<script src>` tag, which works fine on `file://`. However, if you add a new note and haven't re-run `build-manifest.py`, the new note won't appear.

For full local fidelity (including the blog's `fetch`-based features, if you add any), run a simple HTTP server:

```bash
# Python (built-in, run from repo root)
python3 -m http.server 8000
# then open http://localhost:8000
```

or if you have Node:

```bash
npx serve .
```

---

## Adding / Editing Content Cheatsheet

| Task | What to do |
|---|---|
| Update bio or photo | Edit `index.html` → `.hero` section |
| Add an experiment | Edit `research.html` → `experiments` array in `<script>` |
| Add a publication | Edit `research.html` → Publications section |
| Add a blog post | Copy `blogs/template.html`, write it, add entry to `posts[]` in `blogs/index.html` |
| Add a wiki note | Create `.md` in `wiki/` in Obsidian, run `python3 wiki/build-manifest.py`, commit |
| Add a learning resource | Edit `learning.html` → copy a `.resource` block |
| Change accent color | Edit `--accent` in `styles.css` `:root` and `:root.dark` blocks |
| Change email address | Edit `tutoring.html` → `const to = '...'` in the form script |
| Update CV | Replace `assets/Resume_PhD-2.pdf` (or update the `href` in `index.html`) |
