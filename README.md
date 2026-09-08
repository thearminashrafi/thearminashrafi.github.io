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
├── index.html          # Home — profile, bio, and publications
├── contact.html        # Contact
├── styles.css          # Shared styles (edit this to change colors/fonts)
│
├── posts/               # Blog posts, written in plain Markdown (edit these)
│
├── blogs/
│   ├── index.html      # Post listing (generated — don't hand-edit the posts[] array)
│   ├── *.html           # Individual post pages (generated from posts/*.md — don't hand-edit)
│   └── template.html   # The page shell used to generate a post — edit this to change how ALL posts look
│
├── scripts/
│   ├── new_post.py      # Start a new post
│   └── build_post.py    # Turn a post's Markdown into its page
│
└── assets/             # Images, PDFs
```

---

## Reflections (Blog)

Posts are written as plain Markdown files in `posts/`. A script turns each one
into the actual HTML page in `blogs/` and keeps the post listing in
`blogs/index.html` up to date — so writing a post never involves touching HTML.

### 1. Start a post

```bash
python3 scripts/new_post.py "My Post Title"
```

This prompts for an excerpt and read time, then creates `posts/my-post-title.md`
with a front-matter header already filled in:

```
---
title: My Post Title
date: 2026-09-07
excerpt: One sentence shown in the listing.
read: 5
---

Write your post here, in plain Markdown.
```

### 2. Write the post

Open `posts/my-post-title.md` in any text editor and write the post below the
`---` header, in plain Markdown — headings, lists, `code`, fenced code blocks,
blockquotes, and inline math `$a^2+b^2=c^2$` / display math `$$\int_0^1 x\,dx$$`
all render on the live page.

You can freely edit the front-matter fields (`title`, `date`, `excerpt`, `read`)
at the top of the file too — they control what's shown in the post listing.

### 3. Build the page

```bash
python3 scripts/build_post.py my-post-title
```

This generates `blogs/my-post-title.html` from `blogs/template.html` and the
Markdown you wrote, and adds (or updates) the post's entry in
`blogs/index.html`. It's safe to run again after further edits — it
regenerates the page and updates the listing in place rather than duplicating
it.

To rebuild every post at once (for example after changing `blogs/template.html`,
the page shell all posts share):

```bash
python3 scripts/build_post.py --all
```

### 4. Preview locally (optional)

```bash
python3 -m http.server 8000
```

then open `http://localhost:8000/blogs/my-post-title.html` in a browser.

### 5. Push

```bash
git add posts/ blogs/
git commit -m "blog: add post on policy gradients"
git push origin main
```

The site updates at `https://thearminashrafi.github.io` within a minute or two.

### Changing how posts look

`blogs/template.html` is the shell every post is generated from — fonts,
layout, syntax highlighting, math rendering. Edit it, then run
`python3 scripts/build_post.py --all` to apply the change to every existing
post.

---

## Research — Adding a publication

In `index.html`, find the `.pub-list` block and copy an existing `.pub-entry` div,
updating the title, authors, venue, links, thumbnail, abstract, and BibTeX.

Then push:

```bash
git add index.html
git commit -m "research: add publication on ..."
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
| Add a blog post | `python3 scripts/new_post.py "Title"` → write `posts/title.md` → `python3 scripts/build_post.py title` → `git push` |
| Rebuild all posts | `python3 scripts/build_post.py --all` |
| Add a publication | Copy a `.pub-entry` block in `index.html` → `.pub-list`, `git push` |
| Update bio / photo | Edit `index.html` → `.research-intro` section; replace `assets/armin.jpg` |
| Change accent color | Edit `--accent` in `styles.css` |
| Change contact email | Edit `contact.html` → `emailBtn` click handler |
| Update CV | Replace `assets/Resume_PhD.pdf` |

---

## Notes (Quartz)

Your Obsidian vault at `wiki/` is published at `https://thearminashrafi.github.io/wiki/` using
[Quartz](https://quartz.jzhao.xyz/). `wiki/` is your live Obsidian vault (open it directly in Obsidian) —
only `wiki/.obsidian/` (Obsidian's local app settings) is excluded from git; everything else you write
there gets published.

### How it works

- `quartz/` is a self-contained Quartz project (its own `package.json`, ignored `node_modules/`).
- `quartz/content` is a symlink to `../wiki`, so Quartz always reads your current notes — nothing to sync by hand.
- A GitHub Actions workflow (`.github/workflows/deploy.yml`) builds Quartz from `wiki/` and combines it
  with the rest of this site (`index.html`, `blogs/`, etc.) into `/wiki` on every push to `main`.

### Publishing notes

Just write in Obsidian, then:

```bash
git add wiki/
git commit -m "notes: <what changed>"
git push origin main
```

GitHub Actions rebuilds and redeploys automatically — check the **Actions** tab on GitHub for progress.
The site updates within a couple of minutes at `https://thearminashrafi.github.io/wiki/`.

### Excluding a note from publishing

Add `private: true` to a note's YAML frontmatter, e.g.:

```
---
private: true
---
```

or add its folder name to `ignorePatterns` in `quartz/quartz.config.yaml`.

### Previewing locally

```bash
cd quartz
npx quartz build --serve
```

then open the printed `localhost` URL.

### One-time setup (already done, for reference)

This repo's GitHub Pages source needs to be set to **GitHub Actions** rather than "Deploy from a branch":
repo → **Settings** → **Pages** → **Source** → **GitHub Actions**.
