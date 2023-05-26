from typing import Dict
from sqlalchemy.orm import Session
from app.schemas import tasks
from fastapi import HTTPException, status
from app.models import model

def show_all(db:Session):
    task = db.query(model.Task).all()
    return task

def add_task(rq:tasks.task, db:Session):
    new_task = model.Task(title = rq.title, body = rq.body)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def del_task(id:int, db:Session):
    task = db.query(model.Task).filter(model.Task.id == id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    task.delete(synchronize_session=False)
    db.commit()
    return {"deleted"}

def update(id:int, rq:tasks.task, db:Session):
    task = db.query(model.Task).filter(model.Task.id == id)

    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    task.update(rq.dict())
    db.commit()
    return {"updated"}
