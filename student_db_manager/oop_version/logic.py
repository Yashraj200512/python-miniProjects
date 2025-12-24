import json
import os
import random


class Student:

     def __init__(self,student_id:int=0,name:str="no_name",email:str="no_email"):
          self.student_id=student_id
          self.name=name
          self.email=email
     
     def __repr__(self):
         return f"student_id:{self.student_id} | name:{self.name} | email:{self.email}"

     def to_dict(self):
          return {
               "student_id":self.student_id,
               "name":self.name,
               "email":self.email
          }
     
     @classmethod
     def from_dict(cls,data):
          return cls(data.get("student_id"),data.get("name"),data.get("email"))

     




def load_data():
    try:
         with open("data.json",'r') as f:
          raw_data= json.load(f)
          student_list=[]
          
          for d in raw_data:
           student_list.append(Student.from_dict(d))
          
          return student_list


    except FileNotFoundError:
        return []

def save_data(student_list):
        with open("data.json","w") as f:
         raw_data=[]

         for s in student_list:
           raw_data.append(s.to_dict())

         json.dump(raw_data,f,indent=4)


def generate_student_id(student_list):
     while True:
          new_student_id=int(random.randint(1000,9999))
          if not any(s.student_id==new_student_id for s in student_list):
               return new_student_id


def add_student(student_list,name,email):
     unique_student_id=generate_student_id(student_list) 

     new_student=Student(unique_student_id,name,email)

     student_list.append(new_student)
     
     save_data(student_list)


def get_student_data(student_list,student_id):
   
     for s in student_list:
          if s.student_id==student_id:
               return s     
     return None
     
          
def delete_student(student_list,student_id):
     # i=-1
     # for s in student_list:
     #      i=i+1
     #      if s.get("id")==studentID:
     #          student_list.pop(i)
     #          break

     student_list[:]=[s for s in student_list if s.student_id!=student_id]

     save_data(student_list)
    
  