import discord  # pip install discord

client = discord.Client()

token = ""    # Bot token

@client.event
async def on_ready():
    print(client.user.name) # Bot name
    print("Started bot.")
    game = discord.Game('Testing')
    await client.change_presence(status=discord.Status.online, activity=game)   # Bot online

@client.event
async def on_message(message):
    if message.content == "Hello":  # 입력한 메시지가 "Hello"면 실행
        await message.channel.send("World!")    # Hello를 전송

client.run(token)   # Bot run