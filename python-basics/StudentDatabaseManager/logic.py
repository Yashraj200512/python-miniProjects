import json
import os
import uuid 

def load_data():
    try:
        with open("data.json",'r') as f:
            return json.load(f)

    except FileNotFoundError:
        return []

def save_data(students):
        with open("data.json","w") as f:
            json.dump(students,f,indent=4)


def add_student(students,name,email):
     unique_id=str(uuid.uuid4())

     new_student={
          "id":unique_id,
          "name":name,
          "email":email
     }

     students.append(new_student)
     
     save_data(students)

def get_students():
     return load_data()

