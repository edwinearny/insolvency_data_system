import re

from spellchecker import SpellChecker
from nltk.corpus import stopwords
import nltk

# ============================================
# Setup (runs once)
# ============================================
nltk.download("stopwords", quiet=True)

spell = SpellChecker()
stop_words = set(stopwords.words("english"))


# ============================================
# Functions
# ============================================

def correct_spelling(query):
    """Fix spelling mistakes in the query"""
    words = query.split()
    corrected = []
    for word in words:
        # Skip short words (2 letters or less) and words with punctuation
        if len(word) <= 2 or not word.isalpha():
            corrected.append(word)
        else:
            correction = spell.correction(word)
            if correction:
                corrected.append(correction)
            else:
                corrected.append(word)
    return " ".join(corrected)


def remove_stop_words(query):
    """Remove common words that don't help search"""
    words = query.lower().split()
    filtered = [word for word in words if word not in stop_words]
    return " ".join(filtered)


def clean_punctuation(query):
    """Remove punctuation from query"""
    return re.sub(r'[^\w\s]', '', query)


def enhance_query(query):
    """Full pipeline: correct spelling → remove stop words"""
    cleaned = clean_punctuation(query)
    corrected = correct_spelling(cleaned)
    cleaned = remove_stop_words(corrected)
    return cleaned
