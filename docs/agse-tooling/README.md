# AGSE Tooling — 50 AI Automation Systems

Complete build guide for 50 AI automation systems you can deliver with AGSE Tooling.

## Contents

| File | Purpose |
| --- | --- |
| [50-ai-automation-systems-guide.md](./50-ai-automation-systems-guide.md) | Full guide: what it is, step-by-step process, 3 examples, advantages, monetization, faster/better/cheaper for each of the 50 systems |
| [systems.json](./systems.json) | Structured data for all 50 systems (for product tooling / internals) |
| [generate_guide.py](./generate_guide.py) | Regenerates the Markdown + JSON from the source definitions |

## Categories

1. Sales & Revenue
2. Finance & Billing
3. Customer Success
4. Marketing & Content
5. Operations & Data
6. Operations & Supply Chain
7. HR & People
8. Legal & Compliance
9. Insights & Leadership
10. Infrastructure & Intelligence

## Suggested build waves

1. **Foundation** — Workflow Orchestrator, CRM Updater, Data Entry, Knowledge Base  
2. **Revenue** — Lead Qualification, Scheduler, Follow-Up, Proposal, Sales Assistant  
3. **Retention** — Customer Onboarding, Ticket Triage, Churn Prediction, Client Hub  
4. **Scale** — Report Generator, Insights Dashboard, Compliance Checker, System Health Monitor  

## Regenerating

```bash
python3 docs/agse-tooling/generate_guide.py
```
