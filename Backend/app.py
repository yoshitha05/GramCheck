from flask import Flask, request, jsonify
from grammar import correct_grammar, preprocess_text

app = Flask(__name__)

@app.route('/check-grammar', methods=['POST'])
def check_grammar():
    data = request.json
    text = data.get("text", "")
    cleaned_text = preprocess_text(text)  # Apply NLP preprocessing
    corrected_text = correct_grammar(cleaned_text)  # Correct grammar using Hugging Face model
    return jsonify({"corrected_text": corrected_text})

if __name__ == '__main__':
    app.run(debug=True)