from fastapi import FastAPI

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
    return {
        "status": "healthy"
    }