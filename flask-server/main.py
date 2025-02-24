import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

startingMessageID = None
endingMessageID = None
messages = []


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
                    await message.channel.send(content)
            except discord.NotFound:
                await message.channel.send("Could not find one of the messages. Please check the IDs.")
        else:
            await message.channel.send('Please set both starting and ending message IDs first.')

client.run(os.getenv('TOKEN'))
