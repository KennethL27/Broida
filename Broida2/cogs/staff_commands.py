from discord.ext import commands
import datetime, asyncio
import cogs.variables as variables

class staff_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

def setup(bot):
    bot.add_cog(staff_commands(bot))
    print("Anonymous Commands Online\n")