import { useRef, useState } from "react";

function AudioMonitor() {
  const [recording, setRecording] = useState(false);
  const [message, setMessage] = useState("Ready to monitor");
  const [chunksReceived, setChunksReceived] = useState(0);

  const mediaRecorderRef = useRef(null);
  const streamRef = useRef(null);
  const websocketRef = useRef(null);

  const startRecording = async () => {
    try {
      // Request microphone permission
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });

      streamRef.current = stream;

      // Connect to FastAPI WebSocket
      const websocket = new WebSocket(
        "ws://127.0.0.1:8000/ws/audio"
      );

      websocketRef.current = websocket;

      websocket.onopen = () => {
        console.log("WebSocket connected");

        setMessage("🎙️ Monitoring microphone...");
        setRecording(true);

        const mediaRecorder = new MediaRecorder(stream);

        mediaRecorderRef.current = mediaRecorder;

        // Send audio chunks to backend
        mediaRecorder.ondataavailable = (event) => {
          if (
            event.data.size > 0 &&
            websocket.readyState === WebSocket.OPEN
          ) {
            websocket.send(event.data);
          }
        };

        // Create an audio chunk every 1 second
        mediaRecorder.start(1000);
      };

      websocket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        console.log("Backend:", data);

        if (data.status === "received") {
          setChunksReceived((previous) => previous + 1);
        }
      };

      websocket.onerror = (error) => {
        console.error("WebSocket error:", error);
        setMessage("WebSocket connection failed.");
      };

      websocket.onclose = () => {
        console.log("WebSocket disconnected");
      };

    } catch (error) {
      console.error(error);
      setMessage(
        "Microphone permission was denied or unavailable."
      );
    }
  };

  const stopRecording = () => {
    // Stop MediaRecorder
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      mediaRecorderRef.current = null;
    }

    // Stop microphone
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => {
        track.stop();
      });

      streamRef.current = null;
    }

    // Close WebSocket
    if (websocketRef.current) {
      websocketRef.current.close();
      websocketRef.current = null;
    }

    setRecording(false);
    setMessage("Monitoring stopped.");
  };

  return (
    <div>
      <h1>VoiceShield AI</h1>

      <h2>Real-Time Voice Protection</h2>

      <p>{message}</p>

      {!recording ? (
        <button onClick={startRecording}>
          🎙️ Start Monitoring
        </button>
      ) : (
        <button onClick={stopRecording}>
          ⏹️ Stop Monitoring
        </button>
      )}

      <hr />

      <h3>Real-Time Connection</h3>

      <p>
        Audio Chunks Sent:
        {" "}
        {chunksReceived}
      </p>

      <h3>Detection Status</h3>

      <p>Speaker Match: Not analyzed</p>
      <p>Deepfake Risk: Not analyzed</p>
      <p>Scam Risk: Not analyzed</p>
      <p>Overall Risk: Not analyzed</p>
    </div>
  );
}

export default AudioMonitor;