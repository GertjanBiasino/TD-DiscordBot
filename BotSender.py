import discord
import socket
import threading
import json

# -------- DISCORD BOT SETUP --------
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# TCP/IP configuratie
TD_HOST = '127.0.0.1'
TD_PORT = 7000  # Dit moet overeenkomen met je TCP/IP DAT in TouchDesigner

def send_to_touchdesigner(message_dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((TD_HOST, TD_PORT))
            s.sendall((json.dumps(message_dict) + "\n").encode('utf-8'))
            print(f"→ TCP verzonden naar TD: {message_dict}")
    except Exception as e:
        print(f"Fout bij verzenden naar TD via TCP: {e}")

@client.event
async def on_ready():
    print(f'Bot is online als {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Bericht van {message.author}: {message.content}")
    data = {
        "author": str(message.author),
        "content": message.content
    }
    send_to_touchdesigner(data)

# -------- MAIN --------
if __name__ == '__main__':
    client.run("DISCORD_BOT_TOKEN")
