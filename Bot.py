import discord
import os
import Movies as m
import Fetch as f
from dotenv import load_dotenv

#loads hidden token
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


#start the discord bot
client = discord.Client()

def startBot():
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    DID = int(os.getenv('DID')) 
    RID = int(os.getenv('RID'))



    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$help'):
            await message.channel.send('**$request [title] **\n Use the title, specify a version,year, includeposter, etc. Message will be pinned until request is filled')


        if message.content.startswith('$hello'):
            await message.channel.send('https://64.media.tumblr.com/97eb2692a2b37c44668698e6fb504203/a1f82a3c0184708c-8e/s540x810/db45c013d90ad46bf0c2ea93e47010e3caffe0ec.gif')

        if message.content.startswith('$dontpanic'):
            await message.channel.send('a hoopy frood always knows where their towel is!')

        if message.content.startswith('$movies'):
            if message.author.id == DID:
                #sends title, desc, and poster to the channel
                x = m.printList()
                for i in range(5):
                    message = await message.channel.send(x[i])
                
                #creates poll based on titles
                titles = x[-1]
                message = await message.channel.send("**" +titles[0] +  "\n" + titles[1]+ "\n"+ titles[2] + "\n" + titles[3] + "\n" + titles[4]+ "**")
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                await message.add_reaction("4️⃣")
                await message.add_reaction("5️⃣")
                await message.add_reaction("<:thinkofthechildren:921776713065697310>")
            else:
                print("Don't panic!")
                await message.channel.send('https://static.wikia.nocookie.net/jurassicpark/images/b/b3/Ahahahreal.gif')

        if message.content.startswith('$request'):
            if message.channel.name == "requests":
                await message.pin()
            else:
                message = await message.channel.send(f'Please do the thing again over in <#{RID}>')

       
    client.run(DISCORD_TOKEN)