import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import pandas as pd
def preprocess_text(text):
    # Tokenize text into words
    tokens = word_tokenize(text)
    # Remove stopwords from tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    # Stem filtered tokens using Porter stemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # Join stemmed tokens into a string and return it
    return ' '.join(stemmed_tokens)

text = pd.read_csv("Hotel Reservations.csv")
preprocessed_text = preprocess_text(text)
print(preprocessed_text)

