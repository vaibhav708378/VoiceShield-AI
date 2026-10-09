
MAX_CHUNK_SIZE = 5 * 1024 * 1024  # 5 MB


def process_audio_chunk(audio_data: bytes) -> dict:
    """Validate an incoming audio chunk before AI analysis."""

    if not audio_data:
        raise ValueError("Audio chunk is empty")

    if len(audio_data) > MAX_CHUNK_SIZE:
        raise ValueError("Audio chunk exceeds the 5 MB limit")

    return {
        "size": len(audio_data),
        "status": "validated",
        "ai_detection": "not_run",
    }
