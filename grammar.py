import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    words = word_tokenize(text)  
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
    return " ".join(filtered_words)

grammar_model = pipeline("text2text-generation", model="openai/whisper-large-v3-turbo")

def correct_grammar(text):
    result = grammar_model(text, max_length=100)
    return result[0]['generated_text']
