from fastapi import APIRouter

router = APIRouter()

@router.get("/forecast")
async def get_forecast():
    return {"message": "cashflow forecast coming soon"}