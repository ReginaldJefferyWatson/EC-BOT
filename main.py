import discord
from discord.ext import commands
from util import sort, add_student, overwrite_student, format_leaderboard
from discord import context_managers

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
  async def on_ready(self):
    print("EC-Leaderboard is ready!")
    
    
client = MyClient(intents=intents)


@client.event
async def on_message(message):
    leaderboard = sort()
    if message.author == client.user:
        return
      
    if message.content.startswith('$leaderboard'):
      format_leaderboard()
      await message.channel.send(file=discord.File("leaderboard.txt"))
      
    if message.content.startswith('$post'):
      try:
        args = message.content.split(" ")

        for user in leaderboard:
          if user["username"] == message.author.id:
            overwrite_student(args[1], message.author.id, args[2])
        if len(args) == 3:
          add_student(args[1], message.author.id, args[2])
        else:
          await message.channel.send("Wrong arguments! $init <name> <fitness score>")
      except:
        await message.channel.send("Wrong arguments! $init <name> <fitness score>")
     


client.run('MTAzNDg5MTg2OTk3MDIzNTQ0Mg.GxKKMj.r1BAJMz6TlccgByqWktHiHpBVDfyVRkpSsP-QQ')