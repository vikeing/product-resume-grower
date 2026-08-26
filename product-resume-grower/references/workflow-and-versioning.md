# Workflow and versioning

## Intent controls writes

| User intent | Evidence-bank action |
| --- | --- |
| Record, capture, add, or update experience | Write/update the relevant card and index |
| Draft or rewrite bullets | Read-only by default |
| Discuss, analyze, evaluate, or diagnose | Read-only |
| Explicitly says do not modify | Strictly read-only |
| Ambiguous | Ask before writing |

Saving resume files is separate from updating facts. Do not let one operation silently trigger the other.

## Capture workflow

1. Resolve supplied materials and the matching project card.
2. Extract the five-part evidence chain.
3. Label fact status, ownership, confidentiality, claim risk, grade, modules, and capabilities.
4. Ask at most three high-leverage questions.
5. Update only when write intent is clear.
6. Report added, changed, conflicting, and pending items.

## Resume workflow

1. Resolve the target role/JD and source evidence snapshot.
2. Apply fact admission and module rules.
3. Rank and coverage-correct evidence.
4. Produce the requested bullets, draft, or full resume.
5. List critical pending facts separately.
6. Do not update the evidence bank unless explicitly requested.

## Version protection

If an existing saved resume may be modified and the user has not specified the mode, ask exactly one choice:

1. Create a new version (recommended)
2. Overwrite the previous version
3. Produce an unsaved draft

Do not ask when the user already selected a mode. Preserve a recoverable prior version when overwriting. Never overwrite a general master with a JD-specific resume.

Record for each saved version:

- version name and source version;
- target role and optional target company/JD;
- evidence cards used;
- pending critical facts;
- concise change summary;
- creation/update date.

## Final artifact workflow

1. Confirm content and all critical facts.
2. Generate a matched HTML/PDF pair.
3. Render and visually inspect the PDF; check that HTML and PDF content agree.
4. Ask the user to confirm that the version is application-ready.
5. Ask version mode if an identically scoped final version exists.
6. Save only the approved pair to `最终精品版`.

Keep drafts, failed renders, overlong versions, and artifacts with yellow/red claims outside `最终精品版`.
