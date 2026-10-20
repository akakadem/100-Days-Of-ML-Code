#!/usr/bin/env python3
"""Generate AGSE Tooling 50 AI Automation Systems guide (Markdown + JSON)."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent


def s(
    id: int,
    name: str,
    category: str,
    what: str,
    steps: list[str],
    examples: list[str],
    advantages: list[str],
    monetization: str,
    faster: str,
    better: str,
    cheaper: str,
) -> dict:
    return {
        "id": id,
        "name": name,
        "category": category,
        "what": what,
        "steps": steps,
        "examples": examples,
        "advantages": advantages,
        "monetization": monetization,
        "fbc": {"faster": faster, "better": better, "cheaper": cheaper},
    }


SYSTEMS: list[dict] = [
    s(
        1,
        "AI Lead Qualification System",
        "Sales & Revenue",
        "Scores and ranks inbound leads using CRM data, firmographics, intent signals, and conversation history so sales only spends time on high-probability opportunities.",
        [
            "Connect lead sources (web forms, ads, chat, imports) and CRM fields.",
            "Define Ideal Customer Profile (ICP) criteria and disqualification rules.",
            "Configure scoring from historical won/lost deals and intent signals.",
            "Auto-enrich leads (company size, industry, tech stack, funding).",
            "Score and tier leads (A/B/C) with explainable reasons.",
            "Route A-tier leads to reps instantly; nurture lower tiers.",
            "Log outcomes and retrain scoring thresholds monthly.",
        ],
        [
            "AGSE Tooling website demo requests scored and routed to enterprise vs SMB reps.",
            "Trade-show badge scans enriched overnight and prioritized for next-day follow-up.",
            "Inbound partner referrals auto-qualified against ICP before SDR outreach.",
        ],
        [
            "Removes bias and inconsistency from manual triage.",
            "Creates a measurable, auditable qualification standard.",
            "Frees SDRs from low-value research work.",
        ],
        "Higher close rates and shorter sales cycles increase revenue per rep; sell as a managed AGSE lead-ops module or usage-based enrichment add-on.",
        "Qualification in seconds instead of hours of research.",
        "Consistent ICP fit scoring with transparent reasons.",
        "Fewer wasted discovery calls and lower cost-per-opportunity.",
    ),
    s(
        2,
        "AI Appointment Scheduler",
        "Sales & Revenue",
        "Books meetings automatically by negotiating times across calendars, time zones, and preference rules via email, SMS, or chat.",
        [
            "Sync calendars (Google/Outlook) and define availability rules.",
            "Set meeting types, durations, buffers, and booking policies.",
            "Deploy booking links and conversational scheduling agents.",
            "Confirm attendees, send reminders, and handle reschedules.",
            "Push events to CRM with lead/opportunity linkage.",
            "Analyze no-show patterns and optimize reminder cadence.",
        ],
        [
            "Prospect replies to an AGSE proposal email and books a technical demo without back-and-forth.",
            "Support-to-sales handoff books a success review when a ticket indicates expansion intent.",
            "Multi-timezone field engineers schedule site assessments with customers automatically.",
        ],
        [
            "Eliminates scheduling ping-pong.",
            "Reduces no-shows with smart reminders.",
            "Protects focus time with policy-aware booking.",
        ],
        "More booked demos and lower SDR coordination overhead; package as AGSE Scheduling Bot subscription.",
        "Meetings booked in one interaction.",
        "Right meeting type with the right stakeholders.",
        "Cuts coordinator and SDR admin time.",
    ),
    s(
        3,
        "AI Email Responder",
        "Sales & Revenue",
        "Drafts or auto-sends context-aware email replies using inbox history, knowledge bases, and CRM context while escalating sensitive threads.",
        [
            "Connect mailboxes and classify intent (pricing, support, sales, spam).",
            "Ground responses in approved knowledge base and CRM records.",
            "Generate draft replies with tone and brand guidelines.",
            "Apply human-in-the-loop for high-risk categories.",
            "Send, track opens/replies, and update CRM activities.",
            "Review quality metrics and refine prompts/templates weekly.",
        ],
        [
            "AGSE Tooling pricing questions answered with approved packaging language.",
            "Partner portal access requests handled with identity checks and next steps.",
            "After-hours inbound RFIs get acknowledgment plus requested datasheets.",
        ],
        [
            "24/7 response coverage.",
            "Consistent brand and compliance language.",
            "Scales inbox volume without linear headcount.",
        ],
        "Sell seats or mailbox packs; faster response increases conversion and retention.",
        "Replies in minutes, not hours.",
        "Accurate, policy-aligned answers.",
        "Lower cost per handled email.",
    ),
    s(
        4,
        "AI Follow-Up Automation",
        "Sales & Revenue",
        "Orchestrates multi-channel follow-ups based on deal stage, engagement signals, and silence thresholds so no opportunity goes cold.",
        [
            "Map stages and SLA timers (e.g., no reply in 2 days).",
            "Define channel sequences (email, LinkedIn, SMS, call task).",
            "Personalize messages with deal context and prior objections.",
            "Trigger nudges on opens, clicks, and page revisits.",
            "Pause on reply or meeting booked; escalate stalled deals.",
            "Report sequence performance by persona and stage.",
        ],
        [
            "Post-demo AGSE prospects get a 5-touch technical nurture if they stall.",
            "Quote viewers who don't respond receive value-focused reminders.",
            "Renewal accounts get automated check-ins 90/60/30 days before expiry.",
        ],
        [
            "Prevents pipeline leakage from forgotten follow-ups.",
            "Personalization at scale.",
            "Clear ownership of next actions.",
        ],
        "Higher pipeline conversion; sell as AGSE Pipeline Nurture automation tier.",
        "Immediate next-touch after inactivity.",
        "Context-aware messaging vs generic drips.",
        "Less manual CRM babysitting.",
    ),
    s(
        5,
        "AI Proposal Generator",
        "Sales & Revenue",
        "Assembles tailored proposals from discovery notes, pricing catalogs, case studies, and past wins into branded, editable documents.",
        [
            "Ingest discovery call transcripts and requirements.",
            "Select solution modules, SLAs, and pricing from catalogs.",
            "Generate narrative, scope, timeline, and risk sections.",
            "Insert relevant case studies and ROI assumptions.",
            "Review/approve in a human workflow; export PDF/Doc.",
            "Track win rates by proposal variant.",
        ],
        [
            "AGSE Tooling RFP responses drafted overnight from a requirements matrix.",
            "SMB packages generated in minutes from a short intake form.",
            "Partner co-branded proposals with auto-inserted partner margins.",
        ],
        [
            "Drastically shorter proposal cycle time.",
            "Fewer pricing/scope errors.",
            "Reusable institutional knowledge.",
        ],
        "Faster deal velocity and higher win rates; charge per proposal or as a sales-enablement SKU.",
        "Hours instead of days to first draft.",
        "Consistent quality and ICP-aligned messaging.",
        "Less senior seller time on formatting.",
    ),
    s(
        6,
        "AI Invoice Automation",
        "Finance & Billing",
        "Creates, validates, and sends invoices from contracts, usage meters, and purchase orders with tax, currency, and approval rules applied automatically.",
        [
            "Connect billing systems, ERP, and contract repositories.",
            "Define invoice templates, tax rules, and approval thresholds.",
            "Detect billable events (milestones, usage, retainers).",
            "Generate invoices, validate line items, and flag anomalies.",
            "Send to customers and sync payment status back to finance.",
            "Reconcile disputes and feed corrections into rules.",
        ],
        [
            "AGSE SaaS subscriptions billed monthly from usage + seat counts.",
            "Professional services milestones invoiced when deliverables are marked complete.",
            "Multi-entity partner invoices generated with correct tax jurisdictions.",
        ],
        [
            "Fewer billing errors and disputes.",
            "On-time invoicing improves cash conversion.",
            "Audit-ready invoice trails.",
        ],
        "Faster cash collection and reduced AR labor; sell AGSE Billing Automation as a finance ops module.",
        "Invoices issued the same day work is completed.",
        "Accurate line items tied to contracts and usage.",
        "Fewer finance FTEs on manual invoice prep.",
    ),
    s(
        7,
        "AI Payment Reminder System",
        "Finance & Billing",
        "Sends polite, escalating, personalized payment reminders and payment links based on aging, customer risk, and communication preferences.",
        [
            "Sync AR aging and payment portals.",
            "Segment accounts by risk, amount, and relationship.",
            "Design escalation ladders (friendly → firm → collections handoff).",
            "Personalize reminder copy and attach invoices/payment links.",
            "Detect payments and stop sequences automatically.",
            "Escalate chronic delinquencies to finance with recommended actions.",
        ],
        [
            "Net-30 AGSE customers receive day-7/21/35 reminders with one-click pay.",
            "Enterprise accounts get account-manager-aware nudges before formal dunning.",
            "International clients receive localized reminders in local currency.",
        ],
        [
            "Reduces days sales outstanding (DSO).",
            "Preserves customer relationships with tone control.",
            "Frees AR teams from repetitive chasing.",
        ],
        "Improved working capital; monetize as AGSE Collections Assist with success-based pricing on recovered AR.",
        "Reminders fire on schedule without manual queues.",
        "Right tone and channel for each customer segment.",
        "Lower cost to collect overdue balances.",
    ),
    s(
        8,
        "AI Customer Onboarding",
        "Customer Success",
        "Guides new customers from signed deal to first value with personalized checklists, training, and proactive risk alerts.",
        [
            "Trigger onboarding from closed-won CRM events.",
            "Generate a plan based on product SKUs and customer maturity.",
            "Assign tasks to customer and internal owners with due dates.",
            "Deliver training content and in-app guidance.",
            "Detect stalled steps and alert CSMs.",
            "Measure time-to-value and onboarding NPS.",
        ],
        [
            "New AGSE Tooling tenants get a 14-day activation plan with integrations checklist.",
            "Enterprise rollouts receive phased department onboarding playbooks.",
            "Self-serve SMB customers get chatbot-guided setup and milestone badges.",
        ],
        [
            "Higher activation and retention.",
            "Standardized onboarding quality.",
            "Early detection of at-risk accounts.",
        ],
        "Lower churn in first 90 days increases LTV; sell onboarding automation as an AGSE Success Pack.",
        "Customers reach first value days sooner.",
        "Personalized paths instead of one-size-fits-all.",
        "Fewer CSM hours per onboarded account.",
    ),
    s(
        9,
        "AI Support Ticket Triage",
        "Customer Success",
        "Classifies, prioritizes, and routes support tickets by urgency, product area, sentiment, and skills required.",
        [
            "Ingest tickets from email, chat, portal, and social.",
            "Classify category, severity, and language.",
            "Detect duplicates and link related incidents.",
            "Route to the best queue or agent skill group.",
            "Suggest macros/knowledge articles for first response.",
            "Monitor SLA breaches and escalate automatically.",
        ],
        [
            "AGSE API outage reports auto-marked P1 and routed to on-call.",
            "Billing questions go to finance ops; how-to questions to L1.",
            "Angry VIP tickets escalate to a dedicated success queue.",
        ],
        [
            "Faster first response and resolution.",
            "Better specialist matching.",
            "Reduced misrouted tickets.",
        ],
        "Higher CSAT and lower cost-to-serve; offer as AGSE Support Intelligence add-on.",
        "Instant prioritization at ticket creation.",
        "Correct queue and suggested answers on first touch.",
        "Less senior engineer time on misrouted noise.",
    ),
    s(
        10,
        "AI Knowledge Base Assistant",
        "Customer Success",
        "Answers employee and customer questions from approved docs, tickets, and runbooks with citations, and flags gaps for content authors.",
        [
            "Index help docs, SOPs, tickets, and release notes.",
            "Enable chat/search with grounded retrieval and citations.",
            "Gate answers by audience (public vs internal).",
            "Capture unanswered questions as content backlog.",
            "Auto-draft article updates from resolved tickets.",
            "Measure deflection rate and answer helpfulness.",
        ],
        [
            "AGSE customers self-serve integration setup via an in-app assistant.",
            "Internal ops asks 'how do we reset partner SSO?' and gets the SOP.",
            "New agents get guided answers during live chats.",
        ],
        [
            "Deflects repetitive tickets.",
            "Keeps knowledge current via feedback loops.",
            "Onboards staff faster.",
        ],
        "Support deflection reduces headcount pressure; sell assistant seats or usage packs.",
        "Answers in seconds with source links.",
        "Cited, approved knowledge instead of tribal lore.",
        "Lower cost per resolved question.",
    ),
    s(
        11,
        "AI Social Media Scheduler",
        "Marketing & Content",
        "Plans, generates, and schedules social posts across channels with brand voice, campaign calendars, and performance feedback.",
        [
            "Connect social accounts and brand style guides.",
            "Generate content calendars from campaigns and product releases.",
            "Draft posts, variants, and assets per channel.",
            "Schedule optimally by audience activity windows.",
            "Moderate comments and surface engagement opportunities.",
            "Report ROI and feed winners into the next calendar.",
        ],
        [
            "AGSE product launches get a 2-week multi-channel rollout calendar.",
            "Thought-leadership snippets from blog posts scheduled across LinkedIn/X.",
            "Regional partners receive localized post packs for co-marketing.",
        ],
        [
            "Consistent presence without daily manual posting.",
            "Channel-native formatting at scale.",
            "Performance-informed content iteration.",
        ],
        "Higher reach and pipeline influence; sell AGSE Social Ops as a marketing automation SKU.",
        "Week of posts prepared in one session.",
        "On-brand, channel-optimized messaging.",
        "Less agency/freelancer spend on routine posting.",
    ),
    s(
        12,
        "AI Content Repurposer",
        "Marketing & Content",
        "Transforms long-form assets (webinars, blogs, proposals) into channel-ready snippets, emails, and social assets.",
        [
            "Ingest source assets (video, PDF, blog, transcript).",
            "Extract key claims, quotes, and CTAs.",
            "Generate formats: threads, carousels, emails, FAQs, shorts scripts.",
            "Apply brand/legal review gates.",
            "Publish or hand off to schedulers/CMS.",
            "Track which derivatives drive engagement.",
        ],
        [
            "One AGSE webinar becomes 12 LinkedIn posts, 3 emails, and a FAQ page.",
            "Customer case study PDF becomes a sales one-pager and ad creative brief.",
            "Release notes become changelog emails and in-app banners.",
        ],
        [
            "Maximizes ROI on every pillar asset.",
            "Maintains message consistency across channels.",
            "Accelerates content velocity.",
        ],
        "More touches from the same production budget; monetize as AGSE Content Factory credits.",
        "Days of content work compressed into hours.",
        "Higher message consistency and coverage.",
        "Lower cost per asset variant.",
    ),
    s(
        13,
        "AI Review Manager",
        "Marketing & Content",
        "Monitors reviews across platforms, drafts responses, flags crises, and routes product insights to the roadmap.",
        [
            "Connect review sites, app stores, and G2/Capterra-like sources.",
            "Classify sentiment, themes, and urgency.",
            "Draft personalized public responses.",
            "Escalate severe complaints to support/legal.",
            "Aggregate themes into product insight reports.",
            "Invite happy customers to leave reviews.",
        ],
        [
            "AGSE Tooling G2 reviews get same-day thank-you or recovery replies.",
            "Negative billing reviews create support tickets automatically.",
            "Feature request themes feed quarterly roadmap briefs.",
        ],
        [
            "Protects brand reputation in public channels.",
            "Turns feedback into product intelligence.",
            "Increases review volume via smart asks.",
        ],
        "Better ratings improve inbound conversion; sell reputation management as an AGSE Growth service.",
        "Near real-time review responses.",
        "Consistent, empathetic public replies.",
        "Less marketing time spent monitoring portals.",
    ),
    s(
        14,
        "AI Data Entry Automation",
        "Operations & Data",
        "Extracts structured fields from emails, PDFs, forms, and screenshots and writes clean records into systems of record.",
        [
            "Identify high-volume manual entry workflows.",
            "Define schemas and validation rules.",
            "OCR/parse documents and map fields.",
            "Human-verify low-confidence extractions.",
            "Write to CRM/ERP/databases with idempotent keys.",
            "Monitor error rates and improve extractors.",
        ],
        [
            "AGSE partner order PDFs become line items in the ERP.",
            "Business cards from events become CRM contacts.",
            "Expense receipts populate accounting categories.",
        ],
        [
            "Eliminates repetitive typing.",
            "Improves data completeness and consistency.",
            "Reduces keying errors.",
        ],
        "Labor savings and cleaner analytics; sell as AGSE Data Capture bots priced by document volume.",
        "Documents processed as they arrive.",
        "Higher field accuracy with validation.",
        "Lower cost per record entered.",
    ),
    s(
        15,
        "AI Document Classifier",
        "Operations & Data",
        "Automatically labels and routes documents (contracts, invoices, SOWs, IDs) into the right repository and workflow.",
        [
            "Inventory document types and destination systems.",
            "Train/configure classifiers on labeled samples.",
            "Ingest from email, scans, and uploads.",
            "Classify, extract metadata, and apply retention tags.",
            "Route to approval queues or archives.",
            "Audit misclassifications and retrain.",
        ],
        [
            "Inbound AGSE legal mailbox sorts NDAs vs MSAs vs DPA addenda.",
            "Vendor packets split into W-9, COI, and MSA automatically.",
            "Customer uploads in the portal go to the correct project folder.",
        ],
        [
            "Faster document findability.",
            "Fewer misplaced files.",
            "Stronger retention/compliance hygiene.",
        ],
        "Reduced search and rework time; offer AGSE Document Ops as part of a content services platform.",
        "Instant sorting at intake.",
        "Correct folder and workflow every time.",
        "Less admin time hunting files.",
    ),
    s(
        16,
        "AI Meeting Notes Assistant",
        "Operations & Data",
        "Transcribes meetings, summarizes decisions, extracts action items, and pushes tasks to project tools and CRM.",
        [
            "Integrate with Zoom/Meet/Teams recordings.",
            "Transcribe with speaker labels.",
            "Summarize decisions, risks, and next steps.",
            "Assign owners and due dates into task systems.",
            "Update CRM opportunity notes automatically.",
            "Share notes to attendees for confirmation.",
        ],
        [
            "AGSE sales discovery calls produce MEDDIC notes in Salesforce.",
            "Internal standup summaries create Jira tickets for blockers.",
            "Customer QBR notes generate follow-up email drafts.",
        ],
        [
            "No more lost action items.",
            "Shared truth across teams.",
            "Sellers stay present in conversations.",
        ],
        "Higher meeting ROI and CRM hygiene; sell AGSE Meeting Intelligence seats.",
        "Notes ready minutes after the call.",
        "Structured decisions and owners, not messy transcripts.",
        "Less time rewriting notes after meetings.",
    ),
    s(
        17,
        "AI CRM Updater",
        "Sales & Revenue",
        "Keeps CRM fields current by reading emails, calls, forms, and product usage so reps don't manually update records.",
        [
            "Map required CRM hygiene fields and ownership rules.",
            "Listen to email/call/product events.",
            "Infer stage, next step, contacts, and competitors.",
            "Propose or auto-write field updates with confidence scores.",
            "Notify owners of material changes.",
            "Score CRM completeness and coach lagging teams.",
        ],
        [
            "AGSE opportunity next-step dates update from email threads.",
            "Champion contacts added when new stakeholders join calls.",
            "Product usage spikes update account health scores.",
        ],
        [
            "Reliable pipeline reporting.",
            "Less rep admin burden.",
            "Better handoffs between teams.",
        ],
        "Cleaner forecasts improve revenue planning; sell CRM hygiene automation as AGSE RevOps Assist.",
        "Records update continuously.",
        "Higher data quality for forecasting.",
        "Reps spend less time on CRM chores.",
    ),
    s(
        18,
        "AI Pipeline Management",
        "Sales & Revenue",
        "Forecasts deal outcomes, flags risk, recommends next best actions, and rebalances pipeline coverage by segment.",
        [
            "Ingest pipeline stages, activities, and historical win data.",
            "Score deal health and close probability.",
            "Surface stuck deals and missing stakeholders.",
            "Recommend plays (discount, exec sponsor, POC).",
            "Generate forecast rollups for leadership.",
            "Close the loop with actual win/loss outcomes.",
        ],
        [
            "AGSE weeklies highlight at-risk enterprise deals with missing economic buyers.",
            "Managers get coaching prompts for reps with thin coverage.",
            "Quarter-end forecasts reweighted by AI probability, not gut feel.",
        ],
        [
            "Earlier intervention on slipping deals.",
            "More accurate forecasts.",
            "Consistent sales coaching signals.",
        ],
        "Improved attainment and forecast reliability; package as AGSE Pipeline Intelligence for RevOps teams.",
        "Risk visible before the deal slips a quarter.",
        "Actionable coaching, not just dashboards.",
        "Less time in manual forecast scrubbing.",
    ),
    s(
        19,
        "AI Inventory Monitor",
        "Operations & Supply Chain",
        "Tracks stock levels, predicts shortages, and triggers reorder or substitution recommendations using demand signals.",
        [
            "Connect WMS/ERP inventory and sales velocity data.",
            "Set safety stock and service-level targets.",
            "Forecast demand by SKU and location.",
            "Alert on stockouts, overstock, and aging inventory.",
            "Recommend purchase orders or transfers.",
            "Review forecast accuracy and tune models.",
        ],
        [
            "AGSE hardware accessory kits auto-reorder before campaign launches.",
            "Regional warehouses get transfer suggestions when demand shifts.",
            "Slow-moving SKUs flagged for promotion or write-down.",
        ],
        [
            "Fewer stockouts and lost sales.",
            "Lower excess inventory carrying costs.",
            "Proactive purchasing decisions.",
        ],
        "Better inventory turns free cash; sell AGSE Inventory Guard for productized tooling SKUs.",
        "Shortage alerts before customers feel them.",
        "Demand-aware reorder quantities.",
        "Less emergency expediting spend.",
    ),
    s(
        20,
        "AI Order Processing",
        "Operations & Supply Chain",
        "Validates and processes orders from email, EDI, and portals—checking credit, inventory, pricing, and shipping rules.",
        [
            "Ingest orders from all channels into a common schema.",
            "Validate SKUs, pricing, taxes, and customer credit.",
            "Check inventory and propose splits/substitutions.",
            "Create ERP sales orders and acknowledgments.",
            "Flag exceptions for human review.",
            "Track first-pass yield and exception causes.",
        ],
        [
            "AGSE reseller email POs become ERP orders without retyping.",
            "Portal orders with pricing mismatches are held with a clear reason.",
            "Rush orders auto-prioritized when SLA tags are present.",
        ],
        [
            "Higher first-pass order accuracy.",
            "Faster order-to-fulfillment cycle.",
            "Clear exception handling.",
        ],
        "Throughput without more ops headcount; sell AGSE Order Autopilot by order volume.",
        "Orders enter the system in minutes.",
        "Pricing and credit rules enforced consistently.",
        "Lower cost per order processed.",
    ),
    s(
        21,
        "AI Shipping Automation",
        "Operations & Supply Chain",
        "Selects carriers, generates labels, notifies customers, and handles exceptions using cost, SLA, and destination rules.",
        [
            "Connect carriers, rate shops, and warehouse systems.",
            "Define shipping policies by customer tier and weight.",
            "Auto-select service level and print labels.",
            "Send tracking updates and ETAs to customers.",
            "Detect delays and trigger proactive communications.",
            "Optimize carrier mix from cost/performance data.",
        ],
        [
            "AGSE kit shipments rate-shop FedEx vs UPS by zone.",
            "VIP customers always get two-day with branded tracking emails.",
            "Delayed parcels trigger apology + revised ETA automatically.",
        ],
        [
            "Lower shipping spend via smart rate shopping.",
            "Better delivery experience.",
            "Fewer 'where's my order?' tickets.",
        ],
        "Freight savings and CSAT lift; monetize AGSE Ship Assist as logistics automation.",
        "Labels and notifications without warehouse bottlenecks.",
        "Policy-correct carrier choices.",
        "Reduced shipping overpay and support load.",
    ),
    s(
        22,
        "AI Expense Categorizer",
        "Finance & Billing",
        "Classifies expenses from receipts and card feeds into GL codes, flags policy violations, and prepares approvals.",
        [
            "Connect corporate cards and receipt uploads.",
            "OCR receipts and match to transactions.",
            "Categorize to chart of accounts and projects.",
            "Flag out-of-policy spend and duplicates.",
            "Route approvals and sync to accounting.",
            "Produce monthly spend insights by team.",
        ],
        [
            "AGSE field travel receipts auto-coded to customer projects.",
            "Software subscriptions flagged if not on the approved vendor list.",
            "Month-end close gets categorized card feeds ready for review.",
        ],
        [
            "Faster month-end close.",
            "Stronger policy compliance.",
            "Cleaner project costing.",
        ],
        "Finance productivity and leakage reduction; sell AGSE Spend Intelligence seats.",
        "Categorization happens as spend occurs.",
        "Consistent GL coding and policy checks.",
        "Less accountant time on receipt sorting.",
    ),
    s(
        23,
        "AI Report Generator",
        "Insights & Leadership",
        "Produces narrative business reports from warehouses and SaaS tools—tables, charts explanations, and recommended actions.",
        [
            "Connect BI warehouse and key SaaS metrics.",
            "Define report templates (weekly leadership, monthly board).",
            "Pull metrics, anomalies, and period comparisons.",
            "Generate narrative commentary and action items.",
            "Distribute via email/Slack with drill-down links.",
            "Collect feedback to improve narrative quality.",
        ],
        [
            "AGSE Monday leadership brief auto-written from CRM + finance + support KPIs.",
            "Customer success QBRs get account health narratives overnight.",
            "Marketing weekly reports explain CAC/ROAS changes in plain language.",
        ],
        [
            "Analysts focus on deep work, not slide assembly.",
            "Consistent reporting cadence.",
            "Action-oriented narratives, not just charts.",
        ],
        "Faster decisions and analyst leverage; sell AGSE Insight Writer as an analytics add-on.",
        "Reports ready before the meeting starts.",
        "Anomaly explanations included automatically.",
        "Lower cost per recurring report.",
    ),
    s(
        24,
        "AI Sales Assistant",
        "Sales & Revenue",
        "Acts as a real-time copilot for sellers—talk tracks, competitive answers, pricing guidance, and next-best-action prompts.",
        [
            "Connect CRM, product catalog, battle cards, and call tools.",
            "Surface account context before meetings.",
            "Provide live suggestions during calls (objections, proofs).",
            "Draft follow-up emails and mutual action plans.",
            "Log activities and coaching insights.",
            "Measure assisted win-rate lift.",
        ],
        [
            "AGSE AEs get competitor rebuttals mid-call from battle cards.",
            "New SDRs receive talk tracks for first discovery calls.",
            "Pricing guardrails appear when discount requests exceed policy.",
        ],
        [
            "Ramps new sellers faster.",
            "Improves live conversation quality.",
            "Enforces pricing discipline.",
        ],
        "Higher attainment per seller; sell AGSE Seller Copilot seats.",
        "Answers and assets available instantly in the flow of work.",
        "Consistent best-practice selling.",
        "Less enablement overhead per rep.",
    ),
    s(
        25,
        "AI Upsell Recommender",
        "Sales & Revenue",
        "Recommends expansion products and timing based on usage, health, and lookalike customer patterns.",
        [
            "Combine product usage, support health, and contract data.",
            "Train propensity models for add-ons and upgrades.",
            "Trigger plays when readiness signals appear.",
            "Generate personalized expansion narratives and quotes.",
            "Assign to AE/CSM with talk tracks.",
            "Track attach rates and refine models.",
        ],
        [
            "AGSE tenants hitting API limits get Pro-tier upgrade prompts.",
            "Accounts using only Module A are offered Module B with ROI proof.",
            "Healthy renewals get multi-year expansion packaging.",
        ],
        [
            "Increases net revenue retention.",
            "Times outreach when value is obvious.",
            "Reduces random spray-and-pray upsells.",
        ],
        "Expansion revenue is high-margin growth; package AGSE Expand AI for CS/AM teams.",
        "Opportunities surface at the right moment.",
        "Recommendations grounded in actual usage.",
        "Less wasted outreach on poor-fit upsells.",
    ),
    s(
        26,
        "AI Churn Prediction",
        "Customer Success",
        "Predicts customers at risk of canceling and recommends retention plays before renewal or cancellation signals harden.",
        [
            "Assemble usage, support, NPS, billing, and engagement features.",
            "Train churn risk models with explainable drivers.",
            "Score accounts daily and tier risk.",
            "Launch save plays (training, exec outreach, credits).",
            "Track save rates and model drift.",
            "Feed learnings into product and onboarding.",
        ],
        [
            "AGSE accounts with declining weekly active users flagged 60 days pre-renewal.",
            "Billing disputes combined with low usage escalate to save desks.",
            "Champion departure events trigger stakeholder mapping plays.",
        ],
        [
            "Protects recurring revenue.",
            "Focuses CSMs on the highest-risk book.",
            "Turns churn drivers into product priorities.",
        ],
        "Retained ARR is pure profit uplift; sell AGSE Retention Radar to SaaS CS orgs.",
        "Risk known weeks earlier than manual review.",
        "Explainable drivers guide the right save play.",
        "CS capacity spent where it matters most.",
    ),
    s(
        27,
        "AI Feedback Analyzer",
        "Customer Success",
        "Clusters qualitative feedback from surveys, tickets, calls, and reviews into themes with sentiment and urgency.",
        [
            "Collect feedback from all channels into one lake.",
            "Cluster themes and map to product areas.",
            "Score severity and frequency.",
            "Publish insight digests to product and CX leaders.",
            "Link themes to tickets/epics for action.",
            "Measure theme resolution impact on CSAT.",
        ],
        [
            "AGSE NPS verbatims reveal onboarding friction as a top theme.",
            "Support tickets cluster around a specific API error after a release.",
            "Sales call objections highlight pricing packaging confusion.",
        ],
        [
            "Turns noise into prioritized insight.",
            "Aligns product with customer voice.",
            "Detects emerging issues early.",
        ],
        "Better product decisions reduce churn and support cost; sell AGSE Voice-of-Customer analytics.",
        "Insights compiled continuously, not quarterly.",
        "Theme clarity across thousands of comments.",
        "Less analyst time coding open text.",
    ),
    s(
        28,
        "AI Survey Automation",
        "Customer Success",
        "Triggers the right survey at the right moment, personalizes questions, and routes responses into workflows.",
        [
            "Define survey triggers (post-support, post-onboarding, renewal).",
            "Personalize question sets by persona and journey stage.",
            "Send via email/in-app/SMS with throttling rules.",
            "Analyze responses and open text in real time.",
            "Create tickets or CSM tasks from detractors.",
            "Close the loop with respondents.",
        ],
        [
            "AGSE support tickets closed → CSAT survey within 1 hour.",
            "Day-14 onboarded users get activation experience survey.",
            "Renewal-90 surveys feed health scores and save plays.",
        ],
        [
            "Higher response rates via timing.",
            "Actionable detractor workflows.",
            "Less survey fatigue with throttling.",
        ],
        "Better CX data improves retention marketing; offer AGSE Survey Orchestrator.",
        "Surveys fire at peak relevance moments.",
        "Questions tailored to the journey stage.",
        "Lower ops cost to run continuous listening.",
    ),
    s(
        29,
        "AI Webinar Automation",
        "Marketing & Content",
        "Runs webinar pipelines end-to-end: promotion, registration nurture, live assistance, and post-event follow-up.",
        [
            "Create landing pages and registration flows.",
            "Generate promo sequences and social assets.",
            "Remind registrants and reduce no-shows.",
            "Assist live Q&A moderation and highlight clips.",
            "Score attendees and route hot leads to sales.",
            "Send personalized replays and nurture tracks.",
        ],
        [
            "AGSE monthly product webinar auto-promoted for 2 weeks.",
            "Attendees who ask pricing questions become sales-ready leads.",
            "No-shows get a replay email with a booking CTA.",
        ],
        [
            "Consistent webinar machine without large event teams.",
            "Higher show-up and conversion rates.",
            "Automatic lead scoring from engagement.",
        ],
        "Pipeline from events with less labor; sell AGSE Webinar OS for demand gen.",
        "Promo-to-follow-up runs without daily babysitting.",
        "Engagement-based lead quality.",
        "Lower cost per webinar-sourced opportunity.",
    ),
    s(
        30,
        "AI Job Application Screener",
        "HR & People",
        "Screens resumes and applications against role criteria, ranks candidates, and flags potential mismatches or compliance risks.",
        [
            "Define role scorecards and must-have skills.",
            "Ingest applications from ATS/email.",
            "Parse resumes and score against scorecards.",
            "Flag gaps, risks, and standout signals.",
            "Shortlist for recruiters with explanations.",
            "Audit for bias and adjust criteria.",
        ],
        [
            "AGSE engineering roles screened for required stack experience.",
            "High-volume SDR applications ranked by relevant outbound history.",
            "Internal mobility applications matched to open role scorecards.",
        ],
        [
            "Faster shortlists.",
            "More consistent screening standards.",
            "Recruiters focus on interviews, not inbox triage.",
        ],
        "Shorter time-to-hire reduces vacancy cost; sell AGSE Talent Screen for hiring teams.",
        "Hundreds of resumes reviewed in minutes.",
        "Explainable fit vs gut-feel screening.",
        "Lower cost per screened candidate.",
    ),
    s(
        31,
        "AI Interview Scheduler",
        "HR & People",
        "Coordinates candidate and interviewer calendars, sends prep briefs, and manages reschedules across interview loops.",
        [
            "Connect ATS stages and interviewer pools.",
            "Define loop templates by role.",
            "Offer candidates self-serve slots within constraints.",
            "Send confirmations, prep packets, and Zoom links.",
            "Handle cancellations and redistribute panels.",
            "Track scheduling SLA and candidate experience.",
        ],
        [
            "AGSE hiring loops for engineers auto-book phone + technical + culture stages.",
            "Executive interviews scheduled across multiple time zones.",
            "No-show interviews auto-reschedule with candidate preference memory.",
        ],
        [
            "Cuts days of email coordination.",
            "Improves candidate experience.",
            "Protects interviewer focus time.",
        ],
        "Faster hiring throughput; include in AGSE Talent Ops suite.",
        "Loops booked in one candidate session.",
        "Correct interviewers and prep materials every time.",
        "Less coordinator FTE time.",
    ),
    s(
        32,
        "AI Employee Onboarding",
        "HR & People",
        "Personalizes new-hire setup: accounts, training paths, buddy matching, and day-1-to-day-90 checklists.",
        [
            "Trigger from signed offer / start date in HRIS.",
            "Provision accounts and equipment requests.",
            "Generate role-based learning paths.",
            "Schedule intro meetings and culture sessions.",
            "Track completion and nudge managers on blockers.",
            "Survey new-hire experience and fix friction.",
        ],
        [
            "AGSE new AEs get CRM, dialer, and product certification tracks.",
            "Engineers receive repo access, security training, and buddy intros.",
            "Remote hires get equipment shipping + day-1 IT checklist automation.",
        ],
        [
            "Faster productivity ramp.",
            "Fewer missed IT/setup steps.",
            "Better new-hire experience and retention.",
        ],
        "Reduced early attrition and ramp cost; sell AGSE People Onboard automation.",
        "Day-1 readiness without frantic IT tickets.",
        "Role-specific paths instead of generic packets.",
        "Lower HR/IT coordination cost per hire.",
    ),
    s(
        33,
        "AI Timesheet Collector",
        "HR & People",
        "Reminds employees to submit timesheets, validates entries against projects/policies, and prepares payroll/billing exports.",
        [
            "Connect project codes and payroll systems.",
            "Send smart reminders before deadlines.",
            "Validate hours, overtime, and project allocations.",
            "Flag anomalies for manager approval.",
            "Export clean timesheets to payroll/billing.",
            "Report utilization and missing submissions.",
        ],
        [
            "AGSE consultants submit weekly project hours with client tags.",
            "Internal R&D time auto-suggested from calendar blocks.",
            "Managers approve exception-only timesheets each Friday.",
        ],
        [
            "Higher on-time submission rates.",
            "Cleaner billable utilization data.",
            "Fewer payroll corrections.",
        ],
        "Accurate billing for services firms; sell AGSE Time Capture for professional services.",
        "Reminders and validation before payroll cutoff.",
        "Policy-compliant entries with fewer errors.",
        "Less admin chasing missing timesheets.",
    ),
    s(
        34,
        "AI Compliance Checker",
        "Legal & Compliance",
        "Continuously checks processes, documents, and configurations against policy frameworks and alerts on drift.",
        [
            "Encode policies (SOC2, GDPR, internal controls) as checks.",
            "Scan configs, access lists, and document trails.",
            "Flag violations and missing evidence.",
            "Assign remediation owners with deadlines.",
            "Collect evidence packages for audits.",
            "Track compliance posture over time.",
        ],
        [
            "AGSE AWS configs checked for public bucket exposure.",
            "Vendor DPAs verified before onboarding completes.",
            "Access reviews detect terminated users with lingering SaaS seats.",
        ],
        [
            "Continuous assurance vs annual scramble.",
            "Clear remediation ownership.",
            "Lower audit preparation pain.",
        ],
        "Avoids fines and deal blockers; sell AGSE Compliance Guard to security/GRC teams.",
        "Issues found as they appear, not at audit time.",
        "Consistent policy interpretation.",
        "Less expensive manual control testing.",
    ),
    s(
        35,
        "AI Contract Analyzer",
        "Legal & Compliance",
        "Reviews contracts for risks, non-standard clauses, obligations, and renewal terms—producing negotiation playbooks.",
        [
            "Ingest contracts (PDF/DOCX) into a secure vault.",
            "Extract parties, terms, SLAs, liability, and renewals.",
            "Compare against playbook/fallback positions.",
            "Highlight risky deviations with suggested redlines.",
            "Track obligations and renewal alerts.",
            "Feed approved language back into templates.",
        ],
        [
            "AGSE customer MSAs reviewed for uncapped liability before signature.",
            "Vendor contracts flagged for auto-renewal trap clauses.",
            "Partner agreements summarized for commercial teams in plain language.",
        ],
        [
            "Faster legal turnaround.",
            "Fewer missed risky clauses.",
            "Stronger obligation and renewal hygiene.",
        ],
        "Accelerates deal desk and reduces legal risk; sell AGSE Contract IQ per document or seat.",
        "First-pass review in minutes.",
        "Playbook-aligned risk spotting.",
        "Lower outside-counsel spend on routine reviews.",
    ),
    s(
        36,
        "AI Project Status Reporter",
        "Operations & Data",
        "Compiles project health from tickets, docs, and chat into stakeholder-ready status updates.",
        [
            "Connect Jira/Asana, docs, and Slack channels.",
            "Detect milestones, blockers, and burndown trends.",
            "Draft status narratives by audience (exec vs team).",
            "Highlight risks with owners and ETAs.",
            "Distribute on a cadence; capture feedback.",
            "Archive status history for audits and retros.",
        ],
        [
            "AGSE implementation projects get Friday client status emails auto-drafted.",
            "Internal platform teams publish weekly exec risk digests.",
            "Agency-style client portals update from live ticket data.",
        ],
        [
            "Consistent status quality.",
            "Earlier visibility into blockers.",
            "Less PM time writing updates.",
        ],
        "Higher delivery predictability; sell AGSE Project Pulse for delivery orgs.",
        "Status ready without chasing updates.",
        "Risks framed clearly for the audience.",
        "Lower PM overhead per project.",
    ),
    s(
        37,
        "AI Task Automation",
        "Operations & Data",
        "Detects repetitive digital workflows and automates them with RPA/AI agents across apps—with approvals for exceptions.",
        [
            "Mine repetitive tasks from tickets and process logs.",
            "Prioritize automations by volume and ROI.",
            "Build agents/RPA bots with clear success criteria.",
            "Add exception queues for human review.",
            "Deploy, monitor failure rates, and alert owners.",
            "Expand successful patterns across teams.",
        ],
        [
            "AGSE ops auto-creates customer folders and Slack channels on closed-won.",
            "Support macros become full ticket workflows for password resets.",
            "Finance bots move approved invoices into payment batches.",
        ],
        [
            "Removes busywork from skilled staff.",
            "Standardizes process execution.",
            "Creates a compounding automation portfolio.",
        ],
        "Labor arbitrage and error reduction; sell AGSE Workflow Bots as a platform + build service.",
        "Tasks complete as soon as triggers fire.",
        "Fewer human process deviations.",
        "Lower cost per repeated workflow run.",
    ),
    s(
        38,
        "AI File Organizer",
        "Operations & Data",
        "Renames, tags, deduplicates, and files documents into the correct folders using content understanding.",
        [
            "Connect drives (Google Drive, SharePoint, S3).",
            "Define taxonomy, naming conventions, and retention.",
            "Scan new/changed files for content and duplicates.",
            "Propose moves/renames; auto-apply high-confidence actions.",
            "Quarantine sensitive files found in the wrong places.",
            "Report storage savings and findability metrics.",
        ],
        [
            "AGSE shared drives cleaned of duplicate proposal versions.",
            "Customer folders auto-structured by account ID and year.",
            "PII-bearing files moved to restricted locations automatically.",
        ],
        [
            "Faster file discovery.",
            "Reduced storage bloat.",
            "Better security posture for sensitive docs.",
        ],
        "Productivity and storage savings; include in AGSE Knowledge Ops offering.",
        "Files organized continuously, not in annual cleanups.",
        "Consistent naming and taxonomy.",
        "Less time lost searching for the right version.",
    ),
    s(
        39,
        "AI Transcription Automation",
        "Operations & Data",
        "Converts audio/video into searchable text with speakers, timestamps, and downstream summaries or translations.",
        [
            "Ingest call recordings, podcasts, and training videos.",
            "Transcribe with speaker diarization.",
            "Punctuate, redact PII where required, and index.",
            "Generate summaries, chapters, and highlight clips.",
            "Push text to CRM/KB/search.",
            "Measure accuracy and correct domain vocabulary.",
        ],
        [
            "AGSE support calls transcribed for QA coaching.",
            "Training videos become searchable lesson text.",
            "Customer interviews transcribed for product research.",
        ],
        [
            "Makes spoken content searchable.",
            "Enables coaching and compliance review.",
            "Feeds other AI systems with text.",
        ],
        "Unlocks value trapped in audio; sell AGSE Transcribe as usage-based media intelligence.",
        "Transcripts available shortly after recording.",
        "Searchable, structured speech with speakers.",
        "Cheaper than manual transcription services.",
    ),
    s(
        40,
        "AI Language Translator",
        "Operations & Data",
        "Translates documents, tickets, and UI/help content with domain glossaries while preserving formatting and tone.",
        [
            "Build glossaries for AGSE product terminology.",
            "Connect content sources (tickets, docs, CMS).",
            "Translate with glossary enforcement and QA checks.",
            "Human-review high-visibility content.",
            "Publish localized assets and keep them in sync.",
            "Track quality ratings by language.",
        ],
        [
            "AGSE help center articles localized to Spanish, French, and German.",
            "Support tickets from multilingual customers translated for agents.",
            "Partner contracts drafted bilingual with consistent defined terms.",
        ],
        [
            "Expands addressable markets.",
            "Faster global support.",
            "Consistent product terminology worldwide.",
        ],
        "New-market revenue with less localization overhead; sell AGSE Locale Engine.",
        "Translations in minutes for operational content.",
        "Glossary-consistent product language.",
        "Lower spend on full human translation for drafts.",
    ),
    s(
        41,
        "AI Voice Assistant",
        "Infrastructure & Intelligence",
        "Provides voice interfaces for internal ops or customer channels—answering FAQs, capturing intents, and executing allowed actions.",
        [
            "Define intents, tools, and security boundaries.",
            "Connect telephony/IVR or workplace voice surfaces.",
            "Ground answers in knowledge bases and live systems.",
            "Hand off to humans with full context when needed.",
            "Log transcripts and completion rates.",
            "Improve intents from failed conversations.",
        ],
        [
            "AGSE customers call IVR to check order/shipment status by voice.",
            "Employees ask workplace assistant for PTO balance and IT ticket status.",
            "Field teams dictate inventory counts hands-free into ERP.",
        ],
        [
            "Hands-free access to systems.",
            "24/7 voice coverage for common intents.",
            "Smooth escalation with context.",
        ],
        "Deflects call-center volume; sell AGSE Voice Agent minutes + intent packs.",
        "Common requests resolved without wait queues.",
        "Natural language vs rigid phone trees.",
        "Lower cost per voice interaction.",
    ),
    s(
        42,
        "AI Competitor Monitor",
        "Marketing & Content",
        "Watches competitor sites, pricing pages, job posts, and reviews to surface strategic changes for GTM teams.",
        [
            "Define competitor set and watchlist URLs/feeds.",
            "Scrape/monitor changes to messaging, pricing, and features.",
            "Summarize material changes with business impact.",
            "Alert sales/marketing with battle-card updates.",
            "Archive historical competitor snapshots.",
            "Review monthly for strategic planning.",
        ],
        [
            "AGSE pricing page watches detect a competitor's new free tier.",
            "Job postings signal a competitor building an AI module.",
            "Review spikes highlight a rival outage AGSE can respond to.",
        ],
        [
            "Earlier competitive awareness.",
            "Fresher battle cards.",
            "Evidence-based GTM pivots.",
        ],
        "Protects win rates; sell AGSE Competitive Radar as a GTM intelligence subscription.",
        "Change alerts within hours of publish.",
        "Summaries ready for sellers, not raw HTML diffs.",
        "Less analyst time on manual competitor checks.",
    ),
    s(
        43,
        "AI Price Monitoring",
        "Marketing & Content",
        "Tracks market and competitor pricing, MAP violations, and discount patterns to inform pricing and promotions.",
        [
            "Identify SKUs and competitor/channel price sources.",
            "Collect prices on a schedule with change detection.",
            "Normalize currencies, bundles, and promo terms.",
            "Alert on undercuts, MAP breaches, and anomalies.",
            "Recommend price or promo responses.",
            "Feed insights into pricing committees.",
        ],
        [
            "AGSE channel partners monitored for MAP compliance.",
            "Competitor seat prices tracked before AGSE annual packaging reviews.",
            "Promo end dates detected so AGSE can time counter-offers.",
        ],
        [
            "Protects margin and brand price integrity.",
            "Informs competitive packaging.",
            "Reduces surprise undercutting.",
        ],
        "Margin protection is direct profit; sell AGSE Price Watch for product/finance teams.",
        "Price changes detected quickly across channels.",
        "Normalized comparisons across messy listings.",
        "Less manual price shopping by analysts.",
    ),
    s(
        44,
        "AI Local SEO Monitor",
        "Marketing & Content",
        "Tracks local search rankings, listings accuracy, and reviews for each location—and recommends fixes.",
        [
            "Inventory locations and NAP (name/address/phone) data.",
            "Monitor Google Business Profile and local rank keywords.",
            "Detect listing inconsistencies and duplicate pages.",
            "Recommend content/citation fixes.",
            "Track review velocity and rating trends.",
            "Report local visibility by market.",
        ],
        [
            "AGSE regional offices keep consistent NAP across directories.",
            "Local service keywords monitored for each metro area.",
            "Duplicate listings flagged and merge recommendations issued.",
        ],
        [
            "Higher local discovery and foot/lead traffic.",
            "Consistent brand presence locally.",
            "Faster response to ranking drops.",
        ],
        "More local inbound leads; sell AGSE Local Presence for multi-location GTM.",
        "Ranking/listing issues caught weekly.",
        "Actionable fix lists per location.",
        "Lower agency spend on routine local audits.",
    ),
    s(
        45,
        "AI Ad Performance Monitor",
        "Marketing & Content",
        "Watches paid campaigns across channels, diagnoses underperformance, and recommends budget/creative shifts.",
        [
            "Connect ad platforms and conversion analytics.",
            "Define KPIs (CAC, ROAS, CPA) and alert thresholds.",
            "Detect fatigue, wasted spend, and audience drift.",
            "Recommend pause/scale/creative refresh actions.",
            "Optionally auto-apply bounded budget rules.",
            "Produce weekly performance narratives.",
        ],
        [
            "AGSE LinkedIn campaigns paused when CPA exceeds target for 3 days.",
            "Creative fatigue detected on top ads with refresh suggestions.",
            "Budget shifted from low-ROAS geos to high-intent segments.",
        ],
        [
            "Protects ad budget from silent waste.",
            "Faster optimization loops.",
            "Clear narratives for stakeholders.",
        ],
        "Higher paid efficiency improves pipeline ROI; sell AGSE Ads Pilot for growth teams.",
        "Underperforming spend caught same day.",
        "Root-cause suggestions, not just charts.",
        "Less wasted media budget and analyst time.",
    ),
    s(
        46,
        "AI Client Communication Hub",
        "Infrastructure & Intelligence",
        "Unifies client emails, chats, meetings, and tickets into a single timeline with AI summaries and next actions.",
        [
            "Connect email, Slack/Teams, support, and CRM.",
            "Build a unified per-account activity timeline.",
            "Summarize open threads and commitments.",
            "Suggest replies and owners for dangling actions.",
            "Share a client-safe portal view if needed.",
            "Measure response SLAs across channels.",
        ],
        [
            "AGSE account teams see every customer touch before a QBR.",
            "New CSMs ramp on an account by reading AI timeline summaries.",
            "Open promises across email/Slack become tracked tasks.",
        ],
        [
            "No more lost context across tools.",
            "Faster, consistent client responses.",
            "Cleaner internal handoffs.",
        ],
        "Higher retention via better communication; sell AGSE Client Hub seats for AM/CS teams.",
        "Full context available before every client touch.",
        "Commitments don't fall through cracks.",
        "Less time stitching history from five apps.",
    ),
    s(
        47,
        "AI Backup Automation",
        "Infrastructure & Intelligence",
        "Schedules, verifies, and reports on backups across SaaS and infrastructure—alerting on failures and restore-test gaps.",
        [
            "Inventory critical systems and RPO/RTO targets.",
            "Configure backup jobs and retention policies.",
            "Verify backup success and integrity checks.",
            "Run periodic restore tests with evidence logs.",
            "Alert on failures and missed windows.",
            "Produce compliance-ready backup reports.",
        ],
        [
            "AGSE Salesforce and Postgres backups verified nightly.",
            "Failed SaaS export jobs reopen until resolved.",
            "Quarterly restore drills documented for SOC2 evidence.",
        ],
        [
            "Reduces data-loss risk.",
            "Proves recoverability, not just backups.",
            "Audit-friendly evidence trails.",
        ],
        "Avoids catastrophic loss costs; sell AGSE Resilience Ops monitoring.",
        "Failures known immediately.",
        "Restore-tested confidence vs assumed backups.",
        "Less manual backup babysitting by IT.",
    ),
    s(
        48,
        "AI System Health Monitor",
        "Infrastructure & Intelligence",
        "Correlates metrics, logs, and traces to detect incidents early, suggest causes, and open actionable alerts.",
        [
            "Connect observability stacks (metrics/logs/traces).",
            "Baseline normal behavior per service.",
            "Detect anomalies and correlate related signals.",
            "Open incidents with probable root-cause hints.",
            "Suggest runbooks and owners on-call.",
            "Post-incident, refine detectors and suppress noise.",
        ],
        [
            "AGSE API latency anomalies alert before customer tickets spike.",
            "Error bursts correlated to a specific deploy version.",
            "Noisy alerts suppressed after learning seasonal patterns.",
        ],
        [
            "Earlier incident detection.",
            "Less alert fatigue.",
            "Faster mean time to recovery (MTTR).",
        ],
        "Uptime protects revenue and brand; sell AGSE Observability Copilot.",
        "Issues caught before widespread customer impact.",
        "Correlated signals with suggested causes.",
        "Fewer engineer hours on false alarms.",
    ),
    s(
        49,
        "AI Workflow Orchestrator",
        "Infrastructure & Intelligence",
        "Coordinates multi-step cross-system processes with AI decisioning, retries, and human approvals at control points.",
        [
            "Map end-to-end processes (quote-to-cash, hire-to-retire).",
            "Connect systems via APIs/events.",
            "Encode business rules and AI decision nodes.",
            "Add approval gates and SLA timers.",
            "Monitor runs, failures, and bottlenecks.",
            "Version workflows and roll back safely.",
        ],
        [
            "AGSE quote-to-cash: CRM → proposal → e-sign → billing → provisioning.",
            "Partner onboarding: KYC → contract → portal access → kickoff.",
            "Incident response: detect → page → mitigate → customer notify → RCA.",
        ],
        [
            "Connects siloed automations into outcomes.",
            "Visible process SLAs and failure points.",
            "Governed AI decisions with human gates.",
        ],
        "Platform value compounds across use cases; sell AGSE Orchestration Cloud as the control plane.",
        "Multi-system processes finish without manual glue work.",
        "Consistent, auditable process execution.",
        "Lower integration maintenance vs point scripts.",
    ),
    s(
        50,
        "AI Business Insights Dashboard",
        "Insights & Leadership",
        "Unifies KPIs across sales, finance, product, and support into an executive dashboard with AI anomaly narratives and recommended actions.",
        [
            "Define North Star and departmental KPI trees.",
            "Connect warehouses and SaaS metrics.",
            "Build living dashboards with drill-downs.",
            "Add AI narratives explaining movers and outliers.",
            "Push alerts when KPIs breach thresholds.",
            "Review weekly with owners and update targets.",
        ],
        [
            "AGSE exec dashboard shows ARR, NRR, CAC, churn risk, and uptime together.",
            "Product leaders drill from revenue impact to feature adoption.",
            "Board packs auto-annotate the three biggest weekly changes.",
        ],
        [
            "Single source of operational truth.",
            "Faster executive decision cycles.",
            "Narratives turn data into action.",
        ],
        "Better decisions compound revenue and margin; sell AGSE Command Center as an executive intelligence product.",
        "Cross-functional truth available in one place in real time.",
        "Anomalies explained, not just visualized.",
        "Less analyst time assembling leadership packs.",
    ),
]


CATEGORIES_ORDER = [
    "Sales & Revenue",
    "Finance & Billing",
    "Customer Success",
    "Marketing & Content",
    "Operations & Data",
    "Operations & Supply Chain",
    "HR & People",
    "Legal & Compliance",
    "Insights & Leadership",
    "Infrastructure & Intelligence",
]


def render_markdown(systems: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# 50 AI Automation Systems for AGSE Tooling")
    lines.append("")
    lines.append(
        "A practical build guide for AGSE Tooling: what each system is, how to implement it step by step, "
        "three applicable examples, advantages, monetization angles, and how it makes the organization "
        "**faster, better, and cheaper**."
    )
    lines.append("")
    lines.append("## How to use this guide")
    lines.append("")
    lines.append("1. Skim the category map and pick high-ROI systems for your current bottlenecks.")
    lines.append("2. For each chosen system, follow the step-by-step process as a delivery checklist.")
    lines.append("3. Pilot with one example, measure cycle time / cost / quality, then scale.")
    lines.append("4. Prefer human-in-the-loop gates on money, legal, and customer-facing risk.")
    lines.append("")
    lines.append("## Category map")
    lines.append("")
    by_cat: dict[str, list[dict]] = {}
    for item in systems:
        by_cat.setdefault(item["category"], []).append(item)
    for cat in CATEGORIES_ORDER:
        if cat not in by_cat:
            continue
        items = by_cat[cat]
        lines.append(f"### {cat}")
        lines.append("")
        for item in items:
            lines.append(f"- [{item['id']:02d}. {item['name']}](#{item['id']:02d}-{slug(item['name'])})")
        lines.append("")

    lines.append("---")
    lines.append("")

    for item in systems:
        lines.append(f"## {item['id']:02d}. {item['name']}")
        lines.append("")
        lines.append(f"**Category:** {item['category']}")
        lines.append("")
        lines.append("### What it is")
        lines.append("")
        lines.append(item["what"])
        lines.append("")
        lines.append("### Step-by-step process")
        lines.append("")
        for i, step in enumerate(item["steps"], 1):
            lines.append(f"{i}. {step}")
        lines.append("")
        lines.append("### 3 applicable examples")
        lines.append("")
        for i, ex in enumerate(item["examples"], 1):
            lines.append(f"{i}. {ex}")
        lines.append("")
        lines.append("### Advantages / benefits")
        lines.append("")
        for adv in item["advantages"]:
            lines.append(f"- {adv}")
        lines.append("")
        lines.append("### Monetization benefits")
        lines.append("")
        lines.append(item["monetization"])
        lines.append("")
        lines.append("### Faster · Better · Cheaper")
        lines.append("")
        lines.append(f"- **Faster:** {item['fbc']['faster']}")
        lines.append(f"- **Better:** {item['fbc']['better']}")
        lines.append(f"- **Cheaper:** {item['fbc']['cheaper']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Suggested build order for AGSE Tooling")
    lines.append("")
    lines.append("| Wave | Systems | Why first |")
    lines.append("| --- | --- | --- |")
    lines.append(
        "| 1 – Foundation | 49 Workflow Orchestrator, 17 CRM Updater, 14 Data Entry, 10 Knowledge Base | Creates the data and process spine |"
    )
    lines.append(
        "| 2 – Revenue | 1 Lead Qualification, 2 Scheduler, 4 Follow-Up, 5 Proposal, 24 Sales Assistant | Speeds pipeline and cash |"
    )
    lines.append(
        "| 3 – Retention | 8 Onboarding, 9 Ticket Triage, 26 Churn Prediction, 46 Client Hub | Protects ARR |"
    )
    lines.append(
        "| 4 – Scale | 23 Report Generator, 50 Insights Dashboard, 34 Compliance, 48 Health Monitor | Makes growth governable |"
    )
    lines.append("")
    lines.append("## Implementation principles")
    lines.append("")
    lines.append("- Start with a measurable bottleneck (cycle time, error rate, cost per transaction).")
    lines.append("- Ground every generative step in approved systems of record.")
    lines.append("- Keep humans in the loop for money movement, legal commitments, and public replies until quality is proven.")
    lines.append("- Instrument success: baseline → pilot → A/B → scale.")
    lines.append("- Package winning systems as AGSE Tooling product SKUs, not one-off scripts.")
    lines.append("")
    return "\n".join(lines)


def slug(name: str) -> str:
    out = []
    for ch in name.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in {" ", "-", "/"}:
            out.append("-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


def main() -> None:
    assert len(SYSTEMS) == 50, len(SYSTEMS)
    ids = [x["id"] for x in SYSTEMS]
    assert ids == list(range(1, 51)), ids

    md = render_markdown(SYSTEMS)
    (OUT / "50-ai-automation-systems-guide.md").write_text(md)
    (OUT / "systems.json").write_text(json.dumps(SYSTEMS, indent=2))
    print(f"Wrote {OUT / '50-ai-automation-systems-guide.md'}")
    print(f"Wrote {OUT / 'systems.json'} ({len(SYSTEMS)} systems)")


if __name__ == "__main__":
    main()
