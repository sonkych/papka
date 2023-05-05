from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="HC App")

users = [
    {"id": 1, "name": "Andrei"},
    {"id": 2, "name": "Sofja"},
    {"id": 3, "name": "Egor"},
    {"id": 4, "name": "Makar"}
]


class User(BaseModel):
    id: int
    role: str
    name: str
    email: str
    phone: str
    telegram: str
    access: str
    department: str
    position: str
    password: str



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{users_id}")
def get_user(user_id: int):
    try:
        return [user for user in users if user.get("id") == user_id]
    except IndexError:
        return f"no user with id: {user_id}"


@app.post("/users/{users_id}")
def change_user_data(user_id: int, new_name: str):
    current_user = next(user for user in users if user.get("id") == user_id)
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}

