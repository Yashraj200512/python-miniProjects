
from fastapi import FastAPI,Query,Path
from pydantic import BaseModel,Field
import jwt

app=FastAPI()

SECRET_KEY="secret_dummy_password"
ALGORITHM="HS256"



fake_users_db={
    "yash":{"User":"yash", "password":"abcd123"}

}

fake_habits_db=[
    {"id":1,"title":"watch anime","owner":"yash"},
    {"id":2,"title":"go for run","owner":"yash"}
]



class UserSchema(BaseModel):
    name:str
    password:str


class habits(BaseModel):
    title: str


@app.get("/")
async def root():
    return {
        "message1":"welcome to secure habit tracker",
        "messagee2":"go to /login to login"
    }


@app.post("/login/")
async def user_login(user:UserSchema):

    user_dict=user.model_dump()
    username=user_dict["name"]

    if username in fake_users_db:
     
     if fake_users_db[username]["password"]==user_dict["password"]:
        


        token_data={"sub":username}

        encoded_jwt=jwt.encode(token_data,SECRET_KEY,algorithm=ALGORITHM)
        return{
           "status":"logged in succesfully",
           "access_token":encoded_jwt,
           "token_type": "bearer",
                         }
     else:
        return{
        "status":"wrong password"  
     }
    
    
    else:
       fake_users_db.update({
          username :
             
             {
                "User":username,
                "password":user_dict["password"]
             

          }
          }
        )
       return {"status": "entry created successfully"}
       

@app.get("/login/{username}")
async def get_user_habits(username:str):
   user_habits=[]

   for habit in fake_habits_db:
    if habit["owner"]==username:
       user_habits.append(habit)



   if(user_habits==[]): return{
      "status":"failure,please enter habits first"

   }
   return{
     "status":"succes",
     "your habits":user_habits
  }


@app.post("/login/{username}")

async def add_habit(username:str,habit_data:habits):
   
   if username in fake_users_db:
      fake_habits_db.append({
         "id":3,
         "title":habit_data.title,
         "owner":username
      })
    

@app.delete("/login/{habit_id}")
async def delete_habit(habit_id:int):
   
   for habit in fake_habits_db:
      if habit["id"]==habit_id:
         fake_habits_db.remove(habit)
         return{
            "status":"success,habit removed"
         }
     
   return{
            "status":"failure,habit not found"
         }