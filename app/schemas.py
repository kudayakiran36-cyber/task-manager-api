from pydantic import BaseModel,Field

class TaskCreate(BaseModel):
    name:str=Field(min_length=1,max_length=50)
    task:str=Field(min_length=1,max_length=500)

class TaskResponse(BaseModel):
    id:int
    name:str
    task:str
    model_config={
        "from_attributes":True
    }