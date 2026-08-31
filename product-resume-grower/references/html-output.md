# One-page HTML and PDF output

## Structured input

Use the schema in `assets/resume-data-template.json`. Keep company/title/project fields separate so layout code can control wrapping. Store bullets as arrays; do not insert manual bullet characters.

Generate HTML with:

```bash
python3 scripts/render_resume.py resume-data.json --output resume.html
```

For a candidate final version, add:

```bash
python3 scripts/render_resume.py resume-data.json --output resume.html --strict-final
```

The strict check rejects unresolved markers and excessive bullet counts. It does not prove visual fit.

## HTML requirements

- Use `assets/one-page-product-resume.html`.
- Preserve single-column, no-photo, ATS-readable structure.
- Use semantic text, real lists, selectable text, A4 print CSS, restrained grayscale styling, and no skill bars or decorative charts.
- Do not hide overflow or shrink text below a readable size to force one page.
- Omit empty sections rather than printing empty headings.
- Keep the output ATS parse-safe: single column, no layout tables, no text inside images/icons, no text boxes, selectable text, and standard section headings. See the ATS parse-safety checklist in `references/jd-ranking.md`.

## PDF handoff

Use the available PDF or browser-capable document workflow to export the final HTML to PDF. Render the PDF to page images and visually inspect every page. If it becomes two pages, first remove or compress lower-value content, then adjust spacing modestly; never crop or conceal content.

## Content parity

Check that HTML and PDF contain the same:

- name, contact details, and target title;
- company, role, project, and date fields;
- bullet count and bullet text;
- education, skills, certificates, and links.

Regenerate both files after any content change.

## Save gate

Keep intermediate HTML/PDF in the draft area. Save a matched pair to `最终精品版` only after fact audit, one-page visual QA, parity check, and explicit user approval.

## Interactive typesetting output (final fine-tune only)

After the static HTML passes the save gate, the user may want interactive control over fonts, spacing, margins, bullet symbols, photo, and A4 overflow before exporting the final PDF. Use `assets/typesetting-template.html` to produce a self-contained interactive HTML.

### When to use

Only after:
- Fact audit, interview follow-up defense, and ATS checks have all passed.
- The static HTML version is already saved or ready in `最终精品版`.
- The user explicitly asks for fine-tuning, interactive adjustment, or a typesetting pass.

Do not use the interactive output as a substitute for the static ATS-safe HTML. The static version is the primary deliverable; the interactive version is a convenience layer for visual polish.

### Markdown Schema v2 mapping

The typesetting template accepts Markdown Schema v2. Convert the skill's structured JSON (`assets/resume-data-template.json`) to Markdown as follows:

```
---
schema_version: 2
resume_name: <name>-<target_role>
name: <name>
headline: <target_role>
location: <city extracted from contact[]>
phone: <phone extracted from contact[]>
email: <email extracted from contact[]>
---

## 教育经历

### <education[].title>
date: <education[].dates>

- <education[].details[0]>
- <education[].details[1]>

## 实习经历

### <experience[].title>
role: <experience[].subtitle or derived role>
date: <experience[].dates>

- <experience[].bullets[0]>
- <experience[].bullets[1]>

## 项目经历

### <projects[].title>
date: <projects[].dates>

- <projects[].bullets[0]>

## 技能

- <skills[].label>：<skills[].items>
```

Mapping rules:
- Extract phone, email, city from the `contact[]` array by pattern (phone: digits, email: @, city: short string without /).
- If `experience[].subtitle` is empty, derive `role` from the title segment after the company separator (｜).
- Bullet text is inserted verbatim, preserving `**bold**` and `[link](url)` markdown.
- Omit empty sections (e.g., if `projects[]` is empty, skip the entire `## 项目经历` block).
- `resume_name` is used as the filename for the browser's resume list; keep it concise.

### Producing the interactive HTML

1. Take `assets/typesetting-template.html` as the template.
2. Convert the finalized resume JSON to the Markdown Schema v2 string above.
3. In the template, locate the line `const DEFAULT_RESUME_MD = "...";`.
4. Replace the JSON-stringified value with the user's resume Markdown (JSON-stringified).
5. Replace `const DEFAULT_RESUME_FILENAME = "sample-resume.md";` with a meaningful name like `"<name>-resume.md"`.
6. Write the modified HTML to the user's file space.

When the user opens the resulting HTML in desktop Chrome:
- Their resume is pre-loaded (no import step needed).
- All interactive controls are available: font style, font size, line height, bullet symbols, margins, photo, section reordering, inline editing.
- A4 overflow detection shows if content exceeds one page.
- The user can save an independent HTML or export PDF via Chrome print.

### Privacy

The typesetting template runs entirely in the browser. No resume content, photos, or file handles are uploaded to any server. The template contains no analytics or third-party scripts.

### Attribution

The typesetting template is derived from [resume-formatter](https://github.com/gracexygu/resume-formatter) by gracexygu, MIT License.
