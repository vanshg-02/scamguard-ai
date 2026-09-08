def classify_scam_type(text):
    text = text.lower()

    if any(word in text for word in [
        "kyc", "bank account", "bank", "account blocked",
        "account suspended", "credit card", "debit card"
    ]):
        return "Banking / KYC Scam"

    if any(word in text for word in [
        "upi", "payment", "transfer money", "send money",
        "pay now", "transaction"
    ]):
        return "UPI / Payment Scam"

    if any(word in text for word in [
        "job", "salary", "work from home", "vacancy",
        "interview", "hiring"
    ]):
        return "Job Scam"

    if any(word in text for word in [
        "lottery", "prize", "winner", "cash reward"
    ]):
        return "Lottery / Prize Scam"

    if any(word in text for word in [
        "courier", "parcel", "delivery", "package"
    ]):
        return "Courier / Delivery Scam"

    if any(word in text for word in [
        "investment", "trading", "crypto", "profit",
        "returns", "double your money"
    ]):
        return "Investment Scam"

    if any(word in text for word in [
        "loan", "instant loan", "personal loan"
    ]):
        return "Loan Scam"

    if any(word in text for word in [
        "click this link", "verify your account",
        "login", "password", "otp"
    ]):
        return "Phishing Scam"

    return "General Spam / Suspicious Message"