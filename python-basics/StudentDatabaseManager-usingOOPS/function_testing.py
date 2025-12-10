import json
import os
import random


class studentClass:

     def __init__(self,id,name,email):
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
          class_list=[]
          for d in dict_list:
               
               class_list.append(studentClass.from_dict(d))
          
          return class_list


    except FileNotFoundError:
        return []
    


print(load_data())    