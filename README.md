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

## ⚙️ Installation

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

## Configuration
To generate 200 job descriptions run the following command:
```bash
python jd_Generator.py

```



