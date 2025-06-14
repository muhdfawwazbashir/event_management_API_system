from pydantic import BaseModel


class Speaker(BaseModel):
    id: int
    name: str
    topic: str

# class SpeakerCreate(BaseModel):
#     name: str
#     topic: str

# class Response(BaseModel):
#     message: str
#     date: Optional[dict] = None