# Product evidence model

## Five-part chain

Extract every project using these fields:

1. **Problem**: record the original workflow, user or business problem, objective, and constraint.
2. **Ownership**: distinguish independent ownership, leading, co-ownership, participation, and work owned by others.
3. **Decision**: record product judgments, alternatives, tradeoffs, scope boundaries, exceptions, and fallbacks.
4. **Delivery**: record research, flows, states, rules, PRDs, prototypes, reviews, development tasks, testing, launch, and iteration stage.
5. **Evidence**: record verified metrics, scale, delivery milestones, quality evidence, proof locations, and unresolved facts.

Do not treat tools or deliverables alone as outcomes. A PRD or prototype proves delivery only when tied to a problem, decision, or validation step.

## Fact status

| Status | Definition | Final-resume rule |
| --- | --- | --- |
| Confirmed | Explicitly confirmed by the user | Allow |
| Material-supported | Directly present in a supplied source | Allow |
| Usable inference | Conservative professional synthesis that creates no new objective fact | Allow with restrained wording |
| Critical fact awaiting confirmation | Inferred metric, ownership, launch status, or business result | Draft only and visibly mark |
| Missing | Required information is absent | Exclude or ask |
| Conflicting | Sources disagree | Resolve before use |

Use `supports`, `covers`, `forms`, `designs`, or `advances to review/testing` for usable inference. Do not replace them with `improves`, `reduces`, `launches`, `leads`, or numeric impact unless confirmed.

## Ownership labels

| Label | Safe wording |
| --- | --- |
| Independently owned | independently designed/completed |
| Led | led, drove, owned |
| Co-owned | co-designed, jointly drove, collaborated on |
| Participated | participated, supported, assisted |
| Not personal work | use as context only |

Attribute AI assistance separately. Distinguish product reasoning, source analysis, prompt or workflow design, prototype generation, engineering implementation, and final validation. Never convert AI-assisted HTML generation into an unsupported frontend-engineering claim.

## External-use labels

- Public in resume
- Portfolio after anonymization
- Interview-only
- Internal-only

Apply the strictest label inherited from any underlying source. Do not copy customer data, internal rule values, proprietary lists, or confidential screenshots into public artifacts.

## Claim risk

- **Green**: evidence and ownership are clear; allow in final output.
- **Yellow**: metric, causality, ownership, stage, or wording needs confirmation; allow only in a marked draft.
- **Red**: fabricated, contradictory, confidential, or not explainable; exclude.

## Evidence grade

| Grade | Standard | Resume use |
| --- | --- | --- |
| S | Launched and supported by credible outcome metrics/proof | Core result |
| A | Delivered or accepted with scale, quality, or milestone proof | Core evidence |
| B | Reviewed or in development/testing without outcome data | State the decision and delivery stage |
| C | Completed proposal, prototype, or demo without real delivery | Project section; label prototype/demo |
| D | Idea, discussion, or weak execution-only item | Bank only |

Do not downgrade a strong infrastructure or compliance project merely because growth metrics are unavailable. Use evidence in this order: verified outcome, scale, delivery milestone, quality/closure, then explainable product judgment.

## Evidence card extraction

1. Extract direct facts and cite their source location in the card.
2. Add usable inferences with an explicit `inference` label.
3. Place critical unconfirmed claims in a separate queue.
4. Assign ownership, confidentiality, claim risk, grade, role tags, and capability tags.
5. Ask no more than three questions, prioritizing questions that can change risk, grade, ownership, or JD fit.
