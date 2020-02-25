import discord
import requests
from bs4 import BeautifulSoup as BS

role=1
client=discord.Client()

@client.event
async def on_ready():
    print("logged as")
                           
@client.event
async def on_raw_reaction_add(payload):
    message_id=payload.message_id
    if message_id==677469334972661770:
        guild_id=payload.guild_id
        guild=discord.utils.find(lambda g : g.id==guild_id,client.guilds)
        if payload.emoji.name=="Python":
            role=discord.utils.get(guild.roles,name='Python')
        elif payload.emoji.name=="Ruby":
            role=discord.utils.get(guild.roles,name='Ruby')
        elif payload.emoji.name=="Csharp":
            role=discord.utils.get(guild.roles,name='Csharp')
        elif payload.emoji.name=="Clang":
            role=discord.utils.get(guild.roles,name='Clang')
        elif payload.emoji.name=="C_":
            role=discord.utils.get(guild.roles,name='C++')
        else:
            print("error 404:role are not found")
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id,guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")

@client.event
async def on_raw_reaction_remove(payload):
    message_id=payload.message_id
    if message_id==677469334972661770:
        guild_id=payload.guild_id
        guild=discord.utils.find(lambda g : g.id==guild_id,client.guilds)
        if payload.emoji.name=="Python":
            role=discord.utils.get(guild.roles,name='Python')
        elif payload.emoji.name=="Ruby":
            role=discord.utils.get(guild.roles,name='Ruby')
        elif payload.emoji.name=="Csharp":
            role=discord.utils.get(guild.roles,name='Csharp')
        elif payload.emoji.name=="Clang":
            role=discord.utils.get(guild.roles,name='Clang')
        elif payload.emoji.name=="C_":
            role=discord.utils.get(guild.roles,name='C++')
        else:
            print("error 404:role are not found")
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id,guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")
@client.event
async def on_message(message):
    if message.content=="Tiobe":
        await message.channel.send("1.Java \n 2.C \n 3.Python \n 4.C++ \n 5.C#")
    elif message.content=="PYPL":
        await message.channel.send("1.Python \n 2.Java \n 3.Javascript	 \n 4.C# \n 5.PHP")
    elif message.content=="Наш рейтинг":
        await message.channel.send("1.Python \n 2.Java \n 3.C# \n 4.C++ \n 5.C")
    elif message.content=="help":
        await message.channel.send("Tiobe : Рейтинг языков программивания Tiobe \n PYPL : Рейтинг языков программивания PYPL \n Наш рейтинг : Наш рейтинг языков программивания")
client.run("NjY4ODk4MDY3NDk5NTgxNDcx.Xk7N_Q.O21XPymMp-v4zPPfB4QNvHbBZtA")