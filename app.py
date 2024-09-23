import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import random

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the cookie go to the doctor? Because it was feeling crumbly!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke')
def get_joke():
    return jsonify({'joke': random.choice(jokes)})

@app.route('/explain_joke', methods=['POST'])
def explain_joke():
    joke = request.json['joke']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that explains jokes to children."},
            {"role": "user", "content": f"Explain this joke to a child: {joke}"}
        ]
    )
    explanation = response.choices[0].message['content']
    return jsonify({'explanation': explanation})

if __name__ == '__main__':
    app.run()
