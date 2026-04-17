---
title: "Bartik Instruments: What, When, Why, and How — 深度阅读笔记 — AER"
date: "2026-04-17"
lastmod: "2026-04-17"
author: ["QGQ"]

categories:
- "AER"
tags:
- "论文笔记"
description: ""
summary: ""
weight: 100
slug: "goldsmith-pinkham-2020-bartik-instruments"
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

## 文献信息
- **标题**: Bartik Instruments: What, When, Why, and How
- **作者**: Paul Goldsmith-Pinkham (Yale University), Isaac Sorkin (Stanford University & NBER), Henry Swift
- **年份**: 2018 (Revised 2019)
- **来源**: NBER Working Paper No. 24408
- **JEL Codes**: C1, C18, C2, J0, J2
<!--more-->

---

## 引言(背景和意义)

### 领域基础知识

**工具变量（Instrumental Variables, IV）方法**是计量经济学中处理内生性的核心方法之一。当解释变量与误差项存在相关性（内生性）时，普通最小二乘法（OLS）的估计量会有偏且不一致。工具变量方法通过寻找与内生解释变量相关但与误差项不相关的外生变量来实现对 structural parameter 的识别。

**两阶段最小二乘法**（Two-Stage Least Squares, TSLS）是最常用的 IV 估计方法。第一阶段将内生解释变量对工具变量进行回归，第二阶段将因变量对第一阶段拟合的内生变量进行回归。

**Bartik 工具**（又称 shift-share 工具或本地增长工具）是将局部地区的行业份额与全国性行业增长 rate 相乘来构造的工具变量。其核心思想是：地区就业增长可以分解为该地区各行业份额与各行业增长的加权平均，而全国性行业增长（如来自进口竞争或技术变革的冲击）对地方的影响取决于地方的经济结构。

**识别（Identification）** 是计量经济学分析的核心，指从数据的概率分布中推断参数真值的能力。在 IV 框架下，识别意味着工具变量与误差项的外生性假设能否支撑对 structural parameter 的有效推断。

### Bartik 工具的起源与应用

Bartik 工具得名于 Bartik (1991) 的开创性研究，并在 Blanchard and Katz (1992) 的论文中得到普及。这两篇论文将工具定义为"用本地行业就业份额加权的本地行业就业增长率"。此后，Bartik 方法及其形式上相同的变体被广泛应用于经济学的多个领域，包括劳动经济学、公共经济学、发展经济学、宏观经济学、国际贸易和金融。

**Bartik 工具的典型应用场景**包括：

1. **劳动力供给弹性估计**：用本地行业份额与全国行业增长相互作用来 instrument for 本地就业增长，进而估计工资对就业的响应（Blanchard-Katz 经典应用）

2. **中国进口冲击对美国制造业就业的影响**：Autor, Dorn and Hanson (2013) 的"中国冲击"（China Shock）研究使用 Bartik 工具识别本地劳动力市场对进口竞争的暴露程度

3. **移民对本地工资和就业的影响**：Card (2009) 使用移民聚居地的移民份额作为工具来估计移民对本地劳动市场的影响

### 作者的问题意识

尽管 Bartik 工具被广泛应用，但研究者对其识别假设的理解存在显著分歧。文献中存在两种主要观点：

**观点一（Shares as Instruments）**：Bartik 工具的识别来自行业份额的外生性。核心假设是本地行业份额反映了地区对某些 common shocks 的差异化暴露，而这些 shocks 的分配与误差项不相关。

**观点二（Shocks as Instruments）**：Bartik 工具的识别也可以来自冲击（shocks）的外生性。在此框架下，行业增长的 national component 本身是外生的，工具利用的是地区对全国性冲击的暴露差异。

这两种观点在数学上等价，但对应的识别假设含义不同。作者指出："研究者能够告诉使用者他们正在使用哪种 quasi-experimental 设计吗？"这是一个关键的 methodological 问题。

**本文核心目标**：打开 Bartik 工具的黑匣子——形式化其结构，分解其使用的 variation，提供评估研究设计可信度的工具，使研究者能够区分 Bartik 工具在哪些情况下有效、哪些情况下可能失效。

## 内容及结构(论文结构)

本文共分为7个主要部分和5个附录：

**第一节：引言**。概述 Bartik 工具的应用背景和本文的研究动机。

