import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai.predictor import predict_spam
from django.shortcuts import render
@csrf_exempt
def predict(request):

    if request.method == "POST":

        data = json.loads(request.body)
        text = data.get("text", "")

        result = predict_spam(text)

        return JsonResponse({
            "text": text,
            "result": result["result"],
            "confidence": result["confidence"]
        })

    return JsonResponse({"error": "POST only"})

def home(request):
    return render(request, "index.html")