from fastapi import FastAPI
from pydantic import BaseModel
from matcher import find_answer

app = FastAPI(
    title="FAQChatBot",
    version="2.0",
    description="Business FAQ Chatbot API"
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to FAQChatBot API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "project": "FAQChatBot",
        "version": "2.0"
    }


@app.post("/chat")
def chat(q: Question):

    answer = find_answer(q.question)

    return {
        "question": q.question,
        "answer": answer
    }
