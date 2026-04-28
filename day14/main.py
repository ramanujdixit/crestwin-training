from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


def welcome_mail(name):
    with open("email.txt", "a") as f:
        f.write(f"Welcome email sent to {name}\n")


def audit_log(name):
    with open("audit.txt", "a") as f:
        f.write(f"{name} registered\n")


class UserInput(BaseModel):
    email: str
    name: str
    id: int
    city: str
    organisation: str


@app.post("/sign-up")
def signup(user: UserInput, background_tasks: BackgroundTasks):

    background_tasks.add_task(welcome_mail, user.name)
    background_tasks.add_task(audit_log, user.name)

    return JSONResponse(
        status_code=200, content={"message": f"Thank you for registering {user.name}"}
    )
