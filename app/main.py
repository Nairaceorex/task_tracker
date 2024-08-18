from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import Base, engine, get_db
from models import Task
from schemas import TaskCreate, Task

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=List[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks
