import re
from urllib.parse import urlparse


def analyze_urls(text):
    urls = re.findall(r"https?://\S+|www\.\S+", text)

    results = []

    for url in urls:
        if url.startswith("www."):
            check_url = "http://" + url
        else:
            check_url = url

        parsed = urlparse(check_url)
        domain = parsed.netloc.lower()

        suspicious = False
        reasons = []

        # IP address instead of normal domain
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain):
            suspicious = True
            reasons.append("URL uses an IP address instead of a normal domain")

        # URL contains suspicious keywords
        suspicious_words = [
            "verify",
            "login",
            "update",
            "secure",
            "account",
            "kyc",
            "payment",
            "claim",
        ]

        if any(word in url.lower() for word in suspicious_words):
            suspicious = True
            reasons.append("URL contains suspicious action-related keywords")

        # Very long URL
        if len(url) > 100:
            suspicious = True
            reasons.append("URL is unusually long")

        results.append({
            "url": url,
            "domain": domain,
            "suspicious": suspicious,
            "reasons": reasons
        })

    return results