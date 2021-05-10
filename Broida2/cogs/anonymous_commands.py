from discord.ext import commands
import discord, json, random
import cogs.variables as variables

class anonymous_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delete_counter = 0
        self.user_list = []
        self.generated_user = []

    async def write_json(self, data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    async def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    @commands.command(aliases=['anonymity','a'])
    async def anonymous(self, ctx,*,user_message):
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

            guild = self.bot.get_guild(variables.guild_id)
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

        if user_name not in self.user_list:
            user = random.randint(0,9999)
            self.user_list.append(user_name)
            self.generated_user.append(f'User{user}')

            if not(isinstance(ctx.channel, discord.channel.DMChannel)):
                await ctx.message.delete()
            anonymous_message = await channel.send(f'User{user}: {user_message}')
            self.delete_counter = self.delete_counter + 1
            anonymous_message_id = anonymous_message.id
            
            data = await self.open_json("JSONdata/Anonymous_Log.json")
            message_log = data['anonymous_message']
            new_entry = {"id": anonymous_message_id, "author": user_name.mention, "channel": channel.mention, "message": user_message}
            message_log.append(new_entry)
            await self.write_json(data, "JSONdata/Anonymous_Log.json")

        elif user_name in self.user_list:
            for i in self.user_list:
                if i == user_name:

                    if not(isinstance(ctx.channel, discord.channel.DMChannel)):
                        await ctx.message.delete()
                    anonymous_message = await channel.send(f'{self.generated_user[k]}: {user_message}')
                    self.delete_counter = self.delete_counter + 1
                    anonymous_message_id = anonymous_message.id

                    data = await self.open_json("JSONdata/Anonymous_Log.json")
                    message_log = data['anonymous_message']
                    new_entry = {"id": anonymous_message_id, "author": user_name.mention, "channel": channel.mention, "message": user_message}
                    message_log.append(new_entry)
                    await self.write_json(data, "JSONdata/Anonymous_Log.json")

                k = k + 1
        if self.delete_counter == 30:
            self.user_list.clear()
            self.generated_user.clear()
            self.delete_counter = 0

    @anonymous.error
    async def error_anonymous(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send("Sorry I can't send that message. For more information use `.help anonymous`")

    @commands.command(aliases=['afind'])
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def anonymous_finder(self, ctx, message_id):
        status = False
        try:
            message_id = int(message_id)
        except:
            await ctx.send('Please use the id of the message.')
        if ctx.channel.id != variables.bot_command_channel_id:
            await ctx.message.delete()
            message = await ctx.send("Please do not use this command here!")
            await message.delete(delay = 5)
        else:
            data = await self.open_json('JSONdata/Anonymous_Log.json')
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

    @anonymous_finder.error
    async def error_anonymous_finder(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("Sorry you don't have the required Role to use that command, to view your available commands use `.help`")
        elif isinstance(error, commands.MissingRequiredArgument):
            if ctx.channel.id != variables.bot_command_channel_id:
                await ctx.message.delete()
                await ctx.send("Please do not use this command here!", delete_after = 5)
                return
            await ctx.send("Sorry I couldn't execute that. For more information use `.help anonymous_finder`")

def setup(bot):
    bot.add_cog(anonymous_commands(bot))
    print("Anonymous Commands Online\n")