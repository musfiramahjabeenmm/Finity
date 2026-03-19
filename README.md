# Finity — AI Financial OS for Indian SMEs

> **Finity** is an AI-powered financial assistant for Indian SMEs that automates accounting, GST compliance, payroll, and cash flow management through intelligent agents — giving every business owner real-time financial clarity via a simple chat interface.

---

## The Problem

```
6.3 crore Indian MSMEs manage finance with spreadsheets, manual ledgers & expensive CAs
```

| Pain Point | Impact |
|---|---|
| Manual UPI/bank data entry | 15–20 hrs wasted per month |
| Bookkeeping errors | 5–10% error rate → wrong tax filings |
| Missed GST / TDS deadlines | 40% of SMEs — ₹5,000+ penalty each |
| No real-time P&L visibility | 60% of owners fly blind |
| Tally / Zoho ERP | ₹50,000/yr + 3–6 months training |

---

## The Solution

Finity deploys **6 specialized AI agents** that run 24/7 — no accounting knowledge needed.

```
User Chat  ──▶  Orchestrator Agent  ──▶  Specialist Agent  ──▶  Action / Response
```

| Agent | What it does |
|---|---|
| Orchestrator | Routes every user message to the right specialist |
| Accounting | Auto-categorizes UPI/bank transactions from CSV |
| Compliance | Tracks GST, TDS, PF deadlines — alerts 7 days before |
| Cash Flow | Predicts 14-day cash shortfalls, sends payment reminders |
| Payroll | Calculates salary, PF, TDS — initiates transfers |
| Reporting | Generates plain-language P&L summaries and dashboards |

---

## Demo Flow

```
1. Upload messy UPI CSV
        ↓
2. Accounting Agent categorizes all transactions in seconds
        ↓
3. Ask: "Any GST deadlines this week?"
        ↓
4. Compliance Agent: "GSTR-3B due in 5 days — want me to prepare the draft?"
        ↓
5. Ask: "Can we afford to pay salaries?"
        ↓
6. Cash Flow Agent: "Balance ₹85,000. Salary due ₹75,000. 3 overdue invoices (₹1.2L). Send reminders?"
        ↓
7. Approve → Agent auto-sends WhatsApp reminders with UPI payment links
```

---

## Tech Stack

```
┌─────────────────────────────────────────────┐
│  Frontend       Next.js 14 · Tailwind CSS   │
│                 shadcn/ui · Recharts         │
├─────────────────────────────────────────────┤
│  AI Brain       Claude API (Anthropic)       │
│                 claude-sonnet-4-20250514     │
│                 Multi-agent · Tool calling  │
│                 SSE Streaming               │
├─────────────────────────────────────────────┤
│  Backend        Python · FastAPI            │
│                 Celery · Redis              │
│                 Pydantic · Alembic          │
├─────────────────────────────────────────────┤
│  Database       PostgreSQL · Supabase Auth  │
├─────────────────────────────────────────────┤
│  Infra          Docker · GitHub Actions     │
│                 Vercel · Railway            │
└─────────────────────────────────────────────┘
```

---

## Project Structure

