from discord.ext import commands
import datetime, discord, time, asyncio
import cogs.variables as variables

class ticket_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['tic'])
    async def ticket1(self, ctx, member : discord.Member, * , reason):
        #for DMs, to mention the user use their discord username (not nickname) along with their discriminator. ie PhysicsLegends#6877
        guild = self.bot.get_guild(variables.guild_id)
        if ctx.channel in guild.text_channels:
            await ctx.message.delete()
        channel = self.bot.get_channel(variables.ticket_channel_id)
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
            if use_message.reactions[0].count > 1:
                variables.avoid_gaucho_member.append(member.id)
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
                
                #need to make ban channel open for this user to discuss any information. Also remove access to new user welcome channel.
                ban_channel = self.bot.get_channel(variables.ban_id)
                welcome_channel = self.bot.get_channel(variables.welcome_id)
                await ban_channel.set_permissions(member, read_messages = True, send_messages = True, read_message_history = False)
                await welcome_channel.set_permissions(member, read_messages = False, send_messages = False)
                
                await asyncio.sleep(60) #24 hours ban: in seconds 86400
                
                #add all removed roles
                for i in member_roles_list[1:]:
                    roles = guild.get_role(i)
                    await member.add_roles(roles)
                
                await ban_channel.set_permissions(member, overwrite = None)
                await welcome_channel.set_permissions(member, overwrite = None)
                variables.avoid_gaucho_member.remove(member.id)
                return

            '''for warning, opt 2'''
            #going to need to send the member a DM warning him. Maybe give an option to what rule was broken, for the warning to be enacted
            if use_message.reactions[1].count > 1:
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
                    if use_message_warn.reactions[0].count > 1:
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
                    elif use_message_warn.reactions[1].count > 1:
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
                    elif use_message_warn.reactions[2].count > 1:
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
                    elif use_message_warn.reactions[3].count > 1:
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
                    elif use_message_warn.reactions[4].count > 1:
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
                    elif use_message_warn.reactions[5].count > 1:
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
                    elif use_message_warn.reactions[6].count > 1:
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
            if use_message.reactions[2].count > 1:
                #if 2 people react with red then send a message to the ticket channel stating that nothing will happen, provide a summary still.
                await message.delete()
                embed = discord.Embed(title = '**TICKET EVENT SUMMARY**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                    This ticket is begin ticketed against: {member.mention}',colour = 0X00FF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
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

def setup(bot):
    bot.add_cog(ticket_commands(bot))
    print("Ticket Commands Online\n")