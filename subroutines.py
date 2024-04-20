import jpype
import discord
from discord.ext import commands
import pywhatkit
import pandas as pd

import requests
import json

import asposecells
# import jpype

jpype.startJVM()
from asposecells.api import Workbook


class sidefunctions:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def convert_to_pdf(self, input_json_list):
        print(type(input_json_list))
        contents = []
        for content in input_json_list:
            if 'content' in content:  # Check if 'content' key exists
                if content['content'] != '':
                    contents.append(content['content'])
                elif 'attachments' in content and content['content']=='':
                    for attachment in content['attachments']:
                        if 'url' in attachment:
                            contents.append(attachment['url'])
            # print(content,'\n')
        
        print(contents)
        
# example = [
#     {"id": ("1", "2", "3"), "name": ("bhanu", "sivanagulu"), "department": ("HR", "IT")},
#     {"id": ("4", "5", "6"), "name": ("sai", "poori"), "department": ("HR", "IT")},
#     {"id": ("7", "8", "9"), "name": ("teja", "gowtam"), "department": ("finance", "IT")},
#     {"id": ("10", "11", "12"), "name": ("sai", "jyothi"), "department": ("business", "IT")},
#     {"id": ("13", "14", "15"), "name": ("prudhvi", "nagendram"), "department": ("business", "IT")}
# ]

# sidefunc = sidefunctions('123')
# sidefunc.convert_to_pdf(example)