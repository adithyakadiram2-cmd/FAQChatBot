import string

# Common words to ignore
STOP_WORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "how",
    "who",
    "where",
    "when",
    "of",
    "to",
    "and",
    "in",
    "for"
}


def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")

    # Split into words
    words = text.split()

    # Remove common words
    words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    return words

