import json
import math
from collections import Counter

from preprocess import preprocess_text


# Load FAQs
with open("faq.json", "r", encoding="utf-8") as file:
    data = json.load(file)

faqs = data["faqs"]


def text_to_vector(text):
    words = text.split()
    return Counter(words)


def cosine_similarity(text1, text2):

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    intersection = set(vector1.keys()) & set(vector2.keys())

    numerator = sum(
        vector1[word] * vector2[word]
        for word in intersection
    )

    sum1 = sum(value ** 2 for value in vector1.values())
    sum2 = sum(value ** 2 for value in vector2.values())

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator == 0:
        return 0

    return float(numerator) / denominator


def get_best_match(user_question):

    processed_user = " ".join(
        preprocess_text(user_question)
    ).lower()

    best_score = 0
    best_answer = None

    # Exact Question Match
    for faq in faqs:

        question = faq["question"].lower()

        if user_question.lower() == question:

            return faq["answer"]

    # Keyword Match
    for faq in faqs:

        if "keywords" in faq:

            for keyword in faq["keywords"]:

                if keyword.lower() in user_question.lower():

                    return faq["answer"]

    # Cosine Similarity Match
    for faq in faqs:

        processed_faq = " ".join(
            preprocess_text(
                faq["question"]
            )
        ).lower()

        score = cosine_similarity(
            processed_user,
            processed_faq
        )

        if score > best_score:

            best_score = score
            best_answer = faq["answer"]

    # Confidence Threshold
    if best_score >= 0.20:

        return best_answer

    return (
        "Sorry, I couldn't find an "
        "appropriate answer. "
        "Please ask another question."
    )
