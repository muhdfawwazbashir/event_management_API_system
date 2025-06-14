from fastapi import APIRouter, HTTPException
from database import events
from schemas.event import Event, EventCreate, Response
from services.event_service import event_service

router = APIRouter()

@router.get("/")
def get_events():
    return events


@router.get("/{event_id}")
def get_event_by_id(event_id: str):
    event = event_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/")
def create_event(event_in: EventCreate):
    event = event_service.create_event(event_in)
    return Response(message="Event created successfully", data=event)


@router.put("/{event_id}")
def update_event(event_id: str, updated_event: Event):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    events[event_id] = updated_event
    return updated_event


@router.delete("/{event_id}")
def delete_event(event_id: str):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    del events[event_id]
    return {"message": "Event deleted successfully"}


@router.patch("/{event_id}")
def close_event(event_id: str):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    event = events[event_id]
    event.is_open = False
    events[event_id] = event
    return event
