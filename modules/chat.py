import openai

openai.api_key = 'pk-picRItgpTZAjWHzpezyucAQqMoDxmwApNIIQFRtGcEIbKNar'
openai.api_base = 'https://api.pawan.krd/v1'

# change engine and remove api_base if using official openai api

#   increase max_tokens to get a long response

def chat(prompt):
    response = openai.Completion.create(
        engine="pai-001-light",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()