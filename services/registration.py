from uuid import uuid4
from fastapi import HTTPException
from datetime import datetime

from schemas.registration import Registration, RegistrationCreate
from database import registrations, users, events

class RegistrationService:

    @staticmethod
    def register_user(reg_data: RegistrationCreate):
        #check if user exists and is active
        user = users.get(str(reg_data.user_id))
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.is_active:
            raise HTTPException(status_code=400, detail="User is not active")
        
        #check if event exists and is active
        event = events.get(str(reg_data.event_id))
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if not event.is_open:
            raise HTTPException(status_code=400, detail="Event is closed")
        
        #Prevent duplicate registration
        for reg in registrations.values():
            if reg.user_id == reg_data.user_id and reg.event_id == reg_data.event_id:
                raise HTTPException(status_code=400, detail="User already registered for this event")
            

        #create new registration
        reg_id = str(uuid4())
        new_registration = Registration(
            id = reg_id,
            user_id=reg_data.user_id,
            event_id=reg_data.event_id,
            registration_date=datetime.utcnow(),
        )
        registrations[reg_id] = new_registration
        return new_registration
    


    @staticmethod
    def mark_attendance(reg_id: str):
        reg = registrations.get(reg_id)
        if not reg:
            raise HTTPException(status_code=404, detail="Registration not found")
        reg.attended = True
        registrations[reg_id] = reg
        return reg
    

    @staticmethod
    def get_all():
        return list(registrations.values())
    

    @staticmethod
    def get_by_user(user_id: str):
        return[r for r in registrations.values() if r.user_id == user_id ]
    

registration_service = RegistrationService()