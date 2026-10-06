from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mongodb import db
from app.api.routes.auth import router as auth_router
from app.realtime.websocket import router as websocket_router


app = FastAPI(
    title="VoiceShield AI API",
    description="AI-powered voice deepfake and scam detection system",
    version="1.0.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(websocket_router)


@app.get("/")
def home():
    return {
        "message": "VoiceShield AI Backend is Running!"
    }


@app.get("/health")
def health():
    try:
        db.command("ping")

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "not connected",
            "error": str(e)
        }