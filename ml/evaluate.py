import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# Load dataset
df = pd.read_csv("data/processed/processed_sms.csv")

X = df["clean_text"].fillna("").astype(str)
y = df["label"]


# Same split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Load trained model and vectorizer
model = joblib.load("models/scam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


# Transform test data
X_test_tfidf = vectorizer.transform(X_test)

# Predictions
predictions = model.predict(X_test_tfidf)


# Metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("Model Evaluation")
print("----------------")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))