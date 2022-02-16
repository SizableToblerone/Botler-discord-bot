# Roll Call methods
# All the methods created for the Roll Call procedure, not including the client event "on_raw_reaction_add."
import re
import discord


async def new_rollcall(message):
    """This function creates a new roll call."""
    # confirm that the requester provided an event.
    try:
        # extract event from message
        event = re.findall('for a .* event', str(message.content))

        # convert event from list to str, and trim the "a" and "event" out of the event name.
        event = event.pop()
        event = event[6:len(event) - 6]
    except:
        await message.channel.send('I need you to tell me the event this is for in your request, sir.'
                                   '\n\"**...create an event [event name] (for) [date]**')

    # check whether the requester provided a date.
    date = re.findall('\d+/\d+/\d+', str(message.content))
    if date:
        date = date.pop()
        roll_str = f'__**Roll Call:  {event},  {date}  **__'
    else:
        roll_str = f'__**Roll Call: {event}**__'

    # adds event members to string.

    with open(f'rc_{event}.txt', 'r') as file:
        event_members = file.read()
    roll_str = f'{roll_str}\n{event_members}'

    # sends the rollcall message to the chat requesting it.
    await message.channel.send(roll_str)

    # adds some emojis for easy clickage.
    await message.channel.last_message.add_reaction('✅')
    await message.channel.last_message.add_reaction('❌')
    await message.channel.last_message.add_reaction('☑')

    return


async def update_rollcall(client, payload):
    """This function is called when a raw reaction is detected, and confirmed to be a rollcall reaction. It updates the
    rollcall."""
    # gets the payload channel, then fetches the rollcall's Message object from it.
    rollcall_message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    print(rollcall_message)

    # TODO this is just a bandaid to fid the mysterious exclamation point appearing outside bot-tests for some reason.
    user = payload.member.mention
    user = user.replace('!', '')
    # retrieves the contents of the message, then creates a string with reacting account's emoji status updated.
    if re.findall(f':.*:{user}', rollcall_message.content):
        edited_rollcall_str = re.sub(f':.*:{user}',
                                     f'{payload.emoji}{user}',
                                     rollcall_message.content)
        # print('found')
    else:
        edited_rollcall_str = re.sub(f'.{user}',
                                     f'{payload.emoji}{user}',
                                     rollcall_message.content)
        # print('notfound')

    # executes the edit on the rollcall message.
    await rollcall_message.edit(content=edited_rollcall_str)
    print('end of update')
    return


# TODO only let trusted users create new events.
# adds a discord user to a file containing a list of names
async def add_to_rollcall_event(message_content=str, member=str):
    # extract event from message
    event = re.findall('the .* event', message_content)

    # pop str out of list, and trim the "the" and "event" out of the event name.
    event = event.pop()
    event = event[4:len(event) - 6]

    with open(f'rc_{event}.txt', 'a') as file:
        file.write(f':grey_question:{member}')
    return


# TODO lock to trusted users.
async def remove_from_rollcall_event(event=str, member=str):
    # creates a set of members, then removes the member in the method parameter.
    members_set = set_of_rollcall_event_members(event)
    members_set.discard(member)

    # empties the file.
    with open(f'rc_{event}.txt', 'a') as file:
        pass
    # refills the file with the altered members.set
    for x in members_set:
        if not re.findall(member, x):
            with open(f'rc_{event}.txt', 'a') as file:
                file.write(f':grey_question:{member}')
    return


# returns a list of each line in the event's storage string
async def set_of_rollcall_event_members(event=str):
    members = {}
    with open(f'rc_{event}.txt', 'r') as file:
        members.add(file.readlines())
    return members
