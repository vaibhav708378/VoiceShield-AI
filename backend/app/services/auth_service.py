from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt

from app.database.mongodb import db


pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto"
)

SECRETE_KEY = "voicesheild-secrete-key"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def create_access_token(user_id: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=24)

    payload = {
        "sub": user_id,
        "exp": expire
    }
    return jwt.encode(payload, SECRETE_KEY, algorithm=ALGORITHM)


def register_user(name: str, email: str, password: str):
    existing_user = db.users.find_one({
        "email": email
    })

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
    user = db.users.find_one({
        "email": email
    })

    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return user

