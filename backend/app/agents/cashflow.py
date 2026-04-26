import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """You are Finity's Cash Flow Agent for Indian SMEs.
You analyze transaction history and provide:
- 30/60/90-day runway forecasts
- Overdue invoice flags
- Spending pattern analysis
- Cash flow risk warnings

Always provide specific numbers and dates. Format response as structured JSON when asked."""

async def analyze_cashflow(transactions_summary: str, query: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nTransaction data:\n{transactions_summary}\n\nQuery: {query}"
    response = model.generate_content(prompt)
    return response.text