import os

import openai
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

PROMPT_V1 = "You are a translator. Translate the following English text to Japanese."
PROMPT_V2 = "You are a translator. Translate the following English text to Japanese. Output the hiragana interpretation of any kanji characters as well."

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Japanese Translator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TranslationRequest(BaseModel):
    text: str


class TranslationResponse(BaseModel):
    translated_text: str


@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """
    Translate English text to Japanese using ChatGPT API
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Fixed typo in model name
            messages=[
                {
                    "role": "system",
                    "content": PROMPT_V2,
                },
                {"role": "user", "content": request.text},
            ],
        )
        return TranslationResponse(translated_text=response.choices[0].message.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
