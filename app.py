# app.py
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.claim_extractor import extract_claims
from utils.verifier import verify_claim

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Fact Checker",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Pink Theme CSS + Buttons
# -----------------------------
st.markdown(
    """
    <style>
    /* Body background */
    body {background-color: #ffe6f0;}
    /* Sidebar background */
    .css-1d391kg {background-color: #ffd6e8;}
    /* Headings color */
    h1, h2, h3, h4 {color: #4B0082;}
    /* Buttons color */
    .stButton>button {background-color:#ff99cc; color:white; font-weight:bold;}
    .stButton>button:hover {background-color:#ff66b2; color:white;}
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📤 Upload & Options")
uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])
check_button = st.sidebar.button("🔍 Check Facts")

st.sidebar.markdown("---")
st.sidebar.markdown("Assignment Demo: Fact-checking PDF claims using AI + live web data.")
st.sidebar.markdown("Made by Arpita")

# -----------------------------
# Main Page Header
# -----------------------------
st.title("📄 AI Fact-Checking Dashboard")
st.markdown(
    "Upload a PDF, extract factual claims, and verify them using **live web evidence**."
)

# -----------------------------
# Processing
# -----------------------------
if uploaded_file and check_button:
    with st.spinner("📄 Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🧠 Extracting factual claims..."):
        claims = extract_claims(text)

    if not claims:
        st.warning("No factual claims found in the uploaded PDF.")
    else:
        # Instruction text above claims (black color)
        st.markdown(
            "<h4 style='color:black;'>Here are the factual, verifiable claims extracted from the text:</h4>",
            unsafe_allow_html=True
        )

        # Loop over each claim and make a card
        for idx, claim in enumerate(claims, start=1):
            # Card container with pink background and black text
            st.markdown(
                f"""
                <div style="
                    background-color: #fff0f6;
                    color: black;
                    border-radius: 12px;
                    padding: 20px;
                    box-shadow: 2px 2px 12px #ffb6c1;
                    margin-bottom: 10px;
                ">
                    <h3 style='color:#4B0082;'>Claim {idx}</h3>
                    <p><b>{claim}</b></p>
                </div>
                """,
                unsafe_allow_html=True
            )

            with st.spinner("🔎 Verifying claim using live web..."):
                verdict, sources = verify_claim(claim)

            # Color-coded badge for verdict (black text)
            if "verified" in verdict.lower():
                st.markdown(
                    f"<span style='color:black; background-color:green; padding:5px 10px; border-radius:5px;'>{verdict}</span>",
                    unsafe_allow_html=True
                )
            elif "false" in verdict.lower():
                st.markdown(
                    f"<span style='color:black; background-color:red; padding:5px 10px; border-radius:5px;'>{verdict}</span>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<span style='color:black; background-color:orange; padding:5px 10px; border-radius:5px;'>{verdict}</span>",
                    unsafe_allow_html=True
                )

            # Expandable sources in card style
            if sources:
                with st.expander("📚 View Sources"):
                    for src in sources:
                        st.markdown(f"- **{src.get('title', 'Source')}** — {src.get('url', '')}")

            st.markdown("---")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    "<hr><p style='text-align:center;'>Made by Arpita | Streamlit AI Fact-Checker Demo</p>",
    unsafe_allow_html=True
)
