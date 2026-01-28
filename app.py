from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Google API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are friday. Very advanced AI assistant."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("Friday - Your Advanced AI Assistant")
input_text = st.text_input("Ask your question here")

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or gemini-1.5-pro
    temperature=0.7
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
