import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

from transformers import pipeline

# Load emotion detection model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None,
    device=-1
)

# Define the function that app.py expects
def detect_emotion(text):
    scores = emotion_classifier(text)[0]
    top_emotion = max(scores, key=lambda x: x['score'])
    return top_emotion['label'], round(top_emotion['score'], 2)
