from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/random_phrase")
def random_phrase():
    with open("phrases.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        random_entry = random.choice(data["phrases"])
    return jsonify(random_entry)


if __name__ == "__main__":
    app.run()
