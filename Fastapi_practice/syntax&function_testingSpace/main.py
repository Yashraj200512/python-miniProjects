from fastapi import FastAPI, Query, Path
from typing import Annotated,Literal
from pydantic import BaseModel,Field
from enum import Enum
app = FastAPI()


fake_db = []


class StudentSchema(BaseModel):
    name : str
    surname:str
    age:int | None=None
    email:str =Field(pattern=r".+@.+\..+")
    hobbies:list[str]=[]
    id:int 

class ModelName(str,Enum):
    alexnet="alexnet"
    resnet = "resnet"
    lenet = "lenet"


class FilterParams(BaseModel):
    model_config={"extra":"forbid"}

    limit:int=Field(10,gt=0,le=100)
    skip:int=Field(10,ge=0)
    optional: Literal["created_at","updated_at"]="created_at"
  
                  

@app.get("/")
async def root():

    return {"message": "Hello World", "status": "active"}

@app.get("/items/item")
async def read_item():
    return {"item_id": "item_id_string"}




@app.get("/items/{item_name}")
async def read_item(item_id: Annotated[str | None ,Query( title="Query string",
            description="Query string for the items to search in the database that have a good match",
          max_length=5)],
          item_name: Annotated[str | None , Path(min_length=3)]):
          return {"item_id": item_id,
                  "item_name":item_name
                  }


@app.post("/create-student/")
async def create_student(student:StudentSchema):

    student_dict=student.model_dump()
    if student.name is not None:
        fullname=student.name+student.surname
        student_dict.update({"full_name":fullname})
    return {
        "message": "Student received successfully",
         **student_dict
    }

@app.put("/create-student/{student_id}")
async def update_student(student_id:int ,student:StudentSchema):
    student_dict=student.model_dump()
    
    for key,value in student_dict.items():
        if value is not None:
            student_dict.update({key:value})
    return {
        "message": "Student updated successfully",
         **student_dict,
         "id":student_id
    }



@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.lenet:
        return {
            "model_name":ModelName.lenet.value, "message":"Deep learning FTW"
        }
    else:
     return {
        "model_name":"not matching"
    }



@app.get("/files/{file_path:path}") 
async def read_file(file_path:str):
    return{
        "file_path":file_path
    } 

@app.get("/pagination/")
async def show_page(pagination_query: Annotated[FilterParams,Query()]):
    return{
        "Your_page":f"pages showimg from {pagination_query.limit+pagination_query.skip} and {pagination_query.optional} just now"
    }
