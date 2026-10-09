
import { useRef, useState } from "react";

function AudioMonitor() {
  const [recording, setRecording] = useState(false);
  const [status, setStatus] = useState("Ready");
  const [chunksReceived, setChunksReceived] = useState(0);
  const [lastChunkSize, setLastChunkSize] = useState(0);

  const recorderRef = useRef(null);
  const streamRef = useRef(null);
  const socketRef = useRef(null);

  const startRecording = async () => {
    try {
      setStatus("Requesting microphone permission...");

      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });
      streamRef.current = stream;

      const socket = new WebSocket("ws://127.0.0.1:8000/ws/audio");
      socketRef.current = socket;

      socket.onopen = () => {
        const recorder = new MediaRecorder(stream);
        recorderRef.current = recorder;

        recorder.ondataavailable = (event) => {
          if (
            event.data.size > 0 &&
            socket.readyState === WebSocket.OPEN
          ) {
            socket.send(event.data);
          }
        };

        recorder.start(1000);
        setRecording(true);
        setStatus("Connected — monitoring microphone");
      };

      socket.onmessage = (event) => {
        const result = JSON.parse(event.data);

        if (result.status === "processed") {
          setChunksReceived((count) => count + 1);
          setLastChunkSize(result.size);
          setStatus("Connected — audio chunks processed");
        }
      };

      socket.onerror = () => {
        setStatus("WebSocket connection error");
      };

      socket.onclose = () => {
        setRecording(false);
        setStatus("Connection closed");
      };
    } catch (error) {
      console.error("Audio monitoring error:", error);
      setStatus("Could not access microphone or connect");
      stopRecording();
    }
  };

  const stopRecording = () => {
    if (recorderRef.current) {
      recorderRef.current.stop();
      recorderRef.current = null;
    }

    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
      streamRef.current = null;
    }

    if (socketRef.current) {
      socketRef.current.close();
      socketRef.current = null;
    }

    setRecording(false);
    setStatus("Monitoring stopped");
  };

  return (
    <section>
      <h2>Real-Time Voice Protection</h2>

      <p>
        <strong>Status:</strong> {status}
      </p>

      {!recording ? (
        <button onClick={startRecording}>
          Start Monitoring
        </button>
      ) : (
        <button onClick={stopRecording}>
          Stop Monitoring
        </button>
      )}

      <hr />

      <h3>Audio Stream</h3>
      <p>Processed chunks: {chunksReceived}</p>
      <p>Last chunk size: {lastChunkSize} bytes</p>

      <h3>Detection Results</h3>
      <p>Speaker verification: Not implemented yet</p>
      <p>Deepfake detection: Not implemented yet</p>
      <p>Scam detection: Not implemented yet</p>
      <p>Overall risk: Not evaluated yet</p>
    </section>
  );
}

export default AudioMonitor;
