from discord.ext import commands
import datetime, discord, json
from dateutil import tz
import cogs.variables as variables

class event_cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def write_json(self, data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    async def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        guild = self.bot.get_guild(variables.guild_id)
        message_log_channel = self.bot.get_channel(variables.message_log_id)
        anonymous_channel = self.bot.get_channel(variables.anonymous_id)
        rant_channel = self.bot.get_channel(variables.rant_id)
        advising_channel = self.bot.get_channel(variables.advising_channel_id)
        message = payload.cached_message
        status = False

        try:
            if message.content.startswith('.a ') or  message.content.startswith('.anonymity') or message.content.startswith('.anonymous') or message.content.startswith('.pexam') or message.content.startswith('.meeting_notes'):
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
                if message.author != self.bot.user:
                    if message.content not in variables.list_of_commands:
                        embed = discord.Embed(title = f'A message was delete in #{message.channel} from {message.author}', description = message.content, colour = 0XFFFF00)
                        embed.set_footer(text = f'Created at {convert_zone} | Deleted at {datetime.datetime.now()}')
                        await message_log_channel.send(embed = embed)

        except:
            message_id = payload.message_id
            data = await self.open_json('JSONdata/Update_Message_Log.json')
            for json_message in data['messages']:
                if json_message['id'] == message_id:
                    author = json_message['author']
                    channel = json_message['channel']
                    message = json_message['message']
                    created_at = json_message['created_at']
                    message_channel = self.bot.get_channel(channel[2:-1])
                    message_author = guild.get_member(author[3:-1])
                    if message.startswith('.a') or message.startswith('.anonymity') or message.startswith('.anonymous'):
                        return
                    if message_channel != message_log_channel:
                        if message_channel == anonymous_channel or message_channel == rant_channel or message_channel == advising_channel:
                            if message.startswith('-r'):
                                return
                        if message_author != self.bot.user:
                            if message not in variables.list_of_commands:
                                embed = discord.Embed(title = f'A message was delete while update was in progress', description = f'Channel: {channel} From {author}\n{message}', 
                                colour = 0XFFFF00)
                                embed.set_footer(text = f'Created at {created_at} | Deleted at {datetime.datetime.now()}')
                                await message_log_channel.send(embed = embed)
                                status = True
            if status == False:
                await message_log_channel.send('A deleted message was out of scope. Sorry about that ')

    @commands.Cog.listener('on_message')
    async def on_message(self,message):
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        utc = datetime.datetime.strptime(str(message.created_at)[:-7], "%Y-%m-%d %H:%M:%S")
        utc = utc.replace(tzinfo = from_zone)
        convert_zone = str(utc.astimezone(to_zone))
        data = await self.open_json("JSONdata/Bot_Info.json")
        update_status = data["update-status"]
        if update_status is False:
            return
        else:
            #append to delete_message_log
            message_id = message.id
            user_name = message.author
            channel = message.channel
            user_message = message.content
            data = await self.open_json("JSONdata/Update_Message_Log.json")
            message_log = data['messages']
            new_entry = {"id": message_id, "author": user_name.mention, "channel": channel.mention, "created_at": convert_zone, "message": user_message}
            message_log.append(new_entry)
            await self.write_json(data, "JSONdata/Update_Message_Log.json")

    @commands.Cog.listener()
    async def on_member_join(self, user):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        rules_channel = self.bot.get_channel(775492454338002994)
        manual_channel = self.bot.get_channel(760907945646751804)
        embed = discord.Embed(colour = 0X003560)
        embed.add_field(name = 'Welcome!', value = f'Thank you {user.mention} for joining the UCSB Physics Server! Please read and follow our {rules_channel.mention} while being apart of this community.\n\n\
            If you are a **current UCSB student** or apart of the **UCSB Faculty** please fill out this [form](https://forms.gle/jAsx4TKBeERPQT6K9) to gain access \n\n\
                If you are a **prospective student** and wish to take a small view at UCSB Physics then please fill out this [form](https://forms.gle/bd77bphN1qbVWw7x8)')
        embed.add_field(name = 'New to Discord?', value = f"If you are new to Discord and want to find out more about discord's functionalty please head over to {manual_channel.mention}.")
        embed.set_thumbnail(url = image)
        await user.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(variables.guild_id)
        gaucho_role = guild.get_role(variables.gaucho_id)
        data = await self.open_json("JSONdata/Bot_Info.json")
        avoid_gaucho_member = data["avoid-gaucho-member"]
        if gaucho_role not in before.roles and gaucho_role in after.roles and before.id not in avoid_gaucho_member: # going to need to have avoid_gaucho_member info in bot_info.json
            image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
            embed = discord.Embed(colour = 0X003560)
            rules_channel = self.bot.get_channel(775492454338002994)
            manual_channel = self.bot.get_channel(760907945646751804)
            embed.add_field(name = 'Thank you!', value = f'Thank you {before.mention} for filling out our verification form! You should now have access to our Server, \
                if you have any questions feel free to reach out to any of our moderators. \n\nIf you havent already please read and follow our {rules_channel.mention} while being apart of this community.')
            embed.add_field(name = 'New to Discord?', value = f"If you are new to Discord and want to find out more about discord's functionalty please head over to {manual_channel.mention}.")
            embed.set_thumbnail(url = image)
            await before.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, user):
        channel = self.bot.get_channel(variables.bot_command_channel_id)
        await channel.send(f'Oh no! Looks like {user} has left the server. Please remove this user from the verification list.')

def setup(bot):
    bot.add_cog(event_cogs(bot))
    print("Event Cogs Online\n")