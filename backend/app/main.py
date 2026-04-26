from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, transactions, chat, compliance, cashflow, payroll
from app.models import Business, Transaction, ComplianceAlert, ChatMessage  # add this

app = FastAPI(title="Finity API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router,         prefix="/api/auth",        tags=["auth"])
app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
app.include_router(chat.router,         prefix="/api/chat",         tags=["chat"])
app.include_router(compliance.router,   prefix="/api/compliance",   tags=["compliance"])
app.include_router(cashflow.router,     prefix="/api/cashflow",     tags=["cashflow"])
app.include_router(payroll.router,      prefix="/api/payroll",      tags=["payroll"])

@app.get("/health")
async def health():
    return {"status": "ok", "service": "finity-api"}