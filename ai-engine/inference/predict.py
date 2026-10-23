
import sys
from pathlib import Path
from transformers import pipeline

MODEL_ID = "Vansh180/deepfake-audio-wav2vec2"


def predict_audio(audio_path: str) -> None:
    path = Path(audio_path)

    if not path.is_file():
        print(f"ERROR: Audio file not found: {path}")
        return

    print(f"Loading audio: {path}")
    detector = pipeline(
        "audio-classification",
        model=MODEL_ID,
        device=-1,
    )

    try:
        results = detector(str(path), top_k=None)

        print("\nModel output (not yet validated):")
        for result in results:
            print(
                f"Label: {result['label']}, "
                f"Score: {result['score']:.4f}"
            )

        print(
            "\nNote: scores are model outputs, not verified "
            "probabilities of fraud or voice cloning."
        )

    except Exception as exc:
        print(f"Audio inference failed: {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            'Usage: python predict.py "D:\\path\\to\\audio.wav"'
        )
        raise SystemExit(1)

    predict_audio(sys.argv[1])
