# 🏫 03 · 国内外实验室地图

> 分三个梯队：**A. 文献库中出现的团队**（从论文首页单位直接提取，信息确凿）；
> **B. 国际公认的校准 / UQ 研究中心**（公开资料整理）；
> **C. 国内相关团队**（公开资料整理，标注方向为主，欢迎 PR 补充与校正）。

---

## 梯队 A · 文献库中出现的团队（直接可追踪）

这些团队的近期工作就在本仓库文献库里，读论文 = 读最新动态，适合作为"盯梢对象"。

### A1 · 美国

| 团队 | 机构 | 本库代表工作 | 方向标签 |
| :-- | :-- | :-- | :-- |
| Emmanuel Candès 组（统计系） | Stanford University | LLM Validity via Enhanced Conformal Prediction (NeurIPS 2024) | 保形预测理论、选择性推断 |
| Nigam Shah 组（生物医学数据科学） | Stanford University | CARE: Conformal Safety Layer for Medical Summarization (2026) | 临床文本 + 保形安全层 |
| Guha Balakrishnan 组（ECE） | Rice University | Bias-Aware CP (ISBI 2024)、COMPASS、ConVolt | 影像保形预测三部曲 |
| Jeffrey Nirschl（病理系） | Univ. of Wisconsin-Madison | SNGP 生物医学分类 (ISBI 2026) | 距离感知校准、数字病理 |
| Tal Arbel 组（CIM） | McGill University, 加拿大 | Exposing & Mitigating Calibration Biases in MLLM (MICCAI 2025) | 医学影像 + 公平校准 |
| Narges Razavian 组 | New York University | Uncertainty of Vision Medical Foundation Models (ICLR-W 2025) | 医学基础模型不确定性 |
| FoMoH / EHR 评测团队 | Columbia University DBMI | FoMoH (2025)、ARES (2025) | EHR 基础模型评测 |

### A2 · 欧洲

| 团队 | 机构 | 本库代表工作 | 方向标签 |
| :-- | :-- | :-- | :-- |
| Bernhard Schölkopf / Michael Muehlebach | Max Planck Institute for Intelligent Systems, 德国 | A Critical Perspective on Finite Sample CP (2025) | 保形预测理论批判 |
| Christian Baumgartner | Univ. of Tübingen / Lucerne | PULPo (MICCAI 2024)、CP 批判合作 | 概率配准、医学 UQ |
| Nassir Navab / Matthias Keicher（CAMP） | TU Munich, 德国 | Calibrated Confidence Expression for Radiology Report (2026) | 可信介入与报告生成 |
| Maria Vakalopoulou 组 | Université Paris-Saclay, 法国 | CalCErt 逐 bin 认证 (2026) | 校准认证 |
| Jose Dolz（LIVIA） | ETS Montréal, 加拿大 | CalCErt 合作 | 校准 + 认证 |
| Fons van der Sommen 组 | TU Eindhoven, 荷兰 | MedSymmFlow (MICCAI 2025) | 生成式 + 分类统一 |
| Barbara Hammer 组 | Univ. of Bielefeld, 德国 | Uncertainty-Aware Lifespan Prediction (2025) | 影像 + 生存分析 UQ |
| Saleh Rezaeiravesh 组 | Univ. of Manchester, 英国 | 不确定性驱动 3D 肺结节分类 (2026) | UQ 驱动训练 |
| IRT Saint Exupéry | Toulouse, 法国 | Morphological Prediction Sets (2025) | 工业级保形预测 |

### A3 · 其他地区

| 团队 | 机构 | 本库代表工作 | 方向标签 |
| :-- | :-- | :-- | :-- |
| Muhammad Haris Khan 组 | MBZUAI, 阿联酋 | CalibPrompt (BMVC 2025) | VLM 提示校准 |
| M. Tanveer 组 | IIT Indore, 印度 | Class-Tail Undercoverage in Medical VLM (2026) | 类尾覆盖 |
| IIT Delhi（Vagish Kumar 等） | 印度 | TrustFed (2026) | 隐私约束下可信医疗 AI |
| Edward Kim 组 | Drexel University, 美国 | Risk-Controlled Medical Entity Extraction (2026) | 受控信息抽取 |

---

## 梯队 B · 国际公认的校准 / UQ 中心（公开资料整理）

