#!/usr/bin/env python3
"""Start a new blog post as a plain Markdown file.

Usage:
  python3 scripts/new_post.py "My Post Title"

Creates posts/<slug>.md with a front-matter header (title, date, excerpt,
read time) already filled in. Open that file in any text editor and write
the post below the header, in plain Markdown.

When the post is ready, run:
  python3 scripts/build_post.py <slug>
to generate the actual site page from it.
"""
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def main():
    if len(sys.argv) < 2:
        title = input("Post title: ").strip()
    else:
        title = " ".join(sys.argv[1:]).strip()
    if not title:
        sys.exit("A title is required.")

    slug = slugify(title)
    POSTS.mkdir(parents=True, exist_ok=True)
    post_path = POSTS / f"{slug}.md"
    if post_path.exists():
        sys.exit(f"{post_path} already exists — pick a different title or delete it first.")

    excerpt = input("One-sentence excerpt (shown in the listing): ").strip()
    if not excerpt:
        excerpt = "TODO: write an excerpt."

    read = input("Estimated read time in minutes [5]: ").strip() or "5"

    today = datetime.date.today().isoformat()

    front_matter = (
        "---\n"
        f"title: {title}\n"
        f"date: {today}\n"
        f"excerpt: {excerpt}\n"
        f"read: {read}\n"
        "---\n"
    )
    body = (
        "\n"
        "Write your post here, in plain Markdown. Standard syntax works:\n"
        "\n"
        "- bullet lists\n"
        "- `inline code`\n"
        "- **bold**, *italic*\n"
        "- inline math like $a^2 + b^2 = c^2$ and display math like $$\\int_0^1 x\\,dx = \\tfrac12$$\n"
        "\n"
        "## A section heading\n"
        "\n"
        "```python\n"
        "# fenced code blocks are syntax-highlighted\n"
        "import jax.numpy as jnp\n"
        "```\n"
        "\n"
        "> A blockquote, if you want one.\n"
    )
    post_path.write_text(front_matter + body)

    print(f"\nCreated {post_path.relative_to(ROOT)}")
    print("Open it, replace the placeholder text below the --- header, and write your post.")
    print(f"\nWhen it's ready:  python3 scripts/build_post.py {slug}")


if __name__ == "__main__":
    main()
