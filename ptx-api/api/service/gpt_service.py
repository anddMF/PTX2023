import logging
from bing_chat import BingGPT
import asyncio

async def get_messages(message):
    logging.basicConfig(level=logging.INFO)
    c = BingGPT.Chatbot()
    response = await c.ask(message, conversation_style='balanced')
    messages = response['item']['messages']
    return messages