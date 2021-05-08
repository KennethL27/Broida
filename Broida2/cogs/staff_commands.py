from discord.ext import commands
import datetime, asyncio, discord, re, json, random
import cogs.variables as variables

class staff_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def write_json(self, data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    async def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    @commands.command(aliases = ['anouce', 'post'])
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id)
    async def announcement(self, ctx, time : str, *, announcement):
        original_message = ctx.message
        channel = self.bot.get_channel(variables.announcement_channel_id)
        if ctx.channel.id != variables.bot_command_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel to create announcments. Please use {self.bot.get_channel(variables.bot_command_channel_id).mention}', delete_after = 5)
            return
        if time == 'now':
            await channel.send(content = announcement)
        else:
            try:
                release = datetime.datetime.strptime(time, '%m-%d-%Y %I:%M%p')
            except:
                release = datetime.datetime.strptime(time, '%m/%d/%Y %I:%M%p')
            
            message = await ctx.send(f'__The post will look like:__\n{announcement}')
            await message.add_reaction('🗑️')

            while datetime.datetime.now() < release: #holds off the change in permission until the start time
                await asyncio.sleep(1)
                edit_message_time = original_message.edited_at
                if not edit_message_time:
                    pass
                else:
                    command_message_edit = original_message.content
                    new_announcement = command_message_edit.split('"', 2)[2][1:]
                    await message.edit(content = f'__The post will look like:__\n{new_announcement}')

                use_message = await message.channel.fetch_message(message.id)
                if use_message.reactions[0].count > 1:
                    await ctx.send(f"You have deleted the announcement, please resend your announcement to be posted.")
                    return 
            try:
                await channel.send(content = new_announcement)
            except:
                await channel.send(content = announcement)
    
    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id)
    async def clear_role(self, ctx, role : discord.Role):
        if ctx.channel.id != variables.bot_command_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel to clear roles. Please use {self.bot.get_channel(variables.bot_command_channel_id).mention}', delete_after = 5)
            return
        guild = self.bot.get_guild(variables.guild_id)
        gaucho_role = guild.get_role(variables.gaucho_id)
        graduate_role = guild.get_role(variables.graduate_id)
        super_senior_role = guild.get_role(variables.super_senior_id)
        senior_role = guild.get_role(variables.senior_id)
        junior_role = guild.get_role(variables.junior_id)
        sophomore_role = guild.get_role(variables.sophomore_id)
        freshman_role = guild.get_role(variables.freshman_id)
        role_members = role.members
        if role == gaucho_role or role == graduate_role or role == super_senior_role or role == senior_role or role == junior_role or role == sophomore_role or role == freshman_role or role == freshman_role:
            await ctx.send('Invalid role, please mention another role to clear.')
        if role != gaucho_role or role != graduate_role or role != super_senior_role or role != senior_role or role != junior_role or role != sophomore_role or role != freshman_role or role != freshman_role:
            for i in role_members:
                await i.remove_roles(role)

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def ban(self, ctx, member : discord.Member , *, length):
        variables.avoid_gaucho_member.append(member.id)
        if ctx.channel.id != variables.bot_command_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel for that command. Please use {self.bot.get_channel(variables.bot_command_channel_id).mention}', delete_after = 5)
            return
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

        guild = self.bot.get_guild(variables.guild_id)
        mod_role = guild.get_role(variables.mod_id)
        treasurer_role = guild.get_role(variables.treasurer_id)

        for i in member_roles_list[1:]:
            roles = guild.get_role(i)
            if roles == mod_role or roles == treasurer_role:
                await ctx.send('Invalid user due to having a mod role, please remove the role or select another user.')
                return

        #remove all roles except everyone
        for i in member_roles_list[1:]:
            roles = guild.get_role(i) 
            await member.remove_roles(roles)

        ban_channel = self.bot.get_channel(variables.ban_id)
        welcome_channel = self.bot.get_channel(variables.welcome_id)
        await ban_channel.set_permissions(member, read_messages = True, send_messages = True, read_message_history = False)
        await welcome_channel.set_permissions(member, read_messages = False, send_messages = False)
        
        await asyncio.sleep(time) 
        
        #add all removed roles
        for i in member_roles_list[1:]:
            roles = guild.get_role(i)
            await member.add_roles(roles)
        
        await ban_channel.set_permissions(member, overwrite = None)
        await welcome_channel.set_permissions(member, overwrite = None)
        variables.avoid_gaucho_member.remove(member.id)

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def add_meeting(self, ctx, *, notes):
        if ctx.channel.id != variables.staff_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel for creating meeting notes. Please use {self.bot.get_channel(variables.staff_channel_id).mention}', delete_after = 5)
            return

        await ctx.reply('*You have 10 minutes to make any edits before the notes are submitted*')
        original_message = ctx.message
        release = ctx.message.created_at.now() + datetime.timedelta(0,600) # 600secs = 10 minutes
        while datetime.datetime.now() < release:
            await asyncio.sleep(1)
            edit_message_time = original_message.edited_at
            if not edit_message_time:
                note_message = notes
            else:
                note_message = original_message.content[13:]
        data = await self.open_json("JSONdata/Bot_Info.json")
        data["meeting-notes"].append({"date" : str(ctx.message.created_at.now().date()), f"note-entry" : note_message})
        await self.write_json(data, "JSONdata/Bot_Info.json")

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def meeting_notes(self, ctx, date = None):
        if ctx.channel.id != variables.staff_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel for viewing meeting notes. Please use {self.bot.get_channel(variables.staff_channel_id).mention}', delete_after = 5)
            return

        data = await self.open_json("JSONdata/Bot_Info.json")
        
        if date == None:
            embed = discord.Embed(colour = 0x008000, description = "To view an entire meeting note please use `.meeting_notes 'copy and paste a valid date'`")
            for data_date in data["meeting-notes"]:
                embed.add_field(name = data_date["date"], value = f'{data_date["note-entry"][:20]}...')
            await ctx.send(embed = embed)
        else:
            for data_date in data["meeting-notes"]:
                embed = discord.Embed(colour = 0x008000)
                if data_date["date"].replace('-', '') == date.replace('/', '').replace('-',''):
                    embed.add_field(name = data_date["date"], value = data_date["note-entry"])
                    await ctx.send(embed = embed)

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def winner(self, ctx, channel : discord.TextChannel):
        messages = await channel.history(limit = None).flatten()
        unique_members = []
        not_in_server = []
        for i in messages:
            if i.author.mention not in unique_members:
                role_list = []
                try:
                    for j in i.author.roles:
                        role_list.append(j.id)
                    if not any(role in role_list for role in [variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id]):
                        unique_members.append(i.author.mention)
                except:
                    if i.author.mention not in not_in_server:
                        not_in_server.append(i.author.mention)
                        channel = self.bot.get_channel(variables.bot_command_channel_id)
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
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(staff_commands(bot))
    print("Anonymous Commands Online\n")