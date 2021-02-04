import discord
import os
from discord.utils import get
import time
from discord.ext import commands
BOT_PREFIX ='-'
client = commands.Bot(command_prefix=BOT_PREFIX)
Executioner = (246652133464735746)
VoteCount = 0
Prisoner = None
Vote = False
Seen = set()
AllVotes = []
VotedList = []
Role = "Beheaded"
member = None
role = None
roles = ["Member","Co-Owner","Moderator", "OG", "Owner", "Admin", "WARZONE/COD","Hospital"]
lastwords = False
execute = False
first = True
@client.event
async def on_ready():
    print("Logged {0.user}\nReady".format(client))
@client.command()
async def addrole(ctx,role:discord.Role, user: discord.Member):
    await user.add_roles(role)
@client.command()
async def removerole(ctx,role:discord.Role, user: discord.Member):
    await user.remove_roles(role)
@client.event
async def on_message(message):
    try:
        if message.author.id != (806552138523213874) and message.channel.id == (806620469381693450) or message.channel.id == (806621982748966942):
            global Prisoner
            global Executioner
            global VoteCount
            global Vote
            global VotedList
            global Seen
            global AllVotes
            global user
            global usr
            global roles
            global lastwords
            global execute
            global first

            if message.author.id == Executioner:
                if message.content[0] == "-":
                    tmp = message.content
                    if "-kill " in tmp:
                        tp =''
                        for i in tmp:
                            tp += i
                        tp = tp.split()

                        if len(tp[1]) <= 12:
                            await message.channel.send("```You want me to kill you?!```")
                            Vote = False
                            return

                        pp =""
                        for k in tp[1]:
                            if k != "<" and k != "@" and k != "!" and k!= ">":
                                pp += k
                        Prisoner = int(pp)
                        user = await client.fetch_user(Prisoner)
                        usr=""
                        for j in str(user):
                            if j != "#":
                                usr += j
                            else:
                                break
                        if usr == "Execution":
                            await message.channel.send("```You cannot kill me!```")
                        else:
                            await message.channel.send(f"```We shall kill {usr} [TYPE 'kill' to vote]```")
                            Vote = True
                        return
            if lastwords and message.author.id != Prisoner:
                await message.delete()
                return
            if lastwords and message.author.id == Prisoner:
                print(lastwords)
                print(message.author.id)
                print(Prisoner)
                execute = True
            elif Vote:
                if message.content == "abord" and message.author.id == Executioner:
                    Vote = False
                    VoteCount = 0
                    AllVotes = []
                    Seen = set()
                    VotedList = []
                    await message.channel.send(f"```We shall have mercy for {usr} and his family```")
                    return
                elif message.content == "kill":
                    AllVotes.append(message.author.id)
                    global t
                    t = 0
                    for i in AllVotes:
                        if i not in Seen:
                            t += 1
                            VoteCount += 1
                            VotedList.append(i)
                            Seen.add(i)
                            if VoteCount == 5:
                                await message.channel.send("```" + "~~" + ("|" * (VoteCount-1)) + "~~" + "```")
                            else:
                                await message.channel.send("```"+"|"*VoteCount+"```")
                                return

                            if VoteCount == 5:
                                if first:
                                    await message.channel.send(f"```The execution will be executed, what are your last words {usr}```")
                                    lastwords = True
                                    first = False
                                    return
                    if t == 0:
                        await message.delete()

                else:
                    await message.delete()
                    return

            if execute:
                await message.channel.send("```The executioner is sharpening his blade```")
                await message.channel.send(file=discord.File('img/Sharping.jpg'))
                time.sleep(3)
                await message.channel.send("```The executioner is heading towards the execution table```")
                await message.channel.send(file=discord.File('img/Running.jpg'))
                time.sleep(3)
                await message.channel.send("```The prisoner is tied up on the table```")
                await message.channel.send(file=discord.File('img/Waiting.gif'))
                time.sleep(3)
                await message.channel.send("```The executioner is swinging his blade```")
                await message.channel.send(file=discord.File('img/Beheading.jpg'))
                time.sleep(1)
                await message.channel.send(f"```{usr} has been beheaded by the executioner.```")
                member = user
                mp = "-addrole Beheaded " + str(member)
                message.content = mp
                await client.process_commands(message)
                for h in roles:
                    mp = "-removerole " + h + " " + str(member)
                    message.content = mp
                    await client.process_commands(message)
                time.sleep(3)
                await message.channel.send(file=discord.File('img/Killed.jpg'))
                Vote = False
                VoteCount = 0
                AllVotes = []
                Seen = set()
                VotedList = []
                lastwords = False
                execute = False
                first = True
                await message.channel.send("```The execution is over.```")
                time.sleep(1440)
                mp = "-removerole Beheaded " + str(member)
                message.content = mp
                await client.process_commands(message)
                mp = "-addrole Hospital " + str(member)
                message.content = mp
                await client.process_commands(message)
                await message.channel.send(f"```{usr} has been healed in the hospital.```")
                return
            else:
                if message.content == "kill":
                    await message.channel.send("```No one is being executed```")
                    return
                await message.delete()
                return

    except ValueError:
        await message.channel.send("```Don't waste my time!```")

client.run('ODA2NTUyMTM4NTIzMjEzODc0.YBrGNg.0MHZAEOGx5-wh3_HTcRkAzycCGM')