import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
import os
from notion_client import Client
from notion_client import AsyncClient

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

startingMessageID = None
endingMessageID = None
messages = []

url = "https://api.notion.com/v1/pages"

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

notion = AsyncClient(auth=os.environ["NOTION_API_KEY"])

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

NOTION_TOKEN = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

async def makePage():
    data = {
        "parent": {
            "page_id": "1a1176890f35803caac2e994f6415d8a"
        },
        "properties": {
            "title": {
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "A note from your pals at Notion"
                        }
                    }
                ]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "You made this page using the Notion API. Pretty cool, huh? We hope you enjoy building with us."
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = await notion.pages.create(**data)
    return response

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    global startingMessageID, endingMessageID, messages

    if message.author.bot:
        return  # Ignore bot messages

    if message.content == "Notesman start from here" and message.reference:
        startingMessageID = message.reference.message_id
        await message.channel.send(f'Starting message ID: {startingMessageID}')
    elif message.content == "Notesman end here" and message.reference:
        endingMessageID = message.reference.message_id
        await message.channel.send(f'Ending message ID: {endingMessageID}')
    elif message.content == "Notesman end":
        startingMessageID = None
        endingMessageID = None
        await message.channel.send('Reset starting and ending message IDs.')
    elif message.content == "Notesman start PDF":
        if startingMessageID and endingMessageID:
            try:
                start_message = await message.channel.fetch_message(startingMessageID)
                end_message = await message.channel.fetch_message(endingMessageID)
                async for msg in message.channel.history(after=start_message, before=end_message, oldest_first=True):
                    messages.append(msg)
                messages.append(end_message)  # Include the ending message
                for msg in messages:
                    content = f'{msg.author}: {msg.content}'
                    if msg.attachments:
                        for attachment in msg.attachments:
                            if attachment.content_type.startswith('image/'):
                                content += f'\nImage: {attachment.url}'
                    await makePage()
                    await message.channel.send(content)
            except discord.NotFound:
                await message.channel.send("Could not find one of the messages. Please check the IDs.")
        else:
            await message.channel.send('Please set both starting and ending message IDs first.')

client.run(os.getenv('TOKEN'))