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

## Module combinations

| Target | Modules |
| --- | --- |
| General product | General core |
| AI product | General + AI |
| Risk product | General + Risk |
| Payment product | General + Payment |
| AI risk product | General + AI + Risk |
| Payment risk product | General + Payment + Risk |
| Fintech product | General + Payment + Risk; add AI only when supported by the JD |

Keep underlying facts unchanged across variants. Change selection, ordering, and emphasis only.
