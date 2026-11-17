from fastapi import FastAPI
from streamlit import user

app = FastAPI()

users = [
    {"user_id": 101, "name": "Banwar Singh"},
    {"user_id": 102, "name": "Pushparaj"},
    {"user_id": 103, "name": "Srivalli"},
    {"user_id": 104, "name": "Keshava"},
    {"user_id": 105, "name": "Srinu"},
    {"user_id": 106, "name": "Jali Reddy"},

]

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0:
        return {"error": "Invalid user ID"}
    else:
        for i in users:
            if i["user_id"] == user_id:
                user = i
                break
    return user

