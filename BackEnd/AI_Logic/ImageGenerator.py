from http.client import HTTPException

import openai
import os

#Set this env variable later!
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

def generate_image(explainationText):
    propmt = (
        "Create a simple diagram that visually explains the following cryptography process in a friendly, "
        "educational way: \n\n" + explainationText + "\n\n Use arrows, text, boxes, and labels."
    )
    try:
        response = openai.Image.create(
            prompt=propmt,
            n=1,
            size = "512x512"
        )
        return response['data'][0]['url']
    except Exception as e:
        raise HTTPException(f"Image generation failed: {str(e)}")