# Persistent career evidence structure

Use the user's persistent file space for live evidence and resume artifacts. Follow the available Library workflow for search, read, create, replace, folder management, versioning, and final saves.

## Folder structure

```text
产品求职证据库/
├── 00-个人求职定位.md
├── 01-经历与项目索引.md
├── 项目证据卡/
│   └── <one Markdown file per project>
├── 待确认事实/
├── JD定制记录/
├── 简历版本/
│   ├── 草稿/
│   └── 历史版本/
└── 最终精品版/
    ├── 通用母版/
    ├── AI产品/
    ├── 风控产品/
    ├── 支付产品/
    └── JD定制/
```

Use templates from `assets/` when initializing missing Markdown files. Keep one project per card; do not turn the bank into one long resume document.

## Naming

Evidence card: `<year>-<project-name>-evidence.md`

General final pair:

- `<name>_通用产品实习_简历_v1.0.html`
- `<name>_通用产品实习_简历_v1.0.pdf`

JD-specific final pair:

- `<name>_<company>_<role>_简历_v1.0.html`
- `<name>_<company>_<role>_简历_v1.0.pdf`

Use the same basename and version for both files. If one changes, regenerate and recheck both.

## Read/write behavior

- Resolve exact files before editing; preserve file identity and version history.
- Update a project card and the index together when capture intent is explicit.
- Store usable inference with its source and label.
- Store critical unconfirmed facts in the card and pending queue; do not silently upgrade them.
- Keep general, direction-specific, and JD-specific resumes separate.
- Save drafts under `简历版本/草稿`; save application-ready pairs only under `最终精品版`.

## Final-quality gate

Require all of the following:

- no red claim and no unresolved critical fact used in the resume;
- correct target role/version metadata;
- one A4 page without clipping, overlap, hidden overflow, or accidental second page;
- visually checked PDF and matching HTML content;
- explicit user confirmation that it is final.

Do not label a failed or unchecked artifact as final.
