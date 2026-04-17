---
title: "画一幅我农所在地的道路图"
date: 5/29/2020
lastmod: 5/29/2020
author: ["秦国庆"]

categories:
- "绘图"

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


## 效果展示
<img src="/zh/posts/figure/yanglingroad.png" width="80%" height="80%" align="middle" style="display: block; margin: auto;" />
<center>上图即为最终效果</center>

## 一些必备的工具
一张json格式的我农地图,或者杨陵地图,可从[我的github仓库下载](https://raw.githubusercontent.com/QGQ931001/git-tutorial/master/yangling_map/yangling.json)

```r
download.file("https://raw.githubusercontent.com/QGQ931001/git-tutorial/master/yangling_map/yangling.json", destfile = "~/文档/yangling.json" )
```
<!-- more -->

## 绘制路网地图
导入以下R 包:


```r
library(osmdata)
library(dodgr)
library(tidyverse)
library(sf)
```

读入杨陵区的数据:


```r
yl <- read_sf("~/文档/yangling.json") %>%
  st_make_valid()
```

获取杨陵区的经纬度范围:

```r
st_bbox(yl) %>%
  matrix(nrow = 2,
         dimnames = list(c("x", "y"),
                         c("min", "max"))) -> ebox
ebox
```

```
#>         min       max
#> x 107.94598 108.13869
#> y  34.22145  34.33377
```
提取杨陵区的街道路线:

```r
sraw <- dodgr_streetnet(ebox)
```
把数据保存为**rds**:


```r
sraw %>%
  write_rds('sraw.rds')
```

提取**ebox**和**yl**相交的区域:

```r
streets <- sraw %>%
  st_make_valid() %>%
  st_intersection(yl)
```

然后绘图:


```r
ggplot() +
  geom_sf(data = streets, show.legend = F, size = 0.2 ,color = "#DDE080" ) +
  theme_ipsum(base_family = "Times New Roman") +
  theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          axis.text.x = element_blank(),
          axis.text.y = element_blank(),
          axis.title.x = element_blank(),
          axis.title.y = element_blank(),
          plot.background = element_rect(fill = "#140035",
                                         color = "#140035"),
          panel.background = element_rect(fill = "#140035",
                                          color = "#140035")) +
    labs(y = "")
```
