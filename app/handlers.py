from aiogram import types
from aiogram.dispatcher import Dispatcher
from .openai_client import get_tags_from_gpt
from .podcast_client import get_podcasts

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply("Hi! I'm your Podcast Bot. Send me a phrase like 'Talk about football' and I'll find some podcasts for you.")

    @dp.message_handler()
    async def handle_message(message: types.Message):
        phrase = message.text
        await message.reply("Generating tags...")
        tags = await get_tags_from_gpt(phrase)
        await message.reply(f"Tags generated: {', '.join(tags)}")

        await message.reply("Searching for podcasts...")
        podcasts = await get_podcasts(' '.join(tags))
        if 'items' in podcasts:
            for item in podcasts['items']:
                await message.reply(f"Title: {item['title']}\nSnippet: {item['snippet']}\nLink: {item['link']}")
        else:
            await message.reply("No podcasts found for the given tags.")
