from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str

tasks = []

@app.get("/")
def hello():
    return {"message": "Hello Task Raid!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task created",
        "task": task
    }