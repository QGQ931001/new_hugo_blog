---
title: "R数据科学_ggplot2笔记(1)"
date: 2020-05-26
lastmod: 2020-05-26
author: ["QGQ"]

categories:
- ""
- "2020-05-26"

tags:
- "2020-05-26"

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

## 一个说明

`ggplot2::ggplot()`指使用[**ggplot2**](https://ggplot2.tidyverse.org/)包中的`ggplot`函数,`::`表示快速调用某个包里的函数.


## 示例

使用`ggplot2`包中的`mpg`数据框,这份数据是一份汽车资料:


```r
knitr::kable(head(ggplot2::mpg, 10))
```



|manufacturer |model      | displ| year| cyl|trans      |drv | cty| hwy|fl |class   |
|:------------|:----------|:-----|----:|---:|:----------|:---|---:|---:|:--|:-------|
|audi         |a4         |   1.8| 1999|   4|auto(l5)   |f   |  18|  29|p  |compact |
|audi         |a4         |   1.8| 1999|   4|manual(m5) |f   |  21|  29|p  |compact |
|audi         |a4         |   2.0| 2008|   4|manual(m6) |f   |  20|  31|p  |compact |
|audi         |a4         |   2.0| 2008|   4|auto(av)   |f   |  21|  30|p  |compact |
|audi         |a4         |   2.8| 1999|   6|auto(l5)   |f   |  16|  26|p  |compact |
|audi         |a4         |   2.8| 1999|   6|manual(m5) |f   |  18|  26|p  |compact |
|audi         |a4         |   3.1| 2008|   6|auto(av)   |f   |  18|  27|p  |compact |
|audi         |a4 quattro |   1.8| 1999|   4|manual(m5) |4   |  18|  26|p  |compact |
|audi         |a4 quattro |   1.8| 1999|   4|auto(l5)   |4   |  16|  25|p  |compact |
|audi         |a4 quattro |   2.0| 2008|   4|manual(m6) |4   |  20|  28|p  |compact |

<!-- more -->

创建`ggplot2`图形,散点图:


```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) -> p
p
```

![plot of chunk unnamed-chunk-2](/zh/posts/figure_rdata_science/unnamed-chunk-2-1.png)

其中`mapping`是映射的意思,在`ggplot()`的`()`中出现的内容将传递之后的绘图函数,`p`保存了绘制好的图形,可以进一步进行美化和调整:


```r
p + theme_minimal(base_family = enfont) +
      theme(axis.text.x = element_blank(),
            axis.text.y = element_blank(),
            axis.title = element_text(size = 12))
```

![plot of chunk unnamed-chunk-3](/zh/posts/figure_rdata_science/unnamed-chunk-3-1.png)
可以将一些图片调整的代码存放在`modify`命名的一个对象中:


```r
theme_minimal(base_family = enfont) +
  theme(axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.title = element_text(size = 12)) -> modify
```

实际上,`ggplot2`的魅力之一在于通过颜色(**color**)、形状(**shape**)、透明度(**alpha**)等等属性展示超越**2**维的信息,比如:


```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = class)) +
  modify
```

![plot of chunk unnamed-chunk-5](/zh/posts/figure_rdata_science/unnamed-chunk-5-1.png)

另外一种展示超越2维属性的方法就是**分面**:


```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_wrap(~ class, nrow = 2) +
  modify
```

![plot of chunk unnamed-chunk-6](/zh/posts/figure_rdata_science/unnamed-chunk-6-1.png)

`facet_wrap()`中的第一个参数是**R**中的一种数据结构,叫作"公式",并非数学意义上的意思.也可以使用2个变量进行分面:


```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = class)) +
  facet_wrap(drv ~ cyl, nrow = 2) +
  modify
```

![plot of chunk unnamed-chunk-7](/zh/posts/figure_rdata_science/unnamed-chunk-7-1.png)

可以使用占位符`.`来代替`facet_wrap()`第一个参数中的`drv`,效果如下:


```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = class)) +
  facet_wrap(. ~ cyl, nrow = 2) +
  modify
```

![plot of chunk unnamed-chunk-8](/zh/posts/figure_rdata_science/unnamed-chunk-8-1.png)

## 几何对象

R并非只有`ggplot2`一种绘图方案,比如:


```r
set.seed(123)
n <- 1000
x1  <- matrix(rnorm(n), ncol = 2)
x2  <- matrix(rnorm(n, mean = 3, sd = 1.5), ncol = 2)
x   <- rbind(x1, x2)
head(x)
```

```
#>             [,1]        [,2]
#> [1,] -0.56047565 -0.60189285
#> [2,] -0.23017749 -0.99369859
#> [3,]  1.55870831  1.02678506
#> [4,]  0.07050839  0.75106130
#> [5,]  0.12928774 -1.50916654
#> [6,]  1.71506499 -0.09514745
```

```r
smoothScatter(x, xlab = "x1", ylab = "x2")
```

![plot of chunk unnamed-chunk-9](/zh/posts/figure_rdata_science/unnamed-chunk-9-1.png)

而ggplot2肯定并非只有一类几何对象,比如`geom_smooth`、`geom_line`、`geom_bar`等等,而这些对象生成的图层可以堆叠,比如:



```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = drv),
             show.legend = FALSE) +
  geom_smooth(mapping = aes(x = displ, y = hwy, linetype = drv),
              show.legend = FALSE)
```

![plot of chunk unnamed-chunk-10](/zh/posts/figure_rdata_science/unnamed-chunk-10-1.png)

`geom_smooth()`使用单个几何对象表示多行数据(一条曲线),而`geom_bar()`和`geom_point`则是多个几何对象(多个矩形或点),将`geom_smooth()`的`group`属性映射为一个离散变量时,这样`ggplot2`就会为这个分类变量的每个唯一值绘制一个独立的几何对象.



```r
ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy, group = drv)
 )
```

![plot of chunk unnamed-chunk-11](/zh/posts/figure_rdata_science/unnamed-chunk-11-1.png)


也可以为不同的图层指定不同的数据:


```r
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = drv)) +
  geom_smooth(data = dplyr::filter(mpg, class == "subcompact"),
              mapping = aes(x = displ, y = hwy),
              se = FALSE,
              show.legend = FALSE
 )
```

![plot of chunk unnamed-chunk-12](/zh/posts/figure_rdata_science/unnamed-chunk-12-1.png)


## 统计变换

`geom_bar()`函数可以绘制的基本条形图.


```r
ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut))
```

![plot of chunk unnamed-chunk-13](/zh/posts/figure_rdata_science/unnamed-chunk-13-1.png)

条形图
`x`
轴显示的是
`cut`
,这是
`diamonds`
数据集中的一个变量.
`y`
轴显示的是
`count`
,但
`count`
不是
`diamonds`
中的变量!
`count`
来自哪里呢?很多图形绘制的是数据集的原始数据,比如散点图.另外一些图形则可以绘制那些计算出的新数据,比如条形图.

绘图时用来计算新数据的算法称为stat(statistical transformation),即统计变换.你可能想要覆盖默认的统计变换.在以下代码中,我们将`geom_bar()`函数的统计变换从计数(默认值)修改为标识.这样我们就可以将条形的高度映射为`y`轴变量的初始值.遗憾的是,当随意说起条形图时,人们指的可能就是这种条形图,其中条形高度已经存在于数据中,而不是像前一个图一样,条形高度由对行进行计数来生成:


```r
demo <- tribble(
  ~a,      ~b,
  "bar_1", 20,
  "bar_2", 30,
  "bar_3", 40
)

ggplot(data = demo) +
  geom_bar(
    mapping = aes(x = a, y = b), stat = "identity"
  )
```

![plot of chunk unnamed-chunk-14](/zh/posts/figure_rdata_science/unnamed-chunk-14-1.png)

也可以改变统计变换的默认映射:


```r
ggplot(data = diamonds) +
  geom_bar(
    mapping = aes(x = cut, y = ..prop.., group = 1)
  )
```

![plot of chunk unnamed-chunk-15](/zh/posts/figure_rdata_science/unnamed-chunk-15-1.png)

你可能想要在代码中强调统计变换.例如,你可以使用`stat_summary()`函数将人们的注意力吸引到你计算出的那些摘要统计量上.`stat_summary()`函数为`x`的每个唯一值计算`y`值的摘要统计:


```r
ggplot(data = diamonds) +
  stat_summary(
    mapping = aes(x = cut, y = depth),
        fun.ymin = min,
    fun.ymax = max,
    fun.y = median
  )
```

![plot of chunk unnamed-chunk-16](/zh/posts/figure_rdata_science/unnamed-chunk-16-1.png)

`ggplot2`提供了20多个统计变换以供你使用.每个统计变换都是一个函数,因此你可以按照通用方式获得帮助,例如`?stat_bin`
