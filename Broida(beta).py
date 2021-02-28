'''
Created on Fri Nov 13 3:47:20 2020

@author: Kenneth Lara

'''

import discord, datetime, time, re, asyncio, random, json
from discord.ext import commands
from discord.utils import get
from dateutil import tz

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.emojis = True
intents.reactions = True
intents.guild_reactions = True

client = commands.Bot(command_prefix = '.', fetch_online_members = True, intents = intents)
client.remove_command('help')

# Guild Ids
######################################
guild_id = 730489460113801256

# Role Ids
######################################
everyone = 730489460113801256 
president_id = 411631919370076170 
founder_id = 759317762769420310
admin_id = 777124216876957696
treasurer_id = 759317768364752966
mod_id = 777124177269882902
gaucho_id = 785778216819490836
graduate_id = 785793759874121739
super_senior_id = 1
senior_id = 2
junior_id = 3
sophomore_id = 4
freshman_id = 5
transfer_id = 6

# Channel Ids
######################################
message_log_id = 779721248661176380
ticket_channel_id = 781468089438568448
announcement_channel_id = 782227895925866516
bot_command_channel_id = 804860036207738890
advising_channel_id = 805177278958272572
rant_id = 771845526903586847
anonymous_id = 787685941794832405
ban_id = 794092839280967691 
welcome_id = 775492454338002994 

# Boolean to trigger message delete function
######################################
update_status = False

# Bot Ids
######################################
bot_list_id = [204255221017214977] 

# List of Commands that the bot can disregard when the command message is deleted.
######################################
list_of_commands = ['.physics', '.fiziks', '.uptime', '.dadjoke', '.update']

# List of exams that are set to be at a certain date, need to move to an offline database. 
######################################
open_exam = []

# List of Users to handle for anonymity
######################################
user_list = []
generated_user = []

# Function for writing in json file given the file name
######################################
def write_json(data, file_name):
    with open (file_name, 'w') as file:
        json.dump(data, file, indent = 4)

@client.event
async def on_ready():
    bot_description = discord.Game('missing the crowds | .help')
    await client.change_presence(activity = bot_description)
    print('Bot is ready')


# Commands for any Users
##################################################################################################################
##################################################################################################################


