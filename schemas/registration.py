from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Registration(BaseModel):
    id: str
    user_id: str
    event_id: str
    registration_date: datetime
    attended: bool = False

class RegistrationCreate(BaseModel):
    user_id: str
    event_id: str


class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[dict] = None