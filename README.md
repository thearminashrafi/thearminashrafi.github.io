# thearminashrafi.github.io

Personal academic website — plain HTML/CSS/JS, hosted on GitHub Pages, no build step.

---

## First-time setup

**Prerequisites:** Git.

```bash
# Clone the repo
git clone https://github.com/thearminashrafi/thearminashrafi.github.io.git
cd thearminashrafi.github.io
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
├── one-on-one.html     # One-on-one sessions + contact
├── styles.css          # Shared styles (edit this to change colors/fonts)
│
├── blogs/
│   ├── index.html      # Post listing
│   └── template.html   # Copy this to write a new post
│
└── assets/             # Images, PDFs
```

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

Blog posts are plain HTML files. After writing and registering the post, push manually:

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

For any edits (HTML pages, styles, assets):

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
| Add a blog post | Copy `blogs/template.html`, write it, add to `posts[]` in `blogs/index.html`, `git push` |
| Add an experiment | Edit `experiments[]` in `research.html`, `git push` |
| Update bio / photo | Edit `index.html` → `.hero` section; replace `assets/armin.jpg` |
| Change accent color | Edit `--accent` in `styles.css` |
| Change contact email | Edit `one-on-one.html` → `emailBtn` click handler |
| Update CV | Replace `assets/Resume_PhD.pdf` |
