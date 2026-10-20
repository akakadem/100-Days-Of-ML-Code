import {
  Button,
  Callout,
  Card,
  CardBody,
  CardHeader,
  Divider,
  Grid,
  H1,
  H2,
  H3,
  Pill,
  Row,
  Select,
  Spacer,
  Stack,
  Stat,
  Text,
  TextInput,
  useState,
  useMemo,
} from "cursor/canvas";

type Raw = {
  i: number;
  n: string;
  c: string;
  w: string;
  s: string[];
  e: string[];
  a: string[];
  m: string;
  f: [string, string, string];
};

type System = {
  id: number;
  name: string;
  category: string;
  what: string;
  steps: string[];
  examples: string[];
  advantages: string[];
  monetization: string;
  fbc: { faster: string; better: string; cheaper: string };
};

const RAW = [{"i":1,"n":"AI Lead Qualification System","c":"Sales & Revenue","w":"Scores and ranks inbound leads using CRM data, firmographics, intent signals, and conversation history so sales only spends time on high-probability opportunities.","s":["Connect lead sources (web forms, ads, chat, imports) and CRM fields.","Define Ideal Customer Profile (ICP) criteria and disqualification rules.","Configure scoring from historical won/lost deals and intent signals.","Auto-enrich leads (company size, industry, tech stack, funding).","Score and tier leads (A/B/C) with explainable reasons.","Route A-tier leads to reps instantly; nurture lower tiers.","Log outcomes and retrain scoring thresholds monthly."],"e":["AGSE Tooling website demo requests scored and routed to enterprise vs SMB reps.","Trade-show badge scans enriched overnight and prioritized for next-day follow-up.","Inbound partner referrals auto-qualified against ICP before SDR outreach."],"a":["Removes bias and inconsistency from manual triage.","Creates a measurable, auditable qualification standard.","Frees SDRs from low-value research work."],"m":"Higher close rates and shorter sales cycles increase revenue per rep; sell as a managed AGSE lead-ops module or usage-based enrichment add-on.","f":["Qualification in seconds instead of hours of research.","Consistent ICP fit scoring with transparent reasons.","Fewer wasted discovery calls and lower cost-per-opportunity."]},{"i":2,"n":"AI Appointment Scheduler","c":"Sales & Revenue","w":"Books meetings automatically by negotiating times across calendars, time zones, and preference rules via email, SMS, or chat.","s":["Sync calendars (Google/Outlook) and define availability rules.","Set meeting types, durations, buffers, and booking policies.","Deploy booking links and conversational scheduling agents.","Confirm attendees, send reminders, and handle reschedules.","Push events to CRM with lead/opportunity linkage.","Analyze no-show patterns and optimize reminder cadence."],"e":["Prospect replies to an AGSE proposal email and books a technical demo without back-and-forth.","Support-to-sales handoff books a success review when a ticket indicates expansion intent.","Multi-timezone field engineers schedule site assessments with customers automatically."],"a":["Eliminates scheduling ping-pong.","Reduces no-shows with smart reminders.","Protects focus time with policy-aware booking."],"m":"More booked demos and lower SDR coordination overhead; package as AGSE Scheduling Bot subscription.","f":["Meetings booked in one interaction.","Right meeting type with the right stakeholders.","Cuts coordinator and SDR admin time."]},{"i":3,"n":"AI Email Responder","c":"Sales & Revenue","w":"Drafts or auto-sends context-aware email replies using inbox history, knowledge bases, and CRM context while escalating sensitive threads.","s":["Connect mailboxes and classify intent (pricing, support, sales, spam).","Ground responses in approved knowledge base and CRM records.","Generate draft replies with tone and brand guidelines.","Apply human-in-the-loop for high-risk categories.","Send, track opens/replies, and update CRM activities.","Review quality metrics and refine prompts/templates weekly."],"e":["AGSE Tooling pricing questions answered with approved packaging language.","Partner portal access requests handled with identity checks and next steps.","After-hours inbound RFIs get acknowledgment plus requested datasheets."],"a":["24/7 response coverage.","Consistent brand and compliance language.","Scales inbox volume without linear headcount."],"m":"Sell seats or mailbox packs; faster response increases conversion and retention.","f":["Replies in minutes, not hours.","Accurate, policy-aligned answers.","Lower cost per handled email."]},{"i":4,"n":"AI Follow-Up Automation","c":"Sales & Revenue","w":"Orchestrates multi-channel follow-ups based on deal stage, engagement signals, and silence thresholds so no opportunity goes cold.","s":["Map stages and SLA timers (e.g., no reply in 2 days).","Define channel sequences (email, LinkedIn, SMS, call task).","Personalize messages with deal context and prior objections.","Trigger nudges on opens, clicks, and page revisits.","Pause on reply or meeting booked; escalate stalled deals.","Report sequence performance by persona and stage."],"e":["Post-demo AGSE prospects get a 5-touch technical nurture if they stall.","Quote viewers who don't respond receive value-focused reminders.","Renewal accounts get automated check-ins 90/60/30 days before expiry."],"a":["Prevents pipeline leakage from forgotten follow-ups.","Personalization at scale.","Clear ownership of next actions."],"m":"Higher pipeline conversion; sell as AGSE Pipeline Nurture automation tier.","f":["Immediate next-touch after inactivity.","Context-aware messaging vs generic drips.","Less manual CRM babysitting."]},{"i":5,"n":"AI Proposal Generator","c":"Sales & Revenue","w":"Assembles tailored proposals from discovery notes, pricing catalogs, case studies, and past wins into branded, editable documents.","s":["Ingest discovery call transcripts and requirements.","Select solution modules, SLAs, and pricing from catalogs.","Generate narrative, scope, timeline, and risk sections.","Insert relevant case studies and ROI assumptions.","Review/approve in a human workflow; export PDF/Doc.","Track win rates by proposal variant."],"e":["AGSE Tooling RFP responses drafted overnight from a requirements matrix.","SMB packages generated in minutes from a short intake form.","Partner co-branded proposals with auto-inserted partner margins."],"a":["Drastically shorter proposal cycle time.","Fewer pricing/scope errors.","Reusable institutional knowledge."],"m":"Faster deal velocity and higher win rates; charge per proposal or as a sales-enablement SKU.","f":["Hours instead of days to first draft.","Consistent quality and ICP-aligned messaging.","Less senior seller time on formatting."]},{"i":6,"n":"AI Invoice Automation","c":"Finance & Billing","w":"Creates, validates, and sends invoices from contracts, usage meters, and purchase orders with tax, currency, and approval rules applied automatically.","s":["Connect billing systems, ERP, and contract repositories.","Define invoice templates, tax rules, and approval thresholds.","Detect billable events (milestones, usage, retainers).","Generate invoices, validate line items, and flag anomalies.","Send to customers and sync payment status back to finance.","Reconcile disputes and feed corrections into rules."],"e":["AGSE SaaS subscriptions billed monthly from usage + seat counts.","Professional services milestones invoiced when deliverables are marked complete.","Multi-entity partner invoices generated with correct tax jurisdictions."],"a":["Fewer billing errors and disputes.","On-time invoicing improves cash conversion.","Audit-ready invoice trails."],"m":"Faster cash collection and reduced AR labor; sell AGSE Billing Automation as a finance ops module.","f":["Invoices issued the same day work is completed.","Accurate line items tied to contracts and usage.","Fewer finance FTEs on manual invoice prep."]},{"i":7,"n":"AI Payment Reminder System","c":"Finance & Billing","w":"Sends polite, escalating, personalized payment reminders and payment links based on aging, customer risk, and communication preferences.","s":["Sync AR aging and payment portals.","Segment accounts by risk, amount, and relationship.","Design escalation ladders (friendly → firm → collections handoff).","Personalize reminder copy and attach invoices/payment links.","Detect payments and stop sequences automatically.","Escalate chronic delinquencies to finance with recommended actions."],"e":["Net-30 AGSE customers receive day-7/21/35 reminders with one-click pay.","Enterprise accounts get account-manager-aware nudges before formal dunning.","International clients receive localized reminders in local currency."],"a":["Reduces days sales outstanding (DSO).","Preserves customer relationships with tone control.","Frees AR teams from repetitive chasing."],"m":"Improved working capital; monetize as AGSE Collections Assist with success-based pricing on recovered AR.","f":["Reminders fire on schedule without manual queues.","Right tone and channel for each customer segment.","Lower cost to collect overdue balances."]},{"i":8,"n":"AI Customer Onboarding","c":"Customer Success","w":"Guides new customers from signed deal to first value with personalized checklists, training, and proactive risk alerts.","s":["Trigger onboarding from closed-won CRM events.","Generate a plan based on product SKUs and customer maturity.","Assign tasks to customer and internal owners with due dates.","Deliver training content and in-app guidance.","Detect stalled steps and alert CSMs.","Measure time-to-value and onboarding NPS."],"e":["New AGSE Tooling tenants get a 14-day activation plan with integrations checklist.","Enterprise rollouts receive phased department onboarding playbooks.","Self-serve SMB customers get chatbot-guided setup and milestone badges."],"a":["Higher activation and retention.","Standardized onboarding quality.","Early detection of at-risk accounts."],"m":"Lower churn in first 90 days increases LTV; sell onboarding automation as an AGSE Success Pack.","f":["Customers reach first value days sooner.","Personalized paths instead of one-size-fits-all.","Fewer CSM hours per onboarded account."]},{"i":9,"n":"AI Support Ticket Triage","c":"Customer Success","w":"Classifies, prioritizes, and routes support tickets by urgency, product area, sentiment, and skills required.","s":["Ingest tickets from email, chat, portal, and social.","Classify category, severity, and language.","Detect duplicates and link related incidents.","Route to the best queue or agent skill group.","Suggest macros/knowledge articles for first response.","Monitor SLA breaches and escalate automatically."],"e":["AGSE API outage reports auto-marked P1 and routed to on-call.","Billing questions go to finance ops; how-to questions to L1.","Angry VIP tickets escalate to a dedicated success queue."],"a":["Faster first response and resolution.","Better specialist matching.","Reduced misrouted tickets."],"m":"Higher CSAT and lower cost-to-serve; offer as AGSE Support Intelligence add-on.","f":["Instant prioritization at ticket creation.","Correct queue and suggested answers on first touch.","Less senior engineer time on misrouted noise."]},{"i":10,"n":"AI Knowledge Base Assistant","c":"Customer Success","w":"Answers employee and customer questions from approved docs, tickets, and runbooks with citations, and flags gaps for content authors.","s":["Index help docs, SOPs, tickets, and release notes.","Enable chat/search with grounded retrieval and citations.","Gate answers by audience (public vs internal).","Capture unanswered questions as content backlog.","Auto-draft article updates from resolved tickets.","Measure deflection rate and answer helpfulness."],"e":["AGSE customers self-serve integration setup via an in-app assistant.","Internal ops asks 'how do we reset partner SSO?' and gets the SOP.","New agents get guided answers during live chats."],"a":["Deflects repetitive tickets.","Keeps knowledge current via feedback loops.","Onboards staff faster."],"m":"Support deflection reduces headcount pressure; sell assistant seats or usage packs.","f":["Answers in seconds with source links.","Cited, approved knowledge instead of tribal lore.","Lower cost per resolved question."]},{"i":11,"n":"AI Social Media Scheduler","c":"Marketing & Content","w":"Plans, generates, and schedules social posts across channels with brand voice, campaign calendars, and performance feedback.","s":["Connect social accounts and brand style guides.","Generate content calendars from campaigns and product releases.","Draft posts, variants, and assets per channel.","Schedule optimally by audience activity windows.","Moderate comments and surface engagement opportunities.","Report ROI and feed winners into the next calendar."],"e":["AGSE product launches get a 2-week multi-channel rollout calendar.","Thought-leadership snippets from blog posts scheduled across LinkedIn/X.","Regional partners receive localized post packs for co-marketing."],"a":["Consistent presence without daily manual posting.","Channel-native formatting at scale.","Performance-informed content iteration."],"m":"Higher reach and pipeline influence; sell AGSE Social Ops as a marketing automation SKU.","f":["Week of posts prepared in one session.","On-brand, channel-optimized messaging.","Less agency/freelancer spend on routine posting."]},{"i":12,"n":"AI Content Repurposer","c":"Marketing & Content","w":"Transforms long-form assets (webinars, blogs, proposals) into channel-ready snippets, emails, and social assets.","s":["Ingest source assets (video, PDF, blog, transcript).","Extract key claims, quotes, and CTAs.","Generate formats: threads, carousels, emails, FAQs, shorts scripts.","Apply brand/legal review gates.","Publish or hand off to schedulers/CMS.","Track which derivatives drive engagement."],"e":["One AGSE webinar becomes 12 LinkedIn posts, 3 emails, and a FAQ page.","Customer case study PDF becomes a sales one-pager and ad creative brief.","Release notes become changelog emails and in-app banners."],"a":["Maximizes ROI on every pillar asset.","Maintains message consistency across channels.","Accelerates content velocity."],"m":"More touches from the same production budget; monetize as AGSE Content Factory credits.","f":["Days of content work compressed into hours.","Higher message consistency and coverage.","Lower cost per asset variant."]},{"i":13,"n":"AI Review Manager","c":"Marketing & Content","w":"Monitors reviews across platforms, drafts responses, flags crises, and routes product insights to the roadmap.","s":["Connect review sites, app stores, and G2/Capterra-like sources.","Classify sentiment, themes, and urgency.","Draft personalized public responses.","Escalate severe complaints to support/legal.","Aggregate themes into product insight reports.","Invite happy customers to leave reviews."],"e":["AGSE Tooling G2 reviews get same-day thank-you or recovery replies.","Negative billing reviews create support tickets automatically.","Feature request themes feed quarterly roadmap briefs."],"a":["Protects brand reputation in public channels.","Turns feedback into product intelligence.","Increases review volume via smart asks."],"m":"Better ratings improve inbound conversion; sell reputation management as an AGSE Growth service.","f":["Near real-time review responses.","Consistent, empathetic public replies.","Less marketing time spent monitoring portals."]},{"i":14,"n":"AI Data Entry Automation","c":"Operations & Data","w":"Extracts structured fields from emails, PDFs, forms, and screenshots and writes clean records into systems of record.","s":["Identify high-volume manual entry workflows.","Define schemas and validation rules.","OCR/parse documents and map fields.","Human-verify low-confidence extractions.","Write to CRM/ERP/databases with idempotent keys.","Monitor error rates and improve extractors."],"e":["AGSE partner order PDFs become line items in the ERP.","Business cards from events become CRM contacts.","Expense receipts populate accounting categories."],"a":["Eliminates repetitive typing.","Improves data completeness and consistency.","Reduces keying errors."],"m":"Labor savings and cleaner analytics; sell as AGSE Data Capture bots priced by document volume.","f":["Documents processed as they arrive.","Higher field accuracy with validation.","Lower cost per record entered."]},{"i":15,"n":"AI Document Classifier","c":"Operations & Data","w":"Automatically labels and routes documents (contracts, invoices, SOWs, IDs) into the right repository and workflow.","s":["Inventory document types and destination systems.","Train/configure classifiers on labeled samples.","Ingest from email, scans, and uploads.","Classify, extract metadata, and apply retention tags.","Route to approval queues or archives.","Audit misclassifications and retrain."],"e":["Inbound AGSE legal mailbox sorts NDAs vs MSAs vs DPA addenda.","Vendor packets split into W-9, COI, and MSA automatically.","Customer uploads in the portal go to the correct project folder."],"a":["Faster document findability.","Fewer misplaced files.","Stronger retention/compliance hygiene."],"m":"Reduced search and rework time; offer AGSE Document Ops as part of a content services platform.","f":["Instant sorting at intake.","Correct folder and workflow every time.","Less admin time hunting files."]},{"i":16,"n":"AI Meeting Notes Assistant","c":"Operations & Data","w":"Transcribes meetings, summarizes decisions, extracts action items, and pushes tasks to project tools and CRM.","s":["Integrate with Zoom/Meet/Teams recordings.","Transcribe with speaker labels.","Summarize decisions, risks, and next steps.","Assign owners and due dates into task systems.","Update CRM opportunity notes automatically.","Share notes to attendees for confirmation."],"e":["AGSE sales discovery calls produce MEDDIC notes in Salesforce.","Internal standup summaries create Jira tickets for blockers.","Customer QBR notes generate follow-up email drafts."],"a":["No more lost action items.","Shared truth across teams.","Sellers stay present in conversations."],"m":"Higher meeting ROI and CRM hygiene; sell AGSE Meeting Intelligence seats.","f":["Notes ready minutes after the call.","Structured decisions and owners, not messy transcripts.","Less time rewriting notes after meetings."]},{"i":17,"n":"AI CRM Updater","c":"Sales & Revenue","w":"Keeps CRM fields current by reading emails, calls, forms, and product usage so reps don't manually update records.","s":["Map required CRM hygiene fields and ownership rules.","Listen to email/call/product events.","Infer stage, next step, contacts, and competitors.","Propose or auto-write field updates with confidence scores.","Notify owners of material changes.","Score CRM completeness and coach lagging teams."],"e":["AGSE opportunity next-step dates update from email threads.","Champion contacts added when new stakeholders join calls.","Product usage spikes update account health scores."],"a":["Reliable pipeline reporting.","Less rep admin burden.","Better handoffs between teams."],"m":"Cleaner forecasts improve revenue planning; sell CRM hygiene automation as AGSE RevOps Assist.","f":["Records update continuously.","Higher data quality for forecasting.","Reps spend less time on CRM chores."]},{"i":18,"n":"AI Pipeline Management","c":"Sales & Revenue","w":"Forecasts deal outcomes, flags risk, recommends next best actions, and rebalances pipeline coverage by segment.","s":["Ingest pipeline stages, activities, and historical win data.","Score deal health and close probability.","Surface stuck deals and missing stakeholders.","Recommend plays (discount, exec sponsor, POC).","Generate forecast rollups for leadership.","Close the loop with actual win/loss outcomes."],"e":["AGSE weeklies highlight at-risk enterprise deals with missing economic buyers.","Managers get coaching prompts for reps with thin coverage.","Quarter-end forecasts reweighted by AI probability, not gut feel."],"a":["Earlier intervention on slipping deals.","More accurate forecasts.","Consistent sales coaching signals."],"m":"Improved attainment and forecast reliability; package as AGSE Pipeline Intelligence for RevOps teams.","f":["Risk visible before the deal slips a quarter.","Actionable coaching, not just dashboards.","Less time in manual forecast scrubbing."]},{"i":19,"n":"AI Inventory Monitor","c":"Operations & Supply Chain","w":"Tracks stock levels, predicts shortages, and triggers reorder or substitution recommendations using demand signals.","s":["Connect WMS/ERP inventory and sales velocity data.","Set safety stock and service-level targets.","Forecast demand by SKU and location.","Alert on stockouts, overstock, and aging inventory.","Recommend purchase orders or transfers.","Review forecast accuracy and tune models."],"e":["AGSE hardware accessory kits auto-reorder before campaign launches.","Regional warehouses get transfer suggestions when demand shifts.","Slow-moving SKUs flagged for promotion or write-down."],"a":["Fewer stockouts and lost sales.","Lower excess inventory carrying costs.","Proactive purchasing decisions."],"m":"Better inventory turns free cash; sell AGSE Inventory Guard for productized tooling SKUs.","f":["Shortage alerts before customers feel them.","Demand-aware reorder quantities.","Less emergency expediting spend."]},{"i":20,"n":"AI Order Processing","c":"Operations & Supply Chain","w":"Validates and processes orders from email, EDI, and portals—checking credit, inventory, pricing, and shipping rules.","s":["Ingest orders from all channels into a common schema.","Validate SKUs, pricing, taxes, and customer credit.","Check inventory and propose splits/substitutions.","Create ERP sales orders and acknowledgments.","Flag exceptions for human review.","Track first-pass yield and exception causes."],"e":["AGSE reseller email POs become ERP orders without retyping.","Portal orders with pricing mismatches are held with a clear reason.","Rush orders auto-prioritized when SLA tags are present."],"a":["Higher first-pass order accuracy.","Faster order-to-fulfillment cycle.","Clear exception handling."],"m":"Throughput without more ops headcount; sell AGSE Order Autopilot by order volume.","f":["Orders enter the system in minutes.","Pricing and credit rules enforced consistently.","Lower cost per order processed."]},{"i":21,"n":"AI Shipping Automation","c":"Operations & Supply Chain","w":"Selects carriers, generates labels, notifies customers, and handles exceptions using cost, SLA, and destination rules.","s":["Connect carriers, rate shops, and warehouse systems.","Define shipping policies by customer tier and weight.","Auto-select service level and print labels.","Send tracking updates and ETAs to customers.","Detect delays and trigger proactive communications.","Optimize carrier mix from cost/performance data."],"e":["AGSE kit shipments rate-shop FedEx vs UPS by zone.","VIP customers always get two-day with branded tracking emails.","Delayed parcels trigger apology + revised ETA automatically."],"a":["Lower shipping spend via smart rate shopping.","Better delivery experience.","Fewer 'where's my order?' tickets."],"m":"Freight savings and CSAT lift; monetize AGSE Ship Assist as logistics automation.","f":["Labels and notifications without warehouse bottlenecks.","Policy-correct carrier choices.","Reduced shipping overpay and support load."]},{"i":22,"n":"AI Expense Categorizer","c":"Finance & Billing","w":"Classifies expenses from receipts and card feeds into GL codes, flags policy violations, and prepares approvals.","s":["Connect corporate cards and receipt uploads.","OCR receipts and match to transactions.","Categorize to chart of accounts and projects.","Flag out-of-policy spend and duplicates.","Route approvals and sync to accounting.","Produce monthly spend insights by team."],"e":["AGSE field travel receipts auto-coded to customer projects.","Software subscriptions flagged if not on the approved vendor list.","Month-end close gets categorized card feeds ready for review."],"a":["Faster month-end close.","Stronger policy compliance.","Cleaner project costing."],"m":"Finance productivity and leakage reduction; sell AGSE Spend Intelligence seats.","f":["Categorization happens as spend occurs.","Consistent GL coding and policy checks.","Less accountant time on receipt sorting."]},{"i":23,"n":"AI Report Generator","c":"Insights & Leadership","w":"Produces narrative business reports from warehouses and SaaS tools—tables, charts explanations, and recommended actions.","s":["Connect BI warehouse and key SaaS metrics.","Define report templates (weekly leadership, monthly board).","Pull metrics, anomalies, and period comparisons.","Generate narrative commentary and action items.","Distribute via email/Slack with drill-down links.","Collect feedback to improve narrative quality."],"e":["AGSE Monday leadership brief auto-written from CRM + finance + support KPIs.","Customer success QBRs get account health narratives overnight.","Marketing weekly reports explain CAC/ROAS changes in plain language."],"a":["Analysts focus on deep work, not slide assembly.","Consistent reporting cadence.","Action-oriented narratives, not just charts."],"m":"Faster decisions and analyst leverage; sell AGSE Insight Writer as an analytics add-on.","f":["Reports ready before the meeting starts.","Anomaly explanations included automatically.","Lower cost per recurring report."]},{"i":24,"n":"AI Sales Assistant","c":"Sales & Revenue","w":"Acts as a real-time copilot for sellers—talk tracks, competitive answers, pricing guidance, and next-best-action prompts.","s":["Connect CRM, product catalog, battle cards, and call tools.","Surface account context before meetings.","Provide live suggestions during calls (objections, proofs).","Draft follow-up emails and mutual action plans.","Log activities and coaching insights.","Measure assisted win-rate lift."],"e":["AGSE AEs get competitor rebuttals mid-call from battle cards.","New SDRs receive talk tracks for first discovery calls.","Pricing guardrails appear when discount requests exceed policy."],"a":["Ramps new sellers faster.","Improves live conversation quality.","Enforces pricing discipline."],"m":"Higher attainment per seller; sell AGSE Seller Copilot seats.","f":["Answers and assets available instantly in the flow of work.","Consistent best-practice selling.","Less enablement overhead per rep."]},{"i":25,"n":"AI Upsell Recommender","c":"Sales & Revenue","w":"Recommends expansion products and timing based on usage, health, and lookalike customer patterns.","s":["Combine product usage, support health, and contract data.","Train propensity models for add-ons and upgrades.","Trigger plays when readiness signals appear.","Generate personalized expansion narratives and quotes.","Assign to AE/CSM with talk tracks.","Track attach rates and refine models."],"e":["AGSE tenants hitting API limits get Pro-tier upgrade prompts.","Accounts using only Module A are offered Module B with ROI proof.","Healthy renewals get multi-year expansion packaging."],"a":["Increases net revenue retention.","Times outreach when value is obvious.","Reduces random spray-and-pray upsells."],"m":"Expansion revenue is high-margin growth; package AGSE Expand AI for CS/AM teams.","f":["Opportunities surface at the right moment.","Recommendations grounded in actual usage.","Less wasted outreach on poor-fit upsells."]},{"i":26,"n":"AI Churn Prediction","c":"Customer Success","w":"Predicts customers at risk of canceling and recommends retention plays before renewal or cancellation signals harden.","s":["Assemble usage, support, NPS, billing, and engagement features.","Train churn risk models with explainable drivers.","Score accounts daily and tier risk.","Launch save plays (training, exec outreach, credits).","Track save rates and model drift.","Feed learnings into product and onboarding."],"e":["AGSE accounts with declining weekly active users flagged 60 days pre-renewal.","Billing disputes combined with low usage escalate to save desks.","Champion departure events trigger stakeholder mapping plays."],"a":["Protects recurring revenue.","Focuses CSMs on the highest-risk book.","Turns churn drivers into product priorities."],"m":"Retained ARR is pure profit uplift; sell AGSE Retention Radar to SaaS CS orgs.","f":["Risk known weeks earlier than manual review.","Explainable drivers guide the right save play.","CS capacity spent where it matters most."]},{"i":27,"n":"AI Feedback Analyzer","c":"Customer Success","w":"Clusters qualitative feedback from surveys, tickets, calls, and reviews into themes with sentiment and urgency.","s":["Collect feedback from all channels into one lake.","Cluster themes and map to product areas.","Score severity and frequency.","Publish insight digests to product and CX leaders.","Link themes to tickets/epics for action.","Measure theme resolution impact on CSAT."],"e":["AGSE NPS verbatims reveal onboarding friction as a top theme.","Support tickets cluster around a specific API error after a release.","Sales call objections highlight pricing packaging confusion."],"a":["Turns noise into prioritized insight.","Aligns product with customer voice.","Detects emerging issues early."],"m":"Better product decisions reduce churn and support cost; sell AGSE Voice-of-Customer analytics.","f":["Insights compiled continuously, not quarterly.","Theme clarity across thousands of comments.","Less analyst time coding open text."]},{"i":28,"n":"AI Survey Automation","c":"Customer Success","w":"Triggers the right survey at the right moment, personalizes questions, and routes responses into workflows.","s":["Define survey triggers (post-support, post-onboarding, renewal).","Personalize question sets by persona and journey stage.","Send via email/in-app/SMS with throttling rules.","Analyze responses and open text in real time.","Create tickets or CSM tasks from detractors.","Close the loop with respondents."],"e":["AGSE support tickets closed → CSAT survey within 1 hour.","Day-14 onboarded users get activation experience survey.","Renewal-90 surveys feed health scores and save plays."],"a":["Higher response rates via timing.","Actionable detractor workflows.","Less survey fatigue with throttling."],"m":"Better CX data improves retention marketing; offer AGSE Survey Orchestrator.","f":["Surveys fire at peak relevance moments.","Questions tailored to the journey stage.","Lower ops cost to run continuous listening."]},{"i":29,"n":"AI Webinar Automation","c":"Marketing & Content","w":"Runs webinar pipelines end-to-end: promotion, registration nurture, live assistance, and post-event follow-up.","s":["Create landing pages and registration flows.","Generate promo sequences and social assets.","Remind registrants and reduce no-shows.","Assist live Q&A moderation and highlight clips.","Score attendees and route hot leads to sales.","Send personalized replays and nurture tracks."],"e":["AGSE monthly product webinar auto-promoted for 2 weeks.","Attendees who ask pricing questions become sales-ready leads.","No-shows get a replay email with a booking CTA."],"a":["Consistent webinar machine without large event teams.","Higher show-up and conversion rates.","Automatic lead scoring from engagement."],"m":"Pipeline from events with less labor; sell AGSE Webinar OS for demand gen.","f":["Promo-to-follow-up runs without daily babysitting.","Engagement-based lead quality.","Lower cost per webinar-sourced opportunity."]},{"i":30,"n":"AI Job Application Screener","c":"HR & People","w":"Screens resumes and applications against role criteria, ranks candidates, and flags potential mismatches or compliance risks.","s":["Define role scorecards and must-have skills.","Ingest applications from ATS/email.","Parse resumes and score against scorecards.","Flag gaps, risks, and standout signals.","Shortlist for recruiters with explanations.","Audit for bias and adjust criteria."],"e":["AGSE engineering roles screened for required stack experience.","High-volume SDR applications ranked by relevant outbound history.","Internal mobility applications matched to open role scorecards."],"a":["Faster shortlists.","More consistent screening standards.","Recruiters focus on interviews, not inbox triage."],"m":"Shorter time-to-hire reduces vacancy cost; sell AGSE Talent Screen for hiring teams.","f":["Hundreds of resumes reviewed in minutes.","Explainable fit vs gut-feel screening.","Lower cost per screened candidate."]},{"i":31,"n":"AI Interview Scheduler","c":"HR & People","w":"Coordinates candidate and interviewer calendars, sends prep briefs, and manages reschedules across interview loops.","s":["Connect ATS stages and interviewer pools.","Define loop templates by role.","Offer candidates self-serve slots within constraints.","Send confirmations, prep packets, and Zoom links.","Handle cancellations and redistribute panels.","Track scheduling SLA and candidate experience."],"e":["AGSE hiring loops for engineers auto-book phone + technical + culture stages.","Executive interviews scheduled across multiple time zones.","No-show interviews auto-reschedule with candidate preference memory."],"a":["Cuts days of email coordination.","Improves candidate experience.","Protects interviewer focus time."],"m":"Faster hiring throughput; include in AGSE Talent Ops suite.","f":["Loops booked in one candidate session.","Correct interviewers and prep materials every time.","Less coordinator FTE time."]},{"i":32,"n":"AI Employee Onboarding","c":"HR & People","w":"Personalizes new-hire setup: accounts, training paths, buddy matching, and day-1-to-day-90 checklists.","s":["Trigger from signed offer / start date in HRIS.","Provision accounts and equipment requests.","Generate role-based learning paths.","Schedule intro meetings and culture sessions.","Track completion and nudge managers on blockers.","Survey new-hire experience and fix friction."],"e":["AGSE new AEs get CRM, dialer, and product certification tracks.","Engineers receive repo access, security training, and buddy intros.","Remote hires get equipment shipping + day-1 IT checklist automation."],"a":["Faster productivity ramp.","Fewer missed IT/setup steps.","Better new-hire experience and retention."],"m":"Reduced early attrition and ramp cost; sell AGSE People Onboard automation.","f":["Day-1 readiness without frantic IT tickets.","Role-specific paths instead of generic packets.","Lower HR/IT coordination cost per hire."]},{"i":33,"n":"AI Timesheet Collector","c":"HR & People","w":"Reminds employees to submit timesheets, validates entries against projects/policies, and prepares payroll/billing exports.","s":["Connect project codes and payroll systems.","Send smart reminders before deadlines.","Validate hours, overtime, and project allocations.","Flag anomalies for manager approval.","Export clean timesheets to payroll/billing.","Report utilization and missing submissions."],"e":["AGSE consultants submit weekly project hours with client tags.","Internal R&D time auto-suggested from calendar blocks.","Managers approve exception-only timesheets each Friday."],"a":["Higher on-time submission rates.","Cleaner billable utilization data.","Fewer payroll corrections."],"m":"Accurate billing for services firms; sell AGSE Time Capture for professional services.","f":["Reminders and validation before payroll cutoff.","Policy-compliant entries with fewer errors.","Less admin chasing missing timesheets."]},{"i":34,"n":"AI Compliance Checker","c":"Legal & Compliance","w":"Continuously checks processes, documents, and configurations against policy frameworks and alerts on drift.","s":["Encode policies (SOC2, GDPR, internal controls) as checks.","Scan configs, access lists, and document trails.","Flag violations and missing evidence.","Assign remediation owners with deadlines.","Collect evidence packages for audits.","Track compliance posture over time."],"e":["AGSE AWS configs checked for public bucket exposure.","Vendor DPAs verified before onboarding completes.","Access reviews detect terminated users with lingering SaaS seats."],"a":["Continuous assurance vs annual scramble.","Clear remediation ownership.","Lower audit preparation pain."],"m":"Avoids fines and deal blockers; sell AGSE Compliance Guard to security/GRC teams.","f":["Issues found as they appear, not at audit time.","Consistent policy interpretation.","Less expensive manual control testing."]},{"i":35,"n":"AI Contract Analyzer","c":"Legal & Compliance","w":"Reviews contracts for risks, non-standard clauses, obligations, and renewal terms—producing negotiation playbooks.","s":["Ingest contracts (PDF/DOCX) into a secure vault.","Extract parties, terms, SLAs, liability, and renewals.","Compare against playbook/fallback positions.","Highlight risky deviations with suggested redlines.","Track obligations and renewal alerts.","Feed approved language back into templates."],"e":["AGSE customer MSAs reviewed for uncapped liability before signature.","Vendor contracts flagged for auto-renewal trap clauses.","Partner agreements summarized for commercial teams in plain language."],"a":["Faster legal turnaround.","Fewer missed risky clauses.","Stronger obligation and renewal hygiene."],"m":"Accelerates deal desk and reduces legal risk; sell AGSE Contract IQ per document or seat.","f":["First-pass review in minutes.","Playbook-aligned risk spotting.","Lower outside-counsel spend on routine reviews."]},{"i":36,"n":"AI Project Status Reporter","c":"Operations & Data","w":"Compiles project health from tickets, docs, and chat into stakeholder-ready status updates.","s":["Connect Jira/Asana, docs, and Slack channels.","Detect milestones, blockers, and burndown trends.","Draft status narratives by audience (exec vs team).","Highlight risks with owners and ETAs.","Distribute on a cadence; capture feedback.","Archive status history for audits and retros."],"e":["AGSE implementation projects get Friday client status emails auto-drafted.","Internal platform teams publish weekly exec risk digests.","Agency-style client portals update from live ticket data."],"a":["Consistent status quality.","Earlier visibility into blockers.","Less PM time writing updates."],"m":"Higher delivery predictability; sell AGSE Project Pulse for delivery orgs.","f":["Status ready without chasing updates.","Risks framed clearly for the audience.","Lower PM overhead per project."]},{"i":37,"n":"AI Task Automation","c":"Operations & Data","w":"Detects repetitive digital workflows and automates them with RPA/AI agents across apps—with approvals for exceptions.","s":["Mine repetitive tasks from tickets and process logs.","Prioritize automations by volume and ROI.","Build agents/RPA bots with clear success criteria.","Add exception queues for human review.","Deploy, monitor failure rates, and alert owners.","Expand successful patterns across teams."],"e":["AGSE ops auto-creates customer folders and Slack channels on closed-won.","Support macros become full ticket workflows for password resets.","Finance bots move approved invoices into payment batches."],"a":["Removes busywork from skilled staff.","Standardizes process execution.","Creates a compounding automation portfolio."],"m":"Labor arbitrage and error reduction; sell AGSE Workflow Bots as a platform + build service.","f":["Tasks complete as soon as triggers fire.","Fewer human process deviations.","Lower cost per repeated workflow run."]},{"i":38,"n":"AI File Organizer","c":"Operations & Data","w":"Renames, tags, deduplicates, and files documents into the correct folders using content understanding.","s":["Connect drives (Google Drive, SharePoint, S3).","Define taxonomy, naming conventions, and retention.","Scan new/changed files for content and duplicates.","Propose moves/renames; auto-apply high-confidence actions.","Quarantine sensitive files found in the wrong places.","Report storage savings and findability metrics."],"e":["AGSE shared drives cleaned of duplicate proposal versions.","Customer folders auto-structured by account ID and year.","PII-bearing files moved to restricted locations automatically."],"a":["Faster file discovery.","Reduced storage bloat.","Better security posture for sensitive docs."],"m":"Productivity and storage savings; include in AGSE Knowledge Ops offering.","f":["Files organized continuously, not in annual cleanups.","Consistent naming and taxonomy.","Less time lost searching for the right version."]},{"i":39,"n":"AI Transcription Automation","c":"Operations & Data","w":"Converts audio/video into searchable text with speakers, timestamps, and downstream summaries or translations.","s":["Ingest call recordings, podcasts, and training videos.","Transcribe with speaker diarization.","Punctuate, redact PII where required, and index.","Generate summaries, chapters, and highlight clips.","Push text to CRM/KB/search.","Measure accuracy and correct domain vocabulary."],"e":["AGSE support calls transcribed for QA coaching.","Training videos become searchable lesson text.","Customer interviews transcribed for product research."],"a":["Makes spoken content searchable.","Enables coaching and compliance review.","Feeds other AI systems with text."],"m":"Unlocks value trapped in audio; sell AGSE Transcribe as usage-based media intelligence.","f":["Transcripts available shortly after recording.","Searchable, structured speech with speakers.","Cheaper than manual transcription services."]},{"i":40,"n":"AI Language Translator","c":"Operations & Data","w":"Translates documents, tickets, and UI/help content with domain glossaries while preserving formatting and tone.","s":["Build glossaries for AGSE product terminology.","Connect content sources (tickets, docs, CMS).","Translate with glossary enforcement and QA checks.","Human-review high-visibility content.","Publish localized assets and keep them in sync.","Track quality ratings by language."],"e":["AGSE help center articles localized to Spanish, French, and German.","Support tickets from multilingual customers translated for agents.","Partner contracts drafted bilingual with consistent defined terms."],"a":["Expands addressable markets.","Faster global support.","Consistent product terminology worldwide."],"m":"New-market revenue with less localization overhead; sell AGSE Locale Engine.","f":["Translations in minutes for operational content.","Glossary-consistent product language.","Lower spend on full human translation for drafts."]},{"i":41,"n":"AI Voice Assistant","c":"Infrastructure & Intelligence","w":"Provides voice interfaces for internal ops or customer channels—answering FAQs, capturing intents, and executing allowed actions.","s":["Define intents, tools, and security boundaries.","Connect telephony/IVR or workplace voice surfaces.","Ground answers in knowledge bases and live systems.","Hand off to humans with full context when needed.","Log transcripts and completion rates.","Improve intents from failed conversations."],"e":["AGSE customers call IVR to check order/shipment status by voice.","Employees ask workplace assistant for PTO balance and IT ticket status.","Field teams dictate inventory counts hands-free into ERP."],"a":["Hands-free access to systems.","24/7 voice coverage for common intents.","Smooth escalation with context."],"m":"Deflects call-center volume; sell AGSE Voice Agent minutes + intent packs.","f":["Common requests resolved without wait queues.","Natural language vs rigid phone trees.","Lower cost per voice interaction."]},{"i":42,"n":"AI Competitor Monitor","c":"Marketing & Content","w":"Watches competitor sites, pricing pages, job posts, and reviews to surface strategic changes for GTM teams.","s":["Define competitor set and watchlist URLs/feeds.","Scrape/monitor changes to messaging, pricing, and features.","Summarize material changes with business impact.","Alert sales/marketing with battle-card updates.","Archive historical competitor snapshots.","Review monthly for strategic planning."],"e":["AGSE pricing page watches detect a competitor's new free tier.","Job postings signal a competitor building an AI module.","Review spikes highlight a rival outage AGSE can respond to."],"a":["Earlier competitive awareness.","Fresher battle cards.","Evidence-based GTM pivots."],"m":"Protects win rates; sell AGSE Competitive Radar as a GTM intelligence subscription.","f":["Change alerts within hours of publish.","Summaries ready for sellers, not raw HTML diffs.","Less analyst time on manual competitor checks."]},{"i":43,"n":"AI Price Monitoring","c":"Marketing & Content","w":"Tracks market and competitor pricing, MAP violations, and discount patterns to inform pricing and promotions.","s":["Identify SKUs and competitor/channel price sources.","Collect prices on a schedule with change detection.","Normalize currencies, bundles, and promo terms.","Alert on undercuts, MAP breaches, and anomalies.","Recommend price or promo responses.","Feed insights into pricing committees."],"e":["AGSE channel partners monitored for MAP compliance.","Competitor seat prices tracked before AGSE annual packaging reviews.","Promo end dates detected so AGSE can time counter-offers."],"a":["Protects margin and brand price integrity.","Informs competitive packaging.","Reduces surprise undercutting."],"m":"Margin protection is direct profit; sell AGSE Price Watch for product/finance teams.","f":["Price changes detected quickly across channels.","Normalized comparisons across messy listings.","Less manual price shopping by analysts."]},{"i":44,"n":"AI Local SEO Monitor","c":"Marketing & Content","w":"Tracks local search rankings, listings accuracy, and reviews for each location—and recommends fixes.","s":["Inventory locations and NAP (name/address/phone) data.","Monitor Google Business Profile and local rank keywords.","Detect listing inconsistencies and duplicate pages.","Recommend content/citation fixes.","Track review velocity and rating trends.","Report local visibility by market."],"e":["AGSE regional offices keep consistent NAP across directories.","Local service keywords monitored for each metro area.","Duplicate listings flagged and merge recommendations issued."],"a":["Higher local discovery and foot/lead traffic.","Consistent brand presence locally.","Faster response to ranking drops."],"m":"More local inbound leads; sell AGSE Local Presence for multi-location GTM.","f":["Ranking/listing issues caught weekly.","Actionable fix lists per location.","Lower agency spend on routine local audits."]},{"i":45,"n":"AI Ad Performance Monitor","c":"Marketing & Content","w":"Watches paid campaigns across channels, diagnoses underperformance, and recommends budget/creative shifts.","s":["Connect ad platforms and conversion analytics.","Define KPIs (CAC, ROAS, CPA) and alert thresholds.","Detect fatigue, wasted spend, and audience drift.","Recommend pause/scale/creative refresh actions.","Optionally auto-apply bounded budget rules.","Produce weekly performance narratives."],"e":["AGSE LinkedIn campaigns paused when CPA exceeds target for 3 days.","Creative fatigue detected on top ads with refresh suggestions.","Budget shifted from low-ROAS geos to high-intent segments."],"a":["Protects ad budget from silent waste.","Faster optimization loops.","Clear narratives for stakeholders."],"m":"Higher paid efficiency improves pipeline ROI; sell AGSE Ads Pilot for growth teams.","f":["Underperforming spend caught same day.","Root-cause suggestions, not just charts.","Less wasted media budget and analyst time."]},{"i":46,"n":"AI Client Communication Hub","c":"Infrastructure & Intelligence","w":"Unifies client emails, chats, meetings, and tickets into a single timeline with AI summaries and next actions.","s":["Connect email, Slack/Teams, support, and CRM.","Build a unified per-account activity timeline.","Summarize open threads and commitments.","Suggest replies and owners for dangling actions.","Share a client-safe portal view if needed.","Measure response SLAs across channels."],"e":["AGSE account teams see every customer touch before a QBR.","New CSMs ramp on an account by reading AI timeline summaries.","Open promises across email/Slack become tracked tasks."],"a":["No more lost context across tools.","Faster, consistent client responses.","Cleaner internal handoffs."],"m":"Higher retention via better communication; sell AGSE Client Hub seats for AM/CS teams.","f":["Full context available before every client touch.","Commitments don't fall through cracks.","Less time stitching history from five apps."]},{"i":47,"n":"AI Backup Automation","c":"Infrastructure & Intelligence","w":"Schedules, verifies, and reports on backups across SaaS and infrastructure—alerting on failures and restore-test gaps.","s":["Inventory critical systems and RPO/RTO targets.","Configure backup jobs and retention policies.","Verify backup success and integrity checks.","Run periodic restore tests with evidence logs.","Alert on failures and missed windows.","Produce compliance-ready backup reports."],"e":["AGSE Salesforce and Postgres backups verified nightly.","Failed SaaS export jobs reopen until resolved.","Quarterly restore drills documented for SOC2 evidence."],"a":["Reduces data-loss risk.","Proves recoverability, not just backups.","Audit-friendly evidence trails."],"m":"Avoids catastrophic loss costs; sell AGSE Resilience Ops monitoring.","f":["Failures known immediately.","Restore-tested confidence vs assumed backups.","Less manual backup babysitting by IT."]},{"i":48,"n":"AI System Health Monitor","c":"Infrastructure & Intelligence","w":"Correlates metrics, logs, and traces to detect incidents early, suggest causes, and open actionable alerts.","s":["Connect observability stacks (metrics/logs/traces).","Baseline normal behavior per service.","Detect anomalies and correlate related signals.","Open incidents with probable root-cause hints.","Suggest runbooks and owners on-call.","Post-incident, refine detectors and suppress noise."],"e":["AGSE API latency anomalies alert before customer tickets spike.","Error bursts correlated to a specific deploy version.","Noisy alerts suppressed after learning seasonal patterns."],"a":["Earlier incident detection.","Less alert fatigue.","Faster mean time to recovery (MTTR)."],"m":"Uptime protects revenue and brand; sell AGSE Observability Copilot.","f":["Issues caught before widespread customer impact.","Correlated signals with suggested causes.","Fewer engineer hours on false alarms."]},{"i":49,"n":"AI Workflow Orchestrator","c":"Infrastructure & Intelligence","w":"Coordinates multi-step cross-system processes with AI decisioning, retries, and human approvals at control points.","s":["Map end-to-end processes (quote-to-cash, hire-to-retire).","Connect systems via APIs/events.","Encode business rules and AI decision nodes.","Add approval gates and SLA timers.","Monitor runs, failures, and bottlenecks.","Version workflows and roll back safely."],"e":["AGSE quote-to-cash: CRM → proposal → e-sign → billing → provisioning.","Partner onboarding: KYC → contract → portal access → kickoff.","Incident response: detect → page → mitigate → customer notify → RCA."],"a":["Connects siloed automations into outcomes.","Visible process SLAs and failure points.","Governed AI decisions with human gates."],"m":"Platform value compounds across use cases; sell AGSE Orchestration Cloud as the control plane.","f":["Multi-system processes finish without manual glue work.","Consistent, auditable process execution.","Lower integration maintenance vs point scripts."]},{"i":50,"n":"AI Business Insights Dashboard","c":"Insights & Leadership","w":"Unifies KPIs across sales, finance, product, and support into an executive dashboard with AI anomaly narratives and recommended actions.","s":["Define North Star and departmental KPI trees.","Connect warehouses and SaaS metrics.","Build living dashboards with drill-downs.","Add AI narratives explaining movers and outliers.","Push alerts when KPIs breach thresholds.","Review weekly with owners and update targets."],"e":["AGSE exec dashboard shows ARR, NRR, CAC, churn risk, and uptime together.","Product leaders drill from revenue impact to feature adoption.","Board packs auto-annotate the three biggest weekly changes."],"a":["Single source of operational truth.","Faster executive decision cycles.","Narratives turn data into action."],"m":"Better decisions compound revenue and margin; sell AGSE Command Center as an executive intelligence product.","f":["Cross-functional truth available in one place in real time.","Anomalies explained, not just visualized.","Less analyst time assembling leadership packs."]}] as Raw[];

