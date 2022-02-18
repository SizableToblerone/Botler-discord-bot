# Misc Methods
# just a separate file to tuck my methods into, so I don't have to pile them all up under main.
import re
import discord

import dice


def botler_help():
    """ "Botler, help" / "botler, what can you do?"
    **INCOMPLETE** Sends a message listing documentation of all methods available through Discord. Method documentations
     should include an example of the relevant command, starting with ' "' and ending with '" '."""
    methods = {
        ' \"don\'t call me sir, Botler.\":',
        dice.roll_5e_stat.__doc__,
        dice.roll_5e_char.__doc__,
        dice.botlers_stats.__doc__,
        dice.scaled_roll.__doc__
    }
    help_str = ''
    for x in methods:
        help_item = re.sub(' \"', '__\"', x)
        help_item = re.sub('\":', '\"__', help_item)
        help_str = f'{help_str}\n\n{help_item}'
    return help_str
    # return dice.roll_5e_char.__doc__


async def suggestion(message):
    with open('suggestions.txt', 'a') as file:
        file.write(f'\n{message.author}:\n {message.content}\n')
    return f'I\'ll take that under advisement, sir. My thanks.'


async def eightball(message):
    """"Botler, do you think [...]?"
    **INCOMPLETE** Returns an affirmative or negative in response to a question."""

    # if message.content[-13:-1] == 'do you think' or message.content[-12:-1] == 'do you thin':
    if len(message.content) == 19 or len(message.content) == 20 or len(message.content) == 21:
        return 'I try not to, sir.'

    ascii_sum = 0  # holds the sum of the ascii conversions for each character in the string.
    for x in message.content:
        ascii_sum += ord(x)
    conclusion = bool(ascii_sum % 2)  # converts ascii_sum to TRUE or FALSE based on whether it is even or odd.

    affirmative_responses = {
        'Yes',
        'I beleive so',
        'I would think so',
        'As I see it, yes',
        'Ask again later,'

Better not tell you now

Cannot predict now

Concentrate and ask again

Don’t count on it

It is certain
    }
    negatory_responses = {
        'No',
    }

    return conclusion  # testing ascii conversion


def kill_this_fool(self):
    """"Botler, kill this fool."
    **INCOMPLETE** casts a random lvl 8-9 spell from DnD 5e at most recent user to send a message."""
    return
