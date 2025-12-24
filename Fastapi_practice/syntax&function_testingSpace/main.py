from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


fake_db = []


class StudentSchema(BaseModel):
    name : str
    age:int | None=None
    email:str
    hobbies:list[str]=[]

@app.get("/")
async def root():

    return {"message": "Hello World", "status": "active"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/create-student/")
async def create_student(student:StudentSchema):
    return {
        "message": "Student received successfully",
        "data": student
    }