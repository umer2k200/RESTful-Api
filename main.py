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
from fastapi import FastAPI,Path,HTTPException
from typing import List
from models import User,Gender,Role
from uuid import UUID,uuid4
app=FastAPI()
#--------------------------------------
#This is our database
db: List[User]=[
    User(id=uuid4(),
    first_name="Umer",
    last_name="Zeeshan",
    gender=Gender.male,
    roles=[Role.student,Role.admin]
    ),
    User(id=UUID("e60b2672-b36f-4807-a26b-2e56c7ec9044"),
    first_name="Ammar",
    last_name="Zeeshan",
    gender=Gender.male,
    roles=[Role.student]
    ),
    User(id=uuid4(),
    first_name="Muhammad",
    last_name="Zeeshan",
    middle_name=None,
    gender=Gender.male,
    roles=[Role.user,Role.student])
]
#--------------------------------------
@app.get("/")
def root():
    return {"Hello": "World",
    "welcome" : "umer"}
@app.get("/api/v1/users") 
async def fetch_users(): 
    return db
#now everytime i relaod the page i will get a different id in our database
#so if we want to fix the id then we can do....
#for this go to the database above
#---------------------------------------
@app.post("/api/v1/users")
async def register_user(user:User): #takes user from the request body
    db.append(user)  #this will add the user to the api or the client 
    return {"id":user.id} #will return the user id back to the client
#like here we are registering the user to the client the id for that user
#now there is a problem that we can sent a get request like above but
#we cannot sent a post request to the api throughh a web browser so for this:
#for this we use thunder client extension which we can use to send a request or post
'''now lets suppose if we want to sent a post request so, as  above we have mentioned that
the method registeruser will take the user which is json object and the arrangement of its members
should be the same as of our basemodel defined in models.py. We will put that json object in the body 
of the post request and then hit on send request. This will add a new in our database or server.
Everytime we post it adds the entity to our database
but everytime we reload the server or site we lose the data that we have posted
so this is very to interact with our api through this'''
#---------------------------------------
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id: #if id is found then delete and return(exit from the loop)
            return 
    raise HTTPException(  #for what if it cannot find that id
        status_code=404,
        detail=f"user with the id :{user_id} does not exists"
    )
#this will delete the user from our database
#Now the main issue here is that what we will do if we dont have any sort of data in our database
#we'll handle these exceptions
#---------------------------------------
#you should also know the http responses:
#Informational responses (100-199)
#Successful responses (200-299)
#Redirection responses (300-399)
#Client error responses (400-499)
#like 404 not found which means it couldn't find the requested resource
#Server error responses (500-599)
#These are the status codes
#---------------------------------------
#---------------------------------------
#----------------------------------------------------------
#http defines some request methods
#also known as HTTP verbs 
#like we have used the get method which is used to retrieve the data
#get method needs a path which is route
#and it returns the root()'s json object
#also the post method is used to submit an entity to the specified resource
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
#For this we set a get request and send a get request using async await and a path or route
#it will return the data like we can do /api/users or /api/products
#4)now we can also add some entity or user or anything to the client like above
#for this we send a post request.this can only be done by e.g
#    ->thunder client extension
#    ->http://127.0.0.1:8000/docs
#           (this is a default way)
#    ->http://127.0.0.1:8000/redoc (this one is not interactive so we should use the above ones)
#point to be noted:: searching for a path that we have not defined will giver you nothing.
#5)WE can also delete an entity from our database through our api
#--------------------------------------------------------------------------------------------------
#now we'll work on the autrhentication of the users
#
from fastapi import status
from fastapi.responses import RedirectResponse
import os
os.environ['JWT_SECRET_KEY']='9b9f70b6-8bd0-43de-9217-31fb409c3392'
#from utils import get_hashed_pass

from uuid import uuid4

