import os
import random
from resume_parser import extract_info
from mongo_Db import save_document
from dotenv import load_dotenv
import time
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Role categories and examples
job_roles = {
    "Software Engineering": ["Frontend Developer", "Backend Developer", "Full-Stack Developer"],
    "Data Science": ["Data Scientist", "Data Analyst", "Database Administrator"],
    "DevOps": ["DevOps Engineer", "Site Reliability Engineer", "Cloud Specialist"],
    "Machine Learning": ["ML Engineer", "AI Researcher", "NLP Specialist"],
    "Quality Assurance": ["QA Engineer", "Test Automation Specialist", "QA Manager"],
    "Project Management": ["Project Manager", "Scrum Master", "Product Owner"],
    "Business Analytics": ["Business Analyst", "BI Specialist", "Data Visualization Expert"]
}

def generate_jd(role, category):
    system_prompt = f"You are an HR recruiter. Write a realistic job description for the role of a {role} in the field of {category}. Include title, summary, responsibilities, required skills, experience, location, and employment type."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You generate professional job descriptions."},
            {"role": "user", "content": system_prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def main():
    total_jds = 0
    for category, roles in job_roles.items():
        for role in roles:
            for i in range(10):  # 10 JDs per role x 20 = 200
                try:
                    print(f"Generating JD for: {role}")
                    jd_text = generate_jd(role, category)
                    
                    # Parse using LangChain
                    structured_data = extract_info(jd_text, type="job description")
                    
                    # Save to MongoDB
                    save_document({
                        "category": category,
                        "role": role,
                        "text": jd_text,
                        "data": structured_data
                    }, collection="job_descriptions")
                    
                    total_jds += 1
                    print(f" Saved JD #{total_jds}")
                    time.sleep(2)  # Avoid hitting rate limits
                except Exception as e:
                    print(f"❌ Error for {role}: {e}")
    print(f" Finished generating {total_jds} job descriptions.")

if __name__ == "__main__":
    main()
