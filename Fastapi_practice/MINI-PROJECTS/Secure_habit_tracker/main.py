from fastapi import FastAPI,Query,Path
from pydantic import BaseModel,Field


app=FastAPI()

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
        return{
           "status":"logged in succesfully"
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
       
         