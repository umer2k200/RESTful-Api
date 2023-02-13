#Creating First API
#----------------------------------
#to run the code type this command in the terminal
#uvicorn mian:app --reload  
#             OR
#python -m uvicorn main:app --reload
#this reload command will help us in  a way that we
#do not want to execute the code every time.
#The only thing we will do is to save the code and reload
#the page(the path of this page is given in the terminal)
from fastapi import FastAPI,Path
from typing import List
from models import User,Gender,Role
from uuid import UUID,uuid4
app=FastAPI()
#--------------------------------------
#This is our database
db: List[User]=[
    User(id==uuid4(),
    first_name="Umer",
    last_name="Zeeshan",
    gender=Gender.male,
    roles=[Role.student,Role.admin]
    ),
    User(id==uuid4(),
    first_name="Ammar",
    last_name="Zeeshan",
    gender=Gender.male,
    roles=[Role.student]
    ),
]
#--------------------------------------
@app.get("/")
def root():
    return {"Hello": "World",
    "welcome" : "umer"}
@app.get("/api/v1/users")
async def fetch_users():
    return db
#----------------------------------------------------------
#http defines some request methods
#also known as HTTP verbs 
#like we have used the get method which is used to retrieve the data
#get method needs a path which is route
#and it returns the root()'s json object
#-----------------------------------------------------------
#You can only use await inside of functions created with async def
# async def read_results():
#     results = await some_library()
#     return results
#Basically we use this async/await for the promises
#Like if we we want to fetch some data from a server and we dont want to wait for the response
#and we want to do our work while the data fetch is in progress
#then we create a promise that when we get a response from that promise then tell me
#That's why when we set a method as async then we are telling to the computer that this method is asynchronuous and this method contains a promise inside it 
#and when we use the await command then we wait for the promise to resolve
#Now,when we get the response then we put the response of that promise in the variable
#------------------------------------------------------------------------
#STEPS:
#1)Now, we have created a user model named as models.py
#2)We will store the users in the database
#3)now the client will send the get request from any source then 
#we will use Fastapi to send the data that we have stored in our list(database)
#For this we set a get request
