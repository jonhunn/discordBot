import discord
import os
import Movies as m
import Fetch as f
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


#start the discord bot
client = discord.Client()

def startBot():
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('$dontpanic'):
            await message.channel.send('a hoopy frood always knows where their towel is!')

        if message.content.startswith('$movies'):
            x = m.printList()
            message = await message.channel.send(x)
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("4️⃣")
            await message.add_reaction("5️⃣")
            await message.add_reaction("<:thinkofthechildren:921776713065697310>")


    client.run(DISCORD_TOKEN)