做文献综述的 related work 时，这些中心的经典工作是绕不开的"地基"：

| 团队 | 机构 | 为什么重要 |
| :-- | :-- | :-- |
| Yarin Gal 组（OATML） | Oxford | MC Dropout（2016）与 Deep Ensembles 谱系的源头，持续输出 UQ + 主动学习 + OOD |
| Charles Blundell / DeepMind UQ 线 | DeepMind | 贝叶斯深度学习早期系统化（Bayes by Backprop） |
| Zoubin Ghahramani 谱系 | Cambridge / Google | 不确定性建模理论传统；Google 的 `uncertainty-baselines` 仓库是复现基准的事实标准 |
| Anastasios Angelopoulos / Stephen Bates | UC Berkeley / MIT | 《A Gentle Introduction to Conformal Prediction》教程与代码库，CP 入门第一站 |
| Emmanuel Candès 组 | Stanford | 选择性推断与保形预测理论（见梯队 A） |
| Andreas Krause 组 | ETH Zürich | 贝叶斯优化 + UQ 理论 |
| Zachary Lipton 组 | CMU | 校准与分布偏移的实证研究（"Calibrated predictions under distribution shift"） |
| Ryoma Bise / UQ in MICCAI 社区 | 各校 | MICCAI UNSURE workshop 系列——医学 UQ 专题会议，追踪最新趋势必看 |

> 经典基线与工具库汇总见 [README 的"开源工具箱"](../README.md#-06--开源工具箱)。

---

## 梯队 C · 国内相关团队（公开资料整理，欢迎 PR 校正）

> 说明：以下以**方向**为线索整理，具体课题组动态请以机构主页 / 近两年 MICCAI、TMI、MedIA 论文为准。
> ⚠️ 本表尚未补代表作链接（4.3/4.4 待做）。补齐方法见 **[labs-worksheet.md](labs-worksheet.md)**，填写用表：`data/labs.csv`。**在补完之前，本段不要对外引用。**

| 机构 / 团队 | 相关方向 | 与本仓库主题的接口 |
| :-- | :-- | :-- |
| 清华大学 · 机器学习组（TSAIL） | 贝叶斯深度学习、不确定性估计、安全 AI | 校准方法学的国内理论高地 |
| 上海人工智能实验室（OpenMEDLab） | 开源医学基础模型平台 | 基础模型时代"先选模型再校准"的模型供给方 |
| 香港中文大学 · 医学影像组 | 医学影像分析、可信 AI | MICCAI 高产团队，可信分割相关 |
| 中国科学院自动化研究所 | 医学影像分析与智能诊断 | 影像 + 临床落地场景 |
| 上海交通大学 / 上海科技大学 · 生物医学工程 | 医学影像、AI 辅助诊断 | 分割/配准 UQ 场景 |
| 浙江大学 · 医学信息 | 医学 AI 与 EHR | F09/F13 场景的国内对照 |
| 腾讯觅影 / 华为云医疗 / 联影智能 / 商汤医疗 | 医疗 AI 产品化 | 端侧、云边级联、院内部署——F11 的产业接口 |
| 阿里达摩院（医疗 AI） | 医学影像大规模筛查 | 多中心筛查的校准需求 |

**给国内团队的定位建议**（本仓库观点）：

1. 2024–2026 的方法学热点（条件覆盖、认证、风险控制、多智能体）中国团队尚少系统性输出，**综述 + 方法学的空白窗口还在**。
2. 医疗数据的多中心性（各大医院独立采集）天然适合"子群/条件覆盖"类方法——数据优势可转化为方法优势。
3. 端侧与云边协同的筛查设备（F11）是国内产业界真实需求，学术 + 工程结合点好找。

---

## 怎么用这张地图

- **找合作 / 找导师方向**：梯队 A 的团队都在做"2026 年还有空白"的方向（标注分歧校准、子群覆盖、认证），MAIL 或直接套磁时可引用其本库论文。
- **写综述**：梯队 B 提供 related work 的"经典段"，梯队 A 提供"最新段"，梯队 C 提供"国内现状段"。
- **盯梢节奏**：每月扫一次梯队 A 团队的 arXiv 新作（Google Scholar 关键词：`conformal prediction medical` / `calibration medical imaging`）。
