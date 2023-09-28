#!/usr/bin/env python
# coding: utf-8

# ## Mystic Hallucinations Dev
# 
# - Dialogue with ChatGPT
# - Generate image with DALL-E

import os
import requests
import json

# os.environ["OPENAI_API_KEY"] = ""
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise EnvironmentError


def test_chatgpt_get_chat_completions():
    endpoint = "chat/completions"
    base_url = "https://api.openai.com/v1/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Tell me one interesting word"},
        ]
    }
    resp = requests.post(f"{base_url}/{endpoint}", data=json.dumps(data), headers=headers)
    print(resp)
    return resp


resp = test_chatgpt_get()


resp.ok


resp.json()


resp.json()["choices"][0]["message"]["content"]


import tiktoken
# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


messages = [
    {"role": "user", "content": "Tell me one interesting word"},
]

print(num_tokens_from_messages(messages))


def chatgpt_get_chat_completions(messages):
    endpoint = "chat/completions"
    base_url = "https://api.openai.com/v1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
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

def write_mystic_hallucination():
    system_setting = "You are a poet who writes in the style of the mystic philosopher Rumi."
    prompts = [
        "Write a short story using less than 500 words.",
        "Write a title for the story.",
    ]
    responses = []
    messages = [{"role": "system", "content": system_setting}]
    for prompt in prompts:
        messages.append({"role": "user", "content": prompt})
        gpt_resp = chatgpt_get(messages)
        responses.append(gpt_resp)
        gpt_resp_text = gpt_resp["choices"][0]["message"]["content"]
        messages.append(
            {"role": "assistant", "content": gpt_resp_text}
        )
    
    return messages, responses
        
    


messages, responses = write_mystic_hallucination()


print(messages[-1]["content"])


print(messages[-3]["content"])


from IPython.display import HTML

def display_short_story(messages):
    title_text = messages[-1]["content"].replace('"', "")
    story_text = "\n".join([f"<p>{text}</p>" for text in messages[-3]["content"].split("\n")])
    html = f"""
    <h1>{title_text}</h1>
    <br>
    <div>
    {story_text}
    </div>
    """
    return HTML(html)


display_short_story(messages)



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

def chatgpt_get_images_generations(prompt):
    endpoint = "images/generations"
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",
    }
    return chatgpt_get(endpoint=endpoint, data=data)


image_resp = chatgpt_get_images_generations("""
An illustration of "The Seeker's Journey: Finding the Secret Place Within" in the style of Kalamkari art.
""".strip())


image_resp


from IPython.display import Image


Image(url=image_resp["data"][0]["url"])


def draw_mystic_hallucination_image(story_title):
    prompt = f'An illustration of "{story_title}" in the style of Traditional Indian art'
    gpt_resp = chatgpt_get_images_generations(prompt)
    image_url = gpt_resp["data"][0]["url"]
    
    return image_url, gpt_resp


story_title = messages[-1]["content"].replace('"', "")
image_url, gpt_resp = draw_mystic_hallucination_image(story_title)


gpt_resp


Image(url=image_url)




