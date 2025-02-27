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


def makePage():
    data = notion.pages.create(**
                               {
                                   "cover": {
                                       "type": "external",
                                       "external": {
                                           "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
                                       }
                                   },
                                   "icon": {
                                       "type": "emoji",
                                       "emoji": "🥬"
                                   },
                                   "parent": {
                                       "type": "database_id",
                                       "database_id": "1a1176890f35819ea55dfd414f590369"
                                   },
                                   "properties": {
                                       "Name": {
                                           "title": [
                                               {
                                                   "text": {
                                                       "content": "Tuscan kale"
                                                   }
                                               }
                                           ]
                                       },
                                       "Description": {
                                           "rich_text": [
                                               {
                                                   "text": {
                                                       "content": "A dark green leafy vegetable"
                                                   }
                                               }
                                           ]
                                       },
                                       "Food group": {
                                           "select": {
                                               "name": "🥬 Vegetable"
                                           }
                                       }
                                   },
                                   "children": [
                                       {
                                           "object": "block",
                                           "heading_2": {
                                               "rich_text": [
                                                   {
                                                       "text": {
                                                           "content": "Lacinato kale"
                                                       }
                                                   }
                                               ]
                                           }
                                       },
                                       {
                                           "object": "block",
                                           "paragraph": {
                                               "rich_text": [
                                                   {
                                                       "text": {
                                                           "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                                                           "link": {
                                                               "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                                                           }
                                                       },
                                                       "href": "https://en.wikipedia.org/wiki/Lacinato_kale"
                                                   }
                                               ],
                                               "color": "default"
                                           }
                                       }
                                   ]
                               })


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    global startingMessageID, endingMessageID, messages, properties

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
                    makePage()
                    await message.channel.send(content)
            except discord.NotFound:
                await message.channel.send("Could not find one of the messages. Please check the IDs.")
        else:
            await message.channel.send('Please set both starting and ending message IDs first.')

client.run(os.getenv('TOKEN'))
