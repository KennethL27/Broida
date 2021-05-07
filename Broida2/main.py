import discord, json, time
from discord.ext import commands
from broida_token import token_pass

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.emojis = True
intents.reactions = True
intents.guild_reactions = True

client = commands.Bot(command_prefix = '.', fetch_online_members = True, intents = intents)
# client.remove_command('help')

founder_id = 759317762769420310
admin_id = 777124216876957696
treasurer_id = 759317768364752966
mod_id = 777124177269882902

def open_json(file_name):
    with open (file_name) as file:
        return json.load(file)

@client.event
async def on_ready():
    bot_description = discord.Game('missing the crowds | .help')
    await client.change_presence(activity = bot_description)
    print("Broida's main center is currently online.")

@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def update(ctx, force = None):
    if not force:
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
    # a force update will allow new cogs to be introduced without restarting main.py
    else:
        print()
        print()
        print()
        print('______________________________________________________')
        cog_fields = open_json("JSONdata/Bot_Info.json")["cogs"]
        for cog in cog_fields:
            print(f'Reloading {cog}\n')
            try:
                client.unload_extension(f'cogs.{cog}')
                client.load_extension(f'cogs.{cog}')
            except:
                client.load_extension(f'cogs.{cog}')
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