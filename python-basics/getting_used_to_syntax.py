#ok a,b=0,1

# while a<10:
#     print(a)
#     c=a
#     a=b
#     b=c+b
    

# dict={'name':"Yashraj", 'age':10}    

# # dict['age']=90
# # dict['email']='hmm'
# # print(dict)
# # dict.pop('email')
# # print(dict)

# for key, value in dict.items():
#     print(f"{key}: {value}")

class StudentClass:

     def __init__(self,id : int,name : str,email : str):
          
          self.id=id
          self.name=name
          self.email=email

     def __repr__(self):
        return f"ID:{self.id} | Name:{self.name} | Email:{self.email}"
    
     def to_dict(self):
         return {
             "id":self.id,
             "name":self.name,
             "email":self.email
         }
     
  
     @classmethod
     def from_dict(cls,data):
         return cls(data.get("id"),data.get("name"),data.get("email"))
         



s1=StudentClass(10,'yash','@gmail.com')
 
s2=StudentClass(11,'john',"john@gmail")

list=[s1,s2]

s1_dict=s1.to_dict()
print(s1_dict)

s1_again=StudentClass.from_dict(s1_dict)
print(s1_again)