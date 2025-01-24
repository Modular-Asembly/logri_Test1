from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.utils.verify_password import verify_password
from app.services.auth.issue_auth_token import issue_auth_token
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.User import User

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=TokenResponse)
def authenticate_user(login_data: LoginRequest, db: Session = Depends(get_sql_session)) -> TokenResponse:
    """
    Authenticates a user and returns a JWT token.

    :param login_data: The login data containing username and password.
    :param db: The database session.
    :return: A TokenResponse containing the JWT token.
    """
    user = db.query(User).filter(User.username == login_data.username).first()

    if not user or not verify_password(login_data.password, user.password_hash.__str__()):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token = issue_auth_token(user.id)
    return TokenResponse(access_token=token)
