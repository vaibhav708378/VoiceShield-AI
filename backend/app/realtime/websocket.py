from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.services.audio_service import process_audio_chunk


router = APIRouter()


@router.websocket("/ws/audio")
async def audio_websocket(websocket: WebSocket):

    await websocket.accept()

    print("🎙️ Audio WebSocket connected")

    try:

        while True:

            # Receive audio from frontend
            audio_data = await websocket.receive_bytes()

            print(
                f"Received audio chunk: {len(audio_data)} bytes"
            )

            # Process audio chunk
            result = process_audio_chunk(audio_data)

            # Send processing result back to frontend
            await websocket.send_json({
                "status": "processed",
                "message": "Audio chunk processed successfully",
                "size": result["size"]
            })

    except WebSocketDisconnect:

        print("🔌 Audio WebSocket disconnected")