from langchain_groq import ChatGroq
from tavily import TavilyClient

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


tavily = TavilyClient()

def verify_claim(claim):
    search_results = tavily.search(query=claim, max_results=5)

    context = "\n".join(
        [res["content"] for res in search_results["results"]]
    )

    prompt = f"""
Claim:
{claim}

Web Evidence:
{context}

Classify the claim as:
- Verified
- Inaccurate
- False

Explain briefly and cite sources.
"""

    verdict = llm.invoke(prompt).content
    return verdict, search_results["results"]
