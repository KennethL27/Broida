from discord.ext import commands
import json, datetime, asyncio, discord
from threading import Thread
import cogs.variables as variables

class exam_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def write_json(self, data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    async def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    async def exam_execution(self, channel, role, start_date, end_date, index):
        guild = self.bot.get_guild(variables.guild_id)
        channel = self.bot.get_channel(channel)
        role = guild.get_role(role)
        bot_command_channel = self.bot.get_channel(variables.bot_command_channel_id)

        try:
            start_datetime = datetime.datetime.strptime(start_date, '%m-%d-%Y %I:%M%p')
        except:
            start_datetime = datetime.datetime.strptime(start_date, '%m/%d/%Y %I:%M%p')

        try:
            end_datetime = datetime.datetime.strptime(end_date, '%m-%d-%Y %I:%M%p')
        except:
            end_datetime = datetime.datetime.strptime(end_date, '%m/%d/%Y %I:%M%p')

        open_exam_text = f'{channel.mention} has an exam from {start_date} to {end_date}'
        variables.open_exam.append(open_exam_text)

        message = await bot_command_channel.send(f'The settings for #{channel} from {start_date} to {end_date} will have an exam. This message is being sent becuase Broida had to restart.')

        await message.add_reaction('🗑️')
        
        while datetime.datetime.now() < start_datetime:
            await asyncio.sleep(1)
            use_message = await message.channel.fetch_message(message.id)
            if use_message.reactions[0].count > 1:
                await bot_command_channel.send(f"You have deleted the exam time for #{channel.mention}, please re-enter another timeslot for this course's exam.")
                # remove it from the json file
                data = await self.open_json('JSONdata/Bot_Info.json')
                data["exam"].pop(index)
                await self.write_json(data, 'JSONdata/Bot_Info.json')
                return 
        
        await bot_command_channel.send(f'The settings of #{channel} will now be changed to "only read".')
        await channel.send('Good luck with your final! You can do it')
        await channel.set_permissions(role, read_messages= True, read_message_history = True,send_messages = False, connect = False)

        while datetime.datetime.now() < end_datetime:
            await asyncio.sleep(1)
        
        variables.open_exam.remove(open_exam_text)
        await channel.send('Congrats you have finished, please keep in mind some students might still be taking the final but feel free to start chatting again.')
        await channel.set_permissions(role, read_messages= True, read_message_history = True,send_messages = True, connect = True)
        # remove it from the json file
        data = await self.open_json('JSONdata/Bot_Info.json')
        data["exam"].pop(index)
        await self.write_json(data, 'JSONdata/Bot_Info.json')

    @commands.Cog.listener()
    async def on_ready(self):
        variables.open_exam.clear()
        data = await self.open_json('JSONdata/Bot_Info.json')
        index = 0
        for json_exam in data['exam']:
            asyncio.get_event_loop().create_task(self.exam_execution(json_exam["course-channel"], json_exam["course-role"], json_exam["start-date"], json_exam["end-date"], index))
            index = index + 1

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def exam(self, ctx, channel : discord.TextChannel, role : discord.Role, start_date : str, end_date : str):
        if ctx.channel.id != variables.bot_command_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel for creating exam times. Please use {self.bot.get_channel(variables.bot_command_channel_id).mention}', delete_after = 5)
            return

        try:
            start_datetime = datetime.datetime.strptime(start_date, '%m-%d-%Y %I:%M%p')
        except:
            start_datetime = datetime.datetime.strptime(start_date, '%m/%d/%Y %I:%M%p')

        try:
            end_datetime = datetime.datetime.strptime(end_date, '%m-%d-%Y %I:%M%p')
        except:
            end_datetime = datetime.datetime.strptime(end_date, '%m/%d/%Y %I:%M%p')

        data = await self.open_json('JSONdata/Bot_Info.json')
        data["exam"].append({"start-date" : start_date, "end-date": end_date, "course-channel": channel.id, "course-role" : role.id})
        await self.write_json(data, 'JSONdata/Bot_Info.json')

        open_exam_text = f'{channel.mention} has an exam from {start_date}  to {end_date}'
        variables.open_exam.append(open_exam_text)

        message = await ctx.send(f'You will now change the settings of #{channel} from {start_date} to {end_date}')

        await message.add_reaction('🗑️')

        while datetime.datetime.now() < start_datetime:
            await asyncio.sleep(1)
            use_message = await message.channel.fetch_message(message.id)
            if use_message.reactions[0].count > 1:
                await ctx.send(f"You have deleted the exam time for #{channel.mention}, please re-enter another timeslot for this course's exam.")
                data = await self.open_json('JSONdata/Bot_Info.json')
                index = 0
                for exam_entry in data["exam"]:
                    if exam_entry["course-channel"] == channel.id and exam_entry["course-role"] == role.id and exam_entry["start-date"] == start_date and exam_entry["end-date"] == end_date:
                        data["exam"].pop(index)
                        await self.write_json(data, 'JSONdata/Bot_Info.json')
                    else:
                        index = index + 1
                return 
        
        await ctx.send(f'The settings of #{channel} will now be changed to "only read".')
        await channel.send('Good luck with your final! You can do it')
        await channel.set_permissions(role, read_messages= True, read_message_history = True,send_messages = False, connect = False)

        while datetime.datetime.now() < end_datetime:
            await asyncio.sleep(1)
        
        variables.open_exam.remove(open_exam_text)
        await channel.send('Congrats you have finished, please keep in mind some students might still be taking the final but feel free to start chatting again.')
        await channel.set_permissions(role, read_messages= True, read_message_history = True,send_messages = True, connect = True)
        data = await self.open_json('JSONdata/Bot_Info.json')
        index = 0
        for exam_entry in data["exam"]:
            if exam_entry["course-channel"] == channel.id and exam_entry["course-role"] == role.id and exam_entry["start-date"] == start_date and exam_entry["end-date"] == end_date:
                data["exam"].pop(index)
                await self.write_json(data, 'JSONdata/Bot_Info.json')
            else:
                index = index + 1

    @exam.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if ctx.channel.id != variables.bot_command_channel_id:
                await ctx.message.delete()
                await ctx.send(f'Sorry please do not use this channel for creating exam times. Please use {self.bot.get_channel(variables.bot_command_channel_id).mention}', delete_after = 5)
            else:
                await ctx.send("Please enter all arguments. To get more information about this command use `.help exam`")
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send("Sorry you don't have the required Role to use that command, to view your available commands use `.help`")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send(f'Sorry I could not find that channel. Please mention the channel. (ie. {self.bot.get_channel(variables.bot_command_channel_id).mention})')
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send(f'Sorry I could not find that role. Please mention the role. (ie. {self.bot.get_guild(variables.guild_id).get_role(variables.bot_role_id).mention})')
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"Sorry I couldn't add that exam time. Please use the correct format for exam. Use `.help exam` to get more information.\n{error}")
        else:
            raise error

    @commands.command()
    async def open_exams(self, ctx):
        embed = discord.Embed(title = 'Exam Dates', description = '',
                                colour = 0X003560,
                                timestamp = datetime.datetime.now(datetime.timezone.utc)) 
        data = await self.open_json('JSONdata/Bot_Info.json')
        exams = data["exam"]
        if len(exams) == 0:
            embed.add_field(name = 'Open Exam', value = 'There is no exams planned at this time.')
            await ctx.send(embed = embed)
        else:
            for exam in exams:
                exam_channel = self.bot.get_channel(exam["course-channel"])
                embed.add_field(name = exam_channel.name, value = f'From: {exam["start-date"]} To: {exam["end-date"]}')
            await ctx.send(embed = embed)
            
def setup(bot):
    bot.add_cog(exam_commands(bot))
    print("Exam Commands Online\n")