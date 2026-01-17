📰 AI Fact-Checking Web App

An AI-powered web application that extracts factual claims from PDF documents and verifies them using live web evidence and large language models (LLMs).

🚀 Features

Upload PDF files

Extract factual, verifiable claims

Verify claims using live web search

Classify claims as Verified / Inaccurate / False

Display supporting sources

Clean Streamlit UI

🛠️ Tech Stack

Streamlit

Python

LangChain

Groq (LLM)

Tavily Search API

pdfplumber

🔑 API Keys Required

GROQ_API_KEY

TAVILY_API_KEY

(Stored securely using .env locally or Streamlit Secrets for deployment)

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

🌐 Deployment

Deployed using Streamlit Cloud with secrets managed via TOML configuration.

👩‍💻 Author

Arpita
B.Tech | AI / ML
