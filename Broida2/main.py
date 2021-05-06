import discord, json, time
from discord.ext import commands
from broida_token import token_pass

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    bot_description = discord.Game('missing the crowds | .help')
    await client.change_presence(activity = bot_description)

@client.command()
async def update(ctx):
    for cog in cog_fields:
        print(f'Reloading {cog}')
        client.reload_extension(f'cogs.{cog}')
        print(f'Loaded {cog}')

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

cog_fields = ['user_static_commands']
if __name__ == '__main__':
    for cog in cog_fields:
        print(f'Loading {cog}...')
        client.load_extension(f'cogs.{cog}')
        print(f'Loaded {cog}')

client.run(token_pass)