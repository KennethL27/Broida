from discord.ext import commands
import discord, datetime, random, json

class user_static_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def write_json(self, data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    async def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    @commands.command(aliases = ['classes', 'class', 'schedule'])
    async def courses(self, ctx):
        embed = discord.Embed(title = 'Proposed Courses for 20-21', url = 'https://www.physics.ucsb.edu/resources/teachingassignments', colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif')
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/772690834151571506/782475543404347422/Screenshot_20201128-231814_Drive.jpg')
        await ctx.send(embed = embed) 

    @commands.command()
    async def advising(self, ctx):
        url = 'https://www.physics.ucsb.edu/education/undergrad/advising-help'
        embed = discord.Embed(title = 'UCSB Physics Advising', url = url, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name = '__Schedule Meeting with Jean Dill__', value = 'https://shoreline.ucsb.edu/meetings/1336841/JDOfficeHours', inline = False)
        embed.add_field(name = '__Schedule Meeting with Earnest Cooper Jr.__', value = 'https://shoreline.ucsb.edu/meetings/1336823/Coopersadvisinghours', inline = False)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/794516513730068510/unknown.png')
        await ctx.send(embed = embed)

    @commands.command()
    async def dates(self, ctx):
        url = 'https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/registration-pass-dates/2020-2021-registration-pass-times'
        embed = discord.Embed(title = 'UCSB 2020-2021 Registration Pass Times/Important Deadlines', url = url, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/794508278809100309/UCSBLogo.png')
        await ctx.send(embed = embed)

    @commands.command(aliases = ['discs'])
    async def discords(self, ctx): 
        embed = discord.Embed(title = 'Links to other discords', description = 'The following discord links have been verifed, if you wish to inlude one that is not already here please DM an admin or mod.',
                                colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name = 'UCSB', value = 'https://discord.com/invite/bqEZCWm')
        embed.add_field(name = 'LGBTQ+ in Physics', value = 'https://discord.gg/8dq4PX2KpB')
        embed.add_field(name = 'oSTEM @ UCSB', value = 'https://discord.gg/5FZ8Mdp')
        embed.add_field(name = 'Los Ingenieros', value = 'https://discord.gg/NWnxMdq')
        embed.add_field(name = 'PokemonGo', value = 'https://discord.gg/HmmrXSgXMT')
        embed.add_field(name = 'RPG at UCSB', value = 'https://discord.gg/ebc8UBG')
        await ctx.send(embed = embed)

    @commands.command(aliases = ['mer'])
    async def merch(self, ctx):
        link = 'https://teespring.com/stores/my-store-10181903'
        image = 'https://cdn.discordapp.com/attachments/700224899721199626/782215254540550164/WIP.png'
        embed = discord.Embed(title = 'Merch', url = link, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/783899572786692096/unknown.png')
        embed.set_thumbnail(url = image)
        await ctx.send(embed = embed) 

    @commands.command(aliases = ['fiziks'])
    async def physics(self, ctx):
        await ctx.message.delete()
        data = await self.open_json('JSONdata/Bot_string_list.json')
        phys_facts = data["physics-facts"]
        await ctx.send(phys_facts[random.randint(0,len(phys_facts))])

    @commands.command()
    async def dadjoke(self, ctx):
        await ctx.message.delete()
        data = await self.open_json('JSONdata/Bot_string_list.json')
        dad_jokes = data["dad-jokes"]
        await ctx.send(dad_jokes[random.randint(0, len(dad_jokes))])

def setup(bot):
    bot.add_cog(user_static_commands(bot))