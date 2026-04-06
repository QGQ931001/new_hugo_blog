---
title: "如何在双变量Probit中使用工具变量法IV估计"
date: 2020-05-25
lastmod: 2020-05-25
author: ["秦国庆"]

categories:
- "计量"
- "内生性问题"

tags:
- "stata"

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

# ML两步法
可以采用二步法进行ML估计,以下将会以一段样例代码展示:

```stata
webuse school, clear
set seed 1
capture program drop mybiprobit
program mybiprobit
args lnf m1   m2  athrho  zb1 lns1
tempvar rho
qui:gen double `rho'=tanh(`athrho')
qui:replace `lnf'=ln(normalden($ML_y3,`zb1',exp(`lns1')))
qui:replace `lnf'=`lnf'+ln(binormal(`m1',`m2',`rho')) if $ML_y1==1 & $ML_y2==1
qui:replace `lnf'=`lnf'+ln(binormal(`m1',-`m2',-`rho')) if $ML_y1==1 & $ML_y2==0
qui:replace `lnf'=`lnf'+ln(binormal(-`m1',`m2',-`rho')) if $ML_y1==0 & $ML_y2==1
qui:replace `lnf'=`lnf'+ln(binormal(-`m1',-`m2',`rho')) if $ML_y1==0 & $ML_y2==0
end
**Here I am creating an artificial IV
gen z=logptax-rnormal()
ml model lf mybiprobit (private:private=logptax loginc years)   (vote:vote=logptax loginc years)   /athrho (zb1:logptax=loginc  years z) /lns1

ml maximize,
matrix b=e(b)
```
<!-- more -->

```stata
capture program drop mybiprobitiv
program mybiprobitiv
args lnf mm1 g1  mm2  g2 athrho  zb1 lns1
tempvar rho
qui:gen double `rho'=tanh(`athrho')
qui:replace `lnf'=ln(normalden($ML_y3,`zb1',exp(`lns1')))
tempvar m1 m2
qui:gen double `m1'=`mm1'+`g1'*($ML_y3-`zb1')
qui:gen double `m2'=`mm2'+`g2'*($ML_y3-`zb1')
qui:replace `lnf'=`lnf'+ln(binormal(`m1',`m2',`rho')) if $ML_y1==1 & $ML_y2==1
qui:replace `lnf'=`lnf'+ln(binormal(`m1',-`m2',-`rho')) if $ML_y1==1 & $ML_y2==0
qui:replace `lnf'=`lnf'+ln(binormal(-`m1',`m2',-`rho')) if $ML_y1==0 & $ML_y2==1
qui:replace `lnf'=`lnf'+ln(binormal(-`m1',-`m2',`rho')) if $ML_y1==0 & $ML_y2==0
end


ml model lf mybiprobitiv (private:private=logptax loginc years) (g1:)  (vote:vote=logptax loginc years)  (g2:) /athrho (zb1:logptax=loginc  years z  ) /lns1, init(b)
ml maximize
```
