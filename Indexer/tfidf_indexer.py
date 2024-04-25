import json
import re
import pickle
import numpy as np
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

# First we load the data from JSON file
with open('/Users/mehalgosalia/CS429_IR_Project/chicago_crawler/chicago_data.json', 'r') as file:
    documents = json.load(file)

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser') # Extract all the text from the parsed HTML. This removes all HTML tags and retrieves just the textual content.
    text = soup.get_text() # Replace sequences of whitespace characters (spaces, tabs, newlines, etc.) with a single space. This helps in normalizing the text and reducing unnecessary whitespace.
    text = re.sub(r'\s+', ' ', text)  # Remove whitespace
    return text.lower()  # Converts the text to lower case

# This for loop cleans the HTML content of each document
for doc in documents:
    doc['text'] = clean_html(doc['content'])

# Creates a TfidfVectorizer object
vectorizer = TfidfVectorizer() #T
# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform([doc['text'] for doc in documents])

# Save the vectorizer and the TF-IDF matrix as pickle files
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)
