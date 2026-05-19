import os
import discord
import random
from dotenv import load_dotenv

from components.reaction import QuoteNovelsPoems

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

qts = QuoteNovelsPoems()

@client.event
async def on_ready():
    print(f"ログインしました: {client.user}")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "bot":
        await message.channel.send(qts.create_quote(random.randint(0, qts.n_manuscripts), random.randint(0, qts.max_sentences), random.randint(3, 5)))
#        await message.channel.send("こんにちは。今日も5分だけやってみよう。")


client.run(os.getenv("DISCO_BOT_TOKEN"))
