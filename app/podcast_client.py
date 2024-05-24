import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
GOOGLE_CSE_URL = "https://www.googleapis.com/customsearch/v1"

async def get_podcasts(query):
    params = {
        'key': GOOGLE_API_KEY,
        'cx': GOOGLE_CSE_ID,
        'q': query
    }
    response = requests.get(GOOGLE_CSE_URL, params=params)
    response.raise_for_status()
    return response.json()