# Course Listings
######################################
@client.command(aliases = ['classes', 'class', 'schedule'])
async def courses(ctx):
    embed = discord.Embed(title = 'Proposed Courses for 20-21', url = 'https://www.physics.ucsb.edu/resources/teachingassignments', colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif')
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/772690834151571506/782475543404347422/Screenshot_20201128-231814_Drive.jpg')
    await ctx.send(embed = embed)

# UDIP Merch website
######################################
@client.command(aliases = ['mer'])
async def merch(ctx):
    link = 'https://teespring.com/stores/my-store-10181903'
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782215254540550164/WIP.png'
    embed = discord.Embed(title = 'Merch', url = link, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/783899572786692096/unknown.png')
    embed.set_thumbnail(url = image)
    await ctx.send(embed = embed)

# Returns a Physics Fact, change this to a different file (reduce the amount of code this file needs)
@client.command(aliases = ['fiziks'])
async def physics(ctx):
    await ctx.message.delete()
    phys_facts = ['Mass and inertia are the same thing. (Mass actually measures inertia - in kilogramsÂ… Much as monetary resources measures financial wealth - in dollars.)',
    'Weight (force of gravity) decreases as you move away from the earth by distance squared. (It decreases, but only approaches zero, never reaching it, even far beyond the solar system.)',
    'Weight (in newtons) is mass x acceleration (w = mg). Mass is not Weight! Mass is a scalar and measured in kilograms, weight is a force and a vector and measured in Newtons.',
    'Velocity can only be constant when the net force (and acceleration) is zero. (The velocity can be zero and not constant - for example when a ball, thrown vertically, is at the top of its trajectory.)',
    'Velocity, displacement [s], momentum, force (weight), torque, and acceleration are vectors.',
    'Speed, distance [d], time, length, mass, temperature, charge, power and energy (joules) are scalar quantities.',
    'The slope of the distance-time graph is velocity.',
    'The slope of the velocity-time graph is acceleration.',
    'The area under a velocity-time graph is distance.',
    'Magnitude is a term used to state how large a vector quantity is.',
    'At zero (0) degrees two vectors have a resultant equal to their sum. At 180 degrees two vectors have a resultant equal to their difference. From the minimum value (at 180) to the maximum value (at zero) is the total range of all the possible resultants of any two vectors.',
    'An unbalanced force must produce an acceleration and the object cannot be in equilibrium.',
    'If an object is not accelerating, it is in equilibrium and no unbalanced forces are acting.',
    'The equilibrant force is equal in magnitude but opposite in direction to the resultant vector.',
    'Momentum is conserved in all collision systems. Energy is conserved (in the KE of the objects) only if a collision is perfectly elastic.',
    'Mechanical energy is the sum of the potential and kinetic energy.',
    'UNITS: a = [m/sec2];  F = [kgÂ•m/sec2] = Newton;  work = PE = KE = [kgÂ•m2/sec2] = Joule;   Power = [kgÂ•m2/sec3] = [Joules/sec] = Watt',
    '1ev is a very small energy unit equal to 1.6 x 10-19 joules - used for small objects such as electrons. This is on the Reference Chart.',
    'Gravitational potential energy increases as height increases.',
    'Kinetic energy changes only if mass or velocity changes.',
    'Mechanical energy (PE + KE) does not change for a free falling mass or a swinging pendulum. (when ignoring air friction)',
    'A coulomb is charge, an amp is current [coulomb/sec] and a volt is potential difference [joule/coulomb].',
    'Short, fat, cold wires make the best conductors.',
    'Electrons and protons have equal amounts of charge (1.6 x 10-19 coulombs each - known as one elementary charge). This is on the Reference Chart.',
    'Adding a resistor in series increases the total resistance of a circuit.',
    'Adding a resistor in parallel decreases the total resistance of a circuit.',
    'All resistors in series have equal current (I).',
    'All resistors in parallel have equal voltage (V).',
    'If two similar charged spheres touch each other add the charges and divide by two to find the final charge on each sphere after they are separated.',
    'Insulators contain no electrons free to move.',
    'Ionized gases conduct electric current using positive ions, negative ions and electrons.',
    'Electric fields all point in the direction of the force on a positive test charge.',
    'Electric fields between two parallel plates are uniform in strength except at the edges.',
    'Millikan determined the charge on a single electron using his famous oil-drop experiment.',
    'All charge changes result from the movement of electrons not protons. (an object becomes positive by losing electrons)',
    'The direction of a magnetic field is defined by the direction a compass needle points. (The direction an isolated north pole would feel.)',
    'Magnetic fields point from the north to the south outside the magnet and south to north inside the magnet.',
    'Magnetic flux is measured in webers.',
    'Left hands are for negative charges and reverse answer for positive charges.',
    'The first hand rule deals with the B-field around a current bearing wire, the third hand rule looks at the force on charges moving in a B-field, and the second hand rule is redundant.',
    'Solenoids are stronger with more current or more wire turns or adding a soft iron core.',
    'Sound waves are longitudinal and mechanical.',
    'Light slows down, bends toward the normal and has a shorter wavelength when it enters a medium with a higher index of refraction (n).',
    'All angles in wave theory problems are measured to the normal.',
    'Blue light has more energy, a shorter wavelength and a higher frequency than red light (remember- ROYGBIV).',
    'The electromagnetic spectrum (radio, infrared, visible. Ultraviolet x-ray and gamma) are listed lowest energy to highest. They are all electromagnetic and travel at the speed of light.',
    'The speed (c) of all types of electromagnetic waves is 3.0 x 108 m/sec in a vacuum.',
    "As the frequency of an electromagnetic wave increases its energy increases and its wavelength decreases and its velocity remains constant as long as it doesn't enter a medium with a different refractive index (i.e. optical density).",
    'A prism produces a rainbow from white light by dispersion. (red bends the least because it slows the least).',
    "Transverse wave particles vibrate back and forth perpendicular to the direction of the wave's velocity. Longitudinal wave particles vibrate back and forth parallel to the direction of the wave's velocity.",
    'Light wave are transverse (they, and all (and only)transverse waves can be polarized).',
    'The amplitude of a non-electromagnetic wave (i.e. water, string and sound waves) determines its energy. The frequency determines the pitch of a sound wave. Their wavelength is a function of its frequency and speed. Their speed depends on the medium they are traveling in.',
    'Constructive interference occurs when two waves are zero (0) degrees out of phase or a whole number of wavelengths (360 degrees.) out of phase.',
    'At the critical angle a wave will be refracted to 90 degrees. At angles larger than the critical angle, light is reflected not refracted.',
    'Doppler effect: when a wave source moves toward you, you will perceive waves with a shorter wavelength and higher frequency than the waves emitted by the source. When a wave source moves away from you, you will perceive waves with a longer wavelength and lower frequency.',
    'Double slit diffraction works because of diffraction and interference.',
    'Single slit diffraction produces a much wider central maximum than double slit.',
    'Diffuse reflection occurs from dull surfaces while regular (spectacular) reflection occurs from smooth (mirror-like) surfaces.',
    'Only waves show diffraction, interference and the polarization.',
    'The period of a wave is the inverse of its frequency (T = 1/f ). So waves with higher frequencies have shorter periods.',
    'Monochromatic light has one frequency.',
    'Coherent light waves are all in phase.',
    'In order to explain the photoelectric effect, Einstein proposed particle behavior for light (and all electromagnetic waves) with E = h f and KEmax = hf Â– Wo.',
    'A photon is a particle of light (wave packet).',
    'To preserve the symmetry of the universe, DeBroglie proposed wave behavior for particles ( l = h/mv). Therefore large fast moving objects (baseballs, rockets) have very short wavelengths (that are unobservable) but very small objects, particularly when moving slowly have wavelengths that can be detected in the behavior of the objects.',
    'Whenever charged particles are accelerated, electromagnetic waves are produced.',
    'The lowest energy state of a atom is called the ground state.',
    'Increasing light frequency increases the kinetic energy of the emitted photo-electrons in the photo-electric effect (KEmax = hf Â– Wo).',
    'As the threshold frequency increases for a photo-cell (photo emissive material) the work function also increases (Wo = h fo)',
    'Increasing light intensity increases the number of emitted photo-electrons in the photo-electric effect but not their KE (i.e. more intensity>more photons>more electrons emitted). This is the particle nature shown by light.',
    'Key to understanding trajectories is to separate the motion into two independent components in different dimensions - normally horizontal and vertical. Usually the velocity in the horizontal dimension is constant (not accelerated) and the motion in the vertical dimension is changing (usually with acceleration of g).',
    'Centripetal force and centripetal acceleration vectors are toward the center of the circle- while the velocity vector is tangent to the circle. (Centripetal means towards the center!)',
    'An object in orbit is not weightless - it is its weight that keeps it moving in a circle around the astronomical mass it is orbiting. In other words, its weight is the centripetal force keeping it moving in a circle.',
    'An object in orbit is in free fall - it is falling freely in response to its own weight. Any object inside a freely falling object will appear to be weightless.',
    'Rutherford discovered the positive nucleus using his famous gold-foil experiment.',
    'Fusion is the process in which hydrogen is combined to make helium.',
    'Fission requires that a neutron causes uranium to be split into middle size atoms and produce extra neutrons, which, in turn, can go on and cause more fissions.',
    'Radioactive half-lives are not effected by any changes in temperature or pressure (or anything else for that matter).',
    'One AMU of mass is equal to 931 meV of energy. (E = mc2). This is on the Reference Charts!',
    'Nuclear forces are very strong and very short-ranged.',
    'There are two basic types of elementary particles: Hadrons & Leptons (see Chart).',
    'There are two types of Hadrons: Baryons and Mesons (see Chart).',
    'The two types of Hadrons are different because they are made up of different numbers of quarks. Baryons are made up of 3 quarks, and Mesons of a quark and antiquark.',
    'Notice that to make long-lived Hadron particles quarks must combine in such a way as to give the charge of particle formed a multiple of the elementary charge.',
    'For every particle in the "Standard Model" there is an antiparticle. The major difference of an antipartcle is that its charge is opposite in sign. All antiparticles will anhililate as soon as they come in contact with matter and will release a great amount of energy.']
    await ctx.send(phys_facts[random.randint(0,len(phys_facts))])

# Returns the list of other Discord Servers from UCSB
######################################
@client.command(aliases = ['discs'])
async def discords(ctx): 
    embed = discord.Embed(title = 'Links to other discords', description = 'The following discord links have been verifed, if you wish to inlude one that is not already here please DM an admin or mod.',
        colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name ='UCSB', value = 'pending')
    embed.add_field(name = 'LGBTQ+ in Physics', value = 'https://discord.gg/8dq4PX2KpB')
    embed.add_field(name = 'oSTEM @ UCSB', value = 'https://discord.gg/5FZ8Mdp')
    embed.add_field(name = 'Los Ingenieros', value = 'https://discord.gg/NWnxMdq')
    embed.add_field(name = 'PokemonGo', value = 'https://discord.gg/HmmrXSgXMT')
    embed.add_field(name = 'RPG at UCSB', value = 'https://discord.gg/ebc8UBG')
    await ctx.send(embed = embed)

# Ticket Submission, anonymously. 
# Moderators can take quick action with a reaction to the Bot's message
######################################
@client.command(aliases = ['tic'])
async def ticket(ctx, member : discord.Member, * , reason):
    #for DMs, to mention the user use their discord username (not nickname) along with their discriminator. ie PhysicsLegends#6877
    guild = client.get_guild(guild_id)
    if ctx.channel in guild.text_channels:
        await ctx.message.delete()
    channel = client.get_channel(ticket_channel_id)
    embed = discord.Embed(title = '**TICKET EVENT**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
        This ticket is begin ticketed against: {member.mention}',colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = 'REASON', value = reason, inline = False)
    embed.add_field(name = 'Reactions', value = '**The red squre:** Will be a ban lasting 24 hours\n**The yellow square:** Will be a warning sent to the member in questioned \
        \n**The green square:** Will be nothing and the ticketer will be notified\n\nNote that the ticket will automatically end itself 24hrs from this message.', inline = False)
    message = await channel.send(embed = embed)
    #options for the ticket: ban for a specific amount of time, warning, or nothing 
    await message.add_reaction('🟥') #ban for 24hrs
    await message.add_reaction('🟨') #warn the user
    await message.add_reaction('🟩') #no action

    current_time = time.time()
    end_time = current_time + 3600

    while current_time < end_time:

        use_message = await message.channel.fetch_message(message.id)

        '''for banning, opt 1'''
        if use_message.reactions[0].count > 1:
            await message.delete()
            #need to send an embed message of a summary of the ban.
            embed = discord.Embed(title = '**TICKET EVENT BAN: SUMMARY**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                This ticket is begin ticketed against: {member.mention}',colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name = 'REASON', value = reason, inline = False)
            embed.add_field(name = 'RESULT', value = 'Ticket resulted in a 24 hour ban.')
            await channel.send(embed = embed)

            dm_embed = discord.Embed(title = '**TICKET EVENT BAN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
            dm_embed.add_field(name = 'RESULT', value = 'Under review it has appeared that you have violoated the rules and have been given a ban for 24 hours.\
                You may contact mods and admin in #ban-channel.')
            await member.send(embed = dm_embed)

            member_roles = member.roles
            member_roles_list = []

            for role in member_roles:
                member_roles_list.append(role.id)

            mod_role = guild.get_role(mod_id)
            treasurer_role = guild.get_role(treasurer_id)

            for i in member_roles_list[1:]:
                roles = guild.get_role(i)
                if roles == mod_role or roles == treasurer_role:
                    await ctx.send('Invalid user due to having a mod role, please remove the role or select another user.')
                    return

            #remove all roles except everyone
            for i in member_roles_list[1:]:
                roles = guild.get_role(i) 
                await member.remove_roles(roles)
            
            #need to make ban channel open for this user to discuss any information. Also remove access to new user welcome channel.
            ban_channel = client.get_channel(ban_id)
            welcome_channel = client.get_channel(welcome_id)
            await ban_channel.set_permissions(member, read_messages = True, send_messages = True, read_message_history = False)
            await welcome_channel.set_permissions(member, read_messages = False, send_messages = False)
            
            await asyncio.sleep(60) #24 hours ban: in seconds 86400
            
            #add all removed roles
            for i in member_roles_list[1:]:
                roles = guild.get_role(i)
                await member.add_roles(roles)
            
            await ban_channel.set_permissions(member, overwrite = None)
            await welcome_channel.set_permissions(member, overwrite = None)
            return

        '''for warning, opt 2'''
        #going to need to send the member a DM warning him. Maybe give an option to what rule was broken, for the warning to be enacted
        if use_message.reactions[1].count > 1:
            await message.delete()
            embed = discord.Embed(title = '**TICKET EVENT WARN**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                This ticket is begin ticketed against: {member.mention}',colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name = 'REASON', value = reason, inline = False)
            embed.add_field(name = 'Reactions', value = ':one: The user broke rule 1\n:two: The user broke rule 2\
                \n:three: The user broke rule 3\n*etc*\n:seven: The user did not break any specific rule, and will need to contact one of the mods to understand the warn.\n\n\
                *By default option 7 will be used after 10 mins*', inline = False)
            warn_message = await channel.send(embed = embed)
            await warn_message.add_reaction('1️⃣')
            await warn_message.add_reaction('2️⃣')
            await warn_message.add_reaction('3️⃣')
            await warn_message.add_reaction('4️⃣')
            await warn_message.add_reaction('5️⃣')
            await warn_message.add_reaction('6️⃣')
            await warn_message.add_reaction('7️⃣')

            current_time = time.time()
            end_time = current_time + 600 #for 10 minutes, 600 secs
            j = 0
            while current_time < end_time:
                use_message_warn = await warn_message.channel.fetch_message(warn_message.id)
                if use_message_warn.reactions[0].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = 'Member has broken rule 1\n*Use judgement when posting.\
                        Respect everyone and their opinion. We do not tolerate disrupting and/or offensive behavior, this includes: racist/sexist/insensitive remarks, trolling/baiting, \
                        spamming, doxing, harassing other users, etc. Consider common sense and public decency. Additionally, we do not allow discussions of recent figures such as Hitler, \
                        or similar politically motivated topics involving current politicians, all of which is both insensitive and inappropriate.*', inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = 'Member has broken rule 1\n*Use judgement when posting.\
                        Respect everyone and their opinion. We do not tolerate disrupting and/or offensive behavior, this includes: racist/sexist/insensitive remarks, trolling/baiting, \
                        spamming, doxing, harassing other users, etc. Consider common sense and public decency. Additionally, we do not allow discussions of recent figures such as Hitler, \
                        or similar politically motivated topics involving current politicians, all of which is both insensitive and inappropriate.*', inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[1].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 2\n*Post in the appropriate place. \
                        Each channel contains a description and/or pin that describe what's allowed and what's not allowed there. \
                        NSFW content is currently prohibited on this server.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 2\n*Post in the appropriate place. \
                        Each channel contains a description and/or pin that describe what's allowed and what's not allowed there. \
                        NSFW content is currently prohibited on this server.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[2].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 3\n*Cheating will not be tolerated and will result in an instant ban. \
                        The server will be set to read only during finals week. \
                        Any use of this server to communicate or gain access to information during an exam is prohibited.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 3\n*Cheating will not be tolerated and will result in an instant ban. \
                        The server will be set to read only during finals week. \
                        Any use of this server to communicate or gain access to information during an exam is prohibited.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[3].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 4\n*Real names are not be a rule. \
                        You can use whatever handle you want so long as it's appropriate. Impersonating a professor however is strictly prohibited.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 4\n*Real names are not be a rule. \
                        You can use whatever handle you want so long as it's appropriate. Impersonating a professor however is strictly prohibited.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[4].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 5\n*No posting of private discord links are allowed. \
                        If you want to share a discord link, contact the mods first and we can post it for you.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 5\n*No posting of private discord links are allowed. \
                        If you want to share a discord link, contact the mods first and we can post it for you.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[5].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "Member has broken rule 6\n*Rules are subject to change and will be updated accordingly*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "Member has broken rule 6\n*Rules are subject to change and will be updated accordingly*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                elif use_message_warn.reactions[6].count > 1:
                    j = j+1
                    await warn_message.delete()
                    dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    dm_embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                    embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                        colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.add_field(name = 'REASON', value = reason, inline = False)
                    embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                    await channel.send(embed = embed)
                    await member.send(embed = dm_embed)
                    return
                current_time = time.time()
                await asyncio.sleep(1)

            if j == 0:
                await warn_message.delete()
                dm_embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                    colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                dm_embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                embed = discord.Embed(title = '**TICKET EVENT WARN: SUMMARY**', description = f'This ticket is begin ticketed against: {member.mention}',
                    colour = 0XFFFF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
                embed.add_field(name = 'REASON', value = reason, inline = False)
                embed.add_field(name = 'RESULT', value = "*The user did not break any specific rule, and will need to contact one of the mods to understand the warn.*", inline = False)
                await channel.send(embed = embed)
                await member.send(embed = dm_embed)
                return

        '''no action, opt 3'''
        if use_message.reactions[2].count > 1:
            #if 2 people react with red then send a message to the ticket channel stating that nothing will happen, provide a summary still.
            await message.delete()
            embed = discord.Embed(title = '**TICKET EVENT SUMMARY**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
                This ticket is begin ticketed against: {member.mention}',colour = 0X00FF00, timestamp = datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name = 'REASON', value = reason, inline = False)
            embed.add_field(name = 'RESULT', value = 'Ticket did not warrent any action and the ticketer has been messaged.')
            await channel.send(embed = embed)

            await ctx.author.send(embed = embed)
            return

        current_time = time.time()
        await asyncio.sleep(1)

    await message.delete()
    embed = discord.Embed(title = '**TICKET EVENT TERMINATION**', description = f'The following ticket was sent in by: {ctx.author.mention}\n\
        This ticket is begin ticketed against: {member.mention}',colour = 0Xff0004, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = 'REASON', value = reason, inline = False)
    embed.add_field(name = 'RESULT', value = 'No action was created.')
    await channel.send(embed = embed)

# Error Handling for the ticket command
######################################
@ticket.error
async def ticket_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: I could not find that member. When dming the bot use this format "username#number(ie. PhysicsLegends#6877)", otherwise mention the user by the @ feature.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Error: Please provide all arguments: ie. ".ticket username#number(ie. PhysicsLegends#6877) <insert your argument here>"')
    else:
        raise error

# Recieve the full list of active exam course set to close channels
######################################
@client.command()
async def open_exams(ctx):
    embed = discord.Embed(colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc)) 
    if len(open_exam) == 0:
        embed.add_field(name = 'Open Exam', value = 'There is no exams planned at this time.')
        await ctx.send(embed = embed)
    
    if len(open_exam) != 0:
        for i in range(0, len(open_exam)):
            embed.add_field(name = f'Open Exam {i+1}', value = open_exam[i])
        await ctx.send(embed = embed)

# Recive the amount of time the Bot has been up for. 
# Currently shows the amount of time the Rasberry Pi as been running for, not the code
######################################
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

# Help Command for all users, list of usable commands
######################################
@client.command()
async def help(ctx):
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
    footers = ['Powered by yours turly', 'Powered by your tears', 'Powered by curved that helped you pass', "Powered by Broida's black hole", 'Powered by KennethL <3', 'Powered by hope',\
               'Powered by perpetual motion', 'Powered by the bike lane', 'Powered by flat-eathers', 'Powered by ...', 'Loading...', 'Powered by Storke Tower', 'Powered by love']
    embed = discord.Embed(title = 'Commands for Broida', description = 'When using these commands, begin your statement with "." followed by the name of the command',\
         colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = image)
    embed.add_field(name = 'merch (mer)', value = 'Get the link to the merch website.')
    embed.add_field(name = 'courses (classes, class, schedule)', value = 'Get the link and image to the 2020-21 Teaching Assignments', inline = False)
    embed.add_field(name = 'advising', value = 'Get the link to UCSB Physics Advising as well as direct links to make appointments with Jean Dill or Cooper.', inline = False)
    embed.add_field(name = 'dates', value = 'Get the link to the full list of dates such as drop deadline or past times.', inline = False)
    embed.add_field(name = 'open_exams', value = 'Get the list of planned/current exams, this list is set to close their respective channels at the given time.', inline = False)
    embed.add_field(name = 'physics', value = 'Get random physics facts.', inline = False)
    embed.add_field(name = 'discords (discs)', value = 'Find out other discord serers like RPG at UCSB.', inline = False)
    embed.add_field(name = 'ticket (tic)', value = 'Use this command to submit a ticket. Please wirte your reasons for the ticket after ".ticket". *Please note: while dming the with this command use the username#number \
        (ie.PhysicsLegends#6877* **.ticket <@user> <reason>**', inline = False)
    embed.add_field(name = 'uptime', value = 'This command shows you how long the bot has been running. The message will be delete after 5 seconds.', inline = False)
    embed.set_footer(text = footers[random.randint(0, len(footers))])
    await ctx.send(embed = embed)

# Dad Jokes: Easter Egg, not found in help command
######################################
@client.command()
async def dadjoke(ctx):
    await ctx.message.delete()
    dad_jokes = ["What rock group has four men that don't sing? Mount Rushmore.", "When I was a kid, my mother told me I could be anyone I wanted to be. Turns out, identity theft is a crime.", 
    "A guy goes to his doctor because he can see into the future. The doctor asks him 'How long have you suffered from that condition?' The guy tells him, 'Since next Monday.'",
    "What do sprinters eat before a race? Nothing, they fast!",
    "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
    "What do you call a mac 'n' cheese that gets all up in your face? Too close for comfort food!",
    "Why couldn't the bicycle stand up by itself? It was two tired!",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere!",
    "Why do melons have weddings? Because they cantaloupe!",
    "What happens when you go to the bathroom in France? European.",
    "What's the difference between a poorly dressed man on a tricycle and a well-dressed man on a bicycle? Attire!",
    "How many apples grow on a tree? All of them!",
    "Did you hear the rumor about butter? Well, I'm not going to spread it!",
    "Did you hear about the guy who invented Lifesavers?  They say he made a mint!",
    "Last night I had a dream that I weighed less than a thousandth of a gram. I was like, 0mg.",
    "A cheese factory exploded in France. Da brie is everywhere!",
    "Why did the old man fall in the well? Because he couldn't see that well!",
    "What do you call a factory that sells passable products? A satisfactory!",
    "Why did the invisible man turn down the job offer? He couldn't see himself doing it!",
    "Want to hear a joke about construction? I'm still working on it!",
    "I was really angry at my friend Mark for stealing my dictionary. I told him, 'Mark, my words!'",
    "How does Moses make his coffee? Hebrews it.",
    "I'm starting a new dating service in Prague. It's called Czech-Mate.",
    "I was just reminiscing about the beautiful herb garden I had when I was growing up.\nGood thymes.",
    "Do you know the last thing my grandfather said to me before he kicked the bucket?",
    "Grandson, watch how far I can kick this bucket.",
    "I like telling Dad jokes. Sometimes he laughs!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a fish with two knees? A two-knee fish!",
    "Why do you never see elephants hiding in trees? Because they're so good at it!",
    "How does a penguin build its house? Igloos it together!",
    "Why don't skeletons ever go trick or treating? Because they have no body to go with!",
    "This graveyard looks overcrowded. People must be dying to get in there!",
    "What's ET short for? Because he's only got tiny legs!",
    "What's brown and sticky? A stick!",
    "Can February march? No, but April may!",
    "What's orange and sounds like a parrot? A carrot!",
    "How do you make a Kleenex dance? Put some boogie in it!",
    "Why is Peter Pan always flying? He neverlands!",
    "What's a ninja's favorite type of shoes? Sneakers!",
    "What do Santa's elves listen to ask they work? Wrap music!",
    "Did you hear about the bacon cheeseburger who couldn't stop telling jokes? It was on a roll.",
    "Student: 'Can I go to the bathroom?'",
    "Teacher: 'It's 'may.''",
    "Student: 'No, it's January.'",
    "Why was the coach yelling at a vending machine? He wanted his quarter back.",
    "Why do vampires seem sick? They're always coffin.",
    "Within minutes, the detectives knew what the murder weapon was. It was a brief case.",
    "To whoever stole my copy of Microsoft Office, I will find you. You have my Word!",
    "I used to work in a shoe-recycling shop. It was sole destroying!",
    "My boss told me to have a good day, so I went home!",
    "I'm so good at sleeping I can do it with my eyes closed!",
    "Spring is here! I got so excited I wet my plants!",
    "I thought about going on an all-almond diet… But that's just nuts!",
    "My friend says to me, 'What rhymes with orange?' And I told him, 'No it doesn't!'",
    "My wife told me I had to stop acting like a flamingo. So I had to put my foot down!",
    "I told my girlfriend she drew her eyebrows too high. She seemed surprised!",
    "I tell dad jokes but I have no kids…I'm a faux pa!",
    "So a vowel saves another vowel's life. The other vowel says, 'Aye E! I owe you!'",
    "Did I tell you the time I fell in love during a backflip? I was heels over head!",
    "My uncle named his dogs Rolex and Timex. They're his watch dogs!",
    "If you see a robbery at an Apple Store does that make you an iWitness?!",
    "I would avoid the sushi if I were you. It's a little fishy!",
    "Five out of four people admit they're bad with fractions!",
    "Two goldfish are in a tank. One says to the other, 'Do you know how to drive this thing?'",
    "I'll call you later. Don't call me later, call me Dad!",
    "Did you hear about the Italian chef who died? He pasta way!",
    "When the grocery store clerk asks me if I want the milk in a bag, I always tell him, 'No, I'd rather drink it out of the carton!'",
    "The difference between a numerator and a denominator is a short line. Only a fraction of people will understand this!",
    "I don't play soccer because I enjoy the sport. I'm just doing it for kicks!",
    "I invented a new word today: Plagiarism!",
    "What do you call a donkey with only three legs? A wonkey!",
    "After dinner, my wife asked if I could clear the table. I needed a running start, but I made it!",
    "This morning, Siri said, 'Don't call me Shirley.' I accidentally left my phone in Airplane mode!",
    "A woman is on trial for beating her husband to death with his guitar collection. The judge asks her, 'First offender?' She says, 'No, first a Gibson! Then a Fender!'",
    "I know a lot of jokes about retired people but none of them work!",
    "What do you call a guy with a rubber toe? Roberto!",
    "What rhymes with boo and stinks? You!",
    "I accidentally dropped my pillow on the floor. I think it has a concushion.",
    "Someone complimented my parking today! They left a sweet note on my windshield that said 'parking fine.'",
    "St. Francis worked at Krispy Kreme. He was a deep friar.",
    "In America, using the metric system can get you in legal trouble. In fact, if you sneer at any other method of measuring liquids, you may be held in contempt of quart.",
    "I found a wooden shoe in my toilet today. It was clogged.",
    "Some people can't distinguish between etymology and entomology. They bug me in ways I can't put into words.",
    "My hotel tried to charge me ten dollars extra for air conditioning. That wasn't cool.",
    "If an English teacher is convicted of a crime and doesn't complete the sentence, is that a fragment?",
    "I think my wife is putting glue on my antique weapons collection. She denies it but I'm sticking to my guns!",
    "Which U.S. state is famous for its extra-small soft drinks? Minnesota!",
    "I got a hen to regularly count her own eggs. She's a real mathamachicken!",
    "What did the Ranch say when someone opened the refrigerator door? 'Close the door, I'm dressing!'",
    "Why do trees seem suspicious on sunny days? They just seem a little shady!",
    "What did the policeman say to his belly button? You're under a vest!",
    "What do you call a fake noodle? An Impasta!",
    "I've been bored recently so I've decided to take up fencing. The neighbors said they will call the police unless I put it back.",
    "Why did the math book look so sad? Because of all of its problems!",
    "I don't really call for funerals that start before noon. I guess I'm just not a mourning person!",
    "If two vegans get in a fight, is it still considered a beef?",
    "One of my favorite memories as a kid was when my brothers used to put me inside a tire and roll me down a hill. They were Goodyears!",
    "I'm addicted to collecting vintage Beatles albums. I need Help!",
    "What does the cell say to his sister when she steps on his toe? 'Oh my toe sis!'",
    "I never buy pre-shredded cheese. Because doing it yourself is grate.",
    "I was playing chess with my friend and he said, 'Let's make this interesting.' So we stopped playing chess.",
    "How do you tell the difference between a bull and a milk cow? It is either one or the utter.",
    "I have a great joke about nepotism. But I'll only tell it to my kids.",
    "What do scholars eat when they're hungry? Academia nuts.",
    "What do you call an ant that has been shunned by his community? A socially dissed ant.",
    "A Vicks VapoRub truck overturned on the highway this morning. Amazingly, there was no congestion for eight hours!",
    "When does a joke become a dad joke? When it becomes apparent."]
    await ctx.send(dad_jokes[random.randint(0, len(dad_jokes))])

# Returns the links for setting up an apointment with JD or Cooper (physics Advisors)
######################################
@client.command()
async def advising(ctx):
    url = 'https://www.physics.ucsb.edu/education/undergrad/advising-help'
    embed = discord.Embed(title = 'UCSB Physics Advising', url = url, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.add_field(name = '__Schedule Meeting with Jean Dill__', value = 'https://shoreline.ucsb.edu/meetings/1336841/JDOfficeHours', inline = False)
    embed.add_field(name = '__Schedule Meeting with Earnest Cooper Jr.__', value = 'https://shoreline.ucsb.edu/meetings/1336823/Coopersadvisinghours', inline = False)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/794516513730068510/unknown.png')
    await ctx.send(embed = embed)

# Returns the link to important dates
######################################
@client.command()
async def dates(ctx):
    url = 'https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/registration-pass-dates/2020-2021-registration-pass-times'
    embed = discord.Embed(title = 'UCSB 2020-2021 Registration Pass Times/Important Deadlines', url = url, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/700224899721199626/794508278809100309/UCSBLogo.png')
    await ctx.send(embed = embed)


# Commands for any Moderators
##################################################################################################################
##################################################################################################################


# Create Announcements to be pushed at a later time/date
######################################
@client.command(aliases = ['anouce', 'post'])
@commands.has_any_role(founder_id, admin_id, treasurer_id)
async def announcement(ctx, date, time, *, announcement): #need to be able to edit before it goes live just in case
    channel = client.get_channel(announcement_channel_id)
    if date == 'today' and time == 'now':
        await channel.send(content = announcement)
    else:
        month = int(re.split('/|-',date)[0])
        day = int(re.split('/|-',date)[1])
        year = int(re.split('/|-',date)[2])

        hour = int(re.split(':', time)[0])

        minute = int(re.split(':|am|pm', time)[1])

        if 'am' in time:
            if hour == 12:
                militaryhour = 0
            else:
                militaryhour = hour
        if 'pm' in time:
            if hour == 12:
                militaryhour = 12
            else:
                militaryhour = hour + 12

        release = datetime.datetime(year, month, day, militaryhour, minute, 0)

        message = await ctx.send(f'__The post will look like:__\n{announcement}')
        await message.add_reaction('🗑️')

        while datetime.datetime.now() < release: #holds off the change in permission until the start time
            await asyncio.sleep(1)
            use_message = await message.channel.fetch_message(message.id)
            if use_message.reactions[0].count > 1:
                await ctx.send(f"You have deleted the announcement, please resend your announcement to be posted.")
                return 
        
        await channel.send(content = announcement)

# AutoModeration, listens to message and looks for certain words
# Currently Not in Use. 
######################################
@client.listen('on_message')
async def on_message(message):
    '''
    list_of_word_triggers = ['shoot you', 'kill myself', 'retard', 'kill you', 'youre dumb', "youre so dumb", "you're dumb", "you're so dumb"]
    message_to_send = 'This message is being flag and will be under reviewed by the admins and mods, for more information please contact either an admin or mod.'
    channel = client.get_channel(ticket_channel_id)
    for i in list_of_word_triggers:
        if i in message.content:
            await message.delete()
            await message.channel.send(content = message_to_send)
            embed = discord.Embed(title = '**WORD TRIGGER: PLEASE REVIEW THE SITUATION**', description = f'The triggered message was in {message.channel.mention} by {message.author.mention}')
            embed.add_field(name = 'Message content', value = message.content)
            await channel.send(embed = embed)
    '''
    global update_status
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.datetime.strptime(str(message.created_at)[:-7], "%Y-%m-%d %H:%M:%S")
    utc = utc.replace(tzinfo = from_zone)
    convert_zone = str(utc.astimezone(to_zone))
    if update_status is False:
        return
    else:
        #append to delete_message_log
        message_id = message.id
        user_name = message.author
        channel = message.channel
        user_message = message.content
        with open ("Update_Message_Log.json") as Update_Message_Log_json:
            data = json.load(Update_Message_Log_json)
            message_log = data['messages']
            new_entry = {"id": message_id, "author": user_name.mention, "channel": channel.mention, "created_at": convert_zone, "message": user_message}
            message_log.append(new_entry)
        write_json(data, "Update_Message_Log.json")

# AutoModeration, returns the delete message to a specific channel for Moderators
# Version 2 of deleted_message_log: allows for easy transfer of code update. 
######################################
@client.event
async def on_raw_message_delete(payload):
    guild = client.get_guild(guild_id)
    message_log_channel = client.get_channel(message_log_id)
    anonymous_channel = client.get_channel(anonymous_id)
    rant_channel = client.get_channel(rant_id)
    advising_channel = client.get_channel(advising_channel_id)
    message = payload.cached_message
    status = False

    try:
        if message.content.startswith('.a') or  message.content.startswith('.anonymity') or message.content.startswith('.anonymous'):
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
            if message.author != client.user:
                if message.content not in list_of_commands:
                    # attachment = await message.attachments[0].to_file(use_cached=True)
                    embed = discord.Embed(title = f'A message was delete in #{message.channel} from {message.author}', description = message.content, colour = 0XFFFF00)#,timestamp = datetime.datetime.now(datetime.timezone.utc))
                    embed.set_footer(text = f'Created at {convert_zone} | Deleted at {datetime.datetime.now()}')
                    # embed.set_image(url = f'attachment://{attachment.filename}')
                    await message_log_channel.send(embed = embed)

    except:
        message_id = payload.message_id
        with open ('Update_Message_Log.json') as Update_Message_Log_json:
            data = json.load(Update_Message_Log_json)
            for json_message in data['messages']:
                if json_message['id'] == message_id:
                    author = json_message['author']
                    channel = json_message['channel']
                    message = json_message['message']
                    created_at = json_message['created_at']
                    message_channel = client.get_channel(channel[2:-1])
                    message_author = guild.get_member(author[3:-1])
                    if message.startswith('.a') or message.startswith('.anonymity') or message.startswith('.anonymous'):
                        return
                    if message_channel != message_log_channel:
                        if message_channel == anonymous_channel or message_channel == rant_channel or message_channel == advising_channel:
                            if message.startswith('-r'):
                                return
                        if message_author != client.user:
                            if message not in list_of_commands:
                                embed = discord.Embed(title = f'A message was delete while update was in progress', description = f'Channel: {channel} From {author}\n{message}', 
                                colour = 0XFFFF00)#,timestamp = datetime.datetime.now(datetime.timezone.utc))
                                embed.set_footer(text = f'Created at {created_at} | Deleted at {datetime.datetime.now()}')
                                await message_log_channel.send(embed = embed)
                                status = True
            if status == False:
                await message_log_channel.send('A deleted message was out of scope. Sorry about that ')

# Exam Command 2.0a, Moderators able to close a course channel from time1 to time2.
######################################
@client.command()
async def pexam(ctx, channel : discord.TextChannel, role : discord.Role, space, date, time1, to, time2):
    month = int(re.split('/|-',date)[0])
    day = int(re.split('/|-',date)[1])
    year = int(re.split('/|-',date)[2])

    hour1 = int(re.split(':', time1)[0]) 
    hour2 = int(re.split(':', time2)[0])

    minute1 = int(re.split(':|am|pm', time1)[1])
    minute2 = int(re.split(':|am|pm', time2)[1])

    minute_reader1 = re.split(':|am|pm', time1)[1]
    minute_reader2 = re.split(':|am|pm', time2)[1]

    if 'am' in time1:
        if hour1 == 12:
            militaryhour1 = 0
        else:
            militaryhour1 = hour1
    if 'pm' in time1:
        if hour1 == 12:
            militaryhour1 = 12
        else:
            militaryhour1 = hour1 + 12

    if 'am' in time2:
        if hour2 == 12:
            militaryhour2 = 0
        else:
            militaryhour2 = hour2
    if 'pm' in time2:
        if hour2 == 12:
            militaryhour2 = 12
        else:
            militaryhour2 = hour2 + 12
        
    start_time = datetime.datetime(year, month, day, militaryhour1, minute1, 0)
    end_time = datetime.datetime(year, month, day, militaryhour2, minute2, 0)

    open_exam_text = f'{channel.mention} has an exam from {militaryhour1}:{minute_reader1} on {month}/{day}/{year} to {militaryhour2}:{minute_reader2}'
    open_exam.append(open_exam_text)

    message = await ctx.send(f'You will now change the settings of #{channel} at {militaryhour1}:{minute_reader1} on {month}/{day}/{year} to {militaryhour2}:{minute_reader2} on {month}/{day}/{year}')
    
    await message.add_reaction('🗑️')

    while datetime.datetime.now() < start_time: #holds off the change in permission until the start time      
        await asyncio.sleep(1)
        use_message = await message.channel.fetch_message(message.id)
        if use_message.reactions[0].count > 1:
            await ctx.send(f"You have deleted the exam time for #{channel.mention}, please re-enter another timeslot for this course's exam.")
            return 
    
    await ctx.send(f'The settings of #{channel} will now be changed to "only read".')
    await channel.send('Good luck with your final! You can do it')
    await channel.set_permissions(role, read_messages= True, read_message_history = True,send_messages = False, connect = False)

    while datetime.datetime.now() < end_time: #holds off the change back to the permission
        await asyncio.sleep(1)
    
    open_exam.remove(open_exam_text)
    await channel.send('Congrats you have finished, please keep in mind some students might still be taking the final but feel free to start chatting again.')
    await channel.set_permissions(role, read_messages= True, read_message_history = True,send_messages = True, connect = True)

# Exam Command 1.0a, Moderators able to close a course channel from time1 to time2.
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def exam(ctx, channel_name, course, course_number, space, date, time1, to, time2): 
#need to pass in the specific channel (physics course) and the specific time to close it for (1hr, 2hr, 1 day, etc.)
    role_name = course+' '+course_number

    month = int(re.split('/|-',date)[0])
    day = int(re.split('/|-',date)[1])
    year = int(re.split('/|-',date)[2])

    hour1 = int(re.split(':', time1)[0]) 
    hour2 = int(re.split(':', time2)[0])

    minute1 = int(re.split(':|am|pm', time1)[1])
    minute2 = int(re.split(':|am|pm', time2)[1])

    minute_reader1 = re.split(':|am|pm', time1)[1]
    minute_reader2 = re.split(':|am|pm', time2)[1]

    if 'am' in time1:
        if hour1 == 12:
            militaryhour1 = 0
        else:
            militaryhour1 = hour1
    if 'pm' in time1:
        if hour1 == 12:
            militaryhour1 = 12
        else:
            militaryhour1 = hour1 + 12

    if 'am' in time2:
        if hour2 == 12:
            militaryhour2 = 0
        else:
            militaryhour2 = hour2
    if 'pm' in time2:
        if hour2 == 12:
            militaryhour2 = 12
        else:
            militaryhour2 = hour2 + 12
        
    start_time = datetime.datetime(year, month, day, militaryhour1, minute1, 0)
    end_time = datetime.datetime(year, month, day, militaryhour2, minute2, 0)

    await ctx.send(f'You will now change the settings of #{channel_name} at {militaryhour1}:{minute_reader1} on {month}/{day}/{year} to {militaryhour2}:{minute_reader2} on {month}/{day}/{year}')

    guild = client.get_guild(guild_id) #dont think i need this
    list_of_channels = [] #a list of TextChannel class of discord.py
    list_of_channels_name = [] #a list of strings (names)
    list_of_channels_id = [] #a list of integers (ids)
    list_of_roles = []
    list_of_roles_name = []
    list_of_roles_id =[]

    for guild in client.guilds:
        for channel in guild.text_channels: #gives the full list of channels plus ids
            list_of_channels.append(channel)
            list_of_channels_name.append(channel.name)
            list_of_channels_id.append(channel.id)
        for role in guild.roles:
            list_of_roles.append(role)
            list_of_roles_name.append(role.name)
            list_of_roles_id.append(role.id)

    if channel_name in list_of_channels_name:
        print(f'The following channel will be changed: {channel_name}')
    else:
        await ctx.send('You have not selected a valid channel.')

    while datetime.datetime.now() < start_time: #holds off the change in permission until the start time 
            await asyncio.sleep(1)

    if channel_name in list_of_channels_name: #searches for the postion of the given channel name and returns the location of it 
        index_of_name = list_of_channels_name.index(channel_name)
        id_of_channel = list_of_channels_id[index_of_name]
        channel = client.get_channel(id_of_channel)
        await ctx.send(f'The settings of #{channel_name} will now be changed to "only read".')
        await channel.send('Good luck with your final! You can do it')

    if role_name in list_of_roles_name:
        index_of_role = list_of_roles_name.index(role_name)
        id_of_role = list_of_roles_id[index_of_role]
        role = guild.get_role(id_of_role)
        #this disables the role to stop sending messages but allows them to still see the messages
        perms = discord.Permissions()
        perms.update(read_messages= True, read_message_history=True,send_messages=False, connect = False)
        await role.edit(permissions = perms)

    while datetime.datetime.now() < end_time: #holds off the change back to the permission
        await asyncio.sleep(1)

    if role_name in list_of_roles_name:
        index_of_role = list_of_roles_name.index(role_name)
        id_of_role = list_of_roles_id[index_of_role]
        role = guild.get_role(id_of_role)
        #this disables the role to stop sending messages but allows them to still see the messages
        perms = discord.Permissions()
        perms.update(read_messages= True, read_message_history=True,send_messages=True, connect = True)
        await role.edit(permissions = perms)

# Exam Command 1.0b, Moderators able to close a course channel from time1/date1 to time2/date2.
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def examL(ctx, channel_name, course, course_number, space, date1, time1, to, date2, time2): 
#need to pass in the specific channel (physics course) and the specific time to close it for (1hr, 2hr, 1 day, etc.)
    
    role_name = course+' '+course_number

    month1 = int(re.split('/|-',date1)[0])
    day1 = int(re.split('/|-',date1)[1])
    year1 = int(re.split('/|-',date1)[2])

    month2 = int(re.split('/|-',date2)[0])
    day2 = int(re.split('/|-',date2)[1])
    year2 = int(re.split('/|-',date2)[2])

    hour1 = int(re.split(':', time1)[0]) 
    hour2 = int(re.split(':', time2)[0])

    minute1 = int(re.split(':|am|pm', time1)[1])
    minute2 = int(re.split(':|am|pm', time2)[1])

    minute_reader1 = re.split(':|am|pm', time1)[1]
    minute_reader2 = re.split(':|am|pm', time2)[1]

    if 'am' in time1:
        if hour1 == 12:
            militaryhour1 = 0
        else:
            militaryhour1 = hour1
    if 'pm' in time1:
        if hour1 == 12:
            militaryhour1 = 12
        else:
            militaryhour1 = hour1 + 12

    if 'am' in time2:
        if hour2 == 12:
            militaryhour2 = 0
        else:
            militaryhour2 = hour2
    if 'pm' in time2:
        if hour2 == 12:
            militaryhour2 = 12
        else:
            militaryhour2 = hour2 + 12
        
    start_time = datetime.datetime(year1, month1, day1, militaryhour1, minute1, 0)
    end_time = datetime.datetime(year2, month2, day2, militaryhour2, minute2, 0)

    await ctx.send(f'You will now change the settings of #{channel_name} at {militaryhour1}:{minute_reader1} on {month1}/{day1}/{year1} to {militaryhour2}:{minute_reader2} on {month2}/{day2}/{year2}')

    guild = client.get_guild(guild_id) #dont think i need this
    list_of_channels = [] #a list of TextChannel class of discord.py
    list_of_channels_name = [] #a list of strings (names)
    list_of_channels_id = [] #a list of integers (ids)
    list_of_roles = []
    list_of_roles_name = []
    list_of_roles_id =[]

    for guild in client.guilds:
        for channel in guild.text_channels: #gives the full list of channels plus ids
            list_of_channels.append(channel)
            list_of_channels_name.append(channel.name)
            list_of_channels_id.append(channel.id)
        for role in guild.roles:
            list_of_roles.append(role)
            list_of_roles_name.append(role.name)
            list_of_roles_id.append(role.id)

    if channel_name in list_of_channels_name:
        print(f'The following channel will be changed: {channel_name}')
    else:
        await ctx.send('You have not selected a valid channel.')

    while datetime.datetime.now() < start_time: #holds off the change in permission until the start time 
            await asyncio.sleep(1)

    if channel_name in list_of_channels_name: #searches for the postion of the given channel name and returns the location of it 
        index_of_name = list_of_channels_name.index(channel_name)
        id_of_channel = list_of_channels_id[index_of_name]
        channel = client.get_channel(id_of_channel)
        await ctx.send(f'The settings of #{channel_name} will now be changed to "only read".')
        await channel.send('Good luck with your final! You can do it')

    if role_name in list_of_roles_name:
        index_of_role = list_of_roles_name.index(role_name)
        id_of_role = list_of_roles_id[index_of_role]
        role = guild.get_role(id_of_role)
        #this disables the role to stop sending messages but allows them to still see the messages
        perms = discord.Permissions()
        perms.update(read_messages= True, read_message_history=True,send_messages=False, connect = False)
        await role.edit(permissions = perms)

    while datetime.datetime.now() < end_time: #holds off the change back to the permission
        await asyncio.sleep(1)

    if role_name in list_of_roles_name:
        index_of_role = list_of_roles_name.index(role_name)
        id_of_role = list_of_roles_id[index_of_role]
        role = guild.get_role(id_of_role)
        #this disables the role to stop sending messages but allows them to still see the messages
        perms = discord.Permissions()
        perms.update(read_messages= True, read_message_history=True,send_messages=True, connect = True)
        await role.edit(permissions = perms)

# Moderation Mute Feature
# Currently Discontinued 
######################################
'''
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def mute(ctx, member : discord.Member, *, length=None): #default length is 1 hr
#needs work before actually using
    if not length:
        member_permission = member.guild_permissions
        member_permission.update(send_messages=False)
        await asyncio.sleep(3600)
        member_permission.update(send_messages=True)

    if 'hr' in length or 'hour' in length or 'hours' in length:
        hour = int(re.split('hr|hour|hours', length)[0])
        time = hour * 3600
    if 'min' in length or 'minutes' in length or 'mins' in length:
        minutes = int(re.split('min|minutes|mins', length)[0])
        time = minutes * 60
    if 'day' in length or 'days' in length:
        days = int(re.split('day|days', length)[0])
        time = days * 86400
    if 'week' in length or 'weeks' in length:
        week = int(re.split('week|weeks', length)[0])
        time = week * 604800
    
    member_permission = member.guild_permissions
    member_permission.update(send_messages=False)
    await asyncio.sleep(time)
    member_permission.update(send_messages=True)
'''

# Allow Moderators to clear roles, specifically course channels after the end of the quarter
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id)
async def clear_role(ctx, role : discord.Role):
    guild = client.get_guild(guild_id)
    gaucho_role = guild.get_role(gaucho_id)
    graduate_role = guild.get_role(graduate_id)
    super_senior_role = guild.get_role(super_senior_id)
    senior_role = guild.get_role(senior_id)
    junior_role = guild.get_role(junior_id)
    sophomore_role = guild.get_role(sophomore_id)
    freshman_role = guild.get_role(freshman_id)
    role_members = role.members
    if role == gaucho_role or role == graduate_role or role == super_senior_role or role == senior_role or role == junior_role or role == sophomore_role or role == freshman_role or role == freshman_role:
        await ctx.send('Invalid role, please mention another role to clear.')
    if role != gaucho_role or role != graduate_role or role != super_senior_role or role != senior_role or role != junior_role or role != sophomore_role or role != freshman_role or role != freshman_role:
        for i in role_members:
            await i.remove_roles(role)

# Moderation Ban for x amount of time
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def ban(ctx, member : discord.Member , *, length):
    if 'hr' in length or 'hour' in length or 'hours' in length:
        hour = int(re.split('hr|hour|hours', length)[0])
        time = hour * 3600
    if 'min' in length or 'minutes' in length or 'mins' in length:
        minutes = int(re.split('min|minutes|mins', length)[0])
        time = minutes * 60
    if 'day' in length or 'days' in length:
        days = int(re.split('day|days', length)[0])
        time = days * 86400
    if 'week' in length or 'weeks' in length:
        week = int(re.split('week|weeks', length)[0])
        time = week * 604800
    
    member_roles = member.roles
    
    member_roles_list = []

    for role in member_roles:
        member_roles_list.append(role.id)

    guild = client.get_guild(guild_id)
    mod_role = guild.get_role(mod_id)
    treasurer_role = guild.get_role(treasurer_id)

    for i in member_roles_list[1:]:
        roles = guild.get_role(i)
        if roles == mod_role or roles == treasurer_role:
            await ctx.send('Invalid user due to having a mod role, please remove the role or select another user.')
            return

    #remove all roles except everyone
    for i in member_roles_list[1:]:
        roles = guild.get_role(i) 
        await member.remove_roles(roles)

    ban_channel = client.get_channel(ban_id)
    welcome_channel = client.get_channel(welcome_id)
    await ban_channel.set_permissions(member, read_messages = True, send_messages = True, read_message_history = False)
    await welcome_channel.set_permissions(member, read_messages = False, send_messages = False)
    
    await asyncio.sleep(time) 
    
    #add all removed roles
    for i in member_roles_list[1:]:
        roles = guild.get_role(i)
        await member.add_roles(roles)
    
    await ban_channel.set_permissions(member, overwrite = None)
    await welcome_channel.set_permissions(member, overwrite = None)

# Help Command for all Moderators, list of usable commands
######################################@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def helpA(ctx):
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
    embed = discord.Embed(title = 'Commands for this bot', description = 'When using these commands, begin your statement with "." followed by the name of the command',\
         colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = image)
    embed.add_field(name = 'announcement (post, annouce)', value = 'This command will send an announcment at a specfic time. Use today and now to send an announcement immediately. \
        **.announcement <date (mm-dd-yyyy)> <time (hh:mm)am/pm> <announcement>**')
    embed.add_field(name = 'clear_role', value = 'This command is only available to the founder and admins. This command will clear all the members from role. The format is as follows: **.clear_role @<role_mention>**',
        inline = False)
    embed.add_field(name = 'winner', value = 'This command is declearing a raffle winner for a specific channel.\
        The format is as follows: **.winner <#channel name>**', inline = False)
    embed.add_field(name = 'ban', value = 'This command will ban the member you mention for a certain amount of time, the least amount of time is 1 min. **.ban <member> <time>**', inline = False)
    embed.add_field(name = 'exam', value = 'This command is only available to admins and mods to close channels for a midterm or final. This command is for closing a channel for less than one day.\
        The format is as follows: **.exam <channel name> <role> from <date(mm-dd-yyyy)> <start time(hh:mm)am/pm> to <end time(hh:mm)am/pm>**', inline = False)
    embed.add_field(name = 'examL', value = 'This command is similar to exam but provides closing a channel for more than one day. \
        the format fot this command is as follows: **.exam <channel name> <role> from <first date(mm-dd-yyyy)> <start time(hh:mm)am/pm> to <second date (mm-dd-yyyy)> <end time(hh:mm)am/pm>**', inline = False)
    await ctx.send(embed = embed)

# Moderation Command: Raffle
# On Release had some bugs
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def winner(ctx, channel : discord.TextChannel):
    messages = await channel.history(limit = None).flatten()
    unique_members = []
    not_in_server = []
    for i in messages:
        if i.author.mention not in unique_members:
            role_list = []
            try:
                for j in i.author.roles:
                    role_list.append(j.id)
                if (founder_id or admin_id or treasurer_id or mod_id) not in role_list:
                    unique_members.append(i.author.mention)
            except:
                if i.author.mention not in not_in_server:
                    not_in_server.append(i.author.mention)
                    channel = client.get_channel(bot_command_channel_id)
                    await channel.send(f'{i.author.mention} is no longer in the server')
                    print(f'{i.author.mention} is no longer in the server')
    image = 'https://cdn.discordapp.com/attachments/700224899721199626/782224701229367316/UCSB_Discord_GIF9.gif'
    embed = discord.Embed(title = 'Raffle: the following are entered', description = '\n'.join(unique_members), colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url = image)
    await ctx.send(embed = embed)

    await asyncio.sleep(5)
    winner = unique_members[random.randint(0, len(unique_members)-1)]
    image = 'https://media.giphy.com/media/1Be435nPDxMFnsEq9r/giphy.gif'
    embed = discord.Embed(title = 'Raffle: WINNER', description = winner, colour = 0X003560, timestamp = datetime.datetime.now(datetime.timezone.utc))
    embed.set_image(url = image)
    #embed.set_thumbnail(url = image)
    await ctx.send(embed = embed)
    print(unique_members)


# Commands In Progress (Beta)
##################################################################################################################
##################################################################################################################


# Moderation Warning System
# Needs to be able to keep track of warns (automaton)
######################################
@client.command()
async def warn(ctx, member :discord.Member):
    embed = discord.Embed()
    embed.add_field(name = 'Warning', value = 'You are being warned, 3 warns will result in a 12hr mute.')
    await member.send(embed = embed)

# Moderation Mute Feature
# Still buggy
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def mute(ctx, member : discord.Member):
    # maybe add a channel where they can speak to admins and mods
    # also add maybe a message to the user being muted 
    # also start adding reasons to the audit logs
    guild = client.get_guild(guild_id)
    text_channels_list = guild.text_channels
    voice_channels_list = guild.voice_channels
    for i in text_channels_list:
        await i.set_permissions(member, send_messages = False)
    for j in voice_channels_list:
        await j.set_permissions(member, connect = False)

    await asyncio.sleep(30) #for 12 hrs, 43200 secs

    for i in text_channels_list:
        await i.set_permissions(member, overwrite = None)
    for j in voice_channels_list:
        await j.set_permissions(member, overwrite = None)

# User Command: Create Study Groups within the Server
######################################
@client.command()
async def create_channel(ctx, title, member1 : discord.Member, member2 : discord.Member =  None, member3 : discord.Member =  None, member4 : discord.Member =  None, 
            member5 : discord.Member =  None, member6 : discord.Member =  None, member7 : discord.Member =  None, member8 : discord.Member =  None, member9 : discord.Member =  None, member10 : discord.Member =  None):
            guild = client.get_guild(guild_id)
            list_of_categories = guild.categories
            for i in list_of_categories:
                if i.name == 'Study Group':
                    channel = await guild.i.create_text_channel(name = title)

                    await channel.set_permissions(ctx.author, read_messages = True, send_messages = True)
                    try:
                        await channel.set_permissions(member1, read_messages = True, send_messages = True)
                        await channel.set_permissions(member2, read_messages = True, send_messages = True)
                        await channel.set_permissions(member3, read_messages = True, send_messages = True)
                        await channel.set_permissions(member4, read_messages = True, send_messages = True)
                        await channel.set_permissions(member5, read_messages = True, send_messages = True)
                        await channel.set_permissions(member6, read_messages = True, send_messages = True)
                        await channel.set_permissions(member7, read_messages = True, send_messages = True)
                        await channel.set_permissions(member8, read_messages = True, send_messages = True)
                        await channel.set_permissions(member9, read_messages = True, send_messages = True)
                        await channel.set_permissions(member10, read_messages = True, send_messages = True)
                    except:
                        pass

            # await channel.send(f'Welcome @everyone to your personal study group!')

# Moderation Command: message non-gauchos to fill out the form to sign up for the server.
######################################
@client.command()
async def non_gaucho(ctx):
    guild = client.get_guild(guild_id)
    president = guild.get_member(president_id)
    for i in bot_list_id:
        await guild.get_member(i)

    welcome_channel = client.get_channel(welcome_id)
    non_gaucho_members = welcome_channel.members

    #embed or regular message
    for i in non_gaucho_members:
        message = f'Hey {i}! Welcome to UCSB Physics Discord Server, we are super glad you joined our community!\
            Please fill out the form to gain access to most of the channels. From the discord team we hope to see you there!\n\
            If you have any issues filling out the form, please reach out to {president.mention}.'
        await i.send(message)

    print(non_gaucho_members)

# Anonomity across all channels, use the anonymous code as a command. Will lack the complete anonymity but alllows for a simple anonymous post across the server
######################################
@client.command(aliases=['anonymity','a'])
async def anonymous(ctx,*,user_message):
    k = 0
    user_name = ctx.author
    channel = ctx.channel
    if user_name not in user_list:
        user = random.randint(0,9999)
        user_list.append(user_name)
        generated_user.append(f'User{user}')

        await ctx.message.delete()
        anonymous_message = await ctx.send(f'User{user}: {user_message}')
        anonymous_message_id = anonymous_message.id
        
        with open ("Anonymous_Log.json") as anonymous_log_json:
            data = json.load(anonymous_log_json)
            message_log = data['anonymous_message']
            new_entry = {"id": anonymous_message_id, "author": user_name.mention, "channel": channel.mention, "message": user_message}
            message_log.append(new_entry)
        write_json(data, "Anonymous_Log.json")

    elif user_name in user_list:
        for i in user_list:
            if i == user_name:

                await ctx.message.delete()
                anonymous_message = await ctx.send(f'{generated_user[k]}: {user_message}')
                anonymous_message_id = anonymous_message.id

                with open ("Anonymous_Log.json") as anonymous_log_json:
                    data = json.load(anonymous_log_json)
                    message_log = data['anonymous_message']
                    new_entry = {"id": anonymous_message_id, "author": user_name.mention, "channel": channel.mention, "message": user_message}
                    message_log.append(new_entry)
                write_json(data, "Anonymous_Log.json")

            k = k + 1

# Allows the staff to view the anonymous message, only use when neccessary, planning on adding a feature to only allow the message to show if 3 or more staff approve
######################################
@client.command(aliases=['afind'])
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def anonymous_finder(ctx,message_id):
    status = False
    try:
        message_id = int(message_id)
    except:
        await ctx.send('Please use the id of the message.')
    if ctx.channel.id != bot_command_channel_id:
        await ctx.message.delete()
        message = await ctx.send("Please do not use this command here!")
        await message.delete(delay = 5)
    else:
        with open ('Anonymous_Log.json') as anonymous_log_json:
            data = json.load(anonymous_log_json)
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

# Allows staff to trigger an update, for one day the bot will track messages so that when the update hits, deleted messages can be track from its previous sessions.
######################################
@client.command()
@commands.has_any_role(founder_id, admin_id, treasurer_id, mod_id)
async def update(ctx):
    await ctx.message.delete()
    global update_status
    if ctx.channel.id != bot_command_channel_id:
        message = await ctx.send("Please do not use this command here!")
        await message.delete(delay = 5)
    else: 
        update_status = True
        await ctx.send('Scheduling update for 1 day in advance.')
        await asyncio.sleep(30) #for 24 hrs = 86400
        update_status = False
        await ctx.send('Update will soon begin!')

client.run('TOKEN')