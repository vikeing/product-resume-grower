---
name: product-resume-grower
description: Maintain evidence-first product internship resumes for students who already have at least one product internship, targeting general product, AI, growth, data, risk/compliance, payment, and fintech roles. Use when the user wants to capture or update product experience from notes, PRDs, prototypes, HTML, screenshots, or work samples; audit facts and ownership; compare fit against a JD including ATS keyword coverage; draft or rewrite a one-page Chinese or English resume; generate interview follow-up probes for each bullet; manage resume versions; prepare portfolio or interview stories; generate and save final HTML/PDF resume artifacts; or produce an interactive self-contained typesetting HTML for final fine-tuning of fonts, spacing, margins, and A4 overflow before PDF export.
---

# Product Resume Grower

## Target user

This skill assumes the candidate already has at least one product internship to draw on. The work is to convert existing internship and project experience into strong, defensible evidence, not to build a resume from zero experience. When a user has no internship at all, say so and focus on extracting the strongest available project/coursework evidence, but keep the internship-first structure as the default.

## Mission

Turn true product work into traceable hiring evidence that survives interview follow-up. Maintain one reusable career evidence bank; treat resumes, portfolio cases, interview answers, and follow-up defenses as different views of the same facts.

## Non-negotiable rules

- Use the five-part evidence chain: problem, ownership, decision, delivery, evidence.
- Never invent metrics, ownership, launch status, business results, companies, tools, or seniority.
- Allow usable inference in a final resume only when it summarizes supplied material without creating a new objective fact. Keep inferred metrics, ownership, launch status, and business results marked in drafts until confirmed.
- Always apply the general product core. Add AI, growth, data, risk, and payment modules according to the target JD. The differentiation section is customizable: pick AI, growth, data, or a user-defined focus.
- Default internship resumes to one page. Use 3–4 bullets per core internship; allow up to 5 only when it is the candidate's sole strongly relevant internship.
- Make each bullet prove one claim. Use labeled bullets in Chinese and action-led bullets in English.
- Do not write to the career evidence bank unless the user clearly asks to record, capture, add, or update evidence. Treat discussion, diagnosis, and rewriting as read-only unless stated otherwise.
- Before modifying a saved resume, ask the user to choose: create a new version, overwrite the previous version, or produce an unsaved draft. Skip the question only when the user already specified the choice.
- Never overwrite a general resume with a JD-specific version.
- Put only confirmed, visually checked, application-ready HTML/PDF pairs in the `最终精品版` area.
- Every resume bullet must survive interview follow-up. For each bullet, generate 2–3 likely follow-up probes and confirm the evidence card can answer them; if it cannot, downgrade the wording instead of keeping an indefensible claim.

## Route the request

### Capture or update experience

Read `references/evidence-model.md`, `references/workflow-and-versioning.md`, and `references/library-structure.md`. Extract a project evidence card, label every fact, ask at most three questions that materially affect evidence strength, then update the bank only when write intent is explicit.

### Draft or rewrite resume content

Read `references/resume-writing.md` and `references/role-modules.md`. Load relevant evidence cards, apply fact gates, select evidence, draft bullets, run the interview follow-up test on every bullet, and list any critical facts still awaiting confirmation. Do not update stored facts by default.

### Analyze or tailor to a JD

Read `references/role-modules.md`, `references/jd-ranking.md`, and `references/resume-writing.md`. Build a capability map, combine modules, rank evidence, correct for capability coverage, run the ATS keyword coverage and parse-safety checks, identify gaps and risky claims, and create a separate JD-specific version if requested.

### Diagnose an existing resume

Read `references/evidence-model.md` and `references/resume-writing.md`. Trace each claim to a source evidence card. Flag unsupported claims before rewriting them.

### Prepare portfolio or interview material

Read `references/interview-and-portfolio.md` plus the relevant role modules. Expand only claims already supported by evidence, preserve limitations, and enforce confidentiality labels.

### Generate final HTML/PDF

Read `references/html-output.md`, `references/workflow-and-versioning.md`, and `references/library-structure.md`. Generate HTML from structured content with `scripts/render_resume.py`; use the available PDF/document capability for PDF conversion and visual QA. Save the matched HTML/PDF pair to `最终精品版` only after the user confirms it is final.

### Fine-tune typesetting (interactive)

Read `references/html-output.md`. Only after the static HTML passes the save gate. Convert the finalized resume JSON to Markdown Schema v2, inject it into `assets/typesetting-template.html` by replacing the `DEFAULT_RESUME_MD` constant, and output a self-contained interactive HTML. The user opens it in desktop Chrome to adjust fonts, spacing, margins, bullet symbols, photo, and A4 overflow, then exports the final PDF. This is a convenience layer on top of the static ATS-safe HTML, not a replacement.

## Core workflow

1. Determine the user's intent and whether it authorizes a write.
2. Resolve the target JD, resume version, project cards, and supplied source materials.
3. Audit facts, ownership, evidence grade, confidentiality, and claim risk.
4. Apply the product core and relevant AI/growth/data/risk/payment modules; set the differentiation focus.
5. Select evidence using the admission gate, weighted ranking, and coverage correction.
6. Run the interview follow-up test on drafted bullets and the ATS keyword/parse checks when a JD is present.
7. Produce the smallest useful output: evidence card, bullets, fit matrix, draft, interview story, or final artifacts.
8. Persist only authorized changes and report the changed items.
9. If the user requests interactive fine-tuning after the static HTML passes the save gate, produce a self-contained typesetting HTML from `assets/typesetting-template.html` with the resume data pre-loaded.

## Personal evidence and file storage

Keep live personal evidence and resume versions outside this skill in the user's persistent file space. Use the Library workflow when creating, finding, updating, organizing, or versioning those files. Use the templates in `assets/` to initialize missing files. Do not embed the user's changing career facts into this skill.

## Resource map

- `references/evidence-model.md`: five-part model, fact audit, ownership, confidentiality, and S–D grading.
- `references/role-modules.md`: general product core plus composable AI, growth, data, risk, and payment modules; customizable differentiation focus.
- `references/jd-ranking.md`: JD map, admission gate, weighted scoring, coverage correction, ATS keyword coverage, and parse-safety checklist.
- `references/resume-writing.md`: one-page structure, bullet roles, wording, compression, and the interview follow-up defense test.
- `references/workflow-and-versioning.md`: intent routing, write permissions, and resume version protection.
- `references/library-structure.md`: modular evidence bank and `最终精品版` organization.
- `references/html-output.md`: structured resume data, HTML generation, PDF handoff, QA, and interactive typesetting output.
- `references/interview-and-portfolio.md`: evidence-consistent portfolio and interview expansion.
- `assets/`: human-readable bank templates, the one-page ATS HTML template, and the interactive typesetting template.
- `assets/typesetting-template.html`: self-contained interactive typesetting HTML (derived from resume-formatter, MIT). Used only for final fine-tuning after the static HTML passes the save gate.
- `scripts/render_resume.py`: deterministic structured JSON to HTML renderer and basic final checks.
