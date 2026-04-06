#!/usr/bin/env python3
"""
Convert Hexo posts to Hugo format
"""

import os
import re
from datetime import datetime

SOURCE_DIR = r"C:\Users\Lenovo\Nutstore\1\source\_posts"
TARGET_DIR = r"C:\Users\Lenovo\Nutstore\1\content\posts"

# Hugo frontmatter template
HUGO_TEMPLATE = """---
title: "{title}"
date: {date}
lastmod: {lastmod}
author: ["{author}"]

categories:
{categories}

tags:
{tags}

description: ""
summary: ""
weight:
slug: ""
draft: false
comments: false
showToc: true
TocOpen: true
autonumbering: true
hidemeta: false
disableShare: true
searchHidden: false
showbreadcrumbs: true
mermaid: true
mathjax: true
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

{content}
"""

def parse_hexo_frontmatter(content):
    """Parse Hexo frontmatter and content"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content

    frontmatter_raw = match.group(1)
    body = match.group(2)

    # Parse frontmatter fields
    fm = {}
    lines = frontmatter_raw.split('\n')
    current_key = None
    current_value = []
    in_list = False

    for line in lines:
        if (line.startswith('  - ') or line.startswith('- ')) and ':' not in line.replace('  - ', '').replace('- ', ''):
            # List item (simple)
            value = line.replace('  - ', '').replace('- ', '').strip()
            if current_key and isinstance(fm.get(current_key), list):
                fm[current_key].append(value)
            elif current_key:
                fm[current_key] = [value]
        elif line.startswith('  - ') or line.startswith('- '):
            # List item with key-value (like "  - 姓名:杜宝瑞")
            value = line.replace('  - ', '').replace('- ', '').strip()
            if current_key and isinstance(fm.get(current_key), list):
                fm[current_key].append(value)
            elif current_key:
                fm[current_key] = [value]
        elif ':' in line:
            # Key-value pair
            if current_key and current_value and not isinstance(fm.get(current_key), list):
                fm[current_key] = '\n'.join(current_value).strip()

            parts = line.split(':', 1)
            current_key = parts[0].strip()
            value = parts[1].strip().strip("'\"")

            if current_key in ['categories', 'tags']:
                fm[current_key] = [value] if value else []
            else:
                current_value = [value] if value else []
                fm[current_key] = value

    # Handle last key
    if current_key and current_value and not isinstance(fm.get(current_key), list):
        fm[current_key] = '\n'.join(current_value).strip()

    return fm, body

def format_categories(categories):
    """Format categories for Hugo"""
    if isinstance(categories, str):
        categories = [categories]
    if not categories:
        categories = []
    lines = ['- ""']
    for cat in categories:
        lines.append(f'- "{cat}"')
    return '\n'.join(lines)

def format_tags(tags):
    """Format tags for Hugo"""
    if isinstance(tags, str):
        tags = [tags]
    if not tags:
        tags = []
    lines = []
    for tag in tags:
        lines.append(f'- "{tag}"')
    return '\n'.join(lines) if lines else '- ""'

def convert_img_paths(content):
    """Convert Hexo img paths to Hugo/Netlify paths"""
    # /figure/xxx.png -> /zh/posts/figure/xxx.png
    content = re.sub(r'src="/figure/', 'src="/zh/posts/figure/', content)
    # /figure_rdata_science/xxx.png -> /zh/posts/figure_rdata_science/xxx.png
    content = re.sub(r'src="/figure_rdata_science/', 'src="/zh/posts/figure_rdata_science/', content)
    # /paper_source/xxx.png -> /zh/posts/paper_source/xxx.png
    content = re.sub(r'src="/paper_source/', 'src="/zh/posts/paper_source/', content)
    # /image/xxx.jpg -> /zh/posts/image/xxx.jpg
    content = re.sub(r'src="/image/', 'src="/zh/posts/image/', content)
    return content

def convert_html_img_to_markdown(content):
    """Convert HTML <img> tags to Markdown format"""
    # Convert <img src="..." ... /> to ![...](...)
    def replace_img(match):
        src = match.group(1)
        # Extract title/alt if present
        alt_match = re.search(r'title="([^"]*)"', match.group(0))
        alt = alt_match.group(1) if alt_match else ''
        return f'![{alt}]({src})'

    # Pattern for <img ... src="..." ... />
    content = re.sub(r'<img\s+[^>]*src="([^"]*)"[^>]*/>', replace_img, content)
    content = re.sub(r'<img\s+[^>]*src="([^"]*)"[^>]*>', replace_img, content)

    # Also handle <center> tags around images
    content = re.sub(r'<center>\s*!\[', '![', content)
    content = re.sub(r'\]\(/zh/posts/', '](/zh/posts/', content)

    return content

def convert_post(filename):
    """Convert a single Hexo post to Hugo format"""
    filepath = os.path.join(SOURCE_DIR, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = parse_hexo_frontmatter(content)
    if not fm:
        print(f"Could not parse frontmatter for {filename}")
        return

    # Extract fields
    title = fm.get('title', '').replace('"', '\\"')
    author = fm.get('author', '秦国庆')
    date_str = fm.get('date', datetime.now().strftime('%Y-%m-%d'))
    categories = fm.get('categories', [])
    tags = fm.get('tags', [])

    # Parse date
    try:
        if isinstance(date_str, str):
            # Handle various date formats
            for fmt in ['%Y-%m-%d', '%m/%d/%Y', '%Y-%m-%d %H:%M:%S']:
                try:
                    date = datetime.strptime(date_str.replace("'", '').strip(), fmt)
                    date_str = date.strftime('%Y-%m-%d')
                    break
                except:
                    pass
    except:
        date_str = datetime.now().strftime('%Y-%m-%d')

    lastmod = date_str

    # Format categories and tags
    categories_str = format_categories(categories)
    tags_str = format_tags(tags)

    # Process body - convert image paths
    body = convert_img_paths(body)
    body = convert_html_img_to_markdown(body)

    # Generate Hugo frontmatter
    hugo_fm = HUGO_TEMPLATE.format(
        title=title,
        date=date_str,
        lastmod=lastmod,
        author=author,
        categories=categories_str,
        tags=tags_str,
        content=body.strip()
    )

    # Write output
    output_path = os.path.join(TARGET_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(hugo_fm)

    print(f"Converted: {filename}")

def main():
    # List of posts to convert
    posts = [
        'taobaocun.md',
        'bubblemap.md',
        'testof_mathequation_fontface.md',
        'paper2.md',
        'DID1.md',
        'biprobit_iv.md',
        'jingting1.md',
        'paper1.md',
        'shell_1.md',
        'r_for_data_science.md',
        'ho-1959-population-china.md',
        'lee-2001-one-quarter-humanity.md',
        'elvin-1973-pattern-chinese-past.md',
    ]

    for post in posts:
        try:
            convert_post(post)
        except Exception as e:
            print(f"Error converting {post}: {e}")

    print("\nAll conversions complete!")

if __name__ == '__main__':
    main()