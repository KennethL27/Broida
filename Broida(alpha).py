'''
Created on Sat Nov 14 0:35:04 2020

@author: Kenneth Lara
'''

import discord, datetime, time, re, asyncio, random, json
from discord.ext import commands
from discord.utils import get 
from dateutil import tz

intents = discord.Intents.default()
intents.members = True
intents.messages = True  
intents.emojis = True
intents.reactions = True
intents.guild_reactions = True

client = commands.Bot(command_prefix = '.', fetch_online_members = True, intents = intents)
client.remove_command('help') 

guild_id = 613512375798333450

founder_id = 761719198984175646
admin_id = 613823450838073456
treasurer_id = 770513982926618624
mod_id = 760339279104049162 
gaucho_id = 761355746163163138
graduate_id = 737472618919362632
super_senior_id = 720463295852576788
senior_id = 720465326025998409
junior_id = 720465633543716894
sophomore_id = 720465928537767968
freshman_id = 720466070976200774
transfer_id = 780646137878151190 

message_log_channel_id = 777410376458567690
ticket_channel_id = 785809108213301248
announcement_channel_id = 613825243361837099 
bot_command_channel_id = 787690574001602600
spam_channel_id = 775176870064685126 
rant_channel_id = 718972914434572402
ban_channel_id = 794898870030434325
welcome_channel_id = 761361922322071593
advising_channel_id = 738201497053167717

open_exam = []
user_list = []
generated_user = []

update_status = False

list_of_commands = ['.physics', '.fiziks', '.uptime', '.dadjoke', '.update']

def write_json(data, file_name):
    with open (file_name, 'w') as file:
        json.dump(data, file, indent = 4)

@client.event
async def on_ready():
    bot_description = discord.Game('missing the crowds | .help')
    await client.change_presence(activity = bot_description)
    print('Bot is ready') 


# User Commands
################################################################################################################################################################################################


