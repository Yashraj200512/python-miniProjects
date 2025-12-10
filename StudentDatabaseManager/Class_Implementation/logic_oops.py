import json
import os
import random


class Student:

     def __init__(self,id:int=0,name:str="no_name",email:str="no_email"):
          self.id=id
          self.name=name
          self.email=email
     
     def __repr__(self):
         return f"id:{self.id} | name:{self.name} | email:{self.email}"

     def to_dict(self):
          return {
               "id":self.id,
               "name":self.name,
               "email":self.email
          }
     
     @classmethod
     def from_dict(cls,data):
          return cls(data.get("id"),data.get("name"),data.get("email"))

     




def load_data():
    try:
         with open("data.json",'r') as f:
          dict_list= json.load(f)
          student_list=[]
          
          for d in dict_list:
           student_list.append(Student.from_dict(d))
          
          return student_list


    except FileNotFoundError:
        return []

def save_data(student_list):
        with open("data.json","w") as f:
         dict_list=[]

         for s in student_list:
           dict_list.append(s.to_dict())

         json.dump(dict_list,f,indent=4)


def generate_id(student_list):
     while True:
          new_id=int(random.randint(1000,9999))
          if not any(s.id==new_id for s in student_list):
               return new_id


def add_student(student_list,name,email):
     unique_id=generate_id(student_list) 

     new_student=Student(unique_id,name,email)

     student_list.append(new_student)
     
     save_data(student_list)


def get_student_data(student_list,student_id):
   
     for s in student_list:
          if s.id==student_id:
               return s     
     return None
     
          
def delete_student(student_list,student_id):
     # i=-1
     # for s in student_list:
     #      i=i+1
     #      if s.get("id")==studentID:
     #          student_list.pop(i)
     #          break

     student_list[:]=[s for s in student_list if s.id!=student_id]

     save_data(student_list)
    
  