import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import joblib
from services.scam_classifier import classify_scam_type
from services.risk_engine import calculate_risk
from services.url_analyzer import analyze_urls

# Load trained model and vectorizer
model = joblib.load("models/scam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_scam(text):
    # Convert text into TF-IDF features
    text_tfidf = vectorizer.transform([text])

    # Prediction
    prediction = model.predict(text_tfidf)[0]

    # Probability
    probabilities = model.predict_proba(text_tfidf)[0]
    risk_score = probabilities[1] * 100

    if prediction == 1:
        label = "SCAM / SPAM"
    else:
        label = "LEGITIMATE"

    return {
        "label": label,
        "risk_score": round(risk_score, 2)
    }


# Test
if __name__ == "__main__":
    message = input("Enter a message: ")

    result = predict_scam(message)

    final_result = calculate_risk(
        message,
        result["risk_score"]
    )

    scam_type = classify_scam_type(message)

    url_results = analyze_urls(message)

    print("\nResult")
    print("------")
    print(f"Risk Score: {final_result['risk_score']}%")
    print(f"Risk Level: {final_result['risk_level']}")
    print(f"Scam Type: {scam_type}")

    if final_result["reasons"]:
        print("\nWhy flagged:")
        for reason in final_result["reasons"]:
            print(f"- {reason}")

    if url_results:
        print("\nURL Analysis:")
        for url_info in url_results:
            print(f"URL: {url_info['url']}")
            print(f"Domain: {url_info['domain']}")

            if url_info["suspicious"]:
                print("Status: Suspicious")
                for reason in url_info["reasons"]:
                    print(f"- {reason}")
            else:
                print("Status: No obvious URL red flags detected")