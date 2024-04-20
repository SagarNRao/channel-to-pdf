# def get_message(channel_id):
#     headers = {
#         'authorization': "NjkxNTY1NDkwMjU4MTgyMTc1.Ggf2Vl._3r45KNvHLdMhG7KZPiJxS2ER3f_qYwJDSe5RY"
#     }
#     r = requests.get(
#         f'https://discord.com/api/v9/channels/{channel_id}/messages?', headers=headers)
#     jsonre = json.loads(r.text)
#     for value in jsonre:
#         print(value['content'], '\n')