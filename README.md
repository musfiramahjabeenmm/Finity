# Finity 
### AI-Powered Financial Operating System for Indian SMEs

Finity is a conversational, mobile-first financial OS built for Indian small business owners such as kirana stores, manufacturers, traders, service providers who need to manage their finances without being accountants. You talk to it. It handles the rest.

---

## The Problem

India has 63 million MSMEs. Most of them manage finances in paper notebooks, mental math, or basic Excel. Existing tools like Tally, Zoho Books, and QuickBooks are built *for accountants*, they assume knowledge of double-entry bookkeeping, GST reconciliation, and financial terminology that the average business owner simply doesn't have and shouldn't need to have.

Finity is built for the business owner, not the accountant.

---

## What Finity Does

- **Conversational transaction logging** — "paid 3000 to Ravi for raw materials" is all it takes
- **Receipt scanning** — photograph a bill, Finity reads it and logs it
- **CSV / Excel / PDF import** — upload your bank statement, Finity categorizes everything
- **GST & TDS compliance monitoring** — proactive alerts before problems happen
- **Cash flow forecasting** — "will I have enough money next month?" answered in plain language
- **Payroll calculation** — PF, ESI, TDS handled automatically per Indian regulations
- **No bank API** — you control your data; import from bank exports only

---

## Tech Stack

### Mobile App — React Native + Expo
**Why:** Indian SME owners manage everything from their phones. A mobile-first experience is not a nice-to-have — it is the product. React Native gives us a single codebase for iOS and Android. Expo accelerates development with built-in access to the camera, biometrics, push notifications, and file system — all of which Finity uses heavily.

### Backend — FastAPI (Python)
**Why:** FastAPI is fast to build with, natively async, and integrates cleanly with every AI library in the Python ecosystem. All agent orchestration, file parsing, payroll calculation, and API logic lives here. Python is also the natural home for pandas, pdfplumber, and the Anthropic + Google AI SDKs.

### Database — PostgreSQL + pgvector
**Why:** PostgreSQL is the reliable, battle-tested choice for financial data where correctness matters above everything. The pgvector extension adds vector search on top of the same database — enabling RAG for the Cash Flow Agent without introducing a separate vector database. One database, two jobs.

### Background Jobs — Celery + Redis
**Why:** The Compliance Agent runs a weekly autonomous scan of all transactions — checking GST mismatches, TDS obligations, and filing deadlines. This is a background job, not a user-triggered action. Celery handles task scheduling and queuing. Redis serves as both the Celery broker and the OTP store (with TTL expiry). Redis was already required for Celery, so OTP storage costs nothing extra.

### Authentication — Supabase Auth
**Why:** Supabase provides production-grade email/password authentication with JWT session management out of the box. It handles password hashing, session refresh, and user management so we don't build security infrastructure from scratch. The free tier supports up to 50,000 users.

### OTP Email — Resend API
**Why:** 2FA on new device logins requires OTP delivery that actually reaches the inbox. Raw SMTP fails this. Resend is a developer-first email API with superior deliverability, a free tier of 3,000 emails/month, and a 5-line Python integration. OTP emails reach users, not spam folders.

### Biometric Auth — Expo Local Authentication
**Why:** Daily login should take under 3 seconds — the same experience as GPay or any Indian banking app. Expo Local Authentication gives us fingerprint and Face ID support on both platforms. The security stays on-device; Finity never sees biometric data.

### Push Notifications — Expo Push Notifications
**Why:** Compliance alerts and cash flow warnings need to reach the user even when the app is closed. Expo Push Notifications handles iOS and Android delivery through a single API. This replaces WhatsApp-based notifications — which would require Meta business registration, per-message billing, and ongoing compliance with Meta's platform policies. In-app + push notifications give us full control with zero platform dependency.

### Receipt Parsing — Gemini Vision API
**Why:** Extracting vendor name, amount, date, and item description from a photographed paper bill is a multimodal task. Gemini Vision handles this with a single API call and delivers accurate extraction on Indian receipt formats (which vary wildly in layout and language).

### Transaction Categorization — Gemini 1.5 Flash (fine-tuned)
**Why:** The Accounting Agent processes every transaction the user logs. At scale, this is high-volume and latency-sensitive. Gemini Flash is fast and cost-efficient for classification tasks. Crucially, we fine-tune it on 500–1,000 labeled Indian SME transactions — "Diwali bonus to staff" → Payroll, "paid GST challan" → Tax Liability — because base models categorize Indian business transactions inconsistently. Fine-tuning on Vertex AI grounds it in real patterns.

### Complex Reasoning — Claude API (Anthropic)
**Why:** The Compliance Agent and Cash Flow Agent handle tasks where errors have real consequences — a wrong GST interpretation can result in penalties; a wrong cash flow forecast leads to bad decisions. Claude is used here for its accuracy on multi-step legal and financial reasoning. The Orchestrator also uses Claude to correctly route diverse user intents. Gemini Flash handles volume; Claude handles quality-critical decisions.

