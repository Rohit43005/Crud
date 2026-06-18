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