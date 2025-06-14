from uuid import UUID
from fastapi import HTTPException
from schemas.event import Event, EventCreate
from database import events

class EventService:

   
    @staticmethod
    def create_event(event_in: EventCreate):
        for event in events.values():
            if event.title == event_in.title and event.date == event_in.date:
                raise HTTPException(status_code=400, detail="Event with same title and date already exists")

        event = Event(
            id=str(UUID(int=len(events) + 1)),
            **event_in.model_dump()
        )
        events[event.id] = event
        return event

    @staticmethod
    def get_event_by_id(event_id: str):
        return events.get(event_id)

    @staticmethod
    def get_all_events():
        return list(events.values())

    @staticmethod
    def update_event(event_id: str, event_in: EventCreate):
        event = events.get(event_id)
        if not event:
            return None

        updated_event = event.copy(update=event_in.model_dump())
        events[event_id] = updated_event
        return updated_event

    @staticmethod
    def delete_event(event_id: str):
        if event_id in events:
            del events[event_id]
            return True
        return None

    @staticmethod
    def close_event(event_id: str):
        event = events.get(event_id)
        if not event:
            return None
        event.is_open = False
        return event



event_service = EventService()