from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal,get_db
from app.core.logger import logger
import app.crud as crud
import app.schemas as schemas

router = APIRouter(prefix="/tasks",tags=["Tasks"])

@router.post("/",response_model=schemas.TaskResponse)
def create(task:schemas.TaskCreate,db:Session=Depends(get_db)):
    return crud.create_task(db,task)

@router.get("/",response_model=list[schemas.TaskResponse])
def read_all(db:Session=Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{task_id}",response_model=schemas.TaskResponse)
def read_one(task_id:int,db:Session=Depends(get_db)):
    task=crud.get_task(db,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete(task_id:int,db:Session=Depends(get_db)):
    task=crud.delete_task(db,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return{"message":"Deleted"}