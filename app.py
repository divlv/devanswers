from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)


def get_random_link(phrases, exclude_link=None):
    remaining_phrases = [item for item in phrases if item["link"] != exclude_link]
    return random.choice(remaining_phrases)["link"]


@app.route("/")
def index():
    with open("phrases.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        entry = random.choice(data["phrases"])
        next_link = get_random_link(data["phrases"], exclude_link=entry["link"])
        return render_template(
            "index.html",
            phrase=entry["phrase"],
            link=next_link,
            logo_link=next_link,
            number=entry["number"],
            current_link=entry["link"],
        )


@app.route("/a/<path:subpath>")
def serve_phrase(subpath=None):
    link_filter = f"/a/{subpath}" if subpath else None
    with open("phrases.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        if link_filter:
            filtered_phrases = [
                item for item in data["phrases"] if item["link"] == link_filter
            ]
            entry = (
                filtered_phrases[0]
                if filtered_phrases
                else random.choice(data["phrases"])
            )
        else:
            entry = random.choice(data["phrases"])
        next_link = get_random_link(data["phrases"], exclude_link=entry["link"])
        return render_template(
            "index.html",
            phrase=entry["phrase"],
            link=next_link,
            logo_link=next_link,
            number=entry["number"],
            current_link=entry["link"],
        )


# if __name__ == "__main__":
#    app.run(port=8080)
