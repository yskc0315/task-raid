from database import SessionLocal
from models import Task

db = SessionLocal()

task = Task(
    title = "Pythonの勉強",
    difficulty = 5,
    completed = False,
    exp = 500
)

db.add(task)
db.commit()
db.close()