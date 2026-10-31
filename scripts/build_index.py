#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 data/papers.csv 生成 docs/papers-index.md（逐篇索引）。

用法： python scripts/build_index.py
"""
import csv, os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "data", "papers.csv")
OUT = os.path.join(ROOT, "docs", "papers-index.md")

FAM_NAME = {
    "F01": "概率论与度量基础", "F02": "训练期校准约束", "F03": "贝叶斯近似",
    "F04": "证据深度学习", "F05": "距离/谱范数感知", "F06": "生成式与潜变量",
    "F07": "保形预测与风险控制", "F08": "单次前向确定性 UQ",
    "F09": "基础模型/多模态校准", "F10": "语言模型与多智能体",
    "F11": "决策层与部署治理", "F12": "分布式与隐私", "F13": "评测、基准与理论",
}
TIER_NAME = {"P0": "顶会+官方代码", "P1": "顶会无代码", "P2": "预印本+代码", "P3": "其余预印本"}

rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
lines = [
    "# 🔎 论文逐篇索引（自动生成）",
    "",
    f"> 共 {len(rows)} 篇（2024–2026）。由 `scripts/build_index.py` 从 `data/papers.csv` 生成，请勿手改；",
    "> 修改数据后运行 `python scripts/build_index.py` 重新生成。",
    "",
]
for tier in ["P0", "P1", "P2", "P3"]:
    sub = [r for r in rows if r["tier"] == tier]
    if not sub:
        continue
    lines += [f"## {tier} · {TIER_NAME[tier]}（{len(sub)} 篇）", "",
              "| # | 年份 | 会议/期刊 | 方法族 | 论文 | 任务 | 代码 |",
              "| :-: | :-: | :-: | :-: | :-- | :-- | :-- |"]
    for r in sub:
        title = r["title"].replace("|", "\\|")
        code = f'[{r["code"]}](https://{r["code"]})' if r["code"] else "—"
        lines.append(f'| {r["id"]} | {r["year"]} | {r["venue"]} | {FAM_NAME.get(r["family"], r["family"])} | {title} | {r["task"]} | {code} |')
    lines.append("")

cnt = Counter(FAM_NAME.get(r["family"], r["family"]) for r in rows)
lines += ["## 方法族分布", "", "| 方法族 | 篇数 |", "| :-- | :-: |"]
for k, v in cnt.most_common():
    lines.append(f"| {k} | {v} |")
lines.append("")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("written:", OUT, f"({len(rows)} papers)")