**第二节：Bartik IV 与 GMM 的等价性**。证明 Bartik 工具在数学上等价于使用行业份额作为工具变量的 GMM 估计，进而论证识别条件应从行业份额的角度解释。

**第三节：Bartik 工具如何组合暴露设计**（How Bartik Combines Exposure Designs）。引入 Rotemberg 权重来分解 Bartik 估计量，说明工具如何对各个行业份额设计进行加权。

**第四节：处理效应异质性**（Treatment Effect Heterogeneity）。讨论在处理效应异质性背景下 Bartik 估计量的解释力问题。

**第五节：评估研究设计的可信度**（Assessing Plausibility）。提供三种评估识别假设可信度的实证工具：Shares 的协变量分析、平行趋势检验、过度识别检验。

**第六节：应用实例**。通过三个经典应用来说明上述方法：劳动力供给弹性估计、中国进口冲击对制造业就业的影响、移民与本地劳动力的替代弹性。

**附录**：讨论 Bartik-like 工具的其他应用，包括银行信贷供应和人口统计学交互项。

## 正文(逻辑梳理)

### Bartik 工具的数学结构

#### 基础设定

考虑简化的 cross-sectional 结构方程，链接工资增长到就业增长：

$$y_l = \rho + \beta_0 x_l + \epsilon_l$$

其中：
- $l$ 索引 location（地区）
- $y_l$ 是地区 $l$ 的工资增长率
- $x_l$ 是地区 $l$ 的就业增长率
- $\rho$ 是常数项
- $\epsilon_l$ 是结构性误差项，与 $x_l$ 相关（内生性）
- $\beta_0$ 是我们感兴趣的参数（劳动力供给弹性的倒数）

#### 两个会计恒等式

Bartik 工具结合了两个 accounting identities：

**恒等式一：就业增长的分解**

$$x_l = \sum_k z_{lk} g_{lk}$$

其中：
- $z_{lk}$ 是地区 $l$ 在行业 $k$ 的就业份额
- $g_{lk}$ 是地区 $l$ 行业 $k$ 的增长率

**恒等式二：行业增长率的分解**

$$g_{lk} = g_k + \tilde{g}_{lk}$$

其中：
- $g_k$ 是行业 $k$ 的全国增长率
- $\tilde{g}_{lk}$ 是行业-地区特异的 idiosyncratic 增长

#### Bartik 工具的定义

将第二个恒等式代入第一个：

$$x_l = \sum_k z_{lk} (g_k + \tilde{g}_{lk}) = \underbrace{\sum_k z_{lk} g_k}_{\text{Bartik工具 } B_l} + \underbrace{\sum_k z_{lk} \tilde{g}_{lk}}_{\text{Idiosyncratic 部分}}$$

因此 **Bartik 工具**定义为：

$$B_l = \sum_k z_{lk} g_k$$

即地区 $l$ 的行业份额与全国行业增长率的內积。

### 核心等价性结果

#### 命题1.1：Bartik IV = GMM with Industry Shares

作者证明了一个关键定理：使用 Bartik 工具的两阶段最小二乘（TSLS）估计量在数学上等价于使用行业份额作为工具、权重矩阵为 $W = GG'$ 的广义矩估计（GMM）：

$$\hat{\beta}_{\text{Bartik}} = \frac{B' Y_\perp}{B' X_\perp}$$

$$\hat{\beta}_{\text{GMM}} = \frac{X_\perp' Z W Z' Y_\perp}{X_\perp' Z W Z' X_\perp}$$

**如果 $W = GG'$，则 $\hat{\beta}_{\text{GMM}} = \hat{\beta}_{\text{Bartik}}$**（证明见 Appendix B）

这一结果的含义是：使用 Bartik 工具"等价于"使用行业份额作为工具变量，因此**识别条件应从行业份额的角度来解释**。

#### 对研究设计含义的讨论

**Shares 观点的识别假设**：如果接受 shares 作为 instruments，那么识别要求行业份额与误差项 $\epsilon_l$ 不相关。这一假设被称为"exposure research design"——行业份额测量了对 common shock 的差异化外生暴露。

**Shocks 观点的可能性**：然而，Borusyak, Hull and Jaravel (2018) 强调在某些假设下，估计量的一致性也可以来自 shocks 的外生性。

**如何区分**：作者认为，如果研究者（i）描述研究设计为"反映对 common shocks 的差异化外生暴露"，（ii）强调两行业例子，或（iii）强调特定行业的 shocks 是研究设计的核心，则更可能是在使用基于 shares 假设的研究设计。

