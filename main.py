from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class TestData(BaseModel):
    name:str
    task:str
@app.get("/")
def read_root():
    return{"message":"Hello World"}

@app.get("/test")
def get_test():
    return{"message":"GET request working"}

@app.post("/test")
def post_test(data:TestData):
    return{"message":"POST request working",
           "my data":data
           }
