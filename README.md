# Product Resume Grower｜产品简历增长器

> An evidence-first resume system for students with at least one internship.
>
> 一套面向已拥有至少一段实习经历的学生的、以职业证据为核心的可迭代简历系统。

[产品介绍页](https://vikeing.github.io/product-resume-grower/) · [下载 Skill v2.0.0](https://vikeing.github.io/product-resume-grower/downloads/product-resume-grower-v2.0.0.zip) · [查看 Skill 源码](./product-resume-grower)

## Why this exists

多数简历工具直接从“润色文字”开始，但真正决定简历可信度的，是更早的一层：候选人究竟做过什么、承担了什么、做出了哪些判断，以及能拿出什么证据。

Product Resume Grower 将简历写作改造成一条可追溯链路：

```text
原始材料 → 项目证据卡 → 事实与风险准入 → JD 匹配 → 一页简历 → 作品集 / 面试故事
```

它把简历、作品集和面试故事视为同一个职业证据库的不同视图，让每一次项目复盘都能沉淀为下一次求职的起点。

## What's new in v2.0.0 / v2 版本更新

v2.0.0 在 v1.0.0 基础上完成四项升级，目标从"简历通过率"提升到"面试转化率"。

### 1. 人群重定位

| | v1.0.0 | v2.0.0 |
|---|---|---|
| 目标用户 | 面向所有产品实习求职者 | 面向**已拥有至少一段实习经历**的学生 |
| 前提假设 | 无 | 假设用户已有可沉淀的职业证据，Skill 帮助其提炼而非从零起步 |

SKILL.md 新增 `Target user` 显式声明；`openai.yaml` 的 `short_description` 同步更新。

### 2. 面试反脆弱闭环（核心升级）

v1 的 final audit 仅有一句 "remains explainable under interview follow-up"，是一个勾选项，没有配套动作。真实求职中简历被淘汰往往不在筛选环节，而在面试时一句"这个数据怎么来的""你说的'推动'具体推动了谁"就崩了。

v2 将其升级为独立能力：

- **每条 bullet 反向生成 2-3 个面试追问**（覆盖指标来源、所有权真实性、决策深度、落地阶段真实性）。
- **证据卡必须能回答这些追问**，否则触发措辞降级（Defensible → Partly defensible → Indefensible）。
- **降级阶梯**：从量化结果降为过程描述，从主导降为参与，从已上线降为开发中。
- 集成进 `resume-writing.md` 的 Final audit 与 `interview-and-portfolio.md` 的面试准备流程。

### 3. ATS（简历筛选系统）适配

v1 有 HTML 模板方向正确，但 ATS 的真正杀手是关键词命中和解析失败。

v2 新增两个维度：

- **JD 关键词原文命中检查**：在 `jd-ranking.md` 的 fit matrix 新增 `ATS keyword hit` 维度（hit / synonym-only / missing），检查 JD 高频关键词是否在简历原文逐字出现，而非近义改写。
- **ATS 解析安全清单**：单栏布局、无可选文本的图片、无文本框、无布局表格吞噬内容、标准段落标题、纯文本联系方式。`html-output.md` 新增 ATS parse-safe 强制要求。

### 4. 差异化板块可自定义

v1 的模块为 AI、风控、支付三选一。v2 扩展为可自定义：

| 模块 | 说明 |
|---|---|
| AI 产品 | 能力边界、工作流、评估与人工兜底 |
| 增长产品 | 漏斗、A/B 实验、留存、增长策略 |
| 数据产品 | 指标体系、看板、埋点、数据治理 |
| 自定义 | 用户自行定义方向关键词与能力图谱 |

`role-modules.md` 新增 Growth / Data / Custom 模块定义与组合表；`evidence-card-template.md` 的适配模块与候选简历主张同步扩展。

---

### v1 vs v2 文件变更一览

| 文件 | 变更类型 |
|---|---|
| `SKILL.md` | 新增 Target user、差异化自定义规则、面试追问防御、ATS 校验路由 |
| `agents/openai.yaml` | short_description 更新为"已有实习经历"定位 |
| `references/resume-writing.md` | 新增面试追问防御章节 + 降级阶梯 + Final audit 集成 |
| `references/jd-ranking.md` | fit matrix 新增 ATS keyword hit 维度 + ATS 解析安全清单 |
| `references/role-modules.md` | 新增增长/数据/自定义模块 + 组合表更新 |
| `references/html-output.md` | 新增 ATS parse-safe 强制要求 |
| `references/interview-and-portfolio.md` | 关联复用追问防御 |
| `assets/evidence-card-template.md` | 适配模块扩展 + 面试追问防御表 + 候选主张扩展 |

## Core design

- **五段式证据链**：问题—边界—判断—落地—证据。
- **模块化能力模型**：通用产品内核强制启用，AI、增长、数据、风控、支付模块按 JD 自由组合，支持自定义方向。
- **面试反脆弱**：每条 bullet 反向生成面试追问，证据卡须能回答，否则降级措辞。
- **ATS 适配**：JD 关键词原文命中检查 + 解析安全清单，确保简历能被筛选系统正确解析。
- **事实准入机制**：区分已确认事实、材料支持事实、可用推导和关键待确认事实。
- **S–D 证据等级**：执行型事项可以进入素材库，但只有达到对应准入标准的证据才能进入简历。
- **项目筛选机制**：风险与证据等级准入＋五维加权评分＋能力覆盖校正。
- **版本保护**：改写前明确新版本、覆盖旧版本或仅生成未保存草稿。
- **最终精品版**：仅保存已确认、完成视觉检查、可直接投递的 HTML/PDF 成品。

## Install in ChatGPT

1. 下载 [`product-resume-grower-v2.0.0.zip`](https://vikeing.github.io/product-resume-grower/downloads/product-resume-grower-v2.0.0.zip)。
2. 在 ChatGPT 中打开 **Plugins → Skills → Create → Upload from your computer**。
3. 上传 ZIP，等待扫描完成后安装。

安装后可以这样开始：

```text
使用 product-resume-grower，把这份 PRD 整理成项目证据卡。
```

```text
使用 product-resume-grower，分析这份 JD 与我的项目证据匹配度，先不要修改证据库。
```

```text
使用 product-resume-grower，为这份 AI 产品实习 JD 生成一页中文简历新版本。
```

## Repository structure

```text
product-resume-grower/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/

docs/
├── index.html
├── styles.css
├── app.js
└── downloads/
```

实时个人简历、职业证据库和真实业务材料不属于此仓库，也不会随 Skill 发布。

## License

[MIT](./LICENSE)

