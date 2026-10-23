import torch
from transformers import pipeline

MODEL_ID = "Vansh180/deepfake-audio-wav2vec2"

print("PyTorch:", torch.__version__)
print("Loading model:", MODEL_ID)
print("The first download may take several minutes.")

try:
    detector = pipeline(
        "audio-classification",
        model=MODEL_ID,
        device=-1,
    )

    print("\nModel loaded successfully.")
    print("Labels:", detector.model.config.id2label)
    print("Model test setup: READY")

except Exception as exc:
    print("\nMODEL LOAD FAILED")
    print(type(exc).__name__ + ":", exc)
