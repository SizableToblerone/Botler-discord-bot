# Misc Methods
# just a separate file to tuck my methods into, so I don't have to pile them all up under main.
import re
import discord

import dice


def botler_help(channel):
    """"Botler, help" / "botler, what can you do?"
    **INCOMPLETE** Sends a message listing documentation of all methods available through Discord."""
    methods = {
        dice.roll_5e_stat().__doc__,
        dice.roll_5e_char().__doc__,
        dice.botlers_stats().__doc__,
        dice.scaled_roll().__doc__
    }
    help_str = ''
    for x in methods:
        help_str = f'{help_str}\n\n{methods[x]}'
    return help_str



def kill_this_fool(self):
    """"Botler, kill this fool."
    **INCOMPLETE** casts a random lvl 8-9 spell from DnD 5e at most recent user to send a message."""
    return


async def eightball(message):
    """"Botler, do you think [...]?"
    **INCOMPLETE** Returns an affirmative or negative in response to a question."""
    return ord('ew')
