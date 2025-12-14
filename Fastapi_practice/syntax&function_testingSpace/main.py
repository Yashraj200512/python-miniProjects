from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
app = FastAPI()


fake_db = []


class StudentSchema(BaseModel):
    name : str
    age:int | None=None
    email:str
    hobbies:list[str]=[]

class ModelName(str,Enum):
    alexnet="alexnet"
    resnet = "resnet"
    lenet = "lenet"



@app.get("/")
async def root():

    return {"message": "Hello World", "status": "active"}

@app.get("/items/item")
async def read_item():
    return {"item_id": "item_id_string"}




@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/create-student/")
async def create_student(student:StudentSchema):
    return {
        "message": "Student received successfully",
        "data": student
    }

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.lenet:
        return {
            "model_name":ModelName.lenet.value, "message":"Deep learning FTW"
        }
    


@app.get("/files/{file_path:path}") 
async def read_file(file_path:str):
    return{
        "file_path":file_path
    } 