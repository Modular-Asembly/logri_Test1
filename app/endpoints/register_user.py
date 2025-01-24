from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.utils.hash_password import hash_password
from app.services.user.add_user_to_db import add_user_to_db

router = APIRouter()

class UserRegistrationRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserRegistrationResponse(BaseModel):
    message: str

@router.post("/register", response_model=UserRegistrationResponse)
def register_user(user_data: UserRegistrationRequest) -> UserRegistrationResponse:
    """
    Endpoint to register a new user.

    - **username**: The desired username for the new user.
    - **email**: The email address of the new user.
    - **password**: The plain text password for the new user.

    Returns a success message upon successful registration.
    """
    # Hash the user's password
    hashed_password = hash_password(user_data.password)

    # Store the user in the database
    add_user_to_db(user_data.username, user_data.email, hashed_password)

    return UserRegistrationResponse(message="User registered successfully.")
