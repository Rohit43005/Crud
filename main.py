from fastapi import FastAPI
# uvicorn main:app --reload
# pip install uvicorn

app = FastAPI()
# 127.0.0.1:8000
@app.get("/")
def home():
    return {"message": "Welcome FastAPI"}

# 127.0.0.1:8000/about
@app.get("/about")
def about():
    return {"about": "this website is about ecommerce"}

# 127.0.0.1:8000/contact
@app.get("/contact")
def contact():
    return {"contact": "you can contact us on linkedin"}


# python --version
# pip install fastapi
# pip install uvicorn
# uvicorn main:app --reload

# c:://users/acer/local/FastApi

# cd FastApi
from fastapi import FastAPI
from pydantic import BaseModel # Step A: Import BaseModel

app = FastAPI()

# Step B: Define your data structure using a class
class User(BaseModel):
    name: str
    age: int

# Step C: Pass the Pydantic model into your route
@app.post("/create_user")
def create_user(user: User): # Expect a full JSON body matching the User class
    return {
        "message": "User created",
        "data": user
    }