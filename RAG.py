from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from mongo_Db import get_all_documents
import json

embedding = OpenAIEmbeddings()

def build_faiss_index():
    jds = get_all_documents()
    texts = [json.dumps(doc["data"]) for doc in jds]
    documents = [Document(page_content=text) for text in texts]
    return FAISS.from_documents(documents, embedding)

def get_recommendations(query_text, k=3):
    index = build_faiss_index()
    return index.similarity_search(query_text, k=k)
