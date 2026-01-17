from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Extract factual, verifiable claims from the text below.
Return each claim as a numbered list.

Text:
{text}
"""
)

def extract_claims(text):
    response = llm.invoke(prompt.format(text=text))
    claims = response.content.split("\n")
    return [c.strip() for c in claims if c.strip()]
