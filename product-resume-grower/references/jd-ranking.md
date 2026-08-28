# JD tailoring and evidence ranking

## Build the capability map

Extract:

- core responsibilities;
- must-have capabilities;
- differentiators;
- hidden expectations inferred from workflow, reporting line, product stage, and stakeholders;
- domain and tool keywords;
- likely interview probes.

Separate explicit JD facts from interpretation. Keep the extracted domain and tool keywords as an explicit list; they are reused later for ATS keyword coverage, not only for the internal capability map.

## Admission gate

Before scoring, exclude red claims, unresolved conflicts, and grade-D evidence. Keep yellow claims only in marked drafts. Allow grade C only as an explicitly labeled project, prototype, or demo.

## Weighted score

Score each eligible evidence card from 0–5 on each dimension:

| Dimension | Weight |
| --- | ---: |
| Direct JD relevance | 35% |
| Product judgment depth | 25% |
| Personal ownership | 15% |
| Delivery and validation maturity | 15% |
| Differentiation | 10% |

Use the score for internal ranking only. Do not present false precision when evidence is incomplete; show qualitative strength and the underlying reason.

## Coverage correction

After ranking, avoid selecting projects that all prove the same capability. Prefer:

- one anchor project with direct JD fit and strong product judgment;
- one supporting project that proves a different core capability;
- one differentiating project when space permits.

For multiple project cards under one internship, synthesize 3–4 non-overlapping bullets rather than listing every project. Allow up to 5 only when this is the sole strongly relevant internship.

## Fit matrix

Return these fields when comparing against a JD:

- JD requirement
- selected evidence card
- module/capability
- evidence grade and risk
- strength
- ATS keyword hit: does the JD's exact term (not a synonym or paraphrase) appear verbatim in the resume text? mark hit / synonym-only / missing
- resume action: keep, strengthen, compress, move, or delete
- interview risk or missing proof

Do not generate a tailored final resume until the user asks. Keep the general master and JD-specific versions separate.

## ATS keyword coverage

Applicant tracking systems often filter on exact keyword matches before a human reads the resume. A close synonym can score as a miss. After building the fit matrix:

1. Take the JD's high-frequency domain and tool keywords (job title variants, core skills, tools, domain terms).
2. Check whether each appears verbatim in the resume text, not only as a paraphrase.
3. For any missing high-priority keyword, only add it when the candidate has real, truthful evidence for it. Prefer inserting the exact term into an existing bullet or the skills line where it is accurate; never keyword-stuff, never claim a tool or domain the candidate has not actually used.
4. When the JD term and the candidate's honest wording genuinely differ, include both once (e.g., 真实措辞 with the JD's exact term in parentheses) rather than replacing a truthful term with an unearned one.

Report keyword coverage as hit / synonym-only / missing, and flag any keyword that cannot be truthfully claimed as a real gap, not a wording fix.

## ATS parse-safety checklist

Layout choices can make an ATS drop content it cannot parse. Verify the resume avoids parser traps:

- single-column layout only; no two-column or side-by-side blocks that scramble reading order;
- no text inside images, icons, logos, or graphics (ATS cannot read them);
- no text boxes or floating shapes; keep body text in the normal document flow;
- no tables for layout; key facts (title, dates, skills) must be real inline/selectable text, not table cells that may be flattened or reordered;
- selectable, real text throughout; no scanned or rasterized text;
- standard section headings (Education, Experience, Projects, Skills) so the parser can segment the resume;
- contact details as plain text, not only inside a header/footer that some parsers ignore;
- standard fonts and simple bullet characters; avoid decorative glyphs.

The existing `assets/one-page-product-resume.html` single-column, no-photo template already satisfies these; use this checklist whenever content or layout changes.
