import { useRef, useState } from "react";

function AudioMonitor() {
  const [recording, setRecording] = useState(false);
  const [message, setMessage] = useState("Ready to monitor");
  const mediaRecorderRef = useRef(null);
  const streamRef = useRef(null);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });

      streamRef.current = stream;

      const mediaRecorder = new MediaRecorder(stream);

      mediaRecorderRef.current = mediaRecorder;

      mediaRecorder.start();

      setRecording(true);
      setMessage("🎙️ Monitoring microphone...");
    } catch (error) {
      console.error(error);
      setMessage("Microphone permission was denied.");
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
    }

    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => {
        track.stop();
      });
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

      <h3>Detection Status</h3>

      <p>Speaker Match: Not analyzed</p>
      <p>Deepfake Risk: Not analyzed</p>
      <p>Scam Risk: Not analyzed</p>
      <p>Overall Risk: Not analyzed</p>
    </div>
  );
}

export default AudioMonitor;