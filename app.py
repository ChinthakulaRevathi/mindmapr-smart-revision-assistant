from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "mindmapr.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Get all topics
@app.route("/topics", methods=["GET"])
def get_topics():
    return jsonify(load_data())


# Add topic
@app.route("/topic", methods=["POST"])
def add_topic():
    data = load_data()
    topic = request.json.get("topic")

    if not topic:
        return jsonify({"message": "Topic is required"}), 400

    if topic in data:
        return jsonify({"message": "Topic already exists"}), 400

    data[topic] = {}
    save_data(data)

    return jsonify({"message": "Topic added successfully"})


# Add subtopic
@app.route("/subtopic", methods=["POST"])
def add_subtopic():
    data = load_data()

    topic = request.json.get("topic")
    subtopic = request.json.get("subtopic")
    notes = request.json.get("notes", "")

    if not topic or not subtopic:
        return jsonify({"message": "Topic and subtopic are required"}), 400

    if topic not in data:
        return jsonify({"message": "Topic not found"}), 404

    data[topic][subtopic] = notes
    save_data(data)

    return jsonify({"message": "Subtopic added successfully"})


# Delete topic
@app.route("/delete/topic", methods=["DELETE"])
def delete_topic():
    data = load_data()
    topic = request.json.get("topic")

    if topic in data:
        del data[topic]
        save_data(data)

        return jsonify({
            "message": f"Topic '{topic}' deleted successfully"
        })

    return jsonify({"message": "Topic not found"}), 404


# Delete subtopic
@app.route("/delete/subtopic", methods=["DELETE"])
def delete_subtopic():
    data = load_data()

    topic = request.json.get("topic")
    subtopic = request.json.get("subtopic")

    if topic not in data:
        return jsonify({"message": "Topic not found"}), 404

    if subtopic not in data[topic]:
        return jsonify({"message": "Subtopic not found"}), 404

    del data[topic][subtopic]
    save_data(data)

    return jsonify({
        "message": f"Subtopic '{subtopic}' deleted successfully"
    })


# Get mind map
@app.route("/get_mindmap", methods=["GET"])
def get_mindmap():
    return jsonify(load_data())


if __name__ == "__main__":
    app.run(debug=True)