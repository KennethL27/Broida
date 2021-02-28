# Broida
Alpha: *Version 1.2.0*
Beta: *Version 2.2.2*

![Broida Discord Profile](https://raw.githubusercontent.com/KennethL27/Broida/master/Images/Broida_Profile.jpg "Broida Discord Profile") 

___
## Overview

### Description

<table>
<tr>
<td>
  Broida is made for the Univeristy of California, Santa Barabara Physics Discord. The main purpose behind this project is to provide useful information to both moderators and users. Broida is made by using <a href="https://discordpy.readthedocs.io/en/latest/">Discord's Python API</a>. As the UCSB Physics Discord Community continues to grow, Broida will become more intricate and provide more usufull tools. This project includes a Beta and Alpha Version, where the Alpha Verison is currently running on a Rasberry Pi 4. 
</td>
</tr>
</table>

### Features

#### Alpha

* Provides Users with Purposed Physics Teahing Assignments, Apppointment Link to Physics Advising, Link to Important Dates, the active times that a course will have an exam, UDIP Merch Website, Random Physics Facts, Other UCSB Club Discord Servers, and the amount of time that the bot has been running for.
* Provides Moderators to close course channels for exams, set post to be released at a futer date/time, clear course roles, and ban users for some time.
* Ticket System, delete message log, and channel raffle.
* Help command for both Users and Moderators.

#### Beta

* All Alpha features are inluded in the Beta Version.
* Provides Users the ability to create Study Group Channels.
* Provides Moderators with a Warn System, Mute System, and Reminder System for Non-Gauchos.
* With Beta Version (2.2.1) two commands have been created:
1. anonymous (aka. a or anonymity): allows users within the server to post messages anonymously. For example, a user might message `.a message`, then Broida will remove the user's message and upload the message to a json file and send to the same channel `User1234: message`. Broida keeps track of each unique user and stores it under the same user number, built for continuity. 
2. anonymous_finder (aka afind): This command is only for staff members. This searches through the json file to find the corresponding id and returns the author, channel, and message that the anonymous user sent. This command only works in the dedicated staff bot-command-channel. There are some plans to add an extra step to actually recieve the info, more than 3 staff members must agree to view the anonymous user in order to view the info.
* With Beta Version (2.2.2) user command messages will no longer be deleted, this helps spread the acknowledgement of these commands and will help aim more use of Broida. 

___

## Installation 
*Meant for the Beta Version*

### Discord Bots

In order to run Discord Bots you must first create a [Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) and create one. 
1. Head over to the Developer Portal and sign in with your discord account.
2. Once you successfully sign in go to the "Applications" tab and create a new Application with the "New Application" button on the top right.
3. Create a Name for this new application (or bot) and hit the "Create" button.
4. On the left side cick on "Bot" and on the right side use the "Add Bot" to create the bot. You will need to comfirm by clicking  on "Yes, do it!"
5. You have now created a Bot! Copy the token (next to the Bot's icon) and use it in your code for the bot to run. *Note: Do not give anyone your bot's token! In case the token is shared, use the "Regenerate" button to make sure you Bot is safe.*
6. Before you can actually see you go live, you must invite your bot to a server. On the left side go to "OAuth2"
7. In the "OAuth2" tab, check mark "bot" in the middle column. You will now see more options at the bottom, these options are to grant your bot's permission. For testing sake I suggest check marking "Administrator". This grants all premission to the bot, and most of these permissions can be changed within the server. 
8. With the permissons selected you can copy the link above the permission option and past it in a new tab. Select a server you want to bring the bot into, you must have the permission to manage the server in order to introduce a bot. If you dont have a server with this permission I suggest creating a personal server. 
9. Once you have the server selected, click "Authorize" and begin coding!

### Discord.py

__Windows/Linux__

`pip install discord.py`

___

## Usage
Prerequisites: Python 3.7, Discord.py 1.5.1

For the most basic Discord Bot the following is the base code:

```python
import discord

client = discord.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print('Bot is online')

client.run('Token')
```

Once this simple code has been working correcly with your own bot setup, you may now use functions from Broida(beta).py

___

## Contribution

All of the contribution made so far have been done by Kenneth Lara. Input to form different systems are a collaborative effor made by the staff of UCSB Physics Discord and by the community itself.

## Message from the Founder of UCSB Physics Discord and Broida

I would like to thank all of those who have encouraged me to continuly purseue this avenue. I am more than thankful for all the support and suggestions that the Physics Community has given to me at UCSB. Thank you Thank you Thank you!