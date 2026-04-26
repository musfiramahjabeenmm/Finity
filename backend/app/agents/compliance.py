import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """You are Finity's Compliance Agent for Indian SMEs.
You handle GST, TDS, HSN validation, and filing deadlines.

Indian compliance rules:
- GST: quarterly reconciliation of collected vs paid
- TDS: applicable on vendor payments above ₹30,000 (single) or ₹1,00,000 (annual)
- HSN codes: mandatory on invoices above ₹5 lakh turnover
- PF: 12% of basic salary (both employer and employee)
- ESI: 3.25% of gross salary if gross < ₹21,000/month

Always cite the applicable rule/section. Be precise and actionable."""

async def answer_compliance_query(query: str, business_context: dict = {}) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\n"
    if business_context:
        prompt += f"Business context: {business_context}\n\n"
    prompt += f"Query: {query}"

    response = model.generate_content(prompt)
    return response.text