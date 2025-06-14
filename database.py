from uuid import uuid4
from schemas.user import User
from schemas.event import Event
from schemas.speaker import Speaker
from schemas.registration import Registration


users: dict[str, User] = {}

events: dict[str, Event] = {}

registrations: dict[str, Registration] = {}


speakers: dict[str, Speaker] = {
    1: Speaker(id=1, name="John Doe", topic="Object Oriented Programming"),
    2: Speaker(id=2, name="Chris Evans", topic="API"),
    3: Speaker(id=3, name="Prof. Lucky Danjuma", topic="Geoscience Innovation in Africa"),
}
