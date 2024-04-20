import asposecells
import requests
import json


import pywhatkit

import requests
import json



class mainfuncs:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        # set in driver

    def get_message(self):
        headers = {
            'authorization': "NjkxNTY1NDkwMjU4MTgyMTc1.Ggf2Vl._3r45KNvHLdMhG7KZPiJxS2ER3f_qYwJDSe5RY"
        }
        r = requests.get(
            f'https://discord.com/api/v9/channels/{self.channel_id}/messages?', headers=headers)
        jsonre = json.loads(r.text)
        jsonre = jsonre[::-1]
        for value in jsonre:
            print(value['content'], '\n')
            
        with open('output.json','w') as f:
            json.dump(jsonre,f)
        # the server sends a GET request to the discord API to get  the messages to show in the server, these messages are not   stored locally