### Compliance Intelligence — Claude API (fine-tuned)
**Why:** Indian GST rules, TDS slabs, HSN codes, and CBIC notifications are highly specific. General LLMs hallucinate Indian tax details confidently. The Compliance Agent is fine-tuned on actual GST circulars and MSME compliance guidelines to ground it in correct, current Indian tax law. The cost of a wrong compliance answer justifies this investment.

### Cash Flow Forecasting — Claude API + RAG (pgvector)
**Why:** Forecasting requires reasoning over *this user's specific* transaction history — recurring expenses, seasonal patterns, pending invoices. Fine-tuning doesn't help here because the relevant data is user-specific and changes constantly. RAG (Retrieval Augmented Generation) with pgvector retrieves the most relevant transactions semantically, feeds them to Claude, and Claude reasons over them to produce an accurate, personalized forecast.

### File Parsing — pdfplumber + pandas
**Why:** Since Finity doesn't integrate with bank APIs (which requires RBI Account Aggregator licensing), users import data via exported files. pdfplumber handles bank statement PDFs. pandas handles Excel and CSV. Together they normalize any uploaded transaction file into the standard format the Accounting Agent expects.

### Deployment — Railway
**Why:** Railway hosts FastAPI, PostgreSQL, and Redis under one platform with a free tier sufficient for development and early users. No DevOps configuration required — deploy from GitHub, environment variables set in the dashboard, and it runs.

---

## Agent Architecture

Finity uses 4 specialized AI agents, each with a clear and justified role:

| Agent | LLM | Pattern | Role |
|---|---|---|---|
| Orchestrator | Claude API | Routing | Reads every user message and routes to the correct agent or service |
| Accounting | Gemini Flash (fine-tuned) | ReAct | Parses and categorizes all transactions from chat, photo, or file |
| Compliance | Claude API (fine-tuned) | ReAct + Scheduled | GST/TDS monitoring, proactive weekly scan, filing deadline alerts |
| Cash Flow | Claude API + RAG | ReAct | Runway analysis, forecasting, proactive risk detection |

**What is deliberately NOT an agent:**
- **Payroll** — PF, ESI, TDS calculations are deterministic math. A FastAPI utility function handles this correctly, cheaply, and faster than any agent.
- **Reporting** — A Celery scheduled job + Claude for formatting covers this without the overhead of a dedicated agent.
- **Simple queries** — "What did I spend this month?" is a SQL aggregation, not an AI task.

> Rule: If it's calculations → utility function. If it's reasoning over uncertain or complex data → agent.

---

## LLM Routing Strategy

| Task | LLM | Reason |
|---|---|---|
| Transaction categorization | Gemini Flash | High volume, simple classification, low cost |
| Receipt photo parsing | Gemini Vision | Multimodal task, single API call |
| GST compliance analysis | Claude | Complex multi-step legal reasoning, accuracy critical |
| Cash flow forecasting | Claude | Long context reasoning over financial patterns |
| Conversational queries | Claude | Nuanced, context-aware responses |
| Simple DB aggregations | No LLM | Direct SQL — fastest and cheapest |

---

## Authentication Flow

```
First Setup (once per device)
  Register: Email + Password
  → OTP via Resend email (6-digit, 10-min TTL, stored in Redis)
  → Device remembered
  → Set 6-digit PIN
  → Optional: Enable biometric

Daily Login (every time)
  → 6-digit PIN  OR  Biometric
  → Inside app in under 3 seconds

New Device
  → Email + Password + Resend OTP again
  → Set PIN on new device

Inactivity > 5 min → PIN required again
```

---

## What's Not in V1 (and Why)

| Excluded | Reason |
|---|---|
| Bank API integration | Requires RBI Account Aggregator license — regulatory blocker |
| WhatsApp notifications | Meta business verification + per-conversation billing + platform dependency |
| Multi-user / team access | V2 — scope management |
| Regional language support | V2 — Whisper API + translation layer planned |
| Automated GST filing | V2 — GST Suvidha Provider API integration |

---

## V2 Roadmap

- Account Aggregator integration for live bank balance (post RBI entity registration)
- Regional language support — Tamil, Hindi, Telugu via Whisper API
- Multi-user access with role-based permissions (owner, accountant, employee)
- Automated GST return filing via GST Suvidha Provider APIs
- Invoice generation and payment follow-up agent
- WhatsApp channel alongside the app (once production-ready)

---

## Development Cost

| Service | Cost |
|---|---|
| Gemini 1.5 Flash API | Free (Google AI Studio free tier) |
| Claude API | ~₹800 / $10 (complex queries only) |
| Resend Email API | Free (3,000 emails/month) |
| Railway (Backend + DB + Redis) | Free (500 hours/month) |
| Expo | Free (open source) |
| Supabase Auth | Free (up to 50,000 users) |
| **Total** | **Under ₹1,000 for full development** |

---

*Finity — because your business deserves a CFO, not a spreadsheet.*
