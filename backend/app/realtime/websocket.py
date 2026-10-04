from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()


@router.websocket("/ws/audio")
async def audio_websocket(websocket: WebSocket):

    await websocket.accept()

    print("🎙️ Audio WebSocket connected")

    try:

        while True:

            audio_data = await websocket.receive_bytes()

            print(
                f"Received audio chunk: {len(audio_data)} bytes"
            )

            await websocket.send_json({
                "status": "received",
                "message": "Audio chunk received successfully",
                "size": len(audio_data)
            })

    except WebSocketDisconnect:

        print("🔌 Audio WebSocket disconnected")