---
title: "shell脚本笔记(1)"
date: 2020-05-25 00:00:00
lastmod: 2020-05-25 00:00:00
author: ["QGQ"]

categories:
- "经济研究"

tags:
- "论文笔记"

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



**********************************

# 引言
shell是用C语言编写的程序,但它自身同时也是一种程序设计语言.你可能经常听说"shell脚本",但实际上shell编程并非等同于"shell脚本"编程,前者指shell程序本身的开发,后者则是利用shell程序进行开发.都说java和javascript的区别是周杰和周杰伦的区别,shell和shell script或许也有那么点意思.

# shell脚本
似乎任何程序学习都是从"Hello World!"开始的,对于**shell**而言:

```bash
#!/bin/bash
echo "Hello World !"
```

**#!**是个标记,告知这段命令将用bash执行.echo则是一个向窗口展示文本的命令.
你可以将以上代码框的内容存为一个以.sh为后缀的文件,比如**hw.sh**,并赋予文件执行权限:

```shell
chmod +x ./hw.sh         #赋予执行权限
bash hw.sh               #执行脚本
```
<!-- more -->
未完待续
