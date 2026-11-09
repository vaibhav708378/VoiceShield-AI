VoiceShield AI
  VoiceShield AI is a development project exploring synthetic-voice
  detection, speaker verification, suspicious-speech analysis, and
  real-time audio monitoring.
  Current status: The candidate audio-classification model
  Vansh180/deepfake-audio-wav2vec2 has downloaded and loaded
  successfully. Its reported labels are real and fake. End-to-end
  inference with a valid WAV recording and model evaluation are still
  pending. Do not treat its scores as verified probabilities or proof
  that a voice is genuine or cloned.
---
## Project goals
- Detect possible synthetic or spoofed audio.
- Add consent-based speaker verification.
- Analyze speech for potentially suspicious or scam-related intent.
- Combine available signals into an explainable risk assessment.
- Provide a React dashboard for monitoring and safety guidance.
- Protect audio and speaker data through consent, limited retention,
  and secure handling.
These are project goals; not all capabilities are implemented or
validated.
Current AI model
- Model:
  Vansh180/deepfake-audio-wav2vec2
- Task: Audio classification
- Reported labels: real, fake
- Runtime: Hugging Face Transformers and PyTorch; CPU inference is
  configured.
The model loaded successfully in the development environment. A valid
audio file is still needed to test inference. The previous paths
D:\AudioTests\sample.wav and D:\VoiceShield-AI\my_voice.wav were
examples and did not exist.

The .pt files named deepfake_model.pt, liveness_model.pt, and
speaker_model.pt in the project checkpoints folders were found to be
0 bytes. They are empty placeholders, not trained model weights.
Technology stack
- Backend: Python, FastAPI, Uvicorn
- Frontend: React, Vite, JavaScript
- AI/audio: PyTorch, Transformers, SoundFile, NumPy
- Database: MongoDB
- Realtime transport: WebSocket
## Repository structure
The main working directory is D:\VoiceShield-AI.
VoiceShield-AI/
├── ai-engine/
│   ├── checkpoints/
│   ├── configs/
│   ├── datasets/
│   ├── features/
│   ├── inference/
│   │   ├── predict.py
│   │   └── test_deepfake_model.py
│   ├── models/
│   │   ├── deepfake_detector/
│   │   └── scam_detection/
│   ├── preprocessing/
│   ├── tests/
│   ├── training/
│   └── requirements.txt
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── database/
│   │   ├── realtime/
│   │   ├── routes/
│   │   └── services/
│   └── .env
├── frontend/
│   └── src/
├── realtime/
├── risk-engine/
├── security/
└── tests/
This is a high-level view; the exact repository contents may change.
## Prerequisites
- Windows 10/11 or another supported operating system
- Python 3.13 (current development environment)
- Node.js and npm
- MongoDB running locally or a valid MongoDB connection string
- Internet access for the first model download
Setup
1. Open the project
cd D:\VoiceShield-AI
2. Configure backend environment
Create or update backend\.env:
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=voiceshield_ai
SECRET_KEY=replace-with-a-long-random-secret
Keep .env private. Never commit credentials, tokens, or production
secrets.
3. Install AI dependencies
cd D:\VoiceShield-AI
python -m pip install -r .\ai-engine\requirements.txt
The AI requirements currently include:
transformers
safetensors
soundfile
numpy
PyTorch is also required. The current environment reported
torch 2.14.1+cpu. The local environment also needed tf-keras to
resolve a Transformers/Keras compatibility error.
4. Install backend dependencies
If backend\requirements.txt exists and is populated:
cd D:\VoiceShield-AI\backend
python -m pip install -r requirements.txt
If it is missing or empty, install the backend dependencies separately
before starting the server.
5. Install frontend dependencies
cd D:\VoiceShield-AI\frontend
npm install
Run the application
Run the backend and frontend in separate terminals.
## Backend
cd D:\VoiceShield-AI\backend
python -m uvicorn app.main:app --reload
- API: http://127.0.0.1:8000
- Swagger documentation: http://127.0.0.1:8000/docs
## Frontend
cd D:\VoiceShield-AI\frontend
npm run dev
- Vite development server: http://localhost:5173
The backend must be running for frontend API and WebSocket features to
work.
Test the model
Load the candidate model:
cd D:\VoiceShield-AI
python .\ai-engine\inference\test_deepfake_model.py
Run inference using the path to an actual supported audio file:
python .\ai-engine\inference\predict.py "D:\path\to\your\recording.wav"
Use a recording you own or have permission to analyze. If the supplied
path does not exist, inference cannot start.
## Interpreting model output
The real and fake scores are outputs from the selected model. They
are not automatically calibrated probabilities, proof of authenticity,
or proof of fraud. Evaluate the model using labeled genuine and
synthetic recordings and measure false positives and false negatives
before relying on it.
## Current limitations
- Model loading succeeded, but inference with a valid WAV file has not
  yet been confirmed.
- The candidate model has not been independently evaluated for this
  project's intended use.
- Speaker verification is a separate task and is not provided by the
  current real/fake classifier.
- Scam-intent analysis is separate and needs its own model and
  evaluation.
- Empty .pt checkpoint files cannot be used as trained models.
- Browser microphone capture is not the same as intercepting or
  monitoring ordinary phone calls.
- The application should show an explicit unavailable/unknown state
  when a model is unavailable, audio is invalid, or analysis has not
  run. It must not invent a genuine/fake verdict.
## Privacy and security
- Obtain informed consent before recording or analyzing a person's
  voice.
- Avoid storing raw audio unless necessary and explicitly authorized.
- Protect authentication tokens, database credentials, and speaker
  embeddings.
- Define retention and deletion behavior for stored data.
- Restrict access to recordings and analysis results.
- Treat model output as an aid for review, not a final accusation or
  decision.
## Development roadmap
1. Test inference with known, labeled WAV samples.
2. Build an evaluation set and measure precision, recall,
   false-positive rate, and false-negative rate.
3. Integrate validated inference into the FastAPI audio-processing
   service.
4. Connect WebSocket audio streaming to the backend pipeline with input
   validation and size limits.
5. Implement speaker enrollment and verification as a separate,
   consent-based feature.
6. Add scam-intent analysis as a separate component.
7. Combine available results in an explainable risk engine with an
   explicit unknown/unavailable state.
8. Add dashboard status, warnings, and privacy controls.
9. Perform security, privacy, latency, and robustness testing before
   deployment.
## Contributing
- Work in the outer project directory D:\VoiceShield-AI, not the
  nested duplicate, unless the repository layout is intentionally
  changed.
- Keep secrets and private recordings out of version control.
- Add tests for new services and model integrations.
- Document model source, license, preprocessing, expected input
  format, and evaluation results.
- Do not claim a capability is complete until it has been tested and
  evaluated.
## Disclaimer
VoiceShield AI is a development project. Audio classification can be
wrong, and performance can vary across speakers, languages, devices, and
recording conditions. Do not use an unvalidated result as the sole basis
for financial, legal, employment, or other high-impact decisions.

## 🚧Under Development

