import os
import joblib

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

def predict_spam(text):

    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]

    proba = model.predict_proba(text_vec)[0]

    confidence = float(max(proba)) * 100

    return {
        "result": prediction,
        "confidence": round(confidence, 2)
    }