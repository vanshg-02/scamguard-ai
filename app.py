import streamlit as st
from PIL import Image

from database.supabase_client import (
    sign_up,
    sign_in,
    save_scan,
    get_scan_history
)
from services.legal_info import get_reporting_info
from services.recommendations import get_recommendations
from services.ocr import extract_text_from_image
from ml.predict import predict_scam
from services.risk_engine import calculate_risk
from services.scam_classifier import classify_scam_type
from services.url_analyzer import analyze_urls


st.set_page_config(
    page_title="ScamGuard AI",
    page_icon="🛡️",
    layout="wide"
)
# -----------------------------
# Authentication
# -----------------------------

if "user" not in st.session_state:
    st.session_state.user = None

with st.sidebar:
    st.subheader("  Account")

    auth_mode = st.radio(
        "Choose",
        ["Login", "Signup"]
    )

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if auth_mode == "Signup":

        if st.button("Create Account"):

            if email and password:
                try:
                    response = sign_up(email, password)

                    if response.user:
                        st.success(
                            "Account created! "
                            "Check your email if confirmation is required."
                        )
                    else:
                        st.error("Signup failed.")

                except Exception as e:
                    st.error(str(e))

            else:
                st.warning(
                    "Please enter email and password."
                )

    else:

        if st.button("Login"):
            

            if email and password:
                
                try:
                    response = sign_in(email, password)
                    st.session_state.user = response.user
                    st.session_state.access_token = response.session.access_token
                    st.success("Login successful!")
                except Exception as e:
                        st.error(str(e))

            else:
                st.warning(
                    "Please enter email and password."
                )


# -----------------------------
# Session History
# -----------------------------

if "history" not in st.session_state:
    st.session_state.history = []


if st.session_state.user and st.session_state.access_token:
    try:
        db_history = get_scan_history(
            st.session_state.user.id,
            st.session_state.access_token
        )

        st.session_state.history = db_history

    except Exception as e:
        st.error(f"Could not load scan history: {e}")

# -----------------------------
# Functions
# -----------------------------

def analyze_message(text):

    result = predict_scam(text)

    final_result = calculate_risk(
        text,
        result["risk_score"]
    )

    scam_type = classify_scam_type(text)

    url_results = analyze_urls(text)

    return final_result, scam_type, url_results


def show_report(final_result, scam_type, url_results):

    st.subheader("🔍 Scam Detection Report")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Risk Score",
            f"{final_result['risk_score']}%"
        )

    with col2:
        st.metric(
            "Risk Level",
            final_result["risk_level"]
        )

    with col3:
        st.metric(
            "Scam Type",
            scam_type
        )
    st.subheader("🛡️ Recommended Actions")

    recommendations = get_recommendations(
        final_result["risk_level"],
        scam_type
    )

    for recommendation in recommendations:
        st.write("• " + recommendation)
    st.subheader("🚨 Take Action")

    reporting_info = get_reporting_info()

    st.write(
        "If you believe you have encountered a scam, "
        "you can report it through the official channels."
    )

    st.link_button(
        "🇮🇳 Report Cyber Crime",
        reporting_info["cybercrime_portal"]
    )

    st.info(
        "💰 If you have already lost money in a financial cyber fraud, "
        "call 1930 immediately."
    )

    if final_result["reasons"]:

        st.subheader("🚨 Why Flagged?")

        for reason in final_result["reasons"]:
            st.write("• " + reason)

    if url_results:

        st.subheader("🔗 URL Analysis")

        for url_info in url_results:

            st.write(f"**URL:** {url_info['url']}")
            st.write(f"**Domain:** {url_info['domain']}")

            if url_info["suspicious"]:

                st.error("⚠️ Suspicious URL")

                for reason in url_info["reasons"]:
                    st.write("• " + reason)

            else:

                st.success(
                    "No obvious URL red flags detected"
                )

    


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    

    st.subheader("  Scan History")

    if not st.session_state.history:

        st.caption("No scans yet.")

    else:

        for i, scan in enumerate(
            reversed(st.session_state.history),
            start=1
        ):

            st.write(
                f"**Scan {i}** — "
                f"{scan['risk_score']}%"
            )

            st.caption(
                f"{scan['risk_level']} • "
                f"{scan['scam_type']}"
            )

            st.divider()

    if st.session_state.history:

        if st.button("🗑️ Clear History"):

            st.session_state.history = []

            st.rerun()


# -----------------------------
# Main UI
# -----------------------------

st.title("🛡️ ScamGuard AI")

st.write(
    "AI-powered Scam Detection System"
)

st.divider()


text_input = st.text_area(
    "Paste suspicious message",
    height=150,
    placeholder=(
        "Paste SMS, WhatsApp message, "
        "email or suspicious text..."
    )
)


uploaded_image = st.file_uploader(
    "📸 Upload Screenshot",
    type=["png", "jpg", "jpeg"]
)


# -----------------------------
# Screenshot Analysis
# -----------------------------

if uploaded_image:

    image = Image.open(uploaded_image)

    extracted_text = extract_text_from_image(image)

    if extracted_text:

        final_result, scam_type, url_results = (
            analyze_message(extracted_text)
        )

        # Save history
        st.session_state.history.append({
            "risk_score": final_result["risk_score"],
            "risk_level": final_result["risk_level"],
            "scam_type": scam_type
        })
        if st.session_state.user:
            save_scan(
        st.session_state.user.id,
        extracted_text,
        final_result["risk_score"],
        final_result["risk_level"],
        scam_type,
        final_result["reasons"],
        st.session_state.access_token,
        
    )
        if st.session_state.user:
            save_scan(
        st.session_state.user.id,
        text_input,
        final_result["risk_score"],
        final_result["risk_level"],
        scam_type,
        final_result["reasons"],
        st.session_state.access_token
        
        
    )

        show_report(
            final_result,
            scam_type,
            url_results
        )

    else:

        st.error(
            "Could not extract readable text "
            "from this screenshot."
        )


# -----------------------------
# Text Analysis
# -----------------------------

if st.button(
    "🔍 Analyze Message",
    type="primary"
):

    if not text_input.strip():

        st.warning(
            "Please enter a message or "
            "upload a screenshot."
        )

    else:

        final_result, scam_type, url_results = (
            analyze_message(text_input)
        )

        # Save history
        st.session_state.history.append({
            "risk_score": final_result["risk_score"],
            "risk_level": final_result["risk_level"],
            "scam_type": scam_type
        })
        if st.session_state.user:
            try:
                save_scan(
            st.session_state.user.id,
            text_input,
            final_result["risk_score"],
            final_result["risk_level"],
            scam_type,
            final_result["reasons"],
            st.session_state.access_token
            
        )
                st.success("Scan saved to Supabase")
            except Exception as e:
                st.error(f"Supabase save error: {e}")

        show_report(
            final_result,
            scam_type,
            url_results
        )