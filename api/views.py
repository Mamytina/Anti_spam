import os
import joblib
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

@csrf_exempt
def predict(request):
    if request.method == "POST":

        data = json.loads(request.body)
        text = data.get("text", "")

        # transformation texte → vecteur
        text_vec = vectorizer.transform([text])

        # prédiction
        prediction = model.predict(text_vec)[0]

        # score de confiance (proba)
        proba = model.predict_proba(text_vec)[0]

        spam_score = float(max(proba))  # confiance max

        return JsonResponse({
            "text": text,
            "result": prediction,
            "confidence": round(spam_score * 100, 2)
        })

    return JsonResponse({"error": "POST only"})

def home(request):
    return render(request, "index.html")