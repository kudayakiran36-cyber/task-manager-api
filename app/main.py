from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db,Base,engine
from app.routers import task
import app.models as models

app=FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(task.router)

'''
class TaskCreate(BaseModel):
    name:str
    task:str
@app.get("/")
def read_root():
    return{"message":"Hello World"}

@app.get("/test")
def get_test():
    return{"message":"GET request working"}

@app.post("/test")
def create_task(data:TaskCreate,db:Session=Depends(get_db)):
    new_task=models.Task(
        name=data.name,
        task=data.task
        )
    db.add(new_task)
    print("before commit",new_task.name,new_task.task)
    db.commit()
    db.refresh(new_task)
    return new_task
    '''