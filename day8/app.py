from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated
import json

app = FastAPI()


def load_file():
    with open("project/task_file.json", "r") as f:
        data = json.load(f)

    return data


def save_file(data):
    with open("project/task_file.json", "w") as f:
        json.dump(data, f)


# Request Model
class UserInput(BaseModel):
    title: Annotated[str, Field(..., description="name of your task")]
    description: Annotated[str, Field(..., description="add description of your task")]
    status: Annotated[
        bool,
        Field(..., description="have you completed the task or not"),
    ]


# home page
@app.get("/")
def home():
    return {"message": "welcome to a task manager application"}


#  Create Task
@app.post("/create")
def create_task(task: UserInput):
    data = load_file()

    new_task = {
        "id": len(data) + 1,
        "title": task.title,
        "description": task.description,
        "status": task.status,
    }

    data.append(new_task)
    save_file(data)

    return {"message": "Task added", "task": new_task}


# Get All Tasks
@app.get("/tasks")
def show_tasks():
    return load_file()


# delete a specific task
@app.delete("/tasks/{id}")
def delete_tasks(id: int):
    data = load_file()

    for i, task in enumerate(data):
        if task["id"] == id:
            deleted_task = data.pop(i)
            save_file(data)
            return {"message": "Task deleted", "task": deleted_task}

    raise HTTPException(status_code=404, details="task not found")


@app.put("/tasks/{id}")
def update_task(id: int, task_update: UserInput):
    data = load_file()
    for task in data:
        if task["id"] == id:
            task["title"] = task_update.title
            task["description"] = task_update.description
            task["status"] = task_update.status

            save_file(data)
            return {"message": "Task updated", "task": task}

    raise HTTPException(status_code=404, detail="Task not found")
