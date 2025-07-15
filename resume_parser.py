from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0.4, model="gpt-4")

prompt = PromptTemplate(
    input_variables=["text", "type"],
    template="""
    You are an AI recruiter. Extract the following structured info from a {type}:
    - Title
    - Summary
    - Responsibilities (as bullet points)
    - Required Skills
    - Experience Level
    - Location
    - Employment Type

    Text:
    {text}
    """
)

extract_chain = LLMChain(llm=llm, prompt=prompt)

def extract_info(text, type="job description"):
    return extract_chain.run(text=text, type=type)
