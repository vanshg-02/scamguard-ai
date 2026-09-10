import os
import httpx
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def save_scan(
    user_id,
    message,
    risk_score,
    risk_level,
    scam_type,
    reasons,
    access_token
):
    url = f"{SUPABASE_URL}/rest/v1/scan_history"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    data = {
        "user_id": user_id,
        "message": message,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "scam_type": scam_type,
        "reasons": reasons
    }

    response = httpx.post(
        url,
        headers=headers,
        json=data
    )

    if response.status_code >= 400:
        raise Exception(
            f"Supabase error {response.status_code}: "
            f"{response.text}"
        )

    return response.json()


def sign_up(email, password):
    return supabase.auth.sign_up({
        "email": email,
        "password": password
    })


def sign_in(email, password):
    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })