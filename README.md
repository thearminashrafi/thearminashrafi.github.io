# thearminashrafi.github.io

Personal academic website — plain HTML/CSS/JS, hosted on GitHub Pages, no build step.

---

## Site Structure

```
├── index.html          # Home / profile
├── research.html       # Research, experiments, publications, projects
├── learning.html       # Learning materials
├── tutoring.html       # Tutoring + contact form
├── styles.css          # Shared styles (edit this to change colors/fonts)
├── wiki-sync.sh        # Script: rebuild wiki and push (see below)
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

That's it. The `.obsidian/` config is already committed, so plugins and settings are pre-configured.

---

### Creating a new note

**Step 1 — Create the file**

In Obsidian press `Cmd+N`. A new untitled file opens.

**Step 2 — Insert the template**

Press `Cmd+P`, type `template`, select **Templates: Insert template**, then choose **note**.

This stamps the following frontmatter at the top of the file:

```yaml
---
title: Your Note Title
tags: []
date: 2025-11-01
---
```

Fill in the fields:

| Field | What to write |
|---|---|
| `title` | Human-readable title shown on the website |
| `tags` | List of tags, e.g. `[rl, math]` — used for filters on the wiki index |
| `date` | Today's date in `YYYY-MM-DD` format |

**Step 3 — Write your note**

Write in normal Markdown below the frontmatter block. See the sections below for math, links between notes, and callouts.

---

### Math

Rendered by KaTeX — use standard LaTeX syntax.

Inline: `$\gamma \in [0,1)$`

Display:
```
$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \right]
$$
```

Full list of supported commands: [katex.org/docs/supported](https://katex.org/docs/supported.html)

---

### Links between notes

Use Obsidian's double-bracket syntax — it works in both Obsidian and on the website:

```
[[Note Name]]                 — links to Note Name.md
[[Note Name|Custom text]]     — same link, different display text
[[subfolder/Note Name]]       — note inside a subfolder
```

The website resolves links case-insensitively and treats spaces, hyphens, and underscores as equivalent, so `[[Policy Gradients]]` and `[[policy-gradients]]` both resolve to the same note.

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

### Publishing notes

Run the sync script from the repo root whenever you want to publish:

```bash
./wiki-sync.sh
```

This will:
1. Rebuild `manifest.js` from all your `.md` files
2. Commit the changes
3. Pull any remote updates
4. Push to GitHub — the site updates within seconds

---

## Blog

### Creating a post

1. Copy `blogs/template.html` → `blogs/my-post-name.html`
2. Edit the `<title>` and `<meta name="description">` at the top
3. Update the post title, date, and tags in the `<header>` section
4. Write your content inside `<article id="prose-content" class="prose">`

**Writing in Markdown instead of HTML:**

Uncomment the `<script id="md-content" type="text/markdown">` block in the template and write Markdown (including math) inside it — the page will render it automatically.

### Registering the post

Add an entry to the `posts` array in `blogs/index.html`:

```js
{
  title:   "My Post Title",
  date:    "2025-11-01",
  display: "Nov 1, 2025",
  tags:    ["rl", "math"],
  excerpt: "One sentence shown in the listing.",
  href:    "my-post-name.html"
}
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
  links:  [{ label: "Draft", href: "assets/draft.pdf" }]
}
```

---

## Cheatsheet

| Task | What to do |
|---|---|
| Publish wiki notes | `./wiki-sync.sh` |
| Add a wiki note | Create in Obsidian → insert `note` template → fill frontmatter → write |
| Add a blog post | Copy `blogs/template.html`, write it, add to `posts[]` in `blogs/index.html` |
| Add an experiment | Edit `experiments[]` array in `research.html` |
| Update bio / photo | Edit `index.html` → `.hero` section; replace `assets/armin.jpg` |
| Add a learning resource | Edit `learning.html` → copy a `.resource` block |
| Change accent color | Edit `--accent` in `styles.css` |
| Change contact email | Edit `tutoring.html` → `const to = '...'` |
| Update CV | Replace `assets/Resume_PhD.pdf` |
