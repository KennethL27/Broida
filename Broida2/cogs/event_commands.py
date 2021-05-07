from discord.ext import commands
import datetime, asyncio, json, discord
import cogs.variables as variables

class event_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def write_json(self, data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    async def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    @commands.Cog.listener()
    async def on_ready(self):
        for i in range(1000000000):
            event_date_list = []
            event_name_list = []
            event_mentions = []
            data = await self.open_json('JSONdata/Bot_Info.json')
            for json_event in data['event']:
                event_date_list.append(json_event["date"])
                event_name_list.append(json_event["event-name"])
                event_mentions.append(json_event["mentions"])
            bot_command_channel = self.bot.get_channel(variables.bot_command_channel_id)
            datetime_now = datetime.datetime.now()
            name_index = 0
            for date_string in event_date_list:
                try:
                    date = datetime.datetime.strptime(date_string, '%m-%d-%Y %I:%M%p')
                except:
                    date = datetime.datetime.strptime(date_string, '%m/%d/%Y %I:%M%p')
                if datetime_now > date:
                    embed = discord.Embed(title = f'EVENT REMINDER', description = f'This reminder is for **{event_name_list[name_index]}**', 
                        colour = 0Xfdbf32)
                    embed.set_footer(text = f'Timestamp - {datetime.datetime.now()}')
                    if 'Null' not in event_mentions[name_index]: 
                        mentions = event_mentions[name_index].replace('None', '').replace(',', '')
                        embed.add_field(name = 'Mentions', value = mentions)
                    await bot_command_channel.send(embed = embed)
                    data["event"].pop(name_index)
                    await self.write_json(data, 'JSONdata/Bot_Info.json')
                    break
                name_index = name_index + 1
            await asyncio.sleep(30)

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def add_event(self, ctx, event_name : str, event_time : str, mention1 = None, mention2 = None, mention3 = None, mention4 = None, mention5 = None):
        if ctx.channel.id != variables.staff_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel for creating events. Please use {self.bot.get_channel(variables.staff_channel_id).mention}', delete_after = 5)
            return
        if mention1 == None:
            mention1 = 'Null'
        await ctx.reply('*You have 10 minutes to make any edits before the event is submitted*')
        original_message = ctx.message
        release = ctx.message.created_at.now() + datetime.timedelta(0,6) # 600secs = 10 minutes
        while datetime.datetime.now() < release:
            await asyncio.sleep(1)
            edit_message_time = original_message.edited_at
            if not edit_message_time:
                pass
            else:
                list_of_messages = ctx.message.content.split('"')
                event_time = list_of_messages[3]
                event_name = list_of_messages[1]
                list_of_mentions = list_of_messages[4].split()
                try:
                    mention1 = list_of_mentions[0]
                    mention2 = list_of_mentions[1]
                    mention3 = list_of_mentions[2]
                    mention4 = list_of_mentions[3]
                    mention5 = list_of_mentions[4]
                except:
                    pass
        data = await self.open_json('JSONdata/Bot_Info.json')
        data["event"].append({"date" : event_time, "event-name": event_name, "mentions": f'{mention1}, {mention2}, {mention3}, {mention4}, {mention5}'})
        await self.write_json(data, 'JSONdata/Bot_Info.json')

    @commands.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def events(self, ctx):
        if ctx.channel.id != variables.staff_channel_id:
            await ctx.message.delete()
            await ctx.send(f'Sorry please do not use this channel for creating events. Please use {self.bot.get_channel(variables.staff_channel_id).mention}', delete_after = 5)
            return
        else:
            events = await self.open_json('JSONdata/Bot_Info.json')
            embed = discord.Embed(title = 'Events', description = '',
                                    colour = 0X003560,
                                    timestamp = datetime.datetime.now(datetime.timezone.utc)) 
            for event in events["event"]:
                embed.add_field(name = event["event-name"], value = f'Date: {event["date"]}')
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(event_commands(bot))
    print("Users' Commands Online\n")