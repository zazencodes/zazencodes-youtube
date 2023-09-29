from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/mystic_hallucination/generate', methods=['GET'])
def get_mystic_hallucination():
    data = {
        "title": "My example title ",
        "story_html": "Some HTML <b>bold part</b>",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Viktor_Borisov-Musatov_-_Autumn_Scene.jpg",
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)


