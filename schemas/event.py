from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Event(BaseModel):
    id: str
    title: str
    location: str
    date: datetime
    is_open: bool = True

class EventCreate(BaseModel):
    title: str
    location: str
    date: datetime

class Events(BaseModel):
    events: list[Event]

class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[Event | Events] = None
