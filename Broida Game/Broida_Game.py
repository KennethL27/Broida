import discord, datetime, time, re, asyncio, random
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()

client = commands.Bot(command_prefix = '.', fetch_online_members = True, intnets = intents)

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def game(ctx, duration = None, genre = None):
    top_players = [1, 2, 3]
    question = ['q1', 'q2', 'q3', 'q4']
    choices = ['q1c1', 'q1c2', 'q1c3', 'q1c4', 'q2c1', 'q2c2', 'q2c3', 'q2c4', 'q3', 'q4'] 
    solution = ['s1', 's2', 's3', 's4']
    player_list = []
    if duration != None:
        duration = 5 #make it 30 mins
    
    pinned_message = await ctx.send(f'**SCOREBOARD**\nTop player list: \n1st: Place {top_players[0]}\n2st: Place {top_players[1]}\n3rd: Place {top_players[2]}')
    await pinned_message.pin()
    await ctx.send('The game is will now start!')

    for i in question:
        time1 = 10
        points = 100
        embed = discord.Embed()
        embed.add_field(name = f'Trivia Question: **{i}**', value = i)
        embed.set_footer(text = f'Time left: {time1}')
        question = await ctx.send(embed = embed)
        await question.add_reaction('1️⃣')
        await question.add_reaction('2️⃣')
        await question.add_reaction('3️⃣')
        await question.add_reaction('4️⃣')
        await asyncio.sleep(1)
        current_time = time.time()
        end_time = current_time + 10
        user1 = []
        while current_time < end_time: #make it 60secs
            embed.set_footer(text = f'Time left = {time1}')
            updated_question = await question.edit(embed = embed)

            def check(reaction, user):
                return str(reaction.emoji) == '1️⃣' and user != client.user
            reaction1 = []
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=2, check=check)
                reaction1.append(reaction)
                user1.append(user)
            except:
                pass
            if len(user1) != 0:
                print(user1)
            time1 = time1 - 2
            current_time = time.time()
            await asyncio.sleep(1)
        j=0
        for i in user1:
            if i.id not in player_list:
                player_list.append([i.id,0])
            if i.id == player_list[j][0]:
                new_points = player_list[j][-1] + points
                player_list[j].append(new_points)
            j = j + 1
            points = points - 10
        if len(player_list) != 0:
            print(player_list)

    if time.perf_counter() == duration:
        ctx.send(f'The game has end, congrats to 1st place: {top_players[0]}, 2nd place: {top_players[1]}, 3rd: Place {top_players[2]}')
        return
    # await pinned_message.unpin()
    




client.run("Token")