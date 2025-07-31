import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils import load_documents

model = SentenceTransformer("all-MiniLM-L6-v2")
docs = load_documents()
sentences = [line.strip() for doc in docs for line in doc.split(". ") if line.strip()]
embeddings = model.encode(sentences)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def get_top_chunks(question, k=5):
    q_vec = model.encode([question])
    _, I = index.search(q_vec, k)
    return " ".join([sentences[i] for i in I[0]])
