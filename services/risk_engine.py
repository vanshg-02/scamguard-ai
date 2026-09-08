import re


def calculate_risk(text, ml_score):
    text_lower = text.lower()

    score = ml_score
    reasons = []

    # Urgency / pressure
    urgency_words = [
        "urgent",
        "immediately",
        "right now",
        "within 24 hours",
        "expires today",
        "act now",
    ]

    if any(word in text_lower for word in urgency_words):
        score += 15
        reasons.append("Creates urgency or pressure to act quickly")

    # Account threats
    account_threats = [
    "account blocked",
    "account will be blocked",
    "account suspended",
    "account will be suspended",
    "account will be closed",
    "bank account blocked",
    "bank account will be blocked",
    "kyc expired",
    "kyc update",
    "update your kyc",
    "verify your kyc",
]

    if any(phrase in text_lower for phrase in account_threats):
        score += 20
        reasons.append("Threatens account blocking or suspension")

    # OTP / credentials
    sensitive_requests = [
        "otp","verify your kyc",
"kyc",
        "one time password",
        "password",
        "pin",
        "cvv",
        "card details",
        "verify your account",
    ]

    if any(word in text_lower for word in sensitive_requests):
        score += 20
        reasons.append("Requests sensitive credentials or verification")

    # Payment / money
    payment_words = [
        "send money",
        "transfer money",
        "pay now",
        "payment required",
        "upi",
        "refund",
        "prize",
        "lottery",
    ]

    if any(word in text_lower for word in payment_words):
        score += 15
        reasons.append("Contains payment, money or prize-related language")

    # Suspicious links
    urls = re.findall(r"https?://\S+|www\.\S+", text_lower)

    if urls:
        score += 15
        reasons.append("Contains a link that should be verified before opening")

    # Cap score at 100
    score = min(round(score, 2), 100)

    # Risk level
    if score <= 30:
        level = "Low Risk"
    elif score <= 70:
        level = "Suspicious"
    else:
        level = "High Risk"

    return {
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons,
    }