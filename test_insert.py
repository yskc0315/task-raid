from database import SessionLocal
from models import Task

db = SessionLocal()

task = Task(
    title = "SQLAlchemyの勉強",
    difficulty = 3,
    completed = False,
    exp = 100
)

db.add(task)
db.commit()
db.close()