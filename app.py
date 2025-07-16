import streamlit as st
import pdfplumber
import pandas as pd
from fpdf import FPDF
import tempfile
import json

from resume_parser import extract_info
from RAG import get_recommendations
from mongo_Db import save_document

st.set_page_config(page_title="AI Recruitment Platform", layout="centered")
st.title("🤖 AI-Powered Recruitment Platform")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

recommendations = []

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    st.subheader("📋 Resume Text Preview")
    st.text_area("Extracted Text", text[:1988], height=200)

    with st.expander("🧠 Extracted Data from Resume (Click to Expand)"):
        st.subheader("🧠 Extracted Data from Resume Saved to Database")
        resume_data_raw = extract_info(text, type="resume")
        resume_data = json.loads(resume_data_raw)
        st.json(resume_data)


    save_document({"type": "resume", "data": resume_data}, collection="resumes")

    st.subheader("🎯 Recommended Job Descriptions")
    recommendations = get_recommendations(query_text=str(resume_data))
    for i, r in enumerate(recommendations):
        try:
            job = json.loads(r.page_content)
        except json.JSONDecodeError:
            st.error(f"❌ Failed to parse match #{i+1}")
            continue
        
        with st.expander(f"🎯 Match #{i+1}: {job.get('Title', 'Unknown')} - {job.get('Location', '')}"):
            st.markdown(f"**📌 Title:** {job.get('Title')}")
            st.markdown(f"**📝 Summary:** {job.get('Summary')}")
            st.markdown(f"**🏢 Location:** {job.get('Location')}")
            st.markdown(f"**💼 Experience Level:** {job.get('Experience Level')}")
            st.markdown(f"**💼 Employment Type:** {job.get('Employment Type')}")

            st.markdown("**🧪 Responsibilities:**")
            for task in job.get("Responsibilities", []):
                st.markdown(f"- {task}")

            st.markdown("**🛠 Required Skills:**")
            for skill in job.get("Required Skills", []):
                st.markdown(f"- {skill}")

# ---------- Download Section (only if there are results) ----------
if recommendations:
    def format_jd_text(text):
        """Convert raw JSON JD to readable format for display."""
        try:
            jd = json.loads(text)
        except:
            jd = {"Job Description": text}
        return jd

    def convert_to_csv(results):
        jds = [format_jd_text(r.page_content) for r in results]
        df = pd.DataFrame(jds)
        return df.to_csv(index=False).encode("utf-8")

    def convert_to_pdf(results):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for i, res in enumerate(results):
            jd = format_jd_text(res.page_content)
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(0, 10, f"Match #{i+1}", ln=True)
            pdf.set_font("Arial", size=12)
            for key, value in jd.items():
                content = value if isinstance(value, str) else ', '.join(value)
                pdf.multi_cell(0, 10, f"{key}: {content}")
            pdf.ln(5)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            pdf.output(tmpfile.name)
            return tmpfile.name

    st.subheader("📥 Download Results")

    # CSV Download
    csv_file = convert_to_csv(recommendations)
    st.download_button("⬇️ Download as CSV", csv_file, file_name="job_matches.csv", mime="text/csv")

    # PDF Download
    pdf_path = convert_to_pdf(recommendations)
    with open(pdf_path, "rb") as f:
        st.download_button("⬇️ Download as PDF", f, file_name="job_matches.pdf", mime="application/pdf")




