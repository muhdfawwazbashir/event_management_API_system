from fastapi import APIRouter
from database import speakers



router = APIRouter()

@router.get("/")
def get_speakers():
    return speakers

