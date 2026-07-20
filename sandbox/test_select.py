from database import SessionLocal
from models import Task

db = SessionLocal()

tasks = db.query(Task).all()

for task in tasks:
    print(task.id)
    print(task.title)
    print(task.difficulty)
    print(task.completed)
    print(task.exp)
    print("-----------")

task = db.query(Task).first()
print(task.title)

tasks = db.query(Task).order_by(Task.difficulty.desc()).all()
for task in tasks:
    print(task.id)
    print(task.title)
    print(task.difficulty)
    print(task.completed)
    print(task.exp)
    print("-----------")

db.close()