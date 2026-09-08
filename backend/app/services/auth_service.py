from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt, JWTError

from app.database.mongodb import db
from app.core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def create_access_token(user_id: str):
    expire = datetime.utcnow() + timedelta(hours=24)

    payload = {
        "user_id": user_id,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm="HS256"
    )


def verify_access_token(token: str):
    try:
        payload = payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        user_id = payload.get("user_id")

        if user_id is None:
            return None

        return user_id

    except JWTError:
        return None


def register_user(name: str, email: str, password: str):
    existing_user = db.users.find_one({"email": email})

    if existing_user:
        return None

    user = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "created_at": datetime.utcnow()
    }

    result = db.users.insert_one(user)

    return str(result.inserted_id)


def authenticate_user(email: str, password: str):
    user = db.users.find_one({"email": email})

    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return user