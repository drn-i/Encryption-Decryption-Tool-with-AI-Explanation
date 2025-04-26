import openai
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def TextGenerator(algorithm, input_text, key, operation, additional_key=None):
    base_prompt = (
        f"Explain step-by-step in a beginner-friendly way how the {algorithm.upper()} algorithm performs a {operation.upper()} operation.\n"
        f"Input: '{input_text}'\nKey: '{key}'\n"
    )
    if additional_key:
        base_prompt += f"Additional key (e.g. prime values): '{additional_key}'\n"

    prompt = base_prompt + "Please include key generation steps, and describe the mathematical process clearly using simple terminology."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=600
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating explanation: {str(e)}"