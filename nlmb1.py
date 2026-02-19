# NewLandMafiagameBot1 명령어 #

import string
import discord  # import
import asyncio

client = discord.Client()

token = ""


@client.event
async def on_ready():
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('Bot | *가이드')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "*가이드":
        embed = discord.Embed(title="가이드", description="[명령어 리스트]\n`*가이드` 명령어 사용 방법이나, 게임 플레이 방법을 설명합니다.\n`*방 생성 [room id]` 마피아 게임 전용 방을 생성합니다.\n`*방 목록` 생성된 마피아 게임 전용 방을 전부 보여줍니다.\n`*방 제거 [room id]` 생성된 마피아 게임 전용 방을 제거합니다.", color=0x208f00)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/832497459031965706/b0d6c81fd56f5d3c20d5f3e5f553133d.png?size=128")
        await message.channel.send(embed=embed)

    if message.content.startwith("*방 생성"):
        amount = message.content[6:]
        await message.channel.purge(limit=1)
        await message.channel.purge(limit=int(amount))
        embed = discord.Embed(title="방 생성 안내", description="마피아 게임 전용 방 {}\n룸 매니저 {}님의 요청으로 인해 생성 되었습니다".format(amount, message.author), color=0x208f00)
        embed.set_footer(icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="마피아 게임", description="[참여하기](https://www.google.com)", color=0x208f00)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/832497459031965706/b0d6c81fd56f5d3c20d5f3e5f553133d.png?size=128")
        await message.channel.send(embed=embed)
        await asyncio.sleep(10)
        await message.channel.send("NM1 : 게임을 시작합니다.")
        embed = discord.Embed(title="밤", description="[자세히 보기](https://cdn.discordapp.com/avatars/832497459031965706/b0d6c81fd56f5d3c20d5f3e5f553133d.png?size=128)", color=0x208f00)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/832497459031965706/b0d6c81fd56f5d3c20d5f3e5f553133d.png?size=128")
        await message.channel.send(embed=embed)

    if message.content == "*방 목록":
        await message.channel.send("미구현 명령어")

    if message.content.startswith("*방 제거"):
        amount = message.content[6:]
        await message.channel.purge(limit=1)
        await message.channel.purge(limit=int(amount))
        embed = discord.Embed(title="방 제거 안내", description="마피아 게임 전용 방 {}개가\n룸 매니저 {}님의 요청으로 인해 삭제 되었습니다".format(amount, message.author), color=0x208f00)
        embed.set_footer(icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
        await message.channel.send(embed=embed)

client.run(token)   # client run()