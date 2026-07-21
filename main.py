from fastapi import FastAPI
from pydantic import BaseModel
from matcher import get_best_match
from datetime import datetime

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "FAQ ChatBot API is running successfully."
    }


@app.post("/chat")
def chat(data: Question):

    question = data.question.strip()

    # greetings

    if question.lower() in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]:

        return "Hello! How can I help you today?"


    # date

    if question.lower() == "date":

        return str(datetime.now().date())


    # time

    if question.lower() == "time":

        return str(datetime.now().strftime("%H:%M:%S"))


    # chatbot answer

    answer = get_best_match(question)

    return answer
