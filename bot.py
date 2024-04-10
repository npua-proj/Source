import json
import urllib.parse
import urllib.request
import os

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"


def send_message(chat_id, text):
    url = TELEGRAM_API_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    request = urllib.request.Request(url, json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(request) as response:
        response_text = response.read().decode()
        print(response_text)


def fetch_podcasts_by_tag(tag):
    # Simulate fetching podcasts by tag
    # Replace this with actual code to fetch podcasts
    return f"Found podcasts with the tag '{tag}'."


def fetch_podcasts_by_provider(provider):
    # Simulate fetching podcasts by provider
    # Replace this with actual code to fetch podcasts
    return f"Found podcasts by the provider '{provider}'."


def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    text = message.get('text', '').strip()

    if text.startswith('/byTag '):
        tag = text[len('/byTag '):].strip()
        if tag:
            podcasts = fetch_podcasts_by_tag(tag)
            send_message(chat_id, podcasts)
        else:
            send_message(chat_id, "Please specify a tag after '/byTag'.")
    elif text.startswith('/byProvider '):
        provider = text[len('/byProvider '):].strip()
        if provider:
            podcasts = fetch_podcasts_by_provider(provider)
            send_message(chat_id, podcasts)
        else:
            send_message(chat_id, "Please specify a provider after '/byProvider'.")
    else:
        send_message(chat_id, "Sorry, I didn't understand that command. Try /byTag <tag> or /byProvider <provider>.")

    return {'statusCode': 200}
