from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    difficulty: int

class TaskUpdate(BaseModel):
    completed: bool

class Task(BaseModel):
    id: int
    title: str
    difficulty: int
    completed: bool
    exp: int

tasks = []

@app.get("/")
def hello():
    return {"message": "Hello Task Raid!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: TaskCreate):

    new_task = Task(
        id = len(tasks) + 1,
        title = task.title,
        difficulty = task.difficulty,
        completed = False,
        exp = task.difficulty * 100
    )

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            task.completed = update.completed
            return task
    return {"message": "Task not found"}