@client.command(aliases = ['classes', 'class', 'schedule'])
async def courses(ctx):
    embed = discord.Embed(title = 'Proposed Courses for 20-21', url = 'https://www.physics.ucsb.edu/resources/teachingassignments', colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif')
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/772690834151571506/782475543404347422/Screenshot_20201128-231814_Drive.jpg')
    await ctx.send(embed = embed) 

@client.command(aliases = ['mer'])
async def merch(ctx):
    link = 'https://teespring.com/stores/my-store-10181903'
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782215254540550164/WIP.png'
    embed = discord.Embed(title = 'Merch', url = link, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/783899572786692096/unknown.png')
    embed.set_thumbnail(url = image)
    await ctx.send(embed = embed) 

@client.command(aliases = ['fiziks'])
@client.command(aliases = ['fiziks'])
async def physics(ctx):
    await ctx.message.delete()
    with open ('Bot_string_list.json') as bot_string_list_json:
        data = json.load(bot_string_list_json)
        phys_facts = data["physics-facts"]
    await ctx.send(phys_facts[random.randint(0,len(phys_facts))]) 

@client.command(aliases = ['discs'])
async def discords(ctx):
    embed = discord.Embed(title = 'Links to other discords', description = 'The following discord links have been verifed, if you wish to inlude one that is not already here please DM an admin or mod.',
                          colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = 'UCSB', value = 'https://discord.com/invite/bqEZCWm')
    embed.add_field(name = 'LGBTQ+ in Physics', value = 'https://discord.gg/8dq4PX2KpB')
    embed.add_field(name = 'oSTEM @ UCSB', value = 'https://discord.gg/5FZ8Mdp')
    embed.add_field(name = 'Los Ingenieros', value = 'https://discord.gg/NWnxMdq')
    embed.add_field(name = 'PokemonGo', value = 'https://discord.gg/HmmrXSgXMT')
    embed.add_field(name = 'RPG at UCSB', value = 'https://discord.gg/ebc8UBG')
    await ctx.send(embed = embed)

@client.command(aliases=['anonymity','a'])
async def anonymous(ctx,*,user_message):
    global delete_counter
    k = 0
    user_name = ctx.author
    if isinstance(ctx.channel, discord.channel.DMChannel):
        channel_name = ''
        for i in range(len(user_message)):
            cha = user_message[i]
            if cha == ' ':
                user_message = user_message[i:]
                break
            else:
                channel_name += cha

        guild = client.get_guild(guild_id)
        channel = discord.utils.get(guild.channels, name = channel_name)
        
        if channel == None:
            await ctx.send('{} is not a valid channel name\nUse the format .a channel-name message'.format(channel_name))
            return

        member = guild.get_member(user_name.id)
        permissions = channel.permissions_for(member)
        if permissions.view_channel == False or permissions.send_messages == False:
            await ctx.send('You do not have permissions to send messages in the channel {}'.format(channel_name))
            return
    else:
        channel = ctx.channel
    
    user_message = user_message.replace('@everyone', '@ everyone').replace('@here', '@ here')

    if user_name not in user_list:
        user = random.randint(0,9999)
        user_list.append(user_name)
        generated_user.append(f'User{user}')

        if not(isinstance(ctx.channel, discord.channel.DMChannel)):
            await ctx.message.delete()
        anonymous_message = await channel.send(f'User{user}: {user_message}')
        delete_counter = delete_counter + 1
        anonymous_message_id = anonymous_message.id
        
        with open ("Anonymous_Log.json") as anonymous_log_json:
            data = json.load(anonymous_log_json)
            message_log = data['anonymous_message']
            new_entry = {"id": anonymous_message_id, "author": user_name.mention, "channel": channel.mention, "message": user_message}
            message_log.append(new_entry)
        write_json(data, "Anonymous_Log.json")

    elif user_name in user_list:
        for i in user_list:
            if i == user_name:

                if not(isinstance(ctx.channel, discord.channel.DMChannel)):
                    await ctx.message.delete()
                anonymous_message = await channel.send(f'{generated_user[k]}: {user_message}')
                delete_counter = delete_counter + 1
                anonymous_message_id = anonymous_message.id

                with open ("Anonymous_Log.json") as anonymous_log_json:
                    data = json.load(anonymous_log_json)
                    message_log = data['anonymous_message']
                    new_entry = {"id": anonymous_message_id, "author": user_name.mention, "channel": channel.mention, "message": user_message}
                    message_log.append(new_entry)
                write_json(data, "Anonymous_Log.json")

            k = k + 1
    if delete_counter == 30:
        user_list.clear()
        generated_user.clear()
        delete_counter = 0

@client.command(aliases = ['tic'])
async def ticket(ctx, member : discord.Member, * , reason):
    #for DMs, to mention the user use their discord username (not nickname) along with their discriminator. ie PhysicsLegends#6877
    guild = client.get_guild(guild_id)
    if ctx.channel in guild.text_channels:
        await ctx.message.delete()
    channel = client.get_channel(ticket_channel_id)
    embed = discord.Embed(title = '**TICKET EVENT**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
        This ticket is begin ticketed against: {member.mention}',colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = 'REASON', value = reason, inline = False)
    embed.add_field(name = 'Reactions', value = '**The red squre:** Will be a ban lasting 24 hours\n**The yellow square:** Will be a warning sent to the member in questioned \
        \n**The green square:** Will be nothing and the ticketer will be notified\n\nNote that the ticket will automatically end itself 24hrs from this message.', inline = False)
    message = await channel.send(embed = embed)
    #options for the ticket: ban for a specific amount of time, warning, or nothing
    await message.add_reaction('🟥') #ban for 24hrs 
    await message.add_reaction('🟨') #warn the user 
    await message.add_reaction('🟩') #no action 

    current_time = time.time()
    end_time = current_time + 3600 

    while current_time < end_time:

        use_message = await message.channel.fetch_message(message.id)
 
        '''for banning, opt 1'''

        if use_message.reactions[0].count > 3:
            await message.delete()
            #need to send an embed message of a summary of the ban.
            embed = discord.Embed(title = '**TICKET EVENT BAN: SUMMARY**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                This ticket is begin ticketed against: {member.mention}',colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name = 'REASON', value = reason, inline = False)
            embed.add_field(name = 'RESULT', value = 'Ticket resulted in a 24 hour ban.')
            await channel.send(embed = embed) 

            dm_embed = discord.Embed(title = '**TICKET EVENT BAN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
            dm_embed.add_field(name = 'RESULT', value = 'Under review it has appeared that you have violoated the rules and have been given a ban for 24 hours.\
                You may contact mods and admin in #ban-channel.')
            await member.send(embed = dm_embed) 

            member_roles = member.roles
            member_roles_list = [] 

            for role in member_roles:
                member_roles_list.append(role.id) 

            mod_role = guild.get_role(mod_id)
            treasurer_role = guild.get_role(treasurer_id) 

            for i in member_roles_list[1:]:
                roles = guild.get_role(i)
                if roles == mod_role or roles == treasurer_role:
                    await ctx.send('Invalid user due to having a mod role, please remove the role or select another user.')
                    return 

            #remove all roles except everyone
            for i in member_roles_list[1:]:
                roles = guild.get_role(i)
                await member.remove_roles(roles)           

            #need to make ban channel open for this user to discuss any information. Also remove access to new user welcome channel.
            ban_channel = client.get_channel(ban_channel_id)
            welcome_channel = client.get_channel(welcome_channel_id)
            await ban_channel.set_permissions(member, read_messages = True, send_messages = True, read_message_history = False)
            await welcome_channel.set_permissions(member, read_messages = False, send_messages = False)           

            await asyncio.sleep(86400) #24 hours ban: in seconds 86400

            #add all removed roles
            for i in member_roles_list[1:]:
                roles = guild.get_role(i)
                await member.add_roles(roles)
           
            await ban_channel.set_permissions(member, overwrite = None)
            await welcome_channel.set_permissions(member, overwrite = None)
            return

        '''for warning, opt 2'''
        #going to need to send the member a DM warning him. Maybe give an option to what rule was broken, for the warning to be enacted
        if use_message.reactions[1].count > 3:
            await message.delete()
            embed = discord.Embed(title = '**TICKET EVENT WARN**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                This ticket is begin ticketed against: {member.mention}',colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name = 'REASON', value = reason, inline = False)
            embed.add_field(name = 'Reactions', value = ':one: The user broke rule 1\n:two: The user broke rule 2\
                \n:three: The user broke rule 3\n*etc*\n:seven: The user did not break any specific rule, and will need to contact one of the mods to understand the warn.\n\n\
                *By default option 7 will be used after 10 mins*', inline = False)
            warn_message = await channel.send(embed = embed)
            await warn_message.add_reaction('1️⃣')
            await warn_message.add_reaction('2️⃣')
            await warn_message.add_reaction('3️⃣')
            await warn_message.add_reaction('4️⃣')
            await warn_message.add_reaction('5️⃣')
            await warn_message.add_reaction('6️⃣')
            await warn_message.add_reaction('7️⃣')
 
            current_time = time.time()
            end_time = current_time + 600 #for 10 minutes, 600 secs
            j = 0
            while current_time < end_time:
                use_message_warn = await warn_message.channel.fetch_message(warn_message.id)
                if use_message_warn.reactions[0].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = 'Member has broken rule 1\n*Use judgement when posting.\
                        Respect everyone and their opinion. We do not tolerate disrupting and/or offensive behavior, this includes: racist/sexist/insensitive remarks, trolling/baiting, \
                        spamming, doxing, harassing other users, etc. Consider common sense and public decency. Additionally, we do not allow discussions of recent figures such as Hitler, \
                        or similar politically motivated topics involving current politicians, all of which is both insensitive and inappropriate.*', inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = 'Member has broken rule 1\n*Use judgement when posting.\
                        Respect everyone and their opinion. We do not tolerate disrupting and/or offensive behavior, this includes: racist/sexist/insensitive remarks, trolling/baiting, \
                        spamming, doxing, harassing other users, etc. Consider common sense and public decency. Additionally, we do not allow discussions of recent figures such as Hitler, \
                        or similar politically motivated topics involving current politicians, all of which is both insensitive and inappropriate.*', inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[1].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 2\n*Post in the appropriate place. \
                        Each channel contains a description and/or pin that describe what's allowed and what's not allowed there. \
                        NSFW content is currently prohibited on this server.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 2\n*Post in the appropriate place. \
                        Each channel contains a description and/or pin that describe what's allowed and what's not allowed there. \
                        NSFW content is currently prohibited on this server.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[2].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 3\n*Cheating will not be tolerated and will result in an instant ban. \
                        The server will be set to read only during finals week. \
                        Any use of this server to communicate or gain access to information during an exam is prohibited.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 3\n*Cheating will not be tolerated and will result in an instant ban. \
                        The server will be set to read only during finals week. \
                        Any use of this server to communicate or gain access to information during an exam is prohibited.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[3].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 4\n*Real names are not be a rule. \
                        You can use whatever handle you want so long as it's appropriate. Impersonating a professor however is strictly prohibited.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 4\n*Real names are not be a rule. \
                        You can use whatever handle you want so long as it's appropriate. Impersonating a professor however is strictly prohibited.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[4].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 5\n*No posting of private discord links are allowed. \
                        If you want to share a discord link, contact the mods first and we can post it for you.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 5\n*No posting of private discord links are allowed. \
                        If you want to share a discord link, contact the mods first and we can post it for you.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[5].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 6\n*Rules are subject to change and will be updated accordingly*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 6\n*Rules are subject to change and will be updated accordingly*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[6].count > 2:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                current_time = time.time()
                await asyncio.sleep(1)
 
            if j == 0:
                await warn_message.delete()
                dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                    colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                dm_embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                    colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                embed.add_field(name = 'REASON', value = reason, inline = False)
                embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                await channel.send(embed = embed)
                await member.send(embed = dm_embed)
                return

        '''no action, opt 3'''
        if use_message.reactions[2].count > 3:
            #if 2 people react with red then send a message to the ticket channel stating that nothing will happen, provide a summary still.
            await message.delete()
            embed = discord.Embed(title = '**TICKET EVENT SUMMARY**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                This ticket is begin ticketed against: {member.mention}',colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name = 'REASON', value = reason, inline = False)
            embed.add_field(name = 'RESULT', value = 'Ticket did not warrent any action and the ticketer has been messaged.')
            await channel.send(embed = embed)
 
            await ctx.author.send(embed = embed)
            return
 
        current_time = time.time()
        await asyncio.sleep(1)
 
    await message.delete()
    embed = discord.Embed(title = '**TICKET EVENT TERMINATION**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
        This ticket is begin ticketed against: {member.mention}',colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = 'REASON', value = reason, inline = False)
    embed.add_field(name = 'RESULT', value = 'No action was created.')
    await channel.send(embed = embed)

@ticket.error
async def ticket_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: I could not find that member. When dming the bot use this format "username#number(ie. PhysicsLegends#6877)", otherwise mention the user by the @feature.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Error: Please provide all arguments: ie. ".ticket username#number(ie. PhysicsLegends#6877) <insert your argument here>"')

@client.command()
async def open_exams(ctx):
    embed = discord.Embed(colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    if len(open_exam) == 0:
        embed.add_field(name = 'Open Exams', value = 'There is no exams planned at this time')
        await ctx.send(embed = embed)
    if len(open_exam) != 0:
        for i in range(0, len(open_exam)):
            embed.add_field(name = f'Open Exam {i+1}', value = open_exam[i])
        await ctx.send(embed = embed)

@client.command()
async def advising(ctx):
    url = 'https://www.physics.ucsb.edu/education/undergrad/advising-help'
    embed = discord.Embed(title = 'UCSB Physics Advising', url = url, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = '__Schedule Meeting with Jean Dill__', value = 'https://shoreline.ucsb.edu/meetings/1336841/JDOfficeHours', inline = False)
    embed.add_field(name = '__Schedule Meeting with Earnest Cooper Jr.__', value = 'https://shoreline.ucsb.edu/meetings/1336823/Coopersadvisinghours', inline = False)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/794516513730068510/unknown.png')
    await ctx.send(embed = embed) 

@client.command()
async def dates(ctx):  
    url = 'https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/registration-pass-dates/2020-2021-registration-pass-times'
    embed = discord.Embed(title = 'UCSB 2020-2021 Registration Pass Times/Important Deadlines', url = url, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/794508278809100309/UCSBLogo.png')
    await ctx.send(embed = embed)

@client.command()
async def uptime(ctx):
    await ctx.channel.purge(limit = 1)
    time_seconds = time.perf_counter()
    time_days = time_seconds //(86400)
    time_seconds = time_seconds % 86400
    time_hours = time_seconds // 3600
    time_seconds %= 3600
    time_minutes =  time_seconds // 60
    time_seconds %= 60
    time_seconds = time_seconds
    message = await ctx.send(f'**UPTIME**: Days: {int(time_days)}, Hours: {int(time_hours)}, Minutes: {int(time_minutes)}, Seconds: {round(time_seconds,2)}')
    await message.delete(delay = 5)

@client.command()
async def help(ctx):
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
    footers = ['Powered by yours turly', 'Powered by your tears', 'Powered by curved that helped you pass', "Powered by Broida's black hole", 'Powered by KennethL <3', 'Powered by hope',\
               'Powered by perpetual motion', 'Powered by the bike lane', 'Powered by flat-eathers', 'Powered by ...', 'Loading...', 'Powered by Storke Tower', 'Powered by love']
    embed = discord.Embed(title = 'Commands for Broida', description = 'When using these commands, begin your statement with "." followed by the name of the command',\
         colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = image)
    embed.add_field(name = 'anonymous (anonymity, a)', value = 'Post anonymously in any channel using this command. This follows the same idea as the other anonymous bots. However it does not have the DM feature.')
    embed.add_field(name = 'merch (mer)', value = 'Get the link to the merch website.', inline = False)
    embed.add_field(name = 'courses (classes, class, schedule)', value = 'Get the link and image to the 2020-21 Teaching Assignments', inline = False)
    embed.add_field(name = 'advising', value = 'Get the link to UCSB Physics Advising as well as direct links to make appointments with Jean Dill or Cooper.', inline = False)
    embed.add_field(name = 'dates', value = 'Get the link to the full list of dates such as drop deadline or past times.', inline = False)
    embed.add_field(name = 'open_exams', value = 'Get the list of planned/current exams, this list is set to close their respective channels at the given time.', inline = False)
    embed.add_field(name = 'physics', value = 'Get random physics facts.', inline = False)
    embed.add_field(name = 'discords (discs)', value = 'Find out other discord servers like RPG at UCSB.', inline = False)
    embed.add_field(name = 'ticket (tic)', value = 'Use this command to submit a ticket. Please wirte your reasons for the ticket after ".ticket". *Please note: while dming the both with this command use the username#number (ie. PhysicsLegends#6877)* **.ticket <@user> <reason>**', inline = False)
    embed.add_field(name = 'uptime', value = 'This command shows you how long the bot has been running. The message will be delete after 5 seconds.', inline = False)
    embed.set_footer(text = footers[random.randint(0, len(footers))])
    await ctx.send(embed = embed)

@client.command()
async def dadjoke(ctx):
    await ctx.message.delete()
    with open ('Bot_string_list.json') as bot_string_list_json:
        data = json.load(bot_string_list_json)
        dad_jokes = data["dad-jokes"]
    await ctx.send(dad_jokes[random.randint(0, len(dad_jokes))])


# Moderation Commands (front-end and back-end)
################################################################################################################################################################################################


@client.command(aliases = ['anouce', 'post'])
@commands.has_any_role(founder_id, admin_id, treasurer_id)
async def announcement(ctx, date, time, *, announcement): #need to be able to edit before it goes live just in case
    original_message = ctx.message
    channel = client.get_channel(announcement_channel_id)
    if date == 'today' and time == 'now':
        await channel.send(content = announcement)
    else:
        month = int(re.split('/|-',date)[0])
        day = int(re.split('/|-',date)[1])
        year = int(re.split('/|-',date)[2])

        hour = int(re.split(':', time)[0])

        minute = int(re.split(':|am|pm', time)[1])

        if 'am' in time:
            if hour == 12:
                militaryhour = 0
            else:
                militaryhour = hour
        if 'pm' in time:
            if hour == 12:
                militaryhour = 12
            else:
                militaryhour = hour + 12

        release = datetime.datetime(year, month, day, militaryhour, minute, 0)

        message = await ctx.send(f'__The post will look like:__\n{announcement}')
        await message.add_reaction('🗑️')

        while datetime.datetime.now() < release: #holds off the change in permission until the start time
            await asyncio.sleep(1)
            edit_message_time = original_message.edited_at
            if not edit_message_time:
                pass
            else:
                command_message_edit = original_message.content
                am_split = command_message_edit.split('am',1)
                pm_split = command_message_edit.split('pm',1)
                if len(am_split[0]) < len(pm_split[0]):
                    new_announcement = am_split[1]
                else:
                    new_announcement = pm_split[1]
                await message.edit(content = f'__The post will look like:__\n{new_announcement}')

            use_message = await message.channel.fetch_message(message.id)
            if use_message.reactions[0].count > 1:
                await ctx.send(f"You have deleted the announcement, please resend your announcement to be posted.")
                return 
        try:
            await channel.send(content = new_announcement)
        except:
            await channel.send(content = announcement)

@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def add_event(ctx, event_name : str, event_time : str):
    with open('Bot_Info.json') as bot_info_json:
        data = json.load(bot_info_json)
        data["event"].append({"date" : event_time, "event-name": event_name})
    write_json(data, 'Bot_Info.json')

@client.listen('on_message')
async def on_message(message):
    global update_status
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.datetime.strptime(str(message.created_at)[:-7], "%Y-%m-%d %H:%M:%S")
    utc = utc.replace(tzinfo = from_zone)
    convert_zone = str(utc.astimezone(to_zone))
    if update_status is False:
        return
    else:
        #append to delete_message_log
        message_id = message.id
        user_name = message.author
        channel = message.channel
        user_message = message.content
        with open ("Update_Message_Log.json") as Update_Message_Log_json:
            data = json.load(Update_Message_Log_json)
            message_log = data['messages']
            new_entry = {"id": message_id, "author": user_name.mention, "channel": channel.mention, "created_at": convert_zone, "message": user_message}
            message_log.append(new_entry)
        write_json(data, "Update_Message_Log.json")

@client.event
async def on_raw_message_delete(payload):
    guild = client.get_guild(guild_id)
    message_log_channel = client.get_channel(message_log_channel_id)
    anonymous_channel = client.get_channel(rant_channel_id)
    rant_channel = client.get_channel(rant_channel_id)
    advising_channel = client.get_channel(advising_channel_id)
    message = payload.cached_message
    status = False

    try:
        if message.content.startswith('.a') or  message.content.startswith('.anonymity') or message.content.startswith('.anonymous'):
            return

        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        utc = datetime.datetime.strptime(str(message.created_at)[:-7], "%Y-%m-%d %H:%M:%S")
        utc = utc.replace(tzinfo = from_zone)
        convert_zone = utc.astimezone(to_zone)

        if message.channel != message_log_channel:
            if message.channel == anonymous_channel or message.channel == rant_channel or message.channel == advising_channel:
                if message.content.startswith('-r'):
                    return
            if message.author != client.user:
                if message.content not in list_of_commands:
                    # attachment = await message.attachments[0].to_file(use_cached=True)
                    embed = discord.Embed(title = f'A message was delete in #{message.channel} from {message.author}', description = message.content, colour = 0XFFFF00)#,timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.set_footer(text = f'Created at {convert_zone} | Deleted at {datetime.datetime.now()}')
                    # embed.set_image(url = f'attachment://{attachment.filename}')
                    await message_log_channel.send(embed = embed)

    except:
        message_id = payload.message_id
        with open ('Update_Message_Log.json') as Update_Message_Log_json:
            data = json.load(Update_Message_Log_json)
            for json_message in data['messages']:
                if json_message['id'] == message_id:
                    author = json_message['author']
                    channel = json_message['channel']
                    message = json_message['message']
                    created_at = json_message['created_at']
                    message_channel = client.get_channel(channel[2:-1])
                    message_author = guild.get_member(author[3:-1])
                    if message.startswith('.a') or message.startswith('.anonymity') or message.startswith('.anonymous'):
                        return
                    if message_channel != message_log_channel:
                        if message_channel == anonymous_channel or message_channel == rant_channel or message_channel == advising_channel:
                            if message.startswith('-r'):
                                return
                        if message_author != client.user:
                            if message not in list_of_commands:
                                embed = discord.Embed(title = f'A message was delete while update was in progress', description = f'Channel: {channel} From {author}\n{message}', 
                                colour = 0XFFFF00)#,timestamp = datetime.datetime.now(datetime.timezone.utc))
                                embed.set_footer(text = f'Created at {created_at} | Deleted at {datetime.datetime.now()}')
                                await message_log_channel.send(embed = embed)
                                status = True
            if status == False:
                await message_log_channel.send('A deleted message was out of scope. Sorry about that ')

@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def exam(ctx, channel : discord.TextChannel, role : discord.Role, space, date, time1, to , time2):
    month = int(re.split('/|-',date)[0])
    day = int(re.split('/|-',date)[1])
    year = int(re.split('/|-',date)[2])

    hour1 = int(re.split(':', time1)[0])
    hour2 = int(re.split(':', time2)[0])

    minute1 = int(re.split(':|am|pm', time1)[1])
    minute2 = int(re.split(':|am|pm', time2)[1])

    minute_reader1 = re.split(':|am|pm', time1)[1]
    minute_reader2 = re.split(':|am|pm', time2)[1]

    if 'am' in time1:
        if hour1 == 12:
            militaryhour1 = 0
        else:
            militaryhour1 = hour1
    if 'pm' in time1:
        if hour1 == 12:
            militaryhour1 = 12
        else:
            militaryhour1 = hour1 + 12

    if 'am' in time2:
        if hour2 == 12:
            militaryhour2 = 0
        else:
            militaryhour2 = hour2
    if 'pm' in time2:
        if hour2 == 12:
            militaryhour2 = 12
        else:
            militaryhour2 = hour2 + 12   

    start_time = datetime.datetime(year, month, day, militaryhour1, minute1, 0)
    end_time = datetime.datetime(year, month, day, militaryhour2, minute2, 0)
    
    open_exam_text = f'{channel.mention} has an exam from {militaryhour1}:{minute_reader1} on {month}/{day}/{year} to {militaryhour2}:{minute_reader2}'
    open_exam.append(open_exam_text)
 
    message = await ctx.send(f'You will now change the settings of #{channel} at {militaryhour1}:{minute_reader1} on {month}/{day}/{year} to {militaryhour2}:{minute_reader2} on {month}/{day}/{year}')
    await message.add_reaction('🗑️')
    
    while datetime.datetime.now() < start_time:
        await asyncio.sleep(1)
        use_message = await message.channel.fetch_message(message.id)
        if use_message.reactions[0].count > 1:
            await ctx.send(f"You have deleted the exam time for {channel.mention}, please re-enter another timeslot for this course's exam")
            return
        
    await ctx.send(f'The settings of #{channel} will now be changed to "only read".')
    await channel.send('Good luck with your final! You can do it!')
    await channel.set_permissions(role, read_messages = True, read_message_history = True, send_messages = False, connect = False)
    
    while datetime.datetime.now() < end_time:
        await asyncio.sleep(1)
    
    open_exam.remove(open_exam_text)
    await channel.send('Congrats you have finished, please keep in mind some students might still be taking the final but feel free to start chatting again.')
    await channel.set_permissions(role, read_messages = True, read_message_history = True, send_messages = True, connect = True)

@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def examL(ctx, channel : discord.TextChannel, role : discord.Role, space, date1, time1, to, date2, time2):
#need to pass in the specific channel (physics course) and the specific time to close it for (1hr, 2hr, 1 day, etc.)
    month1 = int(re.split('/|-',date1)[0])
    day1 = int(re.split('/|-',date1)[1])
    year1 = int(re.split('/|-',date1)[2])
 
    month2 = int(re.split('/|-',date2)[0])
    day2 = int(re.split('/|-',date2)[1])
    year2 = int(re.split('/|-',date2)[2])

    hour1 = int(re.split(':', time1)[0])
    hour2 = int(re.split(':', time2)[0])

    minute1 = int(re.split(':|am|pm', time1)[1])
    minute2 = int(re.split(':|am|pm', time2)[1])

    minute_reader1 = re.split(':|am|pm', time1)[1]
    minute_reader2 = re.split(':|am|pm', time2)[1]

    if 'am' in time1:
        if hour1 == 12:
            militaryhour1 = 0
        else:
            militaryhour1 = hour1
    if 'pm' in time1:
        if hour1 == 12:
            militaryhour1 = 12
        else:
            militaryhour1 = hour1 + 12

    if 'am' in time2:
        if hour2 == 12:
            militaryhour2 = 0
        else:
            militaryhour2 = hour2
    if 'pm' in time2:
        if hour2 == 12:
            militaryhour2 = 12
        else:
            militaryhour2 = hour2 + 12   

    start_time = datetime.datetime(year1, month1, day1, militaryhour1, minute1, 0)
    end_time = datetime.datetime(year2, month2, day2, militaryhour2, minute2, 0)
    
    open_exam_text = f'{channel.mention} has an exam from {militaryhour1}:{minute_reader1} on {month1}/{day1}/{year1} to {militaryhour2}:{minute_reader2} on {month2}/{day2}/{year2}'
    open_exam.append(open_exam_text)

    message = await ctx.send(f'You will now change the settings of #{channel} at {militaryhour1}:{minute_reader1} on {month1}/{day1}/{year1} to {militaryhour2}:{minute_reader2} on {month2}/{day2}/{year2}')
    
    await message.add_reaction('🗑️')
    
    while datetime.datetime.now() < start_time:
        await asyncio.sleep(1)
        use_message = await message.channel.fetch_message(message.id)
        if use_message.reactions[0].count > 1:
            await ctx.send(f"You have deleted the exam time for {channel.mention}, please re-enter another timeslot for this course's exam")
            return
        
    await ctx.send(f'The settings of #{channel} will now be changed to "only read".')
    await channel.send('Good luck with your final! You can do it!')
    await channel.set_permissions(role, read_messages = True, read_message_history = True, send_messages = False, connect = False)
    
    while datetime.datetime.now() < end_time:
        await asyncio.sleep(1)
    
    open_exam.remove(open_exam_text)
    await channel.send('Congrats you have finished, please keep in mind some students might still be taking the final but feel free to start chatting again.')
    await channel.set_permissions(role, read_messages = True, read_message_history = True, send_messages = True, connect = True)
     
@client.command()
@commands.has_any_role(founder_id, admin_id)
async def clear_role(ctx, role : discord.Role):
    guild = client.get_guild(guild_id)
    gaucho_role = guild.get_role(gaucho_id)
    graduate_role = guild.get_role(graduate_id)
    super_senior_role = guild.get_role(super_senior_id)
    senior_role = guild.get_role(senior_id)
    junior_role = guild.get_role(junior_id)
    sophomore_role = guild.get_role(sophomore_id)
    freshman_role = guild.get_role(freshman_id)
    role_members = role.members

    if role == gaucho_role or role == graduate_role or role == super_senior_role or role == senior_role or role == junior_role or role == sophomore_role or role == freshman_role or role == freshman_role:
        await ctx.send('Invalid role, please mention another role to clear.')
    if role != gaucho_role or role != graduate_role or role != super_senior_role or role != senior_role or role != junior_role or role != sophomore_role or role != freshman_role or role != freshman_role:
        for i in role_members:
            await i.remove_roles(role)
        
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def winner(ctx, channel : discord.TextChannel):
    messages = await channel.history(limit = None).flatten()
    unique_members = []
    not_in_server = []
    for i in messages:
        if i.author.mention not in unique_members:
            role_list = []
            try:
                for j in i.author.roles:
                    role_list.append(j.id)
                if not any(role in role_list for role in [founder_id, admin_id, treasurer_id, mod_id]):
                    unique_members.append(i.author.mention)
            except:
                if i.author.mention not in not_in_server:
                    not_in_server.append(i.author.mention)
                    channel = client.get_channel(bot_command_channel_id)
                    await channel.send(f'{i.author.mention} is no longer in the server')
                    print(f'{i.author.mention} is no longer in the server')
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
    embed = discord.Embed(title = 'Raffle: the following are entered', description = '\n'.join(unique_members), colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = image)
    await ctx.send(embed = embed)

    await asyncio.sleep(5)
    winner = unique_members[random.randint(0, len(unique_members)-1)]
    image = 'https://media.giphy.com/media/1Be435nPDxMFnsEq9r/giphy.gif'
    embed = discord.Embed(title = 'Raffle: WINNER', description = winner, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_image(url = image)
    #embed.set_thumbnail(url = image)
    await ctx.send(embed = embed)
    print(unique_members)

@client.command(aliases=['afind'])
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def anonymous_finder(ctx,message_id):
    status = False
    try:
        message_id = int(message_id)
    except:
        await ctx.send('Please use the id of the message.')
    if ctx.channel.id != bot_command_channel_id:
        await ctx.message.delete()
        message = await ctx.send("Please do not use this command here!")
        await message.delete(delay = 5)
    else:
        with open ('Anonymous_Log.json') as anonymous_log_json:
            data = json.load(anonymous_log_json)
            for json_message in data['anonymous_message']:
                if json_message['id'] == message_id:
                    author = json_message['author']
                    channel = json_message['channel']
                    message = json_message['message']
                    content = f'User: {author} \nChannel: {channel}\nMessage: {message}'
                    await ctx.send(content)
                    status = True
            if status == False:
                await ctx.send('There is no data on the message you selected.')

@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def ban(ctx, member : discord.Member , *, length):
    if 'hr' in length or 'hour' in length or 'hours' in length:
        hour = int(re.split('hr|hour|hours', length)[0])
        time = hour * 3600
    if 'min' in length or 'minutes' in length or 'mins' in length:
        minutes = int(re.split('min|minutes|mins', length)[0])
        time = minutes * 60
    if 'day' in length or 'days' in length:
        days = int(re.split('day|days', length)[0])
        time = days * 86400
    if 'week' in length or 'weeks' in length:
        week = int(re.split('week|weeks', length)[0])
        time = week * 604800
   
    member_roles = member.roles

    member_roles_list = []

    for role in member_roles:
        member_roles_list.append(role.id)

    guild = client.get_guild(guild_id)
    mod_role = guild.get_role(mod_id)
    treasurer_role = guild.get_role(treasurer_id)
    
    for i in member_roles_list[1:]:
        roles = guild.get_role(i)
        if roles == mod_role or roles == treasurer_role:
            await ctx.send('Invalid user due to having a mod role, please remove the role or select another user.')
            return
            
    #remove all roles except everyone
    for i in member_roles_list[1:]:
        roles = guild.get_role(i)
        await member.remove_roles(roles)
    
    ban_channel = client.get_channel(ban_channel_id)
    welcome_channel = client.get_channel(welcome_channel_id)
    await ban_channel.set_permissions(member, read_messages = True, send_messages = True, read_message_history = False)
    await welcome_channel.set_permissions(member, read_messages = False, send_messages = False)

    await asyncio.sleep(time)

    #add all removed roles
    for i in member_roles_list[1:]:
        roles = guild.get_role(i)
        await member.add_roles(roles)
        
    await ban_channel.set_permissions(member, overwrite = None)
    await welcome_channel.set_permissions(member, overwrite = None)
    
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def update(ctx):
    await ctx.message.delete()
    global update_status
    if ctx.channel.id != bot_command_channel_id:
        message = await ctx.send("Please do not use this command here!")
        await message.delete(delay = 5)
    else: 
        update_status = True
        await ctx.send('Scheduling update for 1 day in advance.')
        await asyncio.sleep(30) #for 24 hrs = 86400
        update_status = False
        await ctx.send('Update will soon begin!')

@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def helpA(ctx):
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
    embed = discord.Embed(title = 'Commands for this bot', description = 'When using these commands, begin your statement with "." followed by the name of the command',\
         colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = image)
    embed.add_field(name = 'announcement (post, annouce)', value = 'This command will send an announcment at a specfic time. Use today and now to send an announcement immediately. \
                    **.announcement <date (mm-dd-yyyy)> <time (hh:mm)am/pm> <announcement>**')
    embed.add_field(name = 'clear_role', value = 'This command is only available to the founder and admins. This command will clear all the members from role. The format is as follows: **.clear_role @<role_mention>**',
                    inline = False)
    embed.add_field(name = 'winner', value = 'This command is declearing a raffle winner for a specific channel.\
        The format is as follows: **.winner <#channel>**', inline = False)
    embed.add_field(name = 'update', value = 'Schedule an update a day in advance, this begins storing messages to allow for an easy transistion between updates.', inline = False)
    embed.add_field(name = 'anonymous_finder (afind)', value = "This command will only work in #bot-commands. The format has to follow `.afind 0123456789`. The integer is the message id, to get this\
        you must have Developer Mode enable. This only works for Broida's anonymous posts.", inline = False)
    embed.add_field(name = 'ban', value = 'This command will ban the member you mention for a certain amount of time, the least amount of time is 1 min. **.ban <member> <time>**', inline = False)
    embed.add_field(name = 'exam', value = 'This command is only available to admins and mods to close channels for a midterm or final. This command is for closing a channel for less than one day.\
        The format is as follows: **.exam <#channel> <@role> from <date(mm-dd-yyyy)> <start time(hh:mm)am/pm> to <end time(hh:mm)am/pm>**', inline = False)
    embed.add_field(name = 'examL', value = 'This command is similar to exam but provides closing a channel for more than one day. \
        the format fot this command is as follows: **.exam <#channel> <@role> from <first date(mm-dd-yyyy)> <start time(hh:mm)am/pm> to <second date (mm-dd-yyyy)> <end time(hh:mm)am/pm>**', inline = False)
    await ctx.send(embed = embed)



client.run('Token')