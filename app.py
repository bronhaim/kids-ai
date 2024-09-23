from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the cookie go to the doctor? Because it was feeling crumbly!",
    "What do you call a sleeping bull? A bulldozer!",
    "Why did the picture go to jail? Because it was framed!",
    "What do you call a boomerang that doesn't come back? A stick!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "What do you call a parade of rabbits hopping backwards? A receding hare-line!",
    "Why couldn't the pirate play cards? Because he was sitting on the deck!",
    "What kind of tree fits in your hand? A palm tree!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    "How do you make a tissue dance? Put a little boogie in it!",
    "Why was six afraid of seven? Because seven eight nine!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke')
def get_joke():
    return jsonify({'joke': random.choice(jokes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)