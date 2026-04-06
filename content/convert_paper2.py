#!/usr/bin/env python3
"""Convert paper2.md separately"""

import os
import re
from datetime import datetime

SOURCE_DIR = r"C:\Users\Lenovo\Nutstore\1\source\_posts"
TARGET_DIR = r"C:\Users\Lenovo\Nutstore\1\content\posts"

def convert_paper2():
    filepath = os.path.join(SOURCE_DIR, 'paper2.md')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from the multiline title
    title_match = re.search(r"title: >-\s*\n\s*(.+)", content)
    title = "文献阅读: Microinsurance and Economic Activities" if title_match else "文献阅读"

    # Extract other fields
    tags = ["文献阅读"]
    categories = ["实验经济学", "保险"]
    author = "杜宝瑞"
    date = "2020-06-06"

    # Find body content (after ---)
    body_match = re.search(r'^---.*?\n---\n(.*)$', content, re.DOTALL)
    body = body_match.group(1) if body_match else ""

    # Convert image paths
    body = re.sub(r'src="/paper_source/', 'src="/zh/posts/paper_source/', body)

    # Convert HTML img to markdown
    def replace_img(match):
        src = match.group(1)
        return f'![]({src})'

    body = re.sub(r'<img\s+[^>]*src="([^"]*)"[^>]*/>', replace_img, body)
    body = re.sub(r'<img\s+[^>]*src="([^"]*)"[^>]*>', replace_img, body)

    hugo_content = f"""---
title: "{title}"
date: {date}
lastmod: {date}
author: ["{author}"]

categories:
- "实验经济学"
- "保险"

tags:
- "文献阅读"

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

{body.strip()}
"""

    output_path = os.path.join(TARGET_DIR, 'paper2.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(hugo_content)
    print("Converted: paper2.md")

if __name__ == '__main__':
    convert_paper2()