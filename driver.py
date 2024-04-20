import discord
from discord.ext import commands
import requests
import json
from mainmodule import mainfuncs

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

# def get_message(channel_id):
#     headers = {
#         'authorization': "NjkxNTY1NDkwMjU4MTgyMTc1.Ggf2Vl._3r45KNvHLdMhG7KZPiJxS2ER3f_qYwJDSe5RY"
#     }
#     r = requests.get(
#         f'https://discord.com/api/v9/channels/{channel_id}/messages?', headers=headers)
#     jsonre = json.loads(r.text)
#     for value in jsonre:
#         print(value['content'], '\n')

main = mainfuncs('1230967154933891273')

@client.event
async def on_ready():
    print("LOGGED IN SUCCESSFULLY")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("#history"):
        main.get_message()

client.run('MTIzMDk0ODU4NTQ3NTE0OTg1NQ.GtWRvN.ENdtOwzPS8tfyvutzGKlO0CiA77C08_mExMpz4')