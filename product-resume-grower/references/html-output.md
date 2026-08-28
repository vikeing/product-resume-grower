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
