from sqlalchemy.orm import Session
from app.core.logger import logger
import app.models as models
import app.schemas as schemas

def get_tasks(db:Session):
    return db.query(models.Task).all()
def get_task(db:Session,task_id:int):
    return db.query(models.Task).filter(models.Task.id==task_id).first()
def delete_task(db:Session,task_id:int):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
def update_task(db:Session,task_id:int,data):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task:
        return None
    task.name=data.name
    task.task=data.task
    db.commit()
    db.refresh(task)
    return task
def create_task(db:Session,task:schemas.TaskCreate):
    logger.info("Inserting task into DB")
    new_task=models.Task(name=task.name,task=task.task)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task