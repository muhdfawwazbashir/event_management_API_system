from fastapi import APIRouter, HTTPException
from database import speakers
from schemas.speaker import Speaker, SpeakerCreate, Response
from services.speaker_service import speaker_service


router = APIRouter()

@router.get("/")
def get_speakers():
    return speakers

@router.get("/{speaker_id}")
def get_speaker_by_id(speaker_id: int):
    speaker = speaker_service.get_speaker_by_id(speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return speaker

@router.post("")
def create_speaker(speaker_in: SpeakerCreate):
    speaker = speaker_service.create_speaker(speaker_in)
    return {"message": "Speaker added successfully", "data": speaker}


@router.delete("/{speaker_id}")
def delete_speaker(speaker_id: int):
   success = speaker_service.delete_speaker(speaker_id)
   if not success:
       raise HTTPException(status_code=404, detail="Speaker not found.")
   return Response(message="Speaker deleted successfully", date={"speaker_id": speaker_id})