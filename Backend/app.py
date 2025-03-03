from flask import Flask, request, jsonify
from flask_cors import CORS
from grammar import check_grammar  # Import function from grammar.py

app = Flask(__name__) #Creates a web server.
CORS(app)  # Enables communication between React (frontend) and Flask (backend).

@app.route('/check_grammar', methods=['POST'])
# API Endpoint (/check_grammar)
# 1. Listens for POST requests.
# 2. Extracts the text input from the request.
# 3. Calls check_grammar(text) from grammar.py.
# 4. Returns the corrected text as JSON.
def check_grammar_api():
    data = request.json        
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400  # Error if text is empty

    corrected_text = check_grammar(text)  # Call grammar checker
    return jsonify({"corrected_text": corrected_text})  # Return corrected text

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
