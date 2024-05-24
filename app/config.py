import os
from dotenv import load_dotenv

load_dotenv()

print("TELEGRAM_API_TOKEN:", os.getenv('TELEGRAM_API_TOKEN'))
print("OPENAI_API_KEY:", os.getenv('OPENAI_API_KEY'))
print("GOOGLE_API_KEY:", os.getenv('GOOGLE_API_KEY'))
print("GOOGLE_CSE_ID:", os.getenv('GOOGLE_CSE_ID'))
