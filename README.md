# Product Resume Grower｜产品简历增长器

> An evidence-first resume system for product internships.
>
> 一套面向产品实习求职的、以职业证据为核心的可迭代简历系统。

[产品介绍页](https://vikeing.github.io/product-resume-grower/) · [下载 Skill v1.0.0](https://vikeing.github.io/product-resume-grower/downloads/product-resume-grower-v1.0.0.zip) · [查看 Skill 源码](./product-resume-grower)

## Why this exists

多数简历工具直接从“润色文字”开始，但真正决定简历可信度的，是更早的一层：候选人究竟做过什么、承担了什么、做出了哪些判断，以及能拿出什么证据。

Product Resume Grower 将简历写作改造成一条可追溯链路：

```text
原始材料 → 项目证据卡 → 事实与风险准入 → JD 匹配 → 一页简历 → 作品集 / 面试故事
```

它把简历、作品集和面试故事视为同一个职业证据库的不同视图，让每一次项目复盘都能沉淀为下一次求职的起点。

## Core design

- **五段式证据链**：问题—边界—判断—落地—证据。
- **模块化能力模型**：通用产品内核强制启用，AI、风控、支付模块按 JD 自由组合。
- **事实准入机制**：区分已确认事实、材料支持事实、可用推导和关键待确认事实。
- **S–D 证据等级**：执行型事项可以进入素材库，但只有达到对应准入标准的证据才能进入简历。
- **项目筛选机制**：风险与证据等级准入＋五维加权评分＋能力覆盖校正。
- **版本保护**：改写前明确新版本、覆盖旧版本或仅生成未保存草稿。
- **最终精品版**：仅保存已确认、完成视觉检查、可直接投递的 HTML/PDF 成品。

## Install in ChatGPT

1. 下载 [`product-resume-grower-v1.0.0.zip`](https://vikeing.github.io/product-resume-grower/downloads/product-resume-grower-v1.0.0.zip)。
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

