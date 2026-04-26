import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """You are Finity's Accounting Agent for Indian SMEs.
Parse transactions and return structured JSON:
{
  "transactions": [
    {
      "date": "YYYY-MM-DD",
      "description": "...",
      "amount": 0.00,
      "type": "debit|credit",
      "category": "...",
      "vendor": "...",
      "gst_applicable": true|false,
      "hsn_code": "..." or null
    }
  ]
}
Return ONLY valid JSON."""

async def parse_transactions(content: str) -> dict:
    response = model.generate_content(f"{SYSTEM_PROMPT}\n\nContent to parse:\n{content}")
    import json
    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)

async def parse_receipt_image(image_bytes: bytes) -> dict:
    import PIL.Image, io
    img = PIL.Image.open(io.BytesIO(image_bytes))
    response = model.generate_content([
        f"{SYSTEM_PROMPT}\n\nExtract transaction data from this receipt:",
        img
    ])
    import json
    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)