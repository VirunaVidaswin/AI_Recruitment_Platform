# 🤖 AI_Recruitment_Platform

An end-to-end **AI-powered recruitment assistant** that uses **LLMs + RAG** to analyze resumes and job descriptions, find the best job matches, and provide intelligent recommendations via an interactive **Streamlit web interface**.

---

## 📘 Overview

**AI_Recruitment_Platform** leverages **LangChain**, **OpenAI LLMs**, **FAISS (RAG)**, and **MongoDB** to:
- Automatically generate and parse job descriptions
- Ingest and analyze uploaded resumes
- Retrieve the most relevant job roles using semantic similarity (RAG)
- Display personalized job recommendations via a web UI

It’s designed to streamline hiring workflows and match candidates to suitable roles based on their skills and experience.

---

## 🧠 Tech Stack

| Layer              | Technology           |
|-------------------|----------------------|
| LLM                | OpenAI GPT-4         |
| Embeddings         | OpenAI Embeddings    |
| Framework          | LangChain            |
| Vector DB (RAG)    | FAISS                |
| Document Store     | MongoDB              |
| Interface          | Streamlit            |

---

## ⚙️ Installation on local Machine

### 🚀 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/AI_Recruitment_Platform.git
   cd AI_Recruitment_Platform


2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows use `source venv/bin/activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Enviornment Variables**
To use external APIs (e.g., OpenAI), create a `.env` file in the project root and add your API key:
    ```env
    OPENAI_API_KEY=your_api_key_here
    MONGO_URI=your_mongodb_connection_uri
    ```
## Usage
To launch the app, run the following command:
```bash
streamlit run app.py

```
This will start a local server and will be given in terminal.

## Streamlit Cloud App
Follow the provided link and upload a pdf of a cv to proceed with the app.

https://ai-platform-app.streamlit.app/

---
## Work FLow

```
AI_Recruitment_Platform/
│
├── app.py                  ← Main Streamlit application
├── resume_parser.py        ← LangChain LLM pipeline to extract structured info
├── RAG.py                  ← Vector-based retrieval and job recommendation logic
├── mongo_Db.py             ← MongoDB connection and document saving utility
├── .env                    ← Stores API keys securely
├── requirements.txt        ← List of dependencies
└── README.md               ← Documentation and explanation
---
---
## Visual Representation

1. **Uploading a CV into the app**
   
![Uploading the PDF CV](Screenshot%20Evidence/1.%20Uploading%20the%20pdf%20cv.PNG)

---


2. **Information extracted from the uploaded File**

   
![Details Extracted](https://github.com/VirunaVidaswin/AI_Recruitment_Platform/blob/1765ebd585da8364fcd044c74ff614c708f397a1/Screenshot%20Evidence/2.%20After%20Cv%20uploaded%20Details%20extracted%20and%20saved%20to%20database.PNG)


---


3. **Displaying Recommendations using RAG**

   
![Displaying Recommendations ](https://github.com/VirunaVidaswin/AI_Recruitment_Platform/blob/1765ebd585da8364fcd044c74ff614c708f397a1/Screenshot%20Evidence/3.%20Reccomendtaions%20are%20displayed%20as%20dropdown%20boxers.PNG)


---

4. **Downloadable Jobs via PDF/CSV**

   
![Downloading jobs](https://github.com/VirunaVidaswin/AI_Recruitment_Platform/blob/1765ebd585da8364fcd044c74ff614c708f397a1/Screenshot%20Evidence/4.%20PDF%20or%20Csv%20file%20downloadable.PNG)
