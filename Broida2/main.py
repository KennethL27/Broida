import discord, json, time
from discord.ext import commands
from broida_token import token_pass

client = commands.Bot(command_prefix = '.')

def open_json(file_name):
    with open (file_name) as file:
        return json.load(file)

@client.event
async def on_ready():
    bot_description = discord.Game('missing the crowds | .help')
    await client.change_presence(activity = bot_description)
    print("Broida's main center is currently online.")

@client.command()
async def update(ctx):
    print()
    print()
    print()
    print('______________________________________________________')
    cog_fields = open_json("JSONdata/Bot_Info.json")["cogs"]
    for cog in cog_fields:
        print(f'Reloading {cog}\n')
        client.reload_extension(f'cogs.{cog}')
        print(f'Loaded {cog}\n')
        print('_______________________________________')

@client.command()
async def uptime(ctx):
    await ctx.channel.purge(limit = 1)
    time_seconds = time.perf_counter()
    time_days = time_seconds //(86400)
    time_seconds = time_seconds % 86400
    time_hours = time_seconds // 3600
    time_seconds %= 3600
    time_minutes =  time_seconds // 60
    time_seconds %= 60
    time_seconds = time_seconds
    message = await ctx.send(f'**UPTIME**: Days: {int(time_days)}, Hours: {int(time_hours)}, Minutes: {int(time_minutes)}, Seconds: {round(time_seconds,2)}')
    await message.delete(delay = 5)

if __name__ == '__main__':
    cog_fields = open_json("JSONdata/Bot_Info.json")["cogs"]
    for cog in cog_fields:
        print(f'Loading {cog}...\n')
        client.load_extension(f'cogs.{cog}')
        print(f'Loaded {cog}\n')
        print('_______________________________________')

client.run(token_pass)