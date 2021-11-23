import threading, json, webbrowser, requests, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests, threading, json, webbrowser, requests
from requests import get
from websocket import WebSocket
from json import dumps
from threading import Thread

guild_id = input("[>] Guild ID: ")
chid = input("[>] Channel ID: ")

with open('config.json') as f:
	config = json.load(f)
 
Token = config["token"]

while True:
    WebSocket.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    WebSocket.send(dumps({"op": 2,"d": {"token": Token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    WebSocket.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": False,"self_deaf": False}}))
