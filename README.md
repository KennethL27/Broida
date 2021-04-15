# Broida
Alpha: *Version 1.2.2*
Beta: *Version 2.2.5*

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
* In the newest Alaha Version (1.2.1) a new command has been introduced for all users: `.a message`. The Anonymous command allows any user to post messages anonymously; however, it is not complete anonymous, if a user begins to type in a channel others in the chat can tell who is typing. Also there is some time between the bot catching the command and deleting it, which users in the channel can have a split second to view the original user. Similarly, like the anonymous bots, staff can view the information behind the anonymous post but it is important to note that this will only happen if the post breaks server rules. Also in this update, the backend for updates on Broida and delete message log has undergone complete changes. The client event for `on_delete_message(message)` has now changed to `on_raw_message_delete(payload)`. This works with the new staff command: `.update`. When an update for broida is going to be released, one of the staff must use the update command to allow Broida to start collecting message for one day (you may also chain this commands for more than 1 day). This allows for the new session of the updated Broida to be able to view its passed message in case of deleted messages. This allows for developers to conduct updates to Broida without having to worry about previous sessions. All new commands are reflected in the help commands for users and staff.
* With the latest Alpha Version (1.2.2), Broida now stores largest static list in a json file. Similarly, Broida has no begun using json files to externally store infomration to be able to recall it after sessions. Broida now allows for event reminders (specifically for moderators) and will allow for new events to be added by the `.add_event` command. The `.announcement` command now allows for command message edit to take into effect rather than deleting the via emoji. The `.winner` command now does not include staff members to be enter into the raffle pool. Lastly, the `.anonymous` command has expanded to Broida's DM. Simply use this format to target a viable text channel to post anonymously: `.anonymous general-chat Here is my message!`. Again a special thanks to Sarah Webster for helping build the anonymous DM feature. 

#### Beta

* All Alpha features are inluded in the Beta Version.
* Provides Users the ability to create Study Group Channels.
* Provides Moderators with a Warn System, Mute System, and Reminder System for Non-Gauchos.
* With Beta Version (2.2.1) two commands have been created:
1. anonymous (aka. a or anonymity): allows users within the server to post messages anonymously. For example, a user might message `.a message`, then Broida will remove the user's message and upload the message to a json file and send to the same channel `User1234: message`. Broida keeps track of each unique user and stores it under the same user number, built for continuity. 
2. anonymous_finder (aka afind): This command is only for staff members. This searches through the json file to find the corresponding id and returns the author, channel, and message that the anonymous user sent. This command only works in the dedicated staff bot-command-channel. There are some plans to add an extra step to actually recieve the info, more than 3 staff members must agree to view the anonymous user in order to view the info.
* With Beta Version (2.2.2) user command messages will no longer be deleted, this helps spread the acknowledgement of these commands and will help aim more use of Broida. 
* With Beta Version (2.2.3) a new staff command is created: update. This feature allows for seamless update of the bot on the client side. Previously, when an update was conducted, deleted messages from the previous session the information was lost. This can cause issues when moderations situation occurs. With the update command, Broida will start collecting all messages for a day, then the update can take place and the messages will be safely be stored. With the next Beta Version, the deleted_message event will improved upon this new command. 
* With Beta Version (2.2.4) a new system is now in place for messages to be saved from one code session to another. To fully use this new feature you must use the command detailed above (in version 2.2.3): `.update`. This allows Broida to start gathering messages being sent through the server for one day. Then once Broida is updated, any deleted messages that happened in that day Broida will be able to check the file for that message. This will send the deleted message to the deleted-message-log for staff to view in case of a situation.
* With Beta Version (2.2.5) there has been a big improvement on how data is going to be stored with Broida. 
1. With this new version there is now two new json files: Bot_Info.json and Bot_string_list.json. The first one will provide useful information such as exam times and events. This information will stay across different sessions. Similarly, the second json file being introduce is to reduce the amount of storage Broida has to hold by replacing the two biggest list into a json file, which Broida can access. 
2. A nice feature being introudce is event reminders, this is set up in the `on_ready()` function and conintues to run in the background of Broida, which works hand-in-hand with the new `.add_event` command. For now it only serves a purpose to the staff and not to every member. Expanding this feature to the whole server depends on its usefullness.
3. A huge improvment has been added to the `.announcement` command! Now staff members can edit their command message, containing the announcement, and Broida will now be able to edit and update each time you make any changes. The trash bin emoji can still serve this function, but its main focus will be to completely eliminate the announcment or change the date/time. The next update for this command will allow staff to edit the date/time on the original message.
4. The bugs found in the `.winner` command have now been fixed, it no longer allows staff members to be part of the raffle pool.
5. Two projects has been started for keeping track of new users and exiting users. The functions for this feature are `on_member_join()` and `on_member_remove()`.
6. Lastly, the largest update in this version is `.anonymous`, which will now allow users to DM Broida in order for them to send completely anonymous messages within the server. As long as the user is able to see and able to send messages in the channel of their choosing, then Broida will be allowed to send anonymous messages for you. This command has also been setup to be able to clear the user generated number ever so often, to retain anonymous. *Important note: staff members can still use `.anonymous_finder`*
Special thanks to Sarah Webster for helping me out with the updated version of the `.anonymous` command.

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