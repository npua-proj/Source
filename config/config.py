# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
REMOTEOK_API_URL = 'https://remoteok.io/api'
