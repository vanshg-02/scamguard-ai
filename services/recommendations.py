def get_recommendations(risk_level, scam_type):
    recommendations = []

    # Instant safety advice
    recommendations.append(
        "Do not click links, share OTP/PIN/passwords, "
        "or send money until you verify the sender."
    )

    if risk_level == "High Risk":
        recommendations.extend([
            "Do not make any payment or UPI transfer.",
            "Do not share OTP, PIN, CVV, bank details or passwords.",
            "Verify the sender using the company's official website or phone number.",
            "Save the message, screenshot, URL and other evidence.",
            "If money has already been lost, contact your bank immediately and report it."
        ])

    elif risk_level == "Suspicious":
        recommendations.extend([
            "Verify the sender before taking any action.",
            "Do not share personal or financial information.",
            "Avoid clicking unknown links or downloading attachments.",
            "Do not make a payment under pressure or urgency."
        ])

    else:
        recommendations.extend([
            "The message appears relatively low risk, but stay cautious.",
            "Verify important requests through an official source.",
            "Avoid sharing sensitive information with unknown people."
        ])

    return recommendations