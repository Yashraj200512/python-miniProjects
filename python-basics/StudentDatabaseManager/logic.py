import json
import os
import random


def load_data():
    try:
         with open("data.json",'r') as f:
          return json.load(f)

    except FileNotFoundError:
        return []

def save_data(studentList):
        with open("data.json","w") as f:
            json.dump(studentList,f,indent=4)


def generate_id(studentLIst):
     while True:
          new_id=str(random.randint(1000,9999))
          if not any(s.get('id')==new_id for s in studentLIst):
               return new_id


def add_student(studentList,name,email):
     unique_id=generate_id(studentList)

     new_student={
          "id":unique_id,
          "name":name,
          "email":email
     }

     studentList.append(new_student)
     
     save_data(studentList)


def get_student_data(studentList,student_id):
   
     for s in studentList:
          if s.get('id')==student_id:
               return s     
     return None
     
          
def delete_student(studentList,studentID):
     # i=-1
     # for s in studentList:
     #      i=i+1
     #      if s.get("id")==studentID:
     #          studentList.pop(i)
     #          break

     studentList[:]=[s for s in studentList if s.get("id")!=studentID]

     save_data(studentList)
    
  