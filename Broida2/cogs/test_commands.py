from discord.ext import commands
import discord, json

class test_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def open_json(self, file_name):
        with open (file_name) as file:
            return json.load(file)

    def write_json(data, file_name):
        with open (file_name, 'w') as file:
            json.dump(data, file, indent = 4)

    @commands.command()
    async def test_update(self, ctx):
        print('\n\n\n______________________________________________________')
        cogs = self.open_json("JSONdata/Bot_Info.json")["cogs"]
        value = str(cogs).replace("']",':🔄\n').replace('[','').replace(']','').replace(',','').replace(' ',': 🔄\n').replace("'", '')
        embed = discord.Embed()
        embed.add_field(name = "Update Status", value = value)
        update_message = await ctx.send(embed = embed)
        for cog in cogs:
            print(f'Reloading {cog}\n')
            try:
                self.bot.reload_extension(f'cogs.{cog}')
                embed = discord.Embed()
                value = value.replace('🔄', '☑️', 1)
                embed.add_field(name = "Update Status", value = value)
                await update_message.edit(embed = embed)
                print(f'Loaded {cog}\n')
                print('_______________________________________')
            except:
                embed = discord.Embed()
                value = value.replace('🔄', '❌', 1)
                embed.add_field(name = "Update Status", value = value)
                await update_message.edit(embed = embed)
                print(f"Couldn't load {cog}\n")
                print('_______________________________________')


def setup(bot):
    bot.add_cog(test_commands(bot))
    print("Test Commands Online\n")