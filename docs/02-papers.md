# 📄 02 · 论文阅读清单（优先级排序）

> 原则来自课题组的共识：**优先阅读"顶会/顶刊 + 有官方代码"的论文**——先复现，再读方法边界，最后才轮到预印本。
> 全部 68 篇的逐篇索引（自动生成）见 [papers-index.md](papers-index.md)；完整字段见 [data/papers.csv](../data/papers.csv)。

| 优先级 | 定义 | 篇数 | 阅读策略 |
| :--: | :-- | :--: | :-- |
| **P0** | 顶会/顶刊 + 官方代码 | 8 | **逐行精读 + 复现**，作为方法学地基 |
| **P1** | 顶会/顶刊，未见官方代码 | 11 | 精读方法与实验设计，结论当"待验证"处理 |
| **P2** | 预印本 + 代码 | 13 | 快速跟进最新方向，代码可直接拿来改 |
| **P3** | 其余预印本 | 36 | 泛读摘要/引言，用到时再深挖 |

---

## P0 · 必读且可复现（8 篇）

| # | 论文 | 会议 | 场景 | 一句话价值 | 代码 |
| :-: | :-- | :--: | :-- | :-- | :-- |
| 01 | PULPo: Probabilistic Unsupervised Laplacian Pyramid Registration | MICCAI 2024 | 配准 | 唯一覆盖"配准"场景的概率 UQ 工作，不确定性驱动的训练目标写得非常完整 | [leonardsiegert/PULPo](https://github.com/leonardsiegert/PULPo) |
| 02 | Towards Trustworthy Breast Tumor Segmentation using MC Dropout & Deep Ensembles | MICCAI 2025 | 超声分割 | MC Dropout × Deep Ensemble 组合的工程模板，含边界校准与 MAMA-MIA 协议 | [toufiqmusah/caladan-mama-mia](https://github.com/toufiqmusah/caladan-mama-mia) |
| 03 | FISHing in Uncertainty: Synthetic Contrastive Learning for Genetic Aberration Detection | MICCAI 2024 | 病理/细胞遗传 | 罕见病数据稀缺时"合成数据 + 对比学习"补不确定性的完整方案 | [SimonBon/FISHing](https://github.com/SimonBon/FISHing) |
| 04 | MedSymmFlow: Bridging Generative Modeling and Classification via Symmetrical Flow Matching | MICCAI 2025 | 胸片分类 | 把生成式建模与判别校准"对称对齐"，是生成式校准路线的样板 | [caetas/MedSymmFlow](https://github.com/caetas/MedSymmFlow) |
| 05 | Large Language Model Validity via Enhanced Conformal Prediction Methods | NeurIPS 2024 | LLM/CXR QA | Candès 组把保形预测系统搬进语言模型，理论+实现一体 | [jjcherian/conformal-safety](https://github.com/jjcherian/conformal-safety) |
| 06 | Calibration-Aware Prompt Learning for Medical Vision-Language Models | BMVC 2025 | 医学 VLM | 首批"在提示层直接优化校准"的工作，不重训底座 | [iabh1shekbasu/CalibPrompt](https://github.com/iabh1shekbasu/CalibPrompt) |
| 07 | Exposing and Mitigating Calibration Biases & Demographic Unfairness in MLLM Few-Shot ICL | MICCAI 2025 | 医学 MLLM | 证明 few-shot 示例会引入子群校准偏差，并给出缓解方案 | [medical-calibration-fairness-mllm](https://github.com/xingbpshen/medical-calibration-fairness-mllm) |
| 08 | Evaluating Reasoning Faithfulness in Medical VLMs using Multimodal Perturbations | ML4H 2025 | 医学 VLM 评测 | 8 类多模态扰动下的推理忠实性协议 + TAIX-VQA 数据集 | [TAIX-VQA](https://huggingface.co/datasets/jomoll/TAIX-VQA) · [cot-eval](https://github.com/jomoll/cot-eval) |

---

## P1 · 顶会/顶刊精读（11 篇）

| # | 论文 | 会议 | 为什么值得读 |
| :-: | :-- | :--: | :-- |
| 09 | SegWithU: Uncertainty as Perturbation Energy for Single-Forward-Pass Risk-Aware Segmentation | MICCAI 2026 | "冻结骨干 + 扰动探针"的范本：单次前向同时拿到校准图与排序图，AURC 全面领先；未见官方代码，实验细节要自己抠 |
| 10 | Uncertainty-Aware Image Classification in Biomedical Imaging Using SNGP | ISBI 2026 | 病理分类上 SNGP 的实证：AUROC-OOD 0.97–1.00，读"距离感知"的落地姿势 |
| 11 | Bias-Aware Conformal Prediction for Metric-Based Imaging Pipelines | ISBI 2024 | Rice 组 CP→医学影像三部曲之一：把覆盖保证放到"度量"层而非像素层 |
| 12 | Backward Conformal Prediction | NeurIPS 2025 | CP 的反向构造，理论新意明显，适合啃推导 |
| 13 | Calibration and Uncertainty for multiRater Volume Assessment (CURVAS) | MICCAI 2025 | 多评分者"真值"协议的挑战赛总结——标注分歧作为校准监督的官方起点 |
| 14 | Overconfidence and Calibration in Medical VQA | COLM 2026 | 医学 VQA 过自信的系统实证 + 幻觉感知缓解 |
| 15 | CXR-LT 2026 Challenge: Multi-Center Long-Tailed and Zero-Shot CXR Classification | MedIA 2026 | 长尾+多中心+零样本的官方基准，做"最差组覆盖"选题的主战场 |
| 16 | FOCUS: Benchmarking Retinal Model Generalization from Foundation Encoders to Multimodal LLMs | NeurIPS 2026 | 基础模型时代"泛化 vs 校准"的基准，模型选择证据 |
| 17 | Impact of Data Augmentation on Confidence Calibration in Melanoma Classification | MIUA 2026 | 增强技巧对校准的实证影响，方向不定——反直觉结论适合做实验设计参考 |
| 18 | On Impact of Loss Function on Neural Networks in Melanoma Diagnosis | MIUA 2026 | 损失函数与校准的系统对照（同上） |
| 19 | On-Device Multi-Species Malaria Detection with Uncertainty-Calibrated Slide-Level Aggregation | MICCAI 2026 | 端侧部署 + 不确定性校准聚合的落地样板（代码依赖通用检测框架） |

---

## P2 · 预印本但带代码（13 篇，追新用）

| # | 论文 | 方向 | 代码 |
| :-: | :-- | :-- | :-- |
| 20 | CalCErt: Bin-wise Certification of Confidence Calibration | 逐 bin 校准认证 | [leofillioux/calcert](https://github.com/leofillioux/calcert) |
| 21 | COMPASS: Robust Feature Conformal Prediction for Medical Segmentation Metrics | 特征保形 | [matthewyccheung/compass](https://github.com/matthewyccheung/compass) |
| 22 | Efficient Conformal Volumetry for Template-Based Segmentation | 体积受控预测集 | [matthewyccheung/convolt](https://github.com/matthewyccheung/convolt) |
| 23 | Conformal Prediction for Image Segmentation Using Morphological Prediction Sets | 形态学预测集 | [deel-ai-papers/consema](https://github.com/deel-ai-papers/consema) |
| 24 | CARE: A Conformal Safety Layer for Medical Summarization | 摘要保形 | [som-shahlab/CARE](https://github.com/som-shahlab/CARE) |
| 25 | Calibrated Confidence Expression for Radiology Report Generation | 报告置信表达 | [ChantalMP/Conrad](https://github.com/ChantalMP/Conrad) |
| 26 | Conformal Prediction for Risk-Controlled Medical Entity Extraction | 受控实体抽取 | 论文内含实现说明 |
| 27 | Uncertainty-Aware Remaining Lifespan Prediction from Images | 影像+生存 | [TKenneweg/RLPredictionWithUncertainty](https://github.com/TKenneweg/RLPredictionWithUncertainty) |
| 28 | FoMoH: Clinically Meaningful Foundation Model Evaluation for Structured EHR | EHR 基础模型评测 | [reAIM-Lab/ehr_foundation_model_benchmark](https://github.com/reAIM-Lab/ehr_foundation_model_benchmark) |
| 29 | Foundation Model of Electronic Medical Records for Adaptive Risk Estimation | EHR 风险估计 | [ipolharvard/ethos-ares](https://github.com/ipolharvard/ethos-ares) |
| 30 | Adaptive Confidence-weighted Expansion for Trustworthy Multi-Omics Fusion | 多组学置信融合 | [AliGreen0/ACE-Dynamics](https://github.com/AliGreen0/ACE-Dynamics) |
| 31 | Missingness Bias Calibration in Feature Attribution Explanations | 解释校准 | [ShaileshSridhar2403/MCal](https://github.com/ShaileshSridhar2403/MCal) |
| 32 | Evaluating Reasoning Faithfulness in Medical VLMs（数据集镜像入口） | VQA 评测 | [jomoll/cot-eval](https://github.com/jomoll/cot-eval) |

> 提示：P2 论文的结论尚未经过同行评审，引用时注意标注 arXiv 版本；代码跑通后再采信其结论。

---

## P3 · 其余预印本（36 篇）

按方法族与场景检索即可，不设精读任务：

- 逐篇索引（标题 / 年份 / 方法族 / 任务 / 一句话贡献）→ [papers-index.md](papers-index.md)
- 完整字段（难点 / 方法 / 数据集 / 贡献 / 文件名）→ [data/papers.csv](../data/papers.csv)

---

## 阅读节奏建议

- **第 1 周**：P0 的 05（NeurIPS 保形）+ 06（CalibPrompt）——一理论一应用，建立两条主线。
- **第 2–3 周**：P0 剩余 6 篇，每篇产出：复现笔记 + 方法边界一页纸。
- **第 4–6 周**：P1 按自己的选题方向挑 4–6 篇精读（分割选 09/13，分类选 10/15，LLM 选 12/14）。
- **持续**：P2 每周扫 2–3 篇，有代码的直接跑 demo。

配套 8 周完整计划见 [05-reading-plan.md](05-reading-plan.md)。
