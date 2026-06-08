import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "random_forest.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)


def rf_predict(url):
    features = extract_lexical_features(url)
    feature_string = url + " " + " ".join(map(str, features))

    vector = vectorizer.transform([feature_string])
    result = rf_model.predict(vector)[0]

    return result == 1
