import os
import httpx
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

email = "vanshgupta80745@gmail.com"
password = "Vv@9876123"

response = supabase.auth.sign_in_with_password({
    "email": email,
    "password": password
})

access_token = response.session.access_token
user_id = response.user.id

print("LOGIN OK")
print("USER:", user_id)
print("TOKEN RECEIVED:", bool(access_token))

headers = {
    "apikey": key,
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}
check_role = httpx.post(
    f"{url}/rest/v1/rpc/check_auth_context",
    headers={
        "apikey": key,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
)

print("DB AUTH CONTEXT STATUS:", check_role.status_code)
print("DB AUTH CONTEXT:", check_role.text)

data = {
    "user_id": user_id,
    "message": "Direct REST test",
    "risk_score": 95.0,
    "risk_level": "High Risk",
    "scam_type": "Banking / KYC Scam",
    "reasons": ["Test"]
}

result = httpx.post(
    f"{url}/rest/v1/scan_history",
    headers=headers,
    json=data
)

print("STATUS:", result.status_code)
print("RESPONSE:", result.text)
# Check what role Supabase sees for this JWT
check = httpx.get(
    f"{url}/auth/v1/user",
    headers={
        "apikey": key,
        "Authorization": f"Bearer {access_token}"
    }
)

print("AUTH STATUS:", check.status_code)
print("AUTH USER:", check.text)