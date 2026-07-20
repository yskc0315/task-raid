from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task_data: TaskCreate):
    new_task = Task(
        title = task.title,
        difficulty = task.difficulty,
        completed = False,
        exp = task.difficulty * 100
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def update_task(db: Session, task_id: int, update: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        return None

    task.completed = update.completed
    
    db.commit()
    
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        return None

    db.delete(task)
    
    db.commit()
    
    return task