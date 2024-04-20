import asposecells
import requests
import json

# import jpype
# from asposecells.api import Workbook
import pywhatkit

import requests
import json


# from subroutines import sidefunctions

# side = sidefunctions('1230967154933891273')

class mainfuncs:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        # set in driver

    def get_message(self):
        headers = {
            'authorization': "NjkxNTY1NDkwMjU4MTgyMTc1.Ggf2Vl.   _3r45KNvHLdMhG7KZPiJxS2ER3f_qYwJDSe5RY"
        }
        # authorization keys are unique to users
        r = requests.get(
            f'https://discord.com/api/v9/channels/{self.channel_id}/ messages?', headers = headers)

        jsonre = json.loads(r.text)
        for value in jsonre:
            print(value['content'], '\n')
        # the server sends a GET request to the discord API to get  the messages to show in the server, these messages are not   stored locally

        # side.convert_to_pdf(r)
