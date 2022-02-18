import discord
import re
import random
import dice
import mm
import rollcall
# from replit import db
# from keep_alive import keep_alive

TOKEN = input('Enter bot token.\n')
TOKEN = re.findall('O.*c', TOKEN).pop()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # abridged call for re.findall, to save visual clutter.
    def heard(str_):
        return re.findall(str_, user_message)

    # abridged call for message.channel.send, to save visual clutter.
    async def speak(str_):
        await message.channel.send(str_)

    if heard('Botler') or heard('botler,'):
        # scaleable dice roller
        if heard('\d+d\d+'):
            await speak(dice.scaled_roll(user_message))

        # report botler's stat block
        elif heard('what are your stat'):
            await speak(dice.botlers_stats())

        # roll a 5e statblock
        elif heard('stats') and heard('roll'):
            await speak(dice.roll_5e_char())

        # correct the way botler refers to a user
        elif heard('call') and heard('me') and heard('sir'):
            # TODO add users to list.
            await speak(dice.scaled_roll(f'Very well, ma\'am.'))

        # add suggestion to suggestions.txt
        elif heard('should') and heard('add'):
            # with open('suggestions.txt', 'a') as file:
            #     file.write(f'\n{username}:\n {user_message}\n')
            # await speak(f'I\'ll take that under advisement, sir. My thanks.')
            await speak(await mm.suggestion(message))

        # add a user to a roll call event
        elif re.findall('add \d+ to the .* roll call', user_message):
            await rollcall.add_to_rollcall_event(message.content, message.author.mention)  # test add me to list

        # create a new roll call
        elif heard('roll call') or heard('rollcall'):
            await rollcall.new_rollcall(message)

        elif heard('d20'):
            roll = random.randint(1, 20)
            await speak(f'A {roll} / 20, sir.')

        elif heard('do you think'):
            await speak(await mm.eightball(message))

        elif heard('kill this fool'):
            await speak(mm.kill_this_fool())

        elif heard('help') or heard('what can you do'):
            await speak(mm.botler_help())

        elif heard('.*, Botler.'):
            await speak(f'Thank you sir.')

        elif re.findall('thank you', user_message.lower()) or re.findall('thanks', user_message.lower()):
            await speak('Of course, sir.')

        elif heard('Botler.'):
            await speak('Here, sir.')

        else:
            await speak('You rang, sir?')
        return

    if (heard('to bed') and heard('going')) or (heard('to sleep') and heard('going')) \
            or heard('goodnight') or heard('good night'):
        await speak('Good night, sir.')
    # todo "botler kill this fool" "one day you'll decompose and ill be there to watch it happen, sir."


# update the rollcall whenever a reaction is added to it.
# https://discordpy.readthedocs.io/en/stable/api.html#discord.on_raw_reaction_add
# https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.fetch_message
@client.event
async def on_raw_reaction_add(payload):
    # gets message of payload
    rollcall_message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)

    # check whether payload is a reaction to a Botler message, and whether it is a rollcall.
    if rollcall_message.author == client.user and re.findall('__\*\*Roll Call', rollcall_message.content):
        await rollcall.update_rollcall(client, payload)

# keep_alive()  # allows uptimerobot to keep the bot alive
client.run(TOKEN)
