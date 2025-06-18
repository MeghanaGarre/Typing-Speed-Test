from flask import Flask, render_template
import random

app = Flask(__name__)

sentences = [
    "Python is a powerful programming language.",
    "Flask is a micro web framework written in Python.",
    "Typing fast can improve your productivity.",
    "Debugging is twice as hard as writing the code.",
    "Stay consistent and never stop learning.",
    "Code is like humor. When you have to explain it, it's bad.",
    "Simplicity is the soul of efficiency.",
    "Programs must be written for people to read.",
    "Typing tests can improve your speed and accuracy.",
    "Knowledge is power, but enthusiasm pulls the switch.",
    "Programming isn't about what you know, it's about what you can figure out.",
    "If you can't explain it simply, you don't understand it well enough.",
    "Talk is cheap. Show me the code.",
    "Learning never exhausts the mind.",
    "The best error message is the one that never shows up.",
]

@app.route("/")
def home():
    sentence = random.choice(sentences)
    return render_template("index.html", sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
