import openai
import os

#Set this env variable later!
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

def generate_text_explanation(algorithm, input_text, key, operation, additional_key=None):
    base_prompt = (
        f"Explain step-by-step in a beginner-friendly way how the {algorithm.upper()} algorithm performs a {operation.upper()} operation.\n"
        f"Input: '{input_text}'\nKey: '{key}'\n"
    )
    if additional_key:
        base_prompt += f"Additional key (e.g. prime values): '{additional_key}'\n"

    prompt = base_prompt + "Please include key generation steps, and describe the mathematical process clearly using simple terminology."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=600
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error generating explanation: {str(e)}"