import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

async def get_tags_from_gpt(phrase):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate tags for podcasts from this phrase: '{phrase}'",
        max_tokens=60
    )
    tags = response.choices[0].text.strip().split(',')
    return [tag.strip() for tag in tags]
