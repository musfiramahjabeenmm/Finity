from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_transactions():
    return {"message": "transactions coming soon"}

@router.post("/upload")
async def upload_file():
    return {"message": "file upload coming soon"}