from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello Task Raid!"}

@app.get("/tasks")
def get_tasks():
    return [
        {
            "id": 1,
            "title": "FastAPIを学ぶ",
            "completed": False
        },
        {
            "id": 2,
            "title": "Task Raidを作る",
            "completed": True
        }
    ]