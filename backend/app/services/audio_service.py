def process_audio_chunk(audio_data: bytes):
    """
    Process one incoming audio chunk.

    For now, this function only analyzes the
    basic properties of the received audio.
    AI detection will be added later.
    """

    return {
        "size": len(audio_data),
        "status": "processed"
    }