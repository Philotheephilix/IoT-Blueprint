import openai
openai.api_key = 'pk-picRItgpTZAjWHzpezyucAQqMoDxmwApNIIQFRtGcEIbKNar'
openai.api_base = 'https://api.pawan.krd/v1'
def chat(prompt):
    response = openai.Completion.create(
        engine="pai-001-light",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()