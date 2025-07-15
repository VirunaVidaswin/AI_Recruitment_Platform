from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client['travelmateai']

def save_document(doc, collection="job_descriptions"):
    db[collection].insert_one(doc)

def get_all_documents(collection="job_descriptions"):
    return list(db[collection].find({}))
