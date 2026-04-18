from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def read_root():
    return{"message":"Hello World"}

@app.get("/test")
def get_test():
    return{"message":"GET request working"}

@app.post("/test")
def post_test(data:dict):
    return{"message":"POST request working",
           "my data":data
           }