```
finity/
├── backend/
│   ├── main.py                  # FastAPI entry point
│   ├── routers/
│   │   ├── chat.py              # /api/chat — SSE streaming
│   │   ├── transactions.py      # /api/upload-csv
│   │   └── compliance.py        # /api/compliance/deadlines
│   ├── agents/
│   │   ├── orchestrator.py      # Routes intent to specialist
│   │   ├── accounting.py        # CSV parse + Claude categorize
│   │   ├── compliance.py        # GST/TDS deadline logic
│   │   ├── cashflow.py          # 14-day prediction
│   │   ├── payroll.py           # Salary + PF + TDS calc
│   │   └── reporting.py         # Natural language P&L
│   ├── services/
│   │   ├── claude_client.py     # Anthropic SDK wrapper
│   │   └── whatsapp.py          # Twilio alerts
│   ├── models/                  # SQLAlchemy models
│   ├── tasks/                   # Celery scheduled tasks
│   └── db/database.py           # PostgreSQL connection
│
├── frontend/
│   ├── app/
│   │   ├── dashboard/page.tsx   # P&L + metrics
│   │   ├── chat/page.tsx        # Streaming chat UI
│   │   ├── transactions/page.tsx
│   │   └── compliance/page.tsx
│   ├── components/
│   │   ├── ChatWindow.tsx
│   │   ├── TransactionTable.tsx
│   │   ├── CashFlowChart.tsx
│   │   └── DeadlineBanner.tsx
│   └── hooks/useStream.ts       # EventSource hook
│
├── docker-compose.yml
└── .env.example
```

---

## Git Module Strategy

Each feature lives in its own branch to prevent conflicts:

```
main
├── feat/core-infra       # FastAPI setup, DB, Claude client
├── feat/auth             # Supabase JWT + login/signup pages
├── feat/transactions     # CSV upload + accounting agent
├── feat/compliance       # GST/TDS deadlines + Celery task
├── feat/cashflow         # Cash flow agent + payroll agent
├── feat/chat             # Orchestrator + streaming chat UI
└── feat/dashboard        # P&L charts + reporting agent
```

**Merge order:** `core-infra` → `auth` → `transactions / compliance / cashflow` (parallel) → `chat` → `dashboard`

---

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker Desktop
- Anthropic API key

### 1. Clone the repo

```bash
git clone https://github.com/your-team/finity.git
cd finity
```

### 2. Set environment variables

```bash
cp .env.example .env
```

```env
ANTHROPIC_API_KEY=sk-ant-...
DATABASE_URL=postgresql://postgres:password@localhost:5432/finity
REDIS_URL=redis://localhost:6379
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=your-anon-key
TWILIO_ACCOUNT_SID=your-sid
TWILIO_AUTH_TOKEN=your-token
```

### 3. Start backend services

```bash
docker-compose up -d        # Starts PostgreSQL + Redis
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 4. Start Celery workers

```bash
# In a new terminal
celery -A tasks.scheduled worker --loglevel=info

# In another terminal (scheduler)
celery -A tasks.scheduled beat --loglevel=info
```

### 5. Start frontend

```bash
cd frontend
npm install
npm run dev
```

App runs at `http://localhost:3000` · API at `http://localhost:8000`

---

## Key API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/chat` | Streaming chat with orchestrator agent |
| `POST` | `/api/upload-csv` | Upload UPI/bank CSV → auto-categorize |
| `GET` | `/api/compliance/deadlines` | Fetch upcoming GST/TDS deadlines |
| `GET` | `/api/cashflow/forecast` | 14-day cash flow prediction |
| `POST` | `/api/payroll/run` | Trigger monthly payroll |
| `GET` | `/api/reports/pl` | P&L summary (natural language) |

---

## Pricing Tiers

| Plan | Price | Agents |
|---|---|---|
| Starter | ₹999/mo | Accounting + Compliance |
| Growth | ₹2,499/mo | + Cash Flow + Payroll |
| Enterprise | ₹4,999/mo | All agents + Tax + Reporting |

**Target market:** 6.3 crore Indian MSMEs · 0.1% penetration = ₹15 crore+ ARR

---

## Team

Built with ❤️ at [Hackathon Name] by a 4-member team.

| Role | Responsibility |
|---|---|
| Backend Lead | FastAPI, DB models, Claude integration |
| Agent Dev | All AI agents, prompt engineering |
| Frontend Lead | Next.js UI, charts, streaming chat |
| DevOps | Docker, CI/CD, deployment, demo data |

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <b>Finity</b> · AI Financial OS for Indian SMEs<br/>
  <i>Your business. Your numbers. Always clear.</i>
</p>
