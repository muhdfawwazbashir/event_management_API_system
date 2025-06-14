from fastapi import FastAPI
from routes import user, event, registration, speaker


app = FastAPI()

app.include_router(user.router, prefix="/users")
app.include_router(event.router, prefix="/events")
app.include_router(speaker.router, prefix="/speakers")
app.include_router(registration.router, prefix="/registration")

@app.get("/")
def home ():
    return "Welcome to the Event Management API"

