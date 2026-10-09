
def analyze_audio(audio_data: bytes) -> dict:
    """
    Prepare a structured result for audio analysis.

    Actual deepfake and speaker detection will be
    integrated after the AI model interface is connected.
    """

    if not audio_data:
        return {
            "status": "invalid",
            "deepfake_risk": None,
            "speaker_match": None,
            "scam_risk": None,
            "message": "No audio data received",
        }

    return {
        "status": "pending",
        "deepfake_risk": None,
        "speaker_match": None,
        "scam_risk": None,
        "message": "Audio received; AI models are not connected yet",
    }
