from fastapi import HTTPException
import openai
import os
from openai import OpenAI

#Set this env variable later!
#openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"

client = OpenAI(api_key="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")

def ImageGenerator(explainationText):
    prompt = (
        "Create a simple diagram that visually explains the following cryptography process in a friendly, "
        "educational way: \n\n" + explainationText + "\n\n Use arrows, text, boxes, and labels."
    )
    try:
        response = client.images.generate(
            model="dall-e-2",  # or "dall-e-3" if you're using it and have access
            prompt=prompt,
            n=1,
            size="512x512"
        )
        return response.data[0].url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")