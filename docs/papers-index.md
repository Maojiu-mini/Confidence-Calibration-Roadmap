# 🔎 论文逐篇索引（自动生成）

> 共 68 篇（2024–2026）。由 `scripts/build_index.py` 从 `data/papers.csv` 生成，请勿手改；
> 修改数据后运行 `python scripts/build_index.py` 重新生成。

## P0 · 顶会+官方代码（8 篇）

| # | 年份 | 会议/期刊 | 方法族 | 论文 | 任务 | 代码 |
| :-: | :-: | :-: | :-: | :-- | :-- | :-- |
| 01 | 2024 | MICCAI | 贝叶斯近似 | PULPo: Probabilistic Unsupervised Laplacian Pyramid Registration | 可变形配准 | [github.com/leonardsiegert/PULPo](https://github.com/leonardsiegert/PULPo) |
| 02 | 2025 | MICCAI | 贝叶斯近似 | Towards Trustworthy Breast Tumor Segmentation using MC Dropout and Deep Ensembles | 分割 | [github.com/toufiqmusah/caladan-mama-mia.git](https://github.com/toufiqmusah/caladan-mama-mia.git) |
| 03 | 2024 | MICCAI | 生成式与潜变量 | FISHing in Uncertainty: Synthetic Contrastive Learning for Genetic Aberration Detection | 分类 | [github.com/SimonBon/FISHing](https://github.com/SimonBon/FISHing) |
| 04 | 2025 | MICCAI | 生成式与潜变量 | MedSymmFlow: Bridging Generative Modeling and Classification through Symmetrical Flow Matching | 分类+生成 | [github.com/caetas/MedSymmFlow](https://github.com/caetas/MedSymmFlow) |
| 05 | 2024 | NeurIPS | 保形预测与风险控制 | LLM Validity via Enhanced Conformal Prediction Methods | LLM事实性 | [github.com/jjcherian/conformal-safety](https://github.com/jjcherian/conformal-safety) |
| 06 | 2025 | BMVC | 基础模型/多模态校准 | Calibration-Aware Prompt Learning for Medical Vision-Language Models (CalibPrompt) | 零/少样本分类 | [github.com/iabh1shekbasu/CalibPrompt](https://github.com/iabh1shekbasu/CalibPrompt) |
| 07 | 2025 | MICCAI | 基础模型/多模态校准 | Exposing and Mitigating Calibration Biases and Demographic Unfairness in MLLM Few-Shot ICL (CALIN) | 少样本分类 | [github.com/xingbpshen/medical-calibration-fairness-mllm](https://github.com/xingbpshen/medical-calibration-fairness-mllm) |
| 08 | 2025 | ML4H | 评测、基准与理论 | Evaluating Reasoning Faithfulness in Medical VLMs using Multimodal Perturbations | VQA+CoT评测 | [huggingface.co/datasets/jomoll/TAIX-VQA](https://huggingface.co/datasets/jomoll/TAIX-VQA) |

## P1 · 顶会无代码（11 篇）

| # | 年份 | 会议/期刊 | 方法族 | 论文 | 任务 | 代码 |
| :-: | :-: | :-: | :-: | :-- | :-- | :-- |
| 09 | 2026 | MIUA | 训练期校准约束 | Impact of Data Augmentation on Confidence Calibration in Melanoma Classification | 二分类 | — |
| 10 | 2026 | MIUA | 训练期校准约束 | On Impact of Loss Function on Neural Networks in Melanoma Diagnosis | 二分类 | — |
| 11 | 2026 | ISBI | 距离/谱范数感知 | Uncertainty-Aware Image Classification Using Spectral-normalized Neural Gaussian Processes (SNGP) | 分类+OOD | — |
| 12 | 2024 | ISBI | 保形预测与风险控制 | Bias-Aware Conformal Prediction for Metric-Based Imaging Pipelines | 分割→临床指标区间 | — |
| 13 | 2025 | NeurIPS | 保形预测与风险控制 | Backward Conformal Prediction | 多类分类 | — |
| 14 | 2026 | MICCAI | 单次前向确定性 UQ | SegWithU: Uncertainty as Perturbation Energy for Single-Forward-Pass Risk-Aware Segmentation | 3D分割+选择性预测 | — |
| 15 | 2026 | COLM | 基础模型/多模态校准 | Overconfidence and Calibration in Medical VQA: Empirical Findings and Hallucination-Aware Mitigation (HAC) | VQA | — |
| 16 | 2026 | MICCAI | 决策层与部署治理 | On-Device Multi-Species Malaria Detection with Uncertainty-Calibrated Slide-Level Aggregation | 检测+定量 | [github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |
| 17 | 2025 | MICCAI | 评测、基准与理论 | Calibration and Uncertainty for multiRater Volume Assessment (CURVAS Challenge) | 多器官分割+体积评估 | — |
| 18 | 2026 | MedIA | 评测、基准与理论 | CXR-LT 2026 Challenge: Multi-Center Long-Tailed and Zero-Shot Chest X-ray Classification | 多标签长尾+开放世界 | — |
| 19 | 2026 | NeurIPS | 评测、基准与理论 | FOCUS: Benchmarking Retinal Model Generalization from Foundation Vision Encoders to Multimodal LLMs | 跨域分类基准 | — |

## P2 · 预印本+代码（13 篇）

| # | 年份 | 会议/期刊 | 方法族 | 论文 | 任务 | 代码 |
| :-: | :-: | :-: | :-: | :-- | :-- | :-- |
| 20 | 2026 | arXiv | 训练期校准约束 | Impact of Domain Adaptation in Deep Learning for Medical Image Classifications | 多疾病分类 | [github.com/AIPMLab/Domain](https://github.com/AIPMLab/Domain) |
| 21 | 2024 | arXiv | 贝叶斯近似 | UQ for Improving Radiomic-based Models in Radiation Pneumonitis Prediction | 分类/结局预测 | [github.com/44REAM/RP-](https://github.com/44REAM/RP-) |
| 22 | 2025 | arXiv | 贝叶斯近似 | Uncertainty-Aware Remaining Lifespan Prediction from Images | 回归 | [github.com/TKenneweg/RLPredictionWithUncertainty](https://github.com/TKenneweg/RLPredictionWithUncertainty) |
| 23 | 2025 | arXiv | 保形预测与风险控制 | COMPASS: Robust Feature Conformal Prediction for Medical Segmentation Metrics | 分割→派生指标 | [github.com/matthewyccheung/compass](https://github.com/matthewyccheung/compass) |
| 24 | 2025 | arXiv | 保形预测与风险控制 | Conformal Prediction for Image Segmentation Using Morphological Prediction Sets | 二值分割 | [github.com/deel-ai-papers/consema](https://github.com/deel-ai-papers/consema) |
| 25 | 2026 | arXiv | 保形预测与风险控制 | CARE: A Conformal Safety Layer for Medical Summarization | LLM摘要安全层 | [github.com/som-shahlab/CARE](https://github.com/som-shahlab/CARE) |
| 26 | 2026 | arXiv | 保形预测与风险控制 | Efficient Conformal Volumetry for Template-Based Segmentation (ConVOLT) | 体积指标区间 | [github.com/matthewyccheung/convolt](https://github.com/matthewyccheung/convolt) |
| 27 | 2025 | arXiv | 基础模型/多模态校准 | Foundation Model of Electronic Medical Records for Adaptive Risk Estimation (ARES) | EHR风险预测 | [github.com/ipolharvard/ethos-ares](https://github.com/ipolharvard/ethos-ares) |
| 28 | 2026 | arXiv | 基础模型/多模态校准 | Adaptive Confidence-weighted Expansion for Trustworthy Multi-Omics Fusion (ACE) | 多组学分类/预后 | [github.com/AliGreen0/ACE-Dynamics](https://github.com/AliGreen0/ACE-Dynamics) |
| 29 | 2026 | arXiv | 基础模型/多模态校准 | Calibrated Confidence Expression for Radiology Report Generation (ConRad) | 报告生成 | [github.com/ChantalMP/Conrad](https://github.com/ChantalMP/Conrad) |
| 30 | 2025 | arXiv | 评测、基准与理论 | FoMoH: A Clinically Meaningful Foundation Model Evaluation for Structured EHR | 临床预测(14任务) | [github.com/reAIM-Lab/ehr_foundation_model_benchmark](https://github.com/reAIM-Lab/ehr_foundation_model_benchmark) |
| 31 | 2026 | arXiv | 评测、基准与理论 | CalCErt: Bin-wise Certification of Confidence Calibration in Medical Image Classification | 分类校准认证 | [github.com/leofillioux/calcert](https://github.com/leofillioux/calcert) |
| 32 | 2026 | arXiv | 评测、基准与理论 | Missingness Bias Calibration in Feature Attribution Explanations (MCal) | 解释校准 | [github.com/ShaileshSridhar2403/MCal](https://github.com/ShaileshSridhar2403/MCal) |

## P3 · 其余预印本（36 篇）

| # | 年份 | 会议/期刊 | 方法族 | 论文 | 任务 | 代码 |
| :-: | :-: | :-: | :-: | :-- | :-- | :-- |
| 33 | 2024 | arXiv | 训练期校准约束 | Focal Calibration Loss: Controlling Posterior Distortion in Deep Neural Classifiers | 分类校准方法学 | — |
| 34 | 2026 | arXiv | 训练期校准约束 | Calibration-First Cross-Cohort Multimodal Temporal Learning for Transferable Asthma-Risk Forecasting | 时序二分类 | — |
| 35 | 2026 | arXiv | 训练期校准约束 | Uncertainty-driven Training for 3D Calibrated Lung Nodule Classification | 3D分类 | — |
| 36 | 2024 | arXiv | 贝叶斯近似 | Deep Bayesian Segmentation for Colon Polyps: Well-calibrated Predictions | 语义分割 | — |
| 37 | 2024 | arXiv | 贝叶斯近似 | Predictive Uncertainty Estimation for Lung Carcinoma Classification in Digital Pathology | 分类 | — |
| 38 | 2025 | arXiv | 贝叶斯近似 | Predictive Posteriors under Hidden Confounding | 分布外回归 | — |
| 39 | 2025 | arXiv | 生成式与潜变量 | ConceptVAE: Self-Supervised Fine-Grained Concept Disentanglement from 2D Echocardiographies | 自监督表征 | — |
| 40 | 2025 | arXiv | 生成式与潜变量 | Evaluating the Clinical Impact of Generative Inpainting on Bone Age Estimation | 回归+分类 | — |
| 41 | 2026 | arXiv | 生成式与潜变量 | Patch-PODiff-ViT: Structured Latent Diffusion with Patchwise POD for Super-Resolution and UQ | 超分/重建+UQ | — |
| 42 | 2026 | ICML-W | 保形预测与风险控制 | CASCADE Conformal Prediction: Uncertainty-Adaptive Intervals for Two-Stage Clinical Decision Support | 两阶段决策(分类+回归) | — |
| 43 | 2026 | arXiv | 保形预测与风险控制 | Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains | 实体抽取 | — |
| 44 | 2026 | arXiv | 保形预测与风险控制 | Fail-closed Conformal Multiresolution Error Control for 3D Dose Remapping | 数值误差控制 | — |
| 45 | 2026 | arXiv | 保形预测与风险控制 | Mitigating Class-Tail Undercoverage in Medical VLMs under Clinical Shift (CALCoDe) | 集值预测+弃权 | — |
| 46 | 2026 | arXiv | 单次前向确定性 UQ | MedFormer-UR: Uncertainty-Routed Transformer for Medical Image Classification | 分类 | — |
| 47 | 2025 | arXiv | 基础模型/多模态校准 | MedImageInsight for Thoracic Cavity Health Classification from Chest X-rays | 二分类 | — |
| 48 | 2025 | arXiv | 基础模型/多模态校准 | Multimodal Foundation Models for Early Disease Detection | 多模态分类 | — |
| 49 | 2026 | arXiv | 基础模型/多模态校准 | Toward Clinically Ready Foundation Models in Medical Image Analysis: Adaptation Mechanisms and Deployment Trade-offs | 综述 | — |
| 50 | 2026 | ICLR-W | 基础模型/多模态校准 | Uncertainty of Vision Medical Foundation Models | 分类(线性探测) | — |
| 51 | 2024 | arXiv | 语言模型与多智能体 | Word-Sequence Entropy: UQ in Free-Form Medical Question Answering | 生成式QA的UQ | — |
| 52 | 2026 | arXiv | 语言模型与多智能体 | Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents | 多智能体事实性 | — |
| 53 | 2026 | arXiv | 语言模型与多智能体 | From Theory to Decision Rule: Calibrating the Noisy-Label Crossover for VLM Weak Supervision | 弱监督分类 | — |
| 54 | 2026 | arXiv | 语言模型与多智能体 | Multi-Agent Reasoning with Consistency Verification Improves Uncertainty Calibration in Medical MCQA (MARC) | 多选QA | — |
| 55 | 2026 | arXiv | 语言模型与多智能体 | TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics | 结局预测 | — |
| 56 | 2025 | NeurIPS-W | 决策层与部署治理 | Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning | 综述 | — |
| 57 | 2025 | arXiv | 决策层与部署治理 | MedBayes-Lite: A Clinical Uncertainty Governance Layer for Risk-Aware Decision Support | 多选QA | — |
| 58 | 2025 | arXiv | 决策层与部署治理 | Selective Diabetic Retinopathy Screening with Accuracy-Weighted Deep Ensembles and Entropy-Guided Abstention | 二分类+弃权 | — |
| 59 | 2026 | arXiv | 决策层与部署治理 | A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty | 解剖预测/轮廓UQ | — |
| 60 | 2026 | arXiv | 决策层与部署治理 | CalTwin: Towards Calibrated, Shift-Robust Medical World Models via Fisher-Information Regularisation | 世界模型多步预测 | — |
| 61 | 2026 | Smart Health | 决策层与部署治理 | Confidence-Gated Cloud-Edge Cascade Triage via Variational Risk Minimization | 二分类分诊 | — |
| 62 | 2025 | arXiv | 分布式与隐私 | FedOAP: Organ Agnostic Tumor Segmentation Using Personalized Federated Learning | 联邦分割 | — |
| 63 | 2026 | arXiv | 分布式与隐私 | TrustFed: Enabling Trustworthy Medical AI under Data Privacy Constraints | 联邦分类 | — |
| 64 | 2024 | arXiv | 评测、基准与理论 | Assessing Uncertainty Estimation Methods for 3D Segmentation under Distribution Shifts | 3D分割 | — |
| 65 | 2025 | arXiv | 评测、基准与理论 | A Critical Perspective on Finite Sample Conformal Prediction Theory in Medical Applications | 分类 | — |
| 66 | 2025 | arXiv | 评测、基准与理论 | A Systematic Evaluation of UQ Techniques in Deep Learning: PPG Case Study | 分类+回归 | — |
| 67 | 2026 | arXiv | 评测、基准与理论 | MedQ-Deg: A Multidimensional Benchmark for Evaluating MLLMs Across Medical Image Quality Degradations | MLLM评测基准 | — |
| 68 | 2026 | MELBA | 评测、基准与理论 | Towards Trustworthy AI for Glioma Diagnosis: Task-Aware Evaluation of UQ | 多任务诊断 | — |

## 方法族分布

| 方法族 | 篇数 |
| :-- | :-: |
| 评测、基准与理论 | 12 |
| 保形预测与风险控制 | 11 |
| 基础模型/多模态校准 | 10 |
| 贝叶斯近似 | 7 |
| 决策层与部署治理 | 7 |
| 训练期校准约束 | 6 |
| 生成式与潜变量 | 5 |
| 语言模型与多智能体 | 5 |
| 单次前向确定性 UQ | 2 |
| 分布式与隐私 | 2 |
| 距离/谱范数感知 | 1 |
