# Broida
Alpha: *Version 1.2.0*
Beta: *Version 2.2.0*

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
* Provides Users the ability to create Study Group Channels and Anonymously post in any channel. 
* Provides Moderators with a Warn System, Mute System, and Reminder System for Non-Gauchos.
___

## Installation 
*Meant for the Beta Version*

### Discord Bots

In order to run Discord Bots you must first create a [Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) and create one. 

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