const SYSTEMS: System[] = RAW.map((r) => ({
  id: r.i,
  name: r.n,
  category: r.c,
  what: r.w,
  steps: r.s,
  examples: r.e,
  advantages: r.a,
  monetization: r.m,
  fbc: { faster: r.f[0], better: r.f[1], cheaper: r.f[2] },
}));

const CATEGORIES = [
  "All",
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
];

const WAVE_HINTS: Record<number, string> = {
  10: "Wave 1 – Foundation",
  14: "Wave 1 – Foundation",
  17: "Wave 1 – Foundation",
  49: "Wave 1 – Foundation",
  1: "Wave 2 – Revenue",
  2: "Wave 2 – Revenue",
  4: "Wave 2 – Revenue",
  5: "Wave 2 – Revenue",
  24: "Wave 2 – Revenue",
  8: "Wave 3 – Retention",
  9: "Wave 3 – Retention",
  26: "Wave 3 – Retention",
  46: "Wave 3 – Retention",
  23: "Wave 4 – Scale",
  34: "Wave 4 – Scale",
  48: "Wave 4 – Scale",
  50: "Wave 4 – Scale",
};

export default function AgseAutomationGuide() {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("All");
  const [selectedId, setSelectedId] = useState(1);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return SYSTEMS.filter((s) => {
      if (category !== "All" && s.category !== category) return false;
      if (!q) return true;
      const hay = [s.name, s.what, s.category, ...s.examples, ...s.advantages].join(" ").toLowerCase();
      return hay.includes(q);
    });
  }, [query, category]);

  const selected = useMemo(() => {
    return filtered.find((s) => s.id === selectedId) ?? filtered[0] ?? SYSTEMS[0];
  }, [filtered, selectedId]);

  const counts = useMemo(() => {
    const map: Record<string, number> = {};
    for (const s of SYSTEMS) map[s.category] = (map[s.category] ?? 0) + 1;
    return map;
  }, []);

  return (
    <Stack gap={20} style={{ padding: 20, maxWidth: 1100 }}>
      <Stack gap={8}>
        <H1>50 AI Automation Systems for AGSE Tooling</H1>
        <Text tone="secondary">
          Explore each system: what it is, step-by-step build process, 3 applications,
          advantages, monetization, and faster / better / cheaper impact.
        </Text>
      </Stack>

      <Grid columns={4} gap={12}>
        <Stat value="50" label="Automation systems" />
        <Stat value={String(Object.keys(counts).length)} label="Categories" />
        <Stat value={String(filtered.length)} label="Matching filter" />
        <Stat value="4" label="Suggested build waves" />
      </Grid>

      <Callout tone="info" title="Suggested AGSE build order">
        Wave 1 Foundation (orchestrator, CRM updater, data entry, knowledge base) then
        Wave 2 Revenue (leads, scheduling, follow-up, proposals, sales assistant) then
        Wave 3 Retention (onboarding, triage, churn, client hub) then
        Wave 4 Scale (reports, dashboard, compliance, health monitor).
      </Callout>

      <Row gap={12} align="end" wrap>
        <Stack gap={4} style={{ flex: 1, minWidth: 220 }}>
          <Text size="small" weight="medium">Search</Text>
          <TextInput
            value={query}
            onChange={setQuery}
            placeholder="Search name, example, benefit..."
          />
        </Stack>
        <Stack gap={4} style={{ minWidth: 220 }}>
          <Text size="small" weight="medium">Category</Text>
          <Select
            value={category}
            onChange={setCategory}
            options={CATEGORIES.map((c) => ({
              value: c,
              label: c === "All" ? "All categories" : c + " (" + String(counts[c] ?? 0) + ")",
            }))}
          />
        </Stack>
      </Row>

      <Grid columns="280px 1fr" gap={16}>
        <Card>
          <CardHeader>Systems</CardHeader>
          <CardBody>
            <Stack gap={6} style={{ maxHeight: 640, overflow: "auto" }}>
              {filtered.map((s) => {
                const active = selected?.id === s.id;
                return (
                  <Button
                    key={s.id}
                    variant={active ? "primary" : "ghost"}
                    onClick={() => setSelectedId(s.id)}
                    style={{ justifyContent: "flex-start", textAlign: "left" }}
                  >
                    {String(s.id).padStart(2, "0")}. {s.name}
                  </Button>
                );
              })}
              {filtered.length === 0 ? (
                <Text tone="secondary">No systems match this filter.</Text>
              ) : null}
            </Stack>
          </CardBody>
        </Card>

        {selected ? (
          <Stack gap={14}>
            <Stack gap={8}>
              <Row gap={8} align="center" wrap>
                <Pill tone="info">{String(selected.id).padStart(2, "0")}</Pill>
                <Pill>{selected.category}</Pill>
                {WAVE_HINTS[selected.id] ? (
                  <Pill tone="success">{WAVE_HINTS[selected.id]}</Pill>
                ) : null}
              </Row>
              <H2>{selected.name}</H2>
              <Text>{selected.what}</Text>
            </Stack>

            <Divider />

            <Stack gap={8}>
              <H3>Step-by-step process</H3>
              <Stack gap={6}>
                {selected.steps.map((step, i) => (
                  <Row key={i} gap={10} align="start">
                    <Pill size="sm">{String(i + 1)}</Pill>
                    <Text>{step}</Text>
                  </Row>
                ))}
              </Stack>
            </Stack>

            <Stack gap={8}>
              <H3>3 applicable examples</H3>
              <Stack gap={8}>
                {selected.examples.map((ex, i) => (
                  <Card key={i}>
                    <CardBody>
                      <Text weight="medium">{i + 1}. {ex}</Text>
                    </CardBody>
                  </Card>
                ))}
              </Stack>
            </Stack>

            <Stack gap={8}>
              <H3>Advantages / benefits</H3>
              <Stack gap={4}>
                {selected.advantages.map((a, i) => (
                  <Text key={i}>• {a}</Text>
                ))}
              </Stack>
            </Stack>

            <Stack gap={8}>
              <H3>Monetization benefits</H3>
              <Text>{selected.monetization}</Text>
            </Stack>

            <Stack gap={8}>
              <H3>Faster · Better · Cheaper</H3>
              <Grid columns={3} gap={10}>
                <Card>
                  <CardHeader>Faster</CardHeader>
                  <CardBody>
                    <Text size="small">{selected.fbc.faster}</Text>
                  </CardBody>
                </Card>
                <Card>
                  <CardHeader>Better</CardHeader>
                  <CardBody>
                    <Text size="small">{selected.fbc.better}</Text>
                  </CardBody>
                </Card>
                <Card>
                  <CardHeader>Cheaper</CardHeader>
                  <CardBody>
                    <Text size="small">{selected.fbc.cheaper}</Text>
                  </CardBody>
                </Card>
              </Grid>
            </Stack>

            <Row gap={8} wrap>
              <Button
                variant="secondary"
                disabled={!filtered.length || filtered[0].id === selected.id}
                onClick={() => {
                  const idx = filtered.findIndex((s) => s.id === selected.id);
                  if (idx > 0) setSelectedId(filtered[idx - 1].id);
                }}
              >
                Previous
              </Button>
              <Button
                variant="secondary"
                disabled={
                  !filtered.length ||
                  filtered[filtered.length - 1].id === selected.id
                }
                onClick={() => {
                  const idx = filtered.findIndex((s) => s.id === selected.id);
                  if (idx >= 0 && idx < filtered.length - 1) {
                    setSelectedId(filtered[idx + 1].id);
                  }
                }}
              >
                Next
              </Button>
            </Row>
          </Stack>
        ) : null}
      </Grid>

      <Spacer />
      <Text size="small" tone="secondary">
        Full written guide also available in the repo at docs/agse-tooling/50-ai-automation-systems-guide.md
      </Text>
    </Stack>
  );
}
