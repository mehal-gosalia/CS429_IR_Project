from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

app = Flask(__name__) # This is to initialize the Flask application

# Load the vectorizer for transforming text queries into vector form
with open('/Users/mehalgosalia/CS429_IR_Project/Indexer/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the TF-IDF matrix that represents the vectorized form of the documents
with open('/Users/mehalgosalia/CS429_IR_Project/Indexer/tfidf_matrix.pkl', 'rb') as f:
    matrix = pickle.load(f)

# Load the original documents from JSON. These are presumably web pages or other text documents related to Chicago.
with open('/Users/mehalgosalia/CS429_IR_Project/chicago_crawler/chicago_data.json', 'r') as f:
    documents = json.load(f)

def search(query, top_k=10):
    query_vector = vectorizer.transform([query])
    similarity = cosine_similarity(query_vector, matrix).flatten() # Calculate the cosine similarity between the query vector and all document vectors in the matrix.
    top_indices = np.argsort(similarity)[-top_k:][::-1]
    results = [{'index': int(idx), 'url': documents[idx]['url'], 'score': float(similarity[idx])} for idx in top_indices]
    return results

@app.route('/')
def home():
    return '''
    <h1>Chicago Wikipedia Page</h1>
    <h2>You can search anything about Chicago through its Wikipedia page over here. <h2>
    <p>Input any word or phrase about Chicago that you would love to explore, few examples are 'History', 'Demographics' etc. </p>
    <form action="/search" method="post">
        <input type="text" name="query" placeholder="Enter search query" required>
        <input type="submit" value="Search">
    </form>
    '''

 # Home page of the application, providing a simple search form
@app.route('/search', methods=['POST', 'GET'])
def search_handler():
    try:
        if request.method == 'POST':
            data = request.get_json() if request.is_json else request.form
            query = data['query']
        elif request.method == 'GET':
            query = request.args.get('query', '')
        if not query:
            return jsonify({'error': 'Empty query provided'}), 400

        results = search(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask application only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
