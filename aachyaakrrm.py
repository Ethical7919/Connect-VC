import threading
from websocket import WebSocket
from json import dumps

guildid = ""
channel = ""
Token = ""

def ok_cool_dude():
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    ws.send(dumps({"op": 2,"d": {"token": Token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(dumps({"op": 4,"d": {"guild_id": guildid,"channel_id": channel, "self_mute": True,"self_deaf": True}}))
        
threading.Thread(target=ok_cool_dude).start()
