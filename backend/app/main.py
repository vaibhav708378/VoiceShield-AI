from fastapi import FastAPI
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuth2 as OAuth2Model

from app.database.mongodb import db
from app.api.routes.auth import router as auth_router


app = FastAPI(
    title="VoiceShield AI API",
    description="AI-powered voice deepfake and scam detection system",
    version="1.0.0"
)

app.include_router(auth_router)


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