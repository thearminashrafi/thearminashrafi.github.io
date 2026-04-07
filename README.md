# thearminashrafi.github.io

Personal academic website — plain HTML/CSS/JS, hosted on GitHub Pages, no build step.

---

## First-time setup

**Prerequisites:** Git, Python 3, and [Obsidian](https://obsidian.md) (free).

```bash
# Clone the repo
git clone https://github.com/thearminashrafi/thearminashrafi.github.io.git
cd thearminashrafi.github.io

# Make the sync script executable (only needed once)
chmod +x wiki-sync.sh
```

**Enable GitHub Pages** (one time, on GitHub):

1. Go to the repo → **Settings** → **Pages**
2. Source: **Deploy from a branch**, branch: `main`, folder: `/ (root)`
3. Click **Save** — the site goes live at `https://thearminashrafi.github.io` within a minute

---

## Site Structure

```
├── index.html          # Home / profile
├── research.html       # Research, experiments, publications, projects
├── learning.html       # Learning materials
├── tutoring.html       # Tutoring + contact form
├── styles.css          # Shared styles (edit this to change colors/fonts)
├── wiki-sync.sh        # Script: rebuild wiki manifest and push
│
├── blogs/
│   ├── index.html      # Post listing
│   └── template.html   # Copy this to write a new post
│
├── wiki/
│   ├── index.html      # Wiki note index
│   ├── page.html       # Note renderer
│   ├── manifest.js     # Auto-generated — do not edit by hand
│   ├── build-manifest.py
│   ├── templates/
│   │   └── note.md     # Obsidian template for new notes
│   └── .obsidian/      # Vault config (committed — travels with the repo)
│
└── assets/             # Images, PDFs
```

---

## Wiki

### Opening the vault

1. Open Obsidian → **Open folder as vault** → select the `wiki/` folder.

The `.obsidian/` config is already committed, so plugins (file explorer, backlinks, graph, templates) are pre-configured — no setup needed.

---

### Creating a new note

**Step 1 — Create and name the file**

In Obsidian press `Cmd+N`. Immediately rename the file to something meaningful (e.g. `policy-gradients.md`) — press `Enter` on the file in the sidebar or use `F2`. The filename becomes the note's URL on the website, so use lowercase with hyphens.

**Step 2 — Insert the template**

Press `Cmd+P`, type `template`, select **Templates: Insert template**, then choose **note**.

The following frontmatter is stamped at the top — the date is filled in automatically by Obsidian:

```yaml
---
title: Your Note Title
tags: []
date: 2026-04-07
---
```

Fill in the fields:

| Field | What to write |
|---|---|
| `title` | Human-readable title shown as the page heading on the website |
| `tags` | List of tags, e.g. `[rl, math]` — drives the filter buttons on the wiki index |
| `date` | Today's date — auto-filled, just verify it's correct |

> **Tip:** keep the `title` and filename in sync. If the title is `Policy Gradients`, the filename should be `policy-gradients.md`. This makes wikilinks predictable.

**Step 3 — Write your note**

Write in Markdown below the frontmatter block. See [Math](#math), [Links between notes](#links-between-notes), and [Callouts](#callouts) below.

---

### Math

Rendered by KaTeX — use standard LaTeX syntax.

**Inline:** `$\gamma \in [0,1)$`

**Display:**
```
$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \right]
$$
```

Full list of supported commands: [katex.org/docs/supported](https://katex.org/docs/supported.html)

---

### Links between notes

Use Obsidian's double-bracket syntax — works in both Obsidian and on the website:

```
[[Note Name]]                 — links to Note Name.md
[[Note Name|Custom text]]     — same link, different display text
[[subfolder/Note Name]]       — note inside a subfolder
```

The website resolves links case-insensitively and treats spaces, hyphens, and underscores as equivalent, so `[[Policy Gradients]]` and `[[policy-gradients]]` both resolve to the same note.

If you **rename a note**, use Obsidian's built-in rename (`F2`) — it automatically updates all `[[wikilinks]]` pointing to that file within the vault.

---

### Callouts

```markdown
> [!NOTE]
> Any additional context worth highlighting.

> [!WARNING]
> Something to watch out for.

> [!TIP]
> A helpful shortcut or insight.
```

Any word after `[!` becomes the callout title.

---

### Images in notes

Put image files in `wiki/assets/` (create the folder if it doesn't exist). Reference them in Markdown with a path relative to the note:

```markdown
![Alt text](assets/my-diagram.png)
```

Obsidian will also display them in the editor. If your note is in a subfolder (e.g. `wiki/rl/my-note.md`), use `../assets/my-diagram.png`.

---

### Publishing notes

Run the sync script from the repo root whenever you want to publish:

```bash
./wiki-sync.sh
```

This will:
1. Rebuild `manifest.js` from all your `.md` files
2. Commit the changes with an auto-generated message
3. Pull any remote updates
4. Push to GitHub — the site updates within a minute or two

**If you delete or rename a note**, run `./wiki-sync.sh` as normal — the manifest is rebuilt from scratch each time, so removed or renamed files are automatically dropped from the index.

---

## Blog

### Creating a post

1. Copy `blogs/template.html` → `blogs/my-post-name.html`
2. Edit the `<title>` and `<meta name="description">` at the top
3. Update the post title, date, and tags in the `<header>` section
4. Write your content inside `<article id="prose-content" class="prose">`

**Writing in Markdown instead of HTML:**

Uncomment the `<script id="md-content" type="text/markdown">` block in the template and write Markdown (including math with `$...$` and `$$...$$`) inside it — the page renders it automatically.

### Registering the post

Add an entry to the `posts` array in `blogs/index.html`:

```js
{
  title:   "My Post Title",
  date:    "2025-11-01",        // ISO format — used for sorting
  display: "Nov 1, 2025",       // shown in the listing UI
  tags:    ["rl", "math"],
  excerpt: "One sentence shown in the listing.",
  href:    "my-post-name.html"
}
```

### Pushing the post

Blog posts are plain HTML files — `wiki-sync.sh` does **not** handle them. After writing and registering the post, push manually:

```bash
git add blogs/
git commit -m "blog: add post on policy gradients"
git push origin main
```

---

## Research — Adding an experiment

In `research.html`, find the `experiments` array in the `<script>` block and add:

```js
{
  title:  "Experiment title",
  date:   "Nov 2025",
  status: "active",        // "active" | "done" | "planned"
  tags:   ["rl", "jax"],
  desc:   "What you tried and what you found.",
  links:  [{ label: "Draft", href: "assets/draft.pdf" }]  // optional
}
```

Then push:

```bash
git add research.html
git commit -m "research: add experiment on ..."
git push origin main
```

---

## Pushing other changes

`wiki-sync.sh` only handles wiki notes. For any other edits (HTML pages, styles, assets):

```bash
git add <files>
git commit -m "describe what changed"
git pull --rebase origin main   # pull first to avoid conflicts
git push origin main
```

---

## Cheatsheet

| Task | What to do |
|---|---|
| Publish wiki notes | `./wiki-sync.sh` |
| Add a wiki note | `Cmd+N` in Obsidian → rename file → insert `note` template → write → `./wiki-sync.sh` |
| Delete / rename a wiki note | Do it in Obsidian, then `./wiki-sync.sh` |
| Add a blog post | Copy `blogs/template.html`, write it, add to `posts[]` in `blogs/index.html`, `git push` |
| Add an experiment | Edit `experiments[]` in `research.html`, `git push` |
| Update bio / photo | Edit `index.html` → `.hero` section; replace `assets/armin.jpg` |
| Add a learning resource | Edit `learning.html` → copy a `.resource` block |
| Change accent color | Edit `--accent` in `styles.css` |
| Change contact email | Edit `tutoring.html` → `const to = '...'` |
| Update CV | Replace `assets/Resume_PhD.pdf` |
