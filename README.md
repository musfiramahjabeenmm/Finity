# Finity

### AI-Powered Financial Operating System for Indian SMEs

> An agentic finance platform that automates accounting, GST compliance, payroll, and cash flow — so business owners can focus on running their business, not their books.

---

## The Problem

India has **6.3 crore MSMEs** — and most of them manage finances through disconnected spreadsheets, manual ledgers, and monthly CA visits.

| Pain Point | Reality |
|---|---|
| Manual transaction entry | 15–20 hrs wasted every month |
| Bookkeeping error rate | 5–10% — leads to wrong tax filings |
| Missed GST / TDS deadlines | 40% of SMEs — ₹5,000+ penalty each time |
| No real-time profit visibility | 60% of owners don't know if they're profitable |
| Existing ERP tools (Tally, Zoho) | ₹50,000/yr + months of training |

**The gap:** No affordable, intelligent, easy-to-use financial tool built specifically for Indian SME owners.

---

## What is Finity?

Finity is a **concept for an agentic financial OS** — a system where specialized AI agents handle every aspect of business finance autonomously, and the owner interacts through a simple chat interface in plain language.

```
Owner asks:  "Can we afford to hire someone next month?"

Finity:      "Current balance ₹1.2L. Projected expenses ₹85K.
              3 overdue invoices worth ₹60K outstanding.
              If collected, yes — comfortably."
```

No accounting knowledge needed. No spreadsheets. No missed deadlines.

---

## Proposed Agent Architecture

```
┌──────────────────────────────────────────────────┐
│               ORCHESTRATOR AGENT                 │
│     Understands intent → routes to specialist    │
└──────────────────────┬───────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│ Accounting │  │ Compliance │  │ Cash Flow  │
│   Agent    │  │   Agent    │  │   Agent    │
│            │  │            │  │            │
│ Auto-tag   │  │ GST / TDS  │  │ 14-day     │
│ expenses   │  │ deadlines  │  │ forecast   │
└────────────┘  └────────────┘  └────────────┘
       ▼               ▼               ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│  Payroll   │  │    Tax     │  │ Reporting  │
│   Agent    │  │ Optimizer  │  │   Agent    │
│            │  │            │  │            │
│ Salary +   │  │ Deductions │  │ Plain-lang │
│ PF + TDS   │  │ + ITR prep │  │ P&L summary│
└────────────┘  └────────────┘  └────────────┘
```

---

## Proposed Features

### Accounting Agent
- Connects to 40+ bank APIs via Setu / RazorpayX
- Auto-categorizes every UPI and bank transaction using Claude AI
- Detects duplicates and flags anomalies in real time
- Updates general ledger without any manual input

### Compliance Agent
- Tracks all filing deadlines — GST (20th), TDS (7th), PF/ESI (15th)
- Sends WhatsApp / SMS alerts 7 days before due date
- Prepares draft filings automatically when data is ready
- Auto-files if configured — saves ₹500 per filing

### Cash Flow Agent
- Predicts 14-day cash position based on transaction history
- Identifies top overdue customers and drafts payment reminders
- Sends reminders via WhatsApp with embedded UPI payment links
- Suggests early payment discounts to speed up collections

### Payroll Agent
- Calculates gross salary, PF (12%+12%), TDS by slab, professional tax
- Generates payslips as PDF and sends via WhatsApp
- Initiates bank transfers automatically via RazorpayX
- Files TDS and PF returns post-disbursement

### Reporting Agent
- Converts P&L data into plain English summaries
- Answers natural language finance questions in real time
- Generates visual dashboards — revenue, expenses, profit trends

---

## Proposed Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, Tailwind CSS, shadcn/ui, Recharts |
| AI / Agents | Claude API (`claude-sonnet-4-20250514`), Anthropic Python SDK |
| Backend | Python, FastAPI, Celery, Redis |
| Database | PostgreSQL, Supabase Auth |
| Integrations | Setu / RazorpayX (bank), Twilio (WhatsApp), GST APIs |
| Infra | Docker, GitHub Actions, Vercel, Railway |

---

## Proposed System Flow

```
User  (chat or dashboard)
          │
          ▼
    FastAPI Backend
          │
          ▼
  Orchestrator Agent ──────── Claude API (Anthropic)
          │
    ┌─────┴──────┐
    ▼            ▼
Specialist    Background
  Agents      Workers (Celery)
    │               │
    ▼               ▼
PostgreSQL      Scheduled tasks
 + Redis        • Daily 8 AM deadline check
                • Cash flow monitoring
                • WhatsApp alerts
```

---

## Proposed Demo Flow

```
Step 1 → Upload messy UPI bank CSV
Step 2 → Accounting Agent categorizes all transactions in seconds
Step 3 → Ask: "Any GST deadlines this week?"
Step 4 → Compliance Agent: "GSTR-3B due in 5 days — prepare draft?"
Step 5 → Ask: "Can we pay salaries this month?"
Step 6 → Cash Flow Agent: "Balance ₹85K, salary due ₹75K.
                            3 overdue invoices (₹1.2L). Send reminders?"
Step 7 → Approve → WhatsApp reminders sent with UPI links automatically
```

---

## Proposed Business Model

| Plan | Price | Agents Included |
|---|---|---|
| Starter | ₹999 / month | Accounting + Compliance |
| Growth | ₹2,499 / month | + Cash Flow + Payroll |
| Enterprise | ₹4,999 / month | All agents + Tax Optimizer |

### Market Opportunity

```
6.3 crore Indian MSMEs
      × 0.1% penetration
      = 63,000 customers
      × ₹2,000 avg / month
      = ₹15 crore+ ARR
```

---

## Why Now?

- **Claude AI** makes multi-agent orchestration production-ready for the first time
- **UPI + open banking APIs** (Setu, RazorpayX) make bank integration frictionless
- **GST digitization** means compliance data is now structured and automatable
- **₹15,000 crore** lost annually by Indian SMEs due to financial mismanagement

---

## Project Status

> This is a **hackathon concept and design submission.**
> The architecture, agent design, product vision, and tech decisions are fully defined.
> Full implementation is planned as the next phase.

| Phase | Status |
|---|---|
| Problem research and validation | Done |
| Product design and agent architecture | Done |
| Tech stack and system design | Done |
| Agent prompt engineering | Done |
| UI/UX wireframes | Done |
| Frontend implementation | Planned |
| Backend + agent integration | Planned |
| Beta launch | Planned |

---

## Team

Built as a hackathon concept by a 4-member team.

| Member | Role |
|---|---|
| Member 1 | Backend architecture + Claude API integration |
| Member 2 | Agent design + prompt engineering |
| Member 3 | Frontend design + UI/UX |
| Member 4 | System design + DevOps + pitch |

---

> *"Your business. Your numbers. Always clear."*

<p align="center"><b>Finity</b> — Hackathon Concept, 2025</p>