### Bartik 工具如何加权不同的暴露设计

#### Rotemberg 权重

为了理解 Bartik 工具如何组合不同的 exposure designs，作者引入 Rotemberg 权重。思路是将 Bartik 估计量分解为加权 sum of just-identified IV 估计量，其中每个行业份额 $z_{lk}$ 作为单独的工具变量。

**定义**：设 $X_\perp = Z_\perp G$，其中 $Z_\perp$ 是 $Z$ 对控制变量的残差。那么 Bartik 工具可以用行业份额表示为：

$$B = Z G = Z_\perp G + \text{(controls 的投影)}$$

对应的 TSLS 可以改写为使用多个工具变量（每个行业份额）的 GMM。

**Rotemberg 权重** $w_k$ 的计算：

每个行业 $k$ 的权重为：

$$w_k = \frac{[Z_\perp G]_k' M_{Z_\perp} Y_\perp}{G' Z_\perp' M_{Z_\perp} Y_\perp}$$

其中 $M_{Z_\perp}$ 是关于 $Z_\perp$ 的投影矩阵。这些权重的性质：

1. **权重之和为1**：$\sum_k w_k = 1$
2. **权重可正可负**
3. **权重反映了协方差结构**：$w_k$ 的大小取决于第 $k$ 个工具的拟合值与实际内生变量的协方差

#### 权重的解释

Rotemberg 权重具有重要的 practical interpretation：

1. **敏感性度量**：权重是 Andrews, Gentzkow and Shapiro (2017) 的"对误设敏感性"（sensitivity-to-misspeciﬁcation）参数的缩放版本，告诉我们在任何工具的内生性情况下，overidentified 估计量对误设的敏感程度。

2. **哪些暴露设计更重要**：权重揭示了哪些 exposure designs 在总体估计中占更大权重，因此哪些识别假设最值得检验。

3. **异质性来源**：高权重工具对应的行业可能在样本中具有更大的残差 dispersion 或更强的识别力。

### 处理效应异质性

#### 问题

当不同 location 的 treatment effect 不同时（即 $\beta_i$ 而非 $\beta$），Bartik 估计量的解释变得复杂。

**关键点**：即使每个工具单独对 location 的参数施加凸权重，Bartik 估计量仍然可能不像 LATE 那样有清晰的 interpretation（局部平均处理效应）。

#### 诊断工具

作者开发了 **Rotemberg 权重的可视化诊断**，帮助研究者理解在 treatment effect 异质性背景下 Bartik 估计量的含义：

1. **权重分布图**：绘制各行业权重的直方图或柱状图
2. **权重符号**：检查正负权重
3. **权重集中度**：如果权重高度集中于少数几个行业，应重点关注这些行业的识别假设

### 评估研究设计的可信度

作者提供了三种评估 Bartik 研究设计可信度的工具：

#### Test 1：Shares 的协变量分析

**核心思想**：如果行业份额通过除研究者 posited 渠道之外的渠道预测结果，则识别假设可能不成立。

**实施方法**：将行业份额对一组协变量（如教育水平、年龄结构、行业集中度等）进行回归，检查 $R^2$ 和各系数的统计显著性。

**解释**：高 $R^2$ 表明份额与 observable characteristics 高度相关，而这些 characteristics 可能也与 outcome 相关。但这不是识别假设失效的充分条件——关键是检查这些协变量是否预测 outcome 的 **变化** 而非 **水平**。

#### Test 2：平行趋势检验

**适用场景**：当研究者有 pre-period 数据时（如标准的 difference-in-differences 设计）。

**核心思想**：如果 shares 反映了外生暴露，那么在 shock 发生前，具有高低 shares 的 location 应该在 outcome 的变化上具有相似趋势。

**实施方法**：估计 event-study 规范，检验 treatment 前各期的系数是否显著异于零。

$$y_{lt} = \alpha_l + \gamma_t + \sum_{\tau \neq pre} \beta_\tau \cdot z_l \cdot 1(t=\tau) + \epsilon_{lt}$$

其中 $z_l$ 是关注的行业份额。

#### Test 3：过度识别检验

**核心思想**：Bartik 工具将多个行业份额组合成一个工具，这提供了过度识别机会。如果所有工具（行业份额）都是有效的，它们应该给出相似的参数估计。

**实施方法**：

1. 比较 Bartik 估计与各单个工具的估计
2. 运行 Sargan-Hansen 过度识别检验
3. 分析 Rotemberg 权重的 dispersion

**重要警告**：过度识别检验拒绝可能意味着：
- 识别假设失效（某些工具是内生的）
- 处理效应异质性（不同 location 有不同的 treatment effects）

作者强调在解释检验结果时需要谨慎，因为拒绝可能反映的是后者而非前者。

## 应用实例

### 应用一：劳动力供给弹性

#### 数据和设定

使用美国2000-2010年 census 数据，以1980年的行业份额作为工具，估计劳动力供给弹性。

#### 主要发现

**第一，全国增长率解释不到1%的 Rotemberg 权重方差**。这意味着增长率对理解哪些 variation 驱动估计几乎没有帮助。

**第二，权重高度偏斜**：前5个行业占据超过40%的权重。其中**油气开采行业**获得最大权重。

**第三，shares 与 observable characteristics 高度相关**：包括移民份额——这是劳动力供给冲击的潜在来源。

**第四，过度识别检验拒绝**：替代估计量给出实质性不同的点估计，检验拒绝外生性 null。

**第五，存在显著的 visual dispersion**：各单个工具的估计存在较大 dispersion，一些极端点估计甚至获得负的 Rotemberg 权重。

**含义**：这些发现对使用 Bartik 工具估计劳动力供给弹性的可信度提出了严重质疑。

### 应用二：中国进口冲击（Autor, Dorn, Hanson 2013）

#### 数据和设定

估计中国进口竞争对美国制造业就业的影响，使用 Bartik 工具测量本地劳动力市场对中国冲击的暴露程度。

#### 主要发现

**第一，进口增长率解释约20%的 Rotemberg 权重方差**：这一比例高于应用一，表明在中国冲击应用中，shocks 的 variation 对识别更为重要。

**第二，前两个高权重行业是电子计算机和游戏玩具**：这意味着估计量主要依赖于电子计算机和游戏玩具行业份额的地区分布差异。

**第三，高权重行业倾向于在教育程度较高的地区占据更高份额**。

**第四，pre-trends 检查令人担忧**：在高权重行业的暴露设计中，pre-2000 时期存在趋势差异，这可能解释了2000年代观察到的较大效应。

**第五，过度识别检验拒绝**：与其他估计量的点估计实质性不同。

**含义**：对于中国冲击应用，pre-trend 差异是需要认真对待的识别威胁。

### 应用三：移民与本地劳动力的替代弹性

#### 数据和设定

使用2000年 census 数据，following Card (2009) 的方法，用移民聚居地的移民份额 instrument for 移民流入。

#### 主要发现

**第一，对于高中及以下教育程度的工人，Rotemberg 权重几乎完全由移民流入解释**：这意味着在低教育工人样本中，shocks 是识别的主要来源。

**第二，对于大学教育程度的工人，流入的解释力更高**。

**第三，墨西哥移民份额在1980年获得近一半权重**：这是 Card (2009) 本身承认的可能性。

**第四，与应用一和应用二不同，过度识别检验大多不拒绝**：研究者对移民应用的识别假设更有信心。

**第五，对于高中程度工人，pre-trend 证据有限**；对于大学程度工人，发现统计显著 pre-trends。

## Bartik-like 工具的扩展

作者定义 **Bartik-like 工具**为使用内生变量內积结构构造工具的任何方法。附录 A 讨论了两个额外例子：

**例子一：银行信贷供应工具**（Greenstone, Mas and Nguyen, Forthcoming）。将预先存在的银行放贷份额与银行放贷量变化相互作用来 instrument for 信贷供应。

**例子二：市场规模工具**（Acemoglu and Linn, 2004）。将年龄组消费模式与人口统计变化相互作用来 instrument for 市场大小。

## 结论(Conclusion)

### 核心方法论贡献

**第一，GMM 等价性结果**：作者证明 Bartik 工具在数学上等价于使用行业份额作为 instruments 的 GMM 估计。这一结果将分散的文献讨论统一到一个清晰的框架中。

**第二，Rotemberg 权重分解**：提供了量化 Bartik 工具如何加权不同 exposure designs 的方法，使研究者能够识别哪些识别假设对估计最为关键。

**第三，识别假设的明确化**：系统地区分了 shares-based 和 shocks-based 两种识别思路，帮助研究者更清晰地理解其 identification strategy。

**第四，实证评估工具**：提供了协变量分析、pre-trend 检验和过度识别检验的系统性框架，用于评估 Bartik 研究设计的可信度。

### 对应用的警示

**过度识别检验的解释**：当过度识别检验拒绝时，研究者应同时考虑工具无效和处理效应异质性两种可能性，而非简单地断定识别假设失效。

**Pre-trend 检验的必要性**：在 Bartik 应用中，pre-trend 检验尤为重要，因为 shares 本身可能预测结果的 level 差异。

**权重可视化**：Rotemberg 权重的可视化可以帮助理解估计量的驱动因素和潜在脆弱性。

### 实践建议

1. **明确识别假设**：研究者应清楚说明其识别是基于 shares 还是 shocks 的外生性
2. **报告 Rotemberg 权重**：作为标准操作，应报告并可视化权重分布
3. **进行敏感性分析**：检验高权重行业的识别假设是否合理
4. **谨慎解释过度识别检验**：结合权重分析和 pre-trend 检验综合判断

## 未来研究方向提及

**第一，空间溢出**：本文假设 location 之间相互独立，但现实中存在跨地区的溢出效应（如通勤模式变化）

**第二，非稳态动态**：Jaeger, Ruist and Stuhler (2019) 讨论了 immigration 背景下偏离稳态的动态问题

**第三，更一般的异质性结构**：在更一般的 treatment effect 异质性假设下，Bartik 估计量的 interpretation 问题值得进一步研究

## 未来研究方向思考

基于对本文的深入理解，以下是值得进一步探索的研究方向：

**第一，Bartik 工具在面板数据情境下的应用**。本文主要讨论 cross-sectional 应用，但 Bartik 工具在面板数据中也很常用。面板情境下的识别假设与 cross-sectional 有何不同？

**第二，Bartik 工具与合成控制法的比较**。合成控制法（Synthetic Control Method）是另一种处理 quasi-experimental variation 的方法，两者各有优缺点。什么时候用 Bartik 更好？什么时候用合成控制法更合适？

**第三，机器学习方法在工具变量选择中的应用**。现代机器学习方法可能有助于自动识别最外生的 shares 或最高效的 weighting scheme。

**第四，Bartik 工具在发展经济学中的应用**。本文主要关注美国背景，但 Bartik 工具在发展中国家的应用可能面临不同的识别挑战（如行业份额的内生性问题更严重）。

**第五，网络相依性下的 Bartik 识别**。当 location 之间通过经济网络相互连接时，标准的独立假设失效。如何修正识别策略？

## 学术思考

**关于识别假设的哲学思考**：计量经济学中"外生性"是一个相对概念而非绝对概念。Shares 的外生性取决于我们能否想到其他影响渠道。在 Bartik 工具的背景下，关键是识别 shares 与 outcomes 变化之间的关联是否确实反映了研究者 posited 的 causal mechanism。

**关于过度识别检验的解释问题**：作者指出过度识别检验拒绝可能反映处理效应异质性而非工具无效，这是一个深刻的方法论洞见。但这一洞见实际上使问题变得更复杂：研究者如何在不事先知道处理效应异质性结构的情况下判断识别是否有效？

**关于"Bartik as an instrument" vs. "Bartik as a GMM"的教学含义**：在教学层面，将 Bartik 呈现为单一工具变量还是多个工具变量的 GMM，会影响学生对识别假设的理解。作者建议后者可能更清晰。

**关于跨学科应用的方法论挑战**：Bartik 工具从劳动经济学扩展到国际贸易、发展经济学等领域时，识别假设的 credibility 可能发生根本性变化。一个领域（如美国劳动力市场）的识别假设可能在另一个领域（如发展中国家的农业）完全不适用。

## 下一步用户可能提的问题

1. **在什么条件下应该优先使用 Bartik 工具而非其他识别策略（如 RCT、RD）？Bartik 的比较优势是什么？**

2. **Rotemberg 权重为负意味着什么？在解释负权重时，应该认为是识别失效还是反映了有价值的异质性？**

3. **如果预检验显示高权重行业存在 pre-trend 问题，应该如何修正？是否可以 drop 这些行业重新估计？**

4. **作者提到 Borusyak-Hull-Jaravel 强调 shocks 的外生性也可以是识别来源。能否详细比较这两种识别框架的适用条件？**

5. **在应用三（移民）中，为什么不同教育程度工人的识别来源差异如此之大？这对政策含义有何启示？**

6. **对于中国这样的发展中国家，Bartik 工具的应用需要考虑哪些特殊的识别挑战？**

7. **当样本量较小时，过度识别检验的 power 会降低。在这种情况下，如何评估识别设计的可信度？**

8. **Bartik 工具是否可以与 diD 方法结合使用以增强识别力？具体的结合策略是什么？**

9. **在处理效应异质性情况下，是否存在比简单加权平均更有经济解释力的 Bartik 估计量解释？**

10. **作者提到的"Bartik-like 工具"扩展到一般均衡设置时，识别假设会发生什么变化？**


## 学术思考

**关于识别假设的哲学思考**：计量经济学中"外生性"是一个相对概念而非绝对概念。Shares 的外生性取决于我们能否想到其他影响渠道。在 Bartik 工具的背景下，关键是识别 shares 与 outcomes 变化之间的关联是否确实反映了研究者 posited 的 causal mechanism。

**关于过度识别检验的解释问题**：作者指出过度识别检验拒绝可能反映处理效应异质性而非工具无效，这是一个深刻的方法论洞见。但这一洞见实际上使问题变得更复杂：研究者如何在不事先知道处理效应异质性结构的情况下判断识别是否有效？

**关于"Bartik as an instrument" vs. "Bartik as a GMM"的教学含义**：在教学层面，将 Bartik 呈现为单一工具变量还是多个工具变量的 GMM，会影响学生对识别假设的理解。作者建议后者可能更清晰。

**关于跨学科应用的方法论挑战**：Bartik 工具从劳动经济学扩展到国际贸易、发展经济学等领域时，识别假设的 credibility 可能发生根本性变化。一个领域（如美国劳动力市场）的识别假设可能在另一个领域（如发展中国家的农业）完全不适用。

## 下一步用户可能提的问题

1. **在什么条件下应该优先使用 Bartik 工具而非其他识别策略（如 RCT、RD）？Bartik 的比较优势是什么？**

2. **Rotemberg 权重为负意味着什么？在解释负权重时，应该认为是识别失效还是反映了有价值的异质性？**

3. **如果预检验显示高权重行业存在 pre-trend 问题，应该如何修正？是否可以 drop 这些行业重新估计？**

4. **作者提到 Borusyak-Hull-Jaravel 强调 shocks 的外生性也可以是识别来源。能否详细比较这两种识别框架的适用条件？**

5. **在应用三（移民）中，为什么不同教育程度工人的识别来源差异如此之大？这对政策含义有何启示？**

6. **对于中国这样的发展中国家，Bartik 工具的应用需要考虑哪些特殊的识别挑战？**

7. **当样本量较小时，过度识别检验的 power 会降低。在这种情况下，如何评估识别设计的可信度？**

8. **Bartik 工具是否可以与 diD 方法结合使用以增强识别力？具体的结合策略是什么？**

9. **在处理效应异质性情况下，是否存在比简单加权平均更有经济解释力的 Bartik 估计量解释？**

10. **作者提到的"Bartik-like 工具"扩展到一般均衡设置时，识别假设会发生什么变化？**


## 下一步用户可能提的问题

1. **在什么条件下应该优先使用 Bartik 工具而非其他识别策略（如 RCT、RD）？Bartik 的比较优势是什么？**

2. **Rotemberg 权重为负意味着什么？在解释负权重时，应该认为是识别失效还是反映了有价值的异质性？**

3. **如果预检验显示高权重行业存在 pre-trend 问题，应该如何修正？是否可以 drop 这些行业重新估计？**

4. **作者提到 Borusyak-Hull-Jaravel 强调 shocks 的外生性也可以是识别来源。能否详细比较这两种识别框架的适用条件？**

5. **在应用三（移民）中，为什么不同教育程度工人的识别来源差异如此之大？这对政策含义有何启示？**

6. **对于中国这样的发展中国家，Bartik 工具的应用需要考虑哪些特殊的识别挑战？**

7. **当样本量较小时，过度识别检验的 power 会降低。在这种情况下，如何评估识别设计的可信度？**

8. **Bartik 工具是否可以与 diD 方法结合使用以增强识别力？具体的结合策略是什么？**

9. **在处理效应异质性情况下，是否存在比简单加权平均更有经济解释力的 Bartik 估计量解释？**

10. **作者提到的"Bartik-like 工具"扩展到一般均衡设置时，识别假设会发生什么变化？**
