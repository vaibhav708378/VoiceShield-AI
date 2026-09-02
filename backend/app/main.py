from fastapi import FastAPI
from app.database.mongodb import db

app = FastAPI(
    title="VoiceShield AI API",
    description="AI-powered voice deepfake and scam detection system",
    version="1.0.0"
)


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