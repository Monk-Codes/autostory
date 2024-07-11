from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

# Read the story
with open("story.txt", "r") as f:
    story = f.read()

# Initialize the words
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

# Loop through the words
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/get_words', methods=['GET'])
def get_words():
    return jsonify(list(words))

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    answers = request.json
    modified_story = story
    for word in words:
        modified_story = modified_story.replace(word, answers[word])
    return modified_story

if __name__ == '__main__':
    app.run(debug=True)
