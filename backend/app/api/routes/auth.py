from fastapi import APIRouter, Depends, HTTPException, status

from app.models.user import UserCreate, UserLogin
from app.services.auth_service import register_user, authenticate_user, create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserCreate):
    user_id = register_user(user.name, user.email, user.password)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return {
        "message": "User registered successfully",
        "user_id": user_id
    }

@router.post("/login")
def login(user: UserLogin):
    existing_user = authenticate_user(
        user.email,
        user.password
    )

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        str(existing_user["_id"])
    )

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }

