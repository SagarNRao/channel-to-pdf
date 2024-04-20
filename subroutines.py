from asposecells.api import Workbook
import discord
from discord.ext import commands
import pywhatkit

import requests
import json

import asposecells
import jpype

jpype.startJVM


class sidefunctions:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def convert_to_pdf(self,input_json):
        jsonre = json.loads(input_json.text)
        jsonre = jsonre[::-1]
        for value in jsonre:
            print(value['content'], '\n')
            
        workbook = Workbook(jsonre)
        workbook.save("Output.pdf")
        jpype.shutdownJVM
