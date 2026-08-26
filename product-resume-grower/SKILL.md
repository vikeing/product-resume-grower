---
name: product-resume-grower
description: Maintain evidence-first product internship resumes for general product, AI, risk/compliance, payment, and fintech roles. Use when the user wants to capture or update product experience from notes, PRDs, prototypes, HTML, screenshots, or work samples; audit facts and ownership; compare fit against a JD; draft or rewrite a one-page Chinese or English resume; manage resume versions; prepare portfolio or interview stories; or generate and save final HTML/PDF resume artifacts.
---

# Product Resume Grower

## Mission

Turn true product work into traceable hiring evidence. Maintain one reusable career evidence bank; treat resumes, portfolio cases, and interview stories as different views of the same facts.

## Non-negotiable rules

- Use the five-part evidence chain: problem, ownership, decision, delivery, evidence.
- Never invent metrics, ownership, launch status, business results, companies, tools, or seniority.
- Allow usable inference in a final resume only when it summarizes supplied material without creating a new objective fact. Keep inferred metrics, ownership, launch status, and business results marked in drafts until confirmed.
- Always apply the general product core. Add AI, risk, and payment modules according to the target JD.
- Default internship resumes to one page. Use 3–4 bullets per core internship; allow up to 5 only when it is the candidate's sole strongly relevant internship.
- Make each bullet prove one claim. Use labeled bullets in Chinese and action-led bullets in English.
- Do not write to the career evidence bank unless the user clearly asks to record, capture, add, or update evidence. Treat discussion, diagnosis, and rewriting as read-only unless stated otherwise.
- Before modifying a saved resume, ask the user to choose: create a new version, overwrite the previous version, or produce an unsaved draft. Skip the question only when the user already specified the choice.
- Never overwrite a general resume with a JD-specific version.
- Put only confirmed, visually checked, application-ready HTML/PDF pairs in the `最终精品版` area.

## Route the request

### Capture or update experience

Read `references/evidence-model.md`, `references/workflow-and-versioning.md`, and `references/library-structure.md`. Extract a project evidence card, label every fact, ask at most three questions that materially affect evidence strength, then update the bank only when write intent is explicit.

### Draft or rewrite resume content

Read `references/resume-writing.md` and `references/role-modules.md`. Load relevant evidence cards, apply fact gates, select evidence, draft bullets, and list any critical facts still awaiting confirmation. Do not update stored facts by default.

### Analyze or tailor to a JD

Read `references/role-modules.md`, `references/jd-ranking.md`, and `references/resume-writing.md`. Build a capability map, combine modules, rank evidence, correct for capability coverage, identify gaps and risky claims, and create a separate JD-specific version if requested.

### Diagnose an existing resume

Read `references/evidence-model.md` and `references/resume-writing.md`. Trace each claim to a source evidence card. Flag unsupported claims before rewriting them.

### Prepare portfolio or interview material

Read `references/interview-and-portfolio.md` plus the relevant role modules. Expand only claims already supported by evidence, preserve limitations, and enforce confidentiality labels.

### Generate final HTML/PDF

Read `references/html-output.md`, `references/workflow-and-versioning.md`, and `references/library-structure.md`. Generate HTML from structured content with `scripts/render_resume.py`; use the available PDF/document capability for PDF conversion and visual QA. Save the matched HTML/PDF pair to `最终精品版` only after the user confirms it is final.

## Core workflow

1. Determine the user's intent and whether it authorizes a write.
2. Resolve the target JD, resume version, project cards, and supplied source materials.
3. Audit facts, ownership, evidence grade, confidentiality, and claim risk.
4. Apply the product core and relevant AI/risk/payment modules.
5. Select evidence using the admission gate, weighted ranking, and coverage correction.
6. Produce the smallest useful output: evidence card, bullets, fit matrix, draft, interview story, or final artifacts.
7. Persist only authorized changes and report the changed items.

## Personal evidence and file storage

Keep live personal evidence and resume versions outside this skill in the user's persistent file space. Use the Library workflow when creating, finding, updating, organizing, or versioning those files. Use the templates in `assets/` to initialize missing files. Do not embed the user's changing career facts into this skill.

## Resource map

- `references/evidence-model.md`: five-part model, fact audit, ownership, confidentiality, and S–D grading.
- `references/role-modules.md`: general product core plus composable AI, risk, and payment modules.
- `references/jd-ranking.md`: JD map, admission gate, weighted scoring, and coverage correction.
- `references/resume-writing.md`: one-page structure, bullet roles, wording, and compression.
- `references/workflow-and-versioning.md`: intent routing, write permissions, and resume version protection.
- `references/library-structure.md`: modular evidence bank and `最终精品版` organization.
- `references/html-output.md`: structured resume data, HTML generation, PDF handoff, and QA.
- `references/interview-and-portfolio.md`: evidence-consistent portfolio and interview expansion.
- `assets/`: human-readable bank templates and the one-page ATS HTML template.
- `scripts/render_resume.py`: deterministic structured JSON to HTML renderer and basic final checks.
