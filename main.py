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
        if message.author.id != (806552138523213874) and message.channel.id == (806620469381693450) and message.channel.id == (806621982748966942):
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
            if Vote:
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
                    t = 0
                    for i in AllVotes:
                        if i not in Seen:
                            t += 1
                            VoteCount += 1
                            VotedList.append(i)
                            Seen.add(i)
                            if VoteCount == 5 or VoteCount == 10:
                                await message.channel.send("```" + "~~" + ("|" * VoteCount) + "~~" + "```")
                            else:
                                await message.channel.send("```"+"|"*VoteCount+"```")

                            if VoteCount == 1:
                                await message.channel.send(f"The execution will be executed, what are your last words {usr}")
                                lastwords = True
                                if not lastwords and message.author.id != Prisoner:
                                    await message.delete()
                                    return
                                else:
                                    execute = True
                            if execute:
                                await message.channel.send("The executioner is sharpening his blade")
                                # Image sharpening
                                time.sleep(3)
                                # Image of executer runing
                                time.sleep(3)
                                #image of prisoner tied up
                                time.sleep(3)
                                #image of beheading
                                member = user
                                mp = "-addrole Beheaded " + str(member)
                                message.content = mp
                                await client.process_commands(message)
                                for h in roles:
                                    mp = "-removerole " + h + " " + str(member)
                                    message.content = mp
                                    await client.process_commands(message)
                                await message.channel.send(f"```{usr} has been beheaded by the executer.```")
                                time.sleep(3)
                                #image of beheaded
                                Vote = False
                                VoteCount = 0
                                AllVotes = []
                                Seen = set()
                                VotedList = []
                                time.sleep(5)
                                mp = "-removerole Beheaded " + str(member)
                                message.content = mp
                                await client.process_commands(message)
                                mp = "-addrole Hospital " + str(member)
                                message.content = mp
                                await client.process_commands(message)
                                await message.channel.send(f"```{usr} has been healed in the hospital.```")
                                return
                    if t == 0:
                        await message.delete()
                else:
                    await message.delete()
                    return
            else:
                if message.content == "kill":
                    await message.channel.send("```No one is being executed```")
                    return
                await message.delete()
                return

    except ValueError:
        await message.channel.send("```Don't waste my time!```")

client.run(os.environ['TOKEN'])