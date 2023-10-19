from flask import Flask, jsonify
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise EnvironmentError


@app.route("/mystic_hallucination/generate", methods=["GET"])
def get_mystic_hallucination():

    gpt_conversation = write_mystic_hallucination()
    title_text = gpt_conversation[-1]["content"].replace('"', '')
    story_html = "\n".join([f"<p>{text}</p>" for text in gpt_conversation[-3]["content"].split("\n")])
    story_html = f"""
    <div>
    {story_html}
    </div>
    """

    gpt_response = draw_mystic_hallucination(title_text)
    image_url = gpt_response["data"][0]["url"]

    data = {
        "title": title_text,
        "story_html": story_html,
        "image_url": image_url,
    }
    return jsonify(data)


def write_mystic_hallucination():
    system_setting = "You are a poet who writes in the style of the mystic philosopher Rumi."
    prompts = [
        "Write a short story using less than 500 words.",
        "Write a title for the story.",
    ]
    messages = [{"role": "system", "content": system_setting}]
    for prompt in prompts:
        messages.append({"role": "user", "content": prompt})
        gpt_resp = chatgpt_get(endpoint="chat/completions", data={
            "model": "gpt-3.5-turbo",
            "messages": messages,
        })
        gpt_resp_text = gpt_resp["choices"][0]["message"]["content"]
        messages.append(
            {"role": "assistant", "content": gpt_resp_text}
        )
    
    return messages


def draw_mystic_hallucination(title_text):
    prompt = f"""An illustration of "{title_text}" in the style of Kalamkari art."""
    gpt_resp = chatgpt_get(endpoint="images/generations", data={
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",
    })
    return gpt_resp


def chatgpt_get(**kwargs):
    endpoint = kwargs["endpoint"]
    data = kwargs["data"]
    
    base_url = "https://api.openai.com/v1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    url = f"{base_url}/{endpoint}"
    print(f"POST {url} with data = {json.dumps(data)}")
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)
    if not resp.ok:
        try:
            print(json.dumps(resp.json(), indent=2))
        except:
            print(resp.text)
        raise Exception
    return resp.json()


if __name__ == '__main__':
    app.run(debug=True)


