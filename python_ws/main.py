import os
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"ログインしました: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!hello":
        await message.channel.send("こんにちは。今日も5分だけやってみよう。")

client.run(os.getenv("DISCO_BOT_TOKEN"))
