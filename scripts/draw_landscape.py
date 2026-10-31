# -*- coding: utf-8 -*-
"""绘制「置信度校准 × 医学AI 现状」气泡时间线图（仿病理基础模型现状风格）。
输出: assets/calibration_landscape.png
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "calibration_landscape.png")
FZ = "/System/Library/Fonts/Hiragino Sans GB.ttc"

def f(sz, bold=False):
    return ImageFont.truetype(FZ, sz, index=1 if bold else 0)

INK = "#22262E"; MUT = "#757B87"; RED = "#C0392B"
LINE = "#B8BDC9"; BLUE = "#2C4A7C"
FILL_A = "#F6EFDC"   # 米黄
FILL_B = "#EDE3C6"
BD = "#D9CCa5"

W, H = 1780, 1280
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 12], fill=BLUE)

def tw(t, fo):
    b = d.textbbox((0, 0), t, font=fo)
    return b[2] - b[0], b[3] - b[1]

def wrap(t, fo, maxw):
    lines, cur = [], ""
    for ch in t:
        if d.textlength(cur + ch, font=fo) <= maxw:
            cur += ch
        else:
            lines.append(cur); cur = ch
    if cur: lines.append(cur)
    return lines

def bubble(cx, cy, w, name, journal, data, fill=FILL_A):
    """journal: 显示在红色里的 venue；data: 数据说明"""
    fn, fj, fd = f(23, True), f(18), f(17)
    maxw = w * 0.80
    name_lines = wrap(name, fn, maxw)
    jw_prefix = "Journal: "
    j_lines = wrap(journal, fj, maxw - d.textlength(jw_prefix, font=fj))
    data_lines = wrap("Data: " + data, fd, maxw)
    gap1, gap2 = 6, 6
    total = (len(name_lines) * 30 + gap1 + len(j_lines) * 26 + gap2 + len(data_lines) * 23)
    hh = total + 44
    d.ellipse([cx - w/2, cy - hh/2, cx + w/2, cy + hh/2], fill=fill, outline=BD, width=2)
    x0 = cx - w * 0.5 + (w - maxw) / 2
    y = cy - total / 2
    for ln in name_lines:
        d.text((x0, y), ln, font=fn, fill=INK); y += 30
    y += gap1
    for i, ln in enumerate(j_lines):
        if i == 0:
            d.text((x0, y), jw_prefix, font=fj, fill=INK)
            d.text((x0 + d.textlength(jw_prefix, font=fj), y), ln, font=fj, fill=RED)
        else:
            d.text((x0 + (0 if i > 0 else 0), y), ln, font=fj, fill=RED)
        y += 26
    y += gap2
    for ln in data_lines:
        d.text((x0, y), ln, font=fd, fill=MUT); y += 23
    return hh

# ============ 标题 ============
d.text((70, 48), "置信度校准 × 医学 AI 现状", font=f(46, True), fill=INK)
d.text((72, 112), "基于文献库 68 篇（2024–2026）· 上：视觉校准主线　下：基础模型 / 语言模型置信线", font=f(22), fill=MUT)
d.line([70, 158, W - 70, 158], fill="#E2E5EA", width=2)

# ============ 双泳道底色 ============
AXIS_Y = 620
d.rounded_rectangle([150, 170, W - 60, AXIS_Y - 8], radius=18, fill="#FBFBF9", outline="#EDEDEA", width=1)
d.rounded_rectangle([150, AXIS_Y + 8, W - 60, 1150], radius=18, fill="#F7F8FA", outline="#E9EBEE", width=1)

# 泳道标签（左侧竖排风格的小牌）
d.rounded_rectangle([24, 320, 138, 430], radius=10, fill="#EEF0F4", outline="#D9DDE4", width=1)
for i, ln in enumerate(["视觉校准", "/ UQ 主线"]):
    d.text((36 + (0 if i == 0 else 8), 336 + i * 34), ln, font=f(21, True), fill=BLUE)
d.rounded_rectangle([24, 780, 138, 940], radius=10, fill="#EEF0F4", outline="#D9DDE4", width=1)
for i, ln in enumerate(["基础模型", "· 语言模型", "  置信线"]):
    d.text((36, 796 + i * 36), ln, font=f(21, True), fill="#7A5C2E")

# ============ 时间轴 ============
d.line([160, AXIS_Y, W - 90, AXIS_Y], fill=LINE, width=4)
d.polygon([(W - 90, AXIS_Y - 9), (W - 66, AXIS_Y), (W - 90, AXIS_Y + 9)], fill=LINE)
YEARS = {2024: 430, 2025: 900, 2026: 1370}
for yr, x in YEARS.items():
    d.ellipse([x - 7, AXIS_Y - 7, x + 7, AXIS_Y + 7], fill=BLUE)
    d.text((x - 26, AXIS_Y + 16), str(yr), font=f(26, True), fill=BLUE)

# ============ 上泳道：视觉校准 / UQ ============
top = [
    # (x, cy, w, 名称, venue, 数据, fill)
    (300, 260, 230, "3D 分割偏移 UQ 评测", "Preprint", "3D 公开分割基准", FILL_A),
    (470, 470, 215, "PULPo 配准", "MICCAI", "配准公开基准", FILL_B),
    (560, 240, 215, "FISHing", "MICCAI", "院内骨髓病理", FILL_A),
    (660, 480, 230, "贝叶斯息肉分割", "Preprint", "息肉公开集", FILL_B),
    (820, 250, 230, "CURVAS 多评分者体积", "MICCAI", "多评分者分割", FILL_A),
    (950, 470, 220, "COMPASS 特征保形", "ISBI", "公共影像管线", FILL_B),
    (1070, 240, 225, "保形覆盖批判", "Preprint", "医疗分类回归", FILL_A),
    (1180, 470, 235, "形态学预测集分割 CP", "Preprint", "公开分割数据集", FILL_B),
    (1300, 245, 215, "CalCErt 逐 bin 认证", "Preprint", "医学影像分类", FILL_A),
    (1420, 475, 225, "SegWithU", "MICCAI", "ACDC·BraTS·LiTS", FILL_B),
    (1540, 245, 230, "CXR-LT 2026 长尾挑战", "MedIA", "多中心长尾胸片", FILL_A),
    (1650, 480, 225, "保形体测量 / 剂量闭环", "Preprint", "放疗剂量闭环", FILL_B),
]
for x, cy, w, n, j, da, fl in top:
    bubble(x, cy, w, n, j, da, fl)

# ============ 下泳道：基础模型 / 语言模型置信 ============
bot = [
    (330, 780, 225, "词序列熵 · 医学问答", "Preprint", "自由式医学 QA", FILL_A),
    (500, 1000, 225, "LLM 增强保形校准", "NeurIPS", "通用 + 医学 QA", FILL_B),
    (670, 780, 230, "校准感知提示学习", "Preprint", "医学 VQA·VLM", FILL_A),
    (830, 1010, 230, "MLLM 少样本校准偏差", "MICCAI", "医学 VQA", FILL_B),
    (960, 780, 220, "MedBayes-Lite 治理层", "Preprint", "临床决策风险", FILL_A),
    (1080, 1010, 225, "医学 VQA 过自信实证", "Preprint", "多数据集 VQA", FILL_B),
    (1210, 780, 220, "CARE 保形安全层", "Preprint", "出院摘要", FILL_A),
    (1330, 1015, 225, "多智能体一致性校准", "Preprint", "医学 QA", FILL_B),
    (1450, 780, 225, "报告生成置信表达", "Preprint", "胸片报告 MIMIC", FILL_A),
    (1580, 1010, 215, "FOCUS 基础模型泛化", "NeurIPS", "眼底多模态", FILL_B),
    (1680, 780, 130, "…", "…", "…", FILL_A),
]
for x, cy, w, n, j, da, fl in bot:
    if n == "…":
        d.text((x - 20, cy - 40), "…", font=f(40, True), fill=MUT)
    else:
        bubble(x, cy, w, n, j, da, fl)

d.text((70, 1200), "注：venue 红字为正式发表（会议/期刊），Preprint 表示 arXiv 预印本；气泡内容为该工作核心贡献与数据规模。完整清单见 data/papers.csv",
       font=f(17), fill="#9AA0AC")

img.save(OUT)
print("saved", OUT, img.size)
