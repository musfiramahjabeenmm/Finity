import google.generativeai as genai
import json
from app.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """You are the Finity Orchestrator. Your ONLY job is to classify user intent and route to the correct agent.
Return a JSON object with:
- agent: one of [accounting, compliance, cashflow, payroll, sql]
- intent: brief description
- params: any extracted parameters

Routing rules:
- accounting → transaction parsing, categorization, receipt upload
- compliance → GST, TDS, HSN, filing deadlines
- cashflow → runway, forecasts, overdue invoices
- payroll → salary, PF, ESI calculations
- sql → simple aggregations like totals, counts, summaries

Return ONLY valid JSON, no explanation."""

async def route_intent(user_message: str, context: dict = {}) -> dict:
    response = model.generate_content(
        f"{SYSTEM_PROMPT}\n\nUser message: {user_message}"
    )
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(text)