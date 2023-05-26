from typing import List,Dict
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import tasks
from app.services import todo
from . import db


router = APIRouter(tags = ['todo'])

get_db = db.get_db


@router.get('/all',response_model=List[tasks.task])
async def all(db:Session = Depends(get_db)): #add_auth
    return todo.show_all(db)

@router.post('/add')
async def add_task(rq:tasks.task, db:Session = Depends(get_db)):
    return todo.add_task(rq,db)

@router.delete('/delete')
async def del_task(id:int, db:Session = Depends(get_db)):
    return todo.del_task(id,db)

@router.put('/{id}')
async def update(id:int, rq:tasks.task, db:Session = Depends(get_db)):
    return todo.update(id,rq,db)