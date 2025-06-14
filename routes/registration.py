from fastapi import APIRouter, HTTPException
from database import registrations
from schemas.registration import Registration, RegistrationCreate, Response
from services.registration import registration_service


router = APIRouter()


@router.post("/")
def register_user(reg_data: RegistrationCreate):
    reg = registration_service.register_user(reg_data)
    return Response(message="Registration successful", data=reg.model_dump())

@router.patch("/{reg_id}/attend")
def mark_attendance(reg_id: str):
    reg = registration_service.mark_attendance(reg_id)
    return Response(message="Attendance marked", data=reg.model_dump())

@router.get("")
def get_all_registrations():
    return registrations
    

@router.get("/user/{user_id}")
def get_registrations_by_user(user_id: str):
    regs = registration_service.get_by_user(user_id)
    if not regs:
        raise HTTPException(status_code=404, detail="No registration found for this user")
    return regs