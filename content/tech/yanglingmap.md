---
title: "画一幅我农所在地的道路图"
date: 2020-05-29
lastmod: 2025-01-02
author: ["秦国庆"]

categories:
- "绘图"

tags:
- "R"



description: "" # 文章描述，与搜索优化相关
summary: "" # 文章简单描述，会展示在主页
weight: # 输入1可以顶置文章，用来给文章展示排序，不填就默认按时间排序
slug: ""
draft: false # 是否为草稿
comments: true
showToc: true # 显示目录
TocOpen: true # 自动展开目录
autonumbering: true # 目录自动编号
hidemeta: false # 是否隐藏文章的元信息，如发布日期、作者等
disableShare: true # 底部不显示分享栏
searchHidden: false # 该页面可以被搜索到
showbreadcrumbs: true #顶部显示当前路径
mermaid: true
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

## 效果展示

![上图即为最终效果](/zh/posts//figure/yanglingroad.png)

## 一些必备的工具
一张json格式的我农地图，或者杨陵地图,可从[我的github仓库下载](https://raw.githubusercontent.com/QGQ931001/git-tutorial/master/yangling_map/yangling.json)

```r
download.file("https://raw.githubusercontent.com/QGQ931001/git-tutorial/master/yangling_map/yangling.json", destfile = "~/文档/yangling.json" )
```
<!-- more -->

## 绘制路网地图
导入以下R 包：


```r
library(osmdata)
library(dodgr)
library(tidyverse)
library(sf)
```

读入杨陵区的数据：


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
提取杨陵区的街道路线：

```r
sraw <- dodgr_streetnet(ebox)
```
把数据保存为**rds**:


```r
sraw %>%
  write_rds('sraw.rds')
```

提取**ebox**和**yl**相交的区域：

```r
streets <- sraw %>%
  st_make_valid() %>%
  st_intersection(yl)
```

然后绘图：


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
