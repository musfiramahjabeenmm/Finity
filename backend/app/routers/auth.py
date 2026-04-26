from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"message": "auth coming soon"}

@router.post("/verify-otp")
async def verify_otp():
    return {"message": "otp verify coming soon"}