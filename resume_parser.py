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

    Return ONLY a valid JSON object with the following fields:
    
    - Title
    - Summary
    - Experience Level
    - Location
    - Employment Type
    - Responsibilities
    - Required Skills

    Text:
    {text}
    """
)

extract_chain = LLMChain(llm=llm, prompt=prompt)

def extract_info(text, type="job description"):
    return extract_chain.run(text=text, type=type)




"""

        You are an AI recruiter. Extract the following structured info from a {type}:

        

        Follow this Format
        JSON Format Example:
        ```json
        {
            "Title": "Title",
            "Summary": "Brief summary here.",
            "Experience Level": "Undergraduate",
            "Location": "City, Country",
            "Employment Type": "Internship"
            "Responsibilities": [
                "Responsibility 1",
                "Responsibility 2"
            ],
            "Required Skills": {
                "AI & ML Fundamentals": [
                "Supervised Learning",
                "NLP"
                ],
                "Technical Skills": [
                "Python", "Git"
                ],
                "Soft Skills": [
                "Teamwork", "Adaptability"
                ]
            }
        }
        Text:
        {text}
    """