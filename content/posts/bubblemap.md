---
title: "大城市人口增长速度🦚"
date: 2020-05-27
lastmod: 2020-05-27
author: ["QGQ"]

categories:
- "绘图"
- "map&sf"

tags:
- "R"

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

![](/zh/posts/figure/bubblemap.png)
<center>上图即为最终效果</center>

## 下载数据
将代码中的**`~/文档/`**更换为要保存的目录.
```r
download.file("https://raw.githubusercontent.com/QGQ931001/git-tutorial/master/bigcity/data-bKvwd.csv", destfile = "~/文档/data-bKvwd.csv" )
download.file("https://raw.githubusercontent.com/QGQ931001/git-tutorial/master/bigcity/world.geo.json", destfile = "~/文档/world.geo.json" )
```

## 加载R包
需要的R包如下所示.

```r
library(sf)
library(readr)
library(tidyverse)
library(hrbrthemes)
library(ggtext)
```
<!-- more -->

## 读取各大城市人口数据并计算年平均人口增长率
`worldmap`为`josn`格式的地图数据,`st_transform`为进行投影坐标变换的函数.

```r
worldmap <- read_sf('/home/qgq/文档/world.geo.json') %>%
  st_transform(crs = 4326)
```

1. `data-bKvwd`包含了世界多个城市的经纬度信息以及多年份的人口数据.
2. `dplyr::select`函数主要用于筛选`data-bKvwd`中的**4**个关键变量,包含经纬度(Lon, Lat),以及**2000**年和**2016**年的人口数据.
3. `st_as_sf`是`sf`包中的函数,其将外来对象转换为`sf`对象,最终数据存储为`con_df`.
3. `con_df$growth.rate`表示在`con_df`数据框^[可以通过`class(con_df)`查看`con_df`属于哪些类]中添加一个`growth.rate`变量,也可以进行对数增长率的计算.


```r
read_csv('~/文档/data-bKvwd.csv') %>%
  dplyr::select(Lat, Lon, `2000`,`2016`) %>%
  st_as_sf(coords = c("Lon", "Lat"), crs = 4326) -> con_df
con_df$growth.rate <- (as.numeric(con_df$`2016`)-as.numeric(con_df$`2000`))/as.numeric(con_df$`2000`)/17
con_df$log.growth.rate <- log(as.numeric(con_df$`2016`)/as.numeric(con_df$`2000`))/17
```

## 对数据进行离散化处理
连续的数据虽然包含更多信息,但是糅合一些离散化的策略,使用颜色或其它图形属性表征,能呈现出更直观的信息.
使用`mutate`函数将`growth.rate`离散化为`interval`.


```r
con_df <- con_df %>% mutate(
    interval = case_when(
      growth.rate < 0 ~ "负增长",
      growth.rate >= 0 & growth.rate < 0.025 ~ "0～2.5%",
      growth.rate >= 0.025 & growth.rate < 0.05 ~ "2.5%～5%",
      growth.rate >= 0.05  ~ "5%以上"
    )
  )
```

与此同时,计算出`growth.rate`的最大值用于辅助分段.


```r
max.gr <- as.numeric(
  max(con_df$growth.rate,na.rm = T))  #>求growth.rate的最大值
mybreaks <- c(0, 0.025, 0.05,max.gr) #>进行分段
```

## 绘图
代码如下,图见上文.

```r
ggplot(worldmap) +
  geom_sf(size = 0.1, color = "#708090", fill = "grey",alpha=0.05) +
  geom_sf(data = con_df,  aes(size = abs(growth.rate),
                              color = interval,
                              alpha = abs(growth.rate))) +
  scale_size_continuous(name = "Average Growth Rate",
                        range = c(2,2.41*4),
                        breaks = mybreaks)  +
  scale_alpha_continuous(name = "Average Growth Rate",
                         range = c(0.4,0.7),
                         breaks = mybreaks) +
  scale_color_manual(values = c("#D9EF8B", "#A6D96A", "#66BD63","#D73027")) +
  coord_sf(crs = "+proj=eck4")+
  theme_minimal(base_family = "Roboto") +
  theme(
    axis.text = element_blank(),
    axis.title = element_blank(),
    panel.grid = element_blank(),
    legend.position = "none",
    plot.caption = element_text(color = "#708090", face = "italic",family = "Times New Roman",size = 11,hjust = 0.95),
    plot.title = element_text(color = "#708090",family = "Times New Roman", size = 19))+
  labs(title = "How fast do big cities grow?",
       subtitle = "<b style='color:#D73027'>Negative Growth</b> / <b style='color:#D9EF8B'>0~2.5%</b> /
       <b style='color:#A6D96A'>2.5%~5%</b> / <b style='color:#66BD63'>5% Plus</b>",
       caption = "Data Source: How fast do big cities grow?")+
  theme(plot.subtitle = element_markdown(lineheight = 1.1))
```
