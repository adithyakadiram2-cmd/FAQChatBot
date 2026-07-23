import json
import os
from preprocess import preprocess

BASE_DIR = os.path.dirname(__file__)

with open(
    os.path.join(BASE_DIR, "faq.json"),
    "r",
    encoding="utf-8"
) as f:
    FAQS = json.load(f)


def find_answer(user_question):

    user_question = preprocess(user_question)

    # Exact Match
    for faq in FAQS:

        if preprocess(faq["question"]) == user_question:
            return faq["answer"]

    # Keyword Match
    user_words = set(user_question.split())

    for faq in FAQS:

        faq_words = set(
            preprocess(
                faq["question"]
            ).split()
        )

        if user_words.intersection(faq_words):
            return faq["answer"]

    return (
        "Sorry, I could not find an answer."
    )
