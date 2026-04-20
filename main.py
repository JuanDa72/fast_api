from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


#GETS METHODS

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
def read_status():
    return {"status": "ok"}

#Path parameter example
@app.get("/path_param/{param}")
def read_path_param(param: str):
    return {"param": param}


#Query parameter example
#The url has to be something like this: http://127.0.0.1/8000/query_param?param=value
#Its important to note that the query parameter is not part of the path, but is passed as a separate parameter in the URL.
#Also it has to have the same name as the parameter
@app.get("/query_param")
def read_query_param(param: str):
    return {"The query parameter is": param}


#Several query parameters example
@app.get("/several_query_params")
def read_several_query_params(param1: str, param2: int):
    return {"The first query parameter is": param1, "The second query parameter is": param2}


#Optionals parameters
@app.get("/optional")
def read_optional_param(param: Optional[str] = None):
    if param:
        return {"The optional parameter is": param}
    else:
        return {"No optional parameter provided"}
    

#POST METHODS
class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
    return {"The student is": student}

