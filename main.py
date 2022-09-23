from fastapi import FastAPI
from typing import List
from models import User, Gender, Role

app = FastAPI()
db: List[User] = [
    User(
        id=1,
        first_name="Bogdan",
        last_name="Ziolko",
        gender=Gender.male,
        roles=[Role.user]
    ),
    User(
        id=2,
        first_name="Kamila",
        last_name="Maj",
        gender=Gender.female,
        roles=[Role.manager, Role.user]
    ),
]

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)