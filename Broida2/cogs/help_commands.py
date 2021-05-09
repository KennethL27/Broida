from discord.ext import commands
import datetime, random, discord
import cogs.variables as variables

class help_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.footers = ['Powered by yours turly', 'Powered by your tears', 'Powered by curved that helped you pass', "Powered by Broida's black hole", 'Powered by KennethL <3', 'Powered by hope',\
                    'Powered by perpetual motion', 'Powered by the bike lane', 'Powered by flat-eathers', 'Powered by ...', 'Loading...', 'Powered by Storke Tower', 'Powered by love']

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'How to use Broida', description = 'Type .help `command` to get more information about the command. All commands begin with `.`',\
            colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = '.help', value = 'Displays all commands available.')
        embed.add_field(name = '.help gaucho', value = 'Get all gaucho commands, which includes: .advising, .courses, .dates, .discords, .merch, open_exams, .physics')
        embed.add_field(name = '.ticket', value = 'See a situation that seem out of line with our guidelines notify staff by using ticket command.')
        embed.add_field(name = '.anonymous', value = 'Want to create a post anonymously, use this command to stay hidden.')
        embed.add_field(name = 'uptime', value = "Want to see how long Broida has been runing for, checkout how long Kenneth's Rasberry Pi has been running for.")
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    
    @help.command()
    async def gaucho(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Commands for all Gauchos', description = 'These commands do not require extra formatting',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = '.advising', value = 'Get the link to UCSB Physics Advising and links to make appointments with Jean Dill or Cooper.')
        embed.add_field(name = '.courses', value = 'Get the link and image to the 2020-21 Teaching Assignments.')
        embed.add_field(name = '.dates', value = 'Get the link to the full list of dates such as drop deadline or past times.')
        embed.add_field(name = '.discords', value = 'Find out other UCSB discord server like RPG at UCSB.')
        embed.add_field(name = '.merch', value = 'Get the link to the merch website.')
        embed.add_field(name = '.open_exams', value = 'Get the list of planned/current exams, this list is set to close their respective channels at the given time.')
        embed.add_field(name = '.physics', value = 'Get random physics facts.')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    
    @help.command()
    async def ticket(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Ticket Command', description = "Format: .ticket `@member` `Reason`\nThis command can be used anywhere in the server and Broida's DM.",
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Aliases', value = '.tic')
        embed.add_field(name = 'Example', value = '.ticket `@Kenneth Lara` This is an example of a ticket')
        embed.add_field(name = 'Direct Message', value = 'The same format is used when direct messaging Broida. However when taging a member use their discord username and #.')
        embed.add_field(name = 'Special DM Formatting', value = '*If the user has a space in their name use quotes around the username.*')
        embed.add_field(name = 'Direct Message Example', value = '.ticket "PhysicsLegends#6877" This is an example of a ticket submitted through DM')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    
    @help.command()
    async def anonymous(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Anonymous Command', description = "Format: .anonymous `Anonymous Message.`\nThis command can be used anywhere in the server and Broida's DM.",
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Aliases', value = '.anonymity\n.a')
        embed.add_field(name = 'Example', value = '.a This is my example of a anonymous message')
        embed.add_field(name = 'Direct Message', value = 'DM requires speical formatting. You must specific where you want the message to be sent to. Format: .a general-chat Anonymous Message')
        embed.add_field(name = 'Direct Message Example', value = '.a general-chat This is an example of an Anonymous Message being sent to the general chat.')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)

    # Staff help commands    

    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def staff(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Commands for staff members', description = 'These commands do not require extra formatting',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = '.announcement', value = 'This command allows you to create an announcement ahead of time.')
        embed.add_field(name = '.exam', value = 'Have a time of an exam make sure Broida knows.')
        embed.add_field(name = '.ban', value = 'This will ban someone, becareful.')
        embed.add_field(name = '.anonymous_finder', value = 'Someone anonymously posted bad things, find out who said it.')
        embed.add_field(name = '.clear_role', value = "It's that time of the quarter. Clear out the classes.")
        embed.add_field(name = '.winner', value = 'Have a prize you need to raffle off, lets see who won.')
        embed.add_field(name = '.events', value = 'Checkout the list of events Broida has.')
        embed.add_field(name = '.add_event', value = 'Need to set a reminder to staff members, let Broida remind you.')
        embed.add_field(name = '.meeting_notes', value = 'Checkout the list of meeting notes Broida has.')
        embed.add_field(name = '.add_meeting', value = 'Done with the weekly meeting, let Broida store it for you.')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def announcement(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Announcement Command', description = 'Format: .announcement "MM/DD/YYYY HH:MMam/pm" `Announcement`',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Aliases', value = '.anouce\n.post')
        embed.add_field(name = 'Example', value = '.post "5/8/2021 4:00pm" Here is an example of an announcement.')
        embed.add_field(name = 'Usage', value = f'This command only works in {self.bot.get_channel(variables.bot_command_channel_id).mention}.')
        embed.add_field(name = 'Additional Notes', value = 'After sending the command, Broida will send back a message to allow you to preview the message.\
             You have until the announcment is made to make any edits to the original message you sent.')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def exam(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Exam Command', description = 'Format: .exam `#course-channel @course-role` "MM/DD/YYYY HH:MMam/pm" "MM/DD/YYYY HH:MMam/pm"',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Example', value = '.exam `#phys-101` `@phys 101` "5/9/2021 11:00am" "5/10/2021 11:00am"')
        embed.add_field(name = 'Usage', value = f'This command only works in {self.bot.get_channel(variables.bot_command_channel_id).mention}.')
        embed.add_field(name = 'Additional Notes', value = "Unlike the previous version of the exam command, this command coveres multi-day exams.\
             You have until the exam goes live to cancel the command by clicking on the trash emoji under the Broida's message.", inline = False)
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def ban(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Ban Command', description = 'Format: .ban `@member` length',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Example', value = '.ban `@user` 1hr')
        embed.add_field(name = 'Usage', value = f'This command only works in {self.bot.get_channel(variables.bot_command_channel_id).mention}.')
        embed.add_field(name = 'Additional Notes', value = 'The length must be speficied by attacking either: minutes, min, mins, hour, hours, hrs, day, days, week, or weeks', inline = False)
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def anonymous_finder(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Anonymous Finder Command', description = 'Format: .afind `message_ID`',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Aliases', value = '.afind')
        embed.add_field(name = 'Example', value = '.afind 123456789')
        embed.add_field(name = 'Usage', value = f'This command only works in {self.bot.get_channel(variables.bot_command_channel_id).mention}.')
        embed.add_field(name = 'Additional Notes', value = 'In order to get the message ID you must have developer mode enabled. To enable head to settings -> Advanced -> toggle Developer Mode.\
             Once enabled simply right click (or press and hold) on the message and select "Copy ID".')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def clear_role(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Clear Role Command', description = 'Format: .clear_role `@role`',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Example', value = '.clear_role `@phys 101`')
        embed.add_field(name = 'Usage', value = f'This command only works in {self.bot.get_channel(variables.bot_command_channel_id).mention}.')
        embed.add_field(name = 'Additional Notes', value = 'Once this command is sent, Broida will take some time removing the role from each memeber.\
             The more members with that role, the longer it will take', inline = False)
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def winner(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Winner Command', description = 'Format: .winner `#channel`',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = 'Example', value = '.winner `#ama-ask-questions-channel`')
        embed.add_field(name = 'Usage', value = f'This command works anywhere in the sever.')
        embed.add_field(name = 'Additional Notes', value = 'Once this command is sent, Broida will try to mention everyone that sent a message in channel provided.\
             Some of the mentions might be numbers, this is normal.', inline = False)
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def events(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Events Commands', description = 'There are 2 event commands: .events and .add_event',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = '.events', value = 'This command allows you to view all future events and only works in the staff channel. This command does not have any futher formatting.')
        embed.add_field(name = '.add_event', value = 'This command allows you to add events to Broida. Format: .add_events "event name" "event time" "@mention1" ... "@mention5"', inline = False)
        embed.add_field(name = '.add_event Usage', value = f'This command only works in the staff channel.')
        embed.add_field(name = '.add_event Additional Notes', value = 'Once this command is sent, you will have 10 minutes to change anything about the event simply by editing your message.\
             You are also allow to mention up to 5 memebers or roles. *if you dont want to use any mentions, you may leave them blank*')
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)
    @help.command()
    @commands.has_any_role(variables.founder_id, variables.admin_id, variables.treasurer_id, variables.mod_id)
    async def meeting_notes(self, ctx):
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
        embed = discord.Embed(title = 'Meeting Notes Commands', description = 'There are 2 event commands: .meeting_notes and .add_meeting',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = image)
        embed.add_field(name = '.meeting_notes', value = 'This command allows you to view all meeting notes and only works in the staff channel. Format: .meeting_notes "date"')
        embed.add_field(name = '.meeting_notes Usage', value = f'This command only works in the staff channel.')
        embed.add_field(name = '.meeting_notes Additional Notes', value = 'Using .meeting_notes allows you to view all notes available by dates.\
             To view specific Notes, simply copy and past the date shown into your command, ie. .meeting_notes "date".', inline = False)
        embed.add_field(name = '.add_meeting', value = 'This command allows you to add meeting notes to Broida. Format: .add_meeting `Notes`')
        embed.add_field(name = '.add_meeting Usage', value = f'This command only works in the staff channel.')
        embed.add_field(name = '.add_meeting Additional Notes', value = 'Once this command is sent, you will have 10 minutes to change anything about the event simply by editing your message.',
                        inline = False)
        embed.set_footer(text = self.footers[random.randint(0, len(self.footers) - 1)])
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(help_commands(bot))
    print("Help Commands Online\n")