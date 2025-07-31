from fastapi import FastAPI, Request, Header, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from retriever import get_top_chunks
from qa_engine import generate_answer
from utils import load_documents
import os

app = FastAPI()

# Secure Header Dependency
security = HTTPBearer()

class QARequest(BaseModel):
    documents: str
    questions: list[str]

@app.post("/hackrx/run")
async def run_query(
    payload: QARequest,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    if token != "30e2ac1ded555d8d9430e4c85e5838077d2902c5aa37ca57c7563c4d2463619a":
        raise HTTPException(status_code=401, detail="Invalid token")

    responses = []
    for question in payload.questions:
        context = get_top_chunks(question)
        answer = generate_answer(question, context)
        responses.append(answer)

    return {"answers": responses}
