# Spam Detector AI (Django + Machine Learning)

## 📌 Description

Ce projet est une application web de détection de spam SMS/email utilisant **Django** et le **Machine Learning**.

Le modèle est entraîné avec :
- TF-IDF (transformation du texte)
- Logistic Regression (classification)

---

# Fonctionnalités

- Détection de spam / non spam
- API REST avec Django
- Score de confiance (%)
- Interface web simple (HTML + JavaScript)
- Architecture modulaire (IA séparée du backend)

---

# Technologies utilisées

- Python
- Django
- scikit-learn
- pandas
- joblib
- HTML / CSS / JavaScript
- Docker (optionnel)

---

# Structure du projet
Anti_spam/
│
├── api/
│ ├── ai/
│ │ ├── predictor.py
│ │ ├── model.pkl
│ │ ├── vectorizer.pkl
│ ├── views.py
│ ├── urls.py
│ ├── dataset.csv
│ ├── templates/
│
├── manage.py
├── Dockerfile
├── requirements.txt
├── README.md

# Comment fonctionne l’IA

1. Le texte est transformé avec **TF-IDF**
2. Le modèle **Logistic Regression** analyse le texte
3. Il prédit :
   - spam
   - ou ham (non spam)
4. Un score de confiance est calculé

---

# API Endpoint

## POST `/api/predict/`

### Exemple requête :

```json
{
  "text": "Gagnez 1 million maintenant !!!"
}

}
Réponse :
{
  "text": "Gagnez 1 million maintenant !!!",
  "result": "spam",
  "confidence": 92.5
}

