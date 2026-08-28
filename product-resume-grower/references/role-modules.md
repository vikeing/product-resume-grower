# Composable role modules

Always apply the general product core. Add domain modules according to the target role or JD; never replace product evidence with domain vocabulary.

## General product core

Evaluate six capabilities:

1. **Problem framing**: identify users, business value, original workflow, pain, goal, and constraints.
2. **Requirements and scope**: turn ambiguous requests into scenes, priority, boundaries, roles, and acceptance criteria.
3. **Solution and system design**: design flows, states, rules, fields, permissions, pages, exceptions, and recovery.
4. **Product judgment**: explain alternatives, tradeoffs, why a design was chosen, and what was intentionally excluded.
5. **Collaboration and delivery**: connect PRD/prototype work to review, development, testing, acceptance, launch, and iteration.
6. **Validation and iteration**: use metrics, acceptance evidence, stakeholder feedback, defects, or version learning to judge quality.

Treat tools as supporting evidence only.

## AI product module

Look for:

- problem–AI fit and why deterministic code alone is insufficient;
- model, rule, workflow, and human-review boundaries;
- inputs, context, outputs, data provenance, and feedback loops;
- evaluation criteria such as accuracy, latency, cost, usability, or failure rate;
- hallucination control, fallback, sandboxing, interruption, and escalation;
- prototype versus production stage and engineering handoff.

Reject claims that confuse model use with model training, prototype generation with engineering ownership, or AI novelty with user value.

## Risk product module

Look for:

- risk object, event, decision point, and business consequence;
- rules, models, manual review, and escalation boundaries;
- segmentation by frequency, severity, or risk level;
- false-positive, false-negative, efficiency, and experience tradeoffs;
- exceptions, retries, circuit breakers, audit logs, explainability, and traceability;
- list/rule/strategy updates, monitoring, and governance.

Do not let KYC/KYB execution volume dominate unless the target role is compliance operations. Prefer productized rules, workflows, states, decisions, and delivery.

## Payment product module

Look for:

- participants, account relationships, user roles, and permissions;
- money flow, information flow, review flow, and payment lifecycle;
- transaction, account, settlement, statement, or review states;
- first/repeated requests, timeout, failure, retry, duplicate submission, idempotency, refund, and consistency;
- reconciliation, ledger, settlement, fee, FX, bank, country, currency, and cross-border constraints when relevant;
- API clients, enterprise users, individual users, and downstream customer differences;
- placement of compliance and risk controls without breaking the core payment experience.

Reject page-only narratives that do not explain the underlying payment state or business flow.

## Growth product module

Look for:

- the target metric (activation, retention, conversion, referral, revenue) and its position in the funnel/lifecycle;
- the specific stage or drop-off the work addressed, and how it was located;
- hypothesis, the change made, and the mechanism expected to move the metric;
- experiment design: A/B or holdout, segment, sample, duration, and the primary metric plus guardrails;
- read of the result: lift vs. noise, statistical or practical significance, and the ship/kill/iterate decision;
- differentiation between correlation and the candidate's causal contribution.

Reject claims that attribute a metric swing to the candidate's change without an experiment, baseline, or plausible mechanism. Do not present seasonal or campaign-driven movement as product-driven impact.

## Data product module

Look for:

- the decision or product question the data work served;
- metric definition: what was measured, the exact formula, the event/source, and the time window;
- data source, collection/tracking setup, cleaning, and known quality limits;
- analysis method (funnel, cohort, segmentation, correlation) and why it fits the question;
- the finding, its confidence and caveats, and the product decision it drove;
- dashboards, tracking specs, or metric systems the candidate defined or owned.

Reject vanity metrics with no decision attached, undefined or shifting metric definitions, and analysis presented without its data-quality limits. Do not confuse pulling a number with owning a metric.

## Customizable differentiation focus

The resume's differentiation bullet(s) are configurable. Choose the focus that best fits the target JD from:

- **AI** — apply the AI product module.
- **Growth** — apply the growth product module.
- **Data** — apply the data product module.
- **Custom** — a user-defined focus (e.g., 出海/国际化, B端效率, 内容生态, 特定行业 domain depth). When custom, first evaluate it through the general product core; only surface differentiation the candidate has real evidence for, and hold it to the same fact gates as every other module.

Pick the focus per target role; do not stack every module onto one resume. Keep the underlying facts unchanged and change only selection, ordering, and emphasis. The general product core always applies underneath the chosen focus.

## Module combinations

| Target | Modules |
| --- | --- |
| General product | General core |
| AI product | General + AI |
| Growth product | General + Growth |
| Data product | General + Data |
| Risk product | General + Risk |
| Payment product | General + Payment |
| AI risk product | General + AI + Risk |
| Payment risk product | General + Payment + Risk |
| Fintech product | General + Payment + Risk; add AI only when supported by the JD |
| Custom-focus product | General + one user-defined differentiation focus |

Keep underlying facts unchanged across variants. Change selection, ordering, and emphasis only. Choose one primary differentiation focus per resume rather than stacking every module.
