import discord
import asncio

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.uset.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='디스코드 봇 대화중', type=1))
    

@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")


client.run('NjUwMjQ0MDMwNDg3MDY4Njcz.XeJf3A.hYs_KjGBKEgzHeaXXs6xMu7ZEpg')