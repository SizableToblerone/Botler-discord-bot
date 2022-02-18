import discord
import math
import random
import re
from typing import overload

botlerstats = {
    "str" : 0,
    "dex" : 0,
    "con" : 0,
    "int" : 20,
    "wis" : 10,
    "cha" : 8,
}


def roll_5e_stat():
    """**INCOMPLETE** "Botler, roll me an ability score.":
    Rolls 4d6, drops the lowest roll, and returns the sum of the other 3 dice."""
    rolls = [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]
    rolls.sort()
    rolls.pop(0)
    stat = 0
    for x in rolls:
        stat += x
    return stat


def roll_5e_char():
    """ "Botler, roll me some stats.":
    Rolls a 5e statblock."""
    strength = roll_5e_stat()
    dexterity = roll_5e_stat()
    constitution = roll_5e_stat()
    intelligence = roll_5e_stat()
    wisdom = roll_5e_stat()
    charisma = roll_5e_stat()
    return f'{strength} ({string_stat_bonus(strength)}) strength\n' \
           f'{dexterity} ({string_stat_bonus(dexterity)}) dexterity\n' \
           f'{constitution} ({string_stat_bonus(constitution)}) constitution\n' \
           f'{intelligence} ({string_stat_bonus(intelligence)}) intelligence\n' \
           f'{wisdom} ({string_stat_bonus(wisdom)}) wisdom\n' \
           f'{charisma} ({string_stat_bonus(charisma)}) charisma\n'


def botlers_stats():
    """ "Botler, what are your stats?":
    Botler displays his 5e ability scores."""
    strength = botlerstats['str']
    dexterity = botlerstats['dex']
    constitution = botlerstats['con']
    intelligence = botlerstats['int']
    wisdom = botlerstats['wis']
    charisma = botlerstats['cha']
    return f'{strength} ({string_stat_bonus(strength)}) strength\n' \
           f'{dexterity} ({string_stat_bonus(dexterity)}) dexterity\n' \
           f'{constitution} ({string_stat_bonus(constitution)}) constitution\n' \
           f'{intelligence} ({string_stat_bonus(intelligence)}) intelligence\n' \
           f'{wisdom} ({string_stat_bonus(wisdom)}) wisdom\n' \
           f'{charisma} ({string_stat_bonus(charisma)}) charisma\n'


def string_stat_bonus(stat):
    return math.floor((stat-10)/2)


def scaled_roll(user_message):
    """ "Botler, roll me 4d6, 5d8, and 2d4.":
    When Botler notices 'XdY' formats in a message, he will parse the message as a dice rolling command, where X is
    the number of dice to roll, and Y the range of the dice. If the message contains multiple 'XdY' items, Botler will
    roll them all. He will display all individual dice rolls, and then the total sum."""
    num_d_nums = re.findall('\d+d\d+', user_message)  # list of '\d+d\d+' items
    rolls_super_sum = 0  # sum of all rolls.

    display = 'Here is your roll, sir: ' \
              '```\n| DIE | SUM | ROLLS          '
    row = '\n| d{:<3}|{:^5}|{:>4}'

    for x in num_d_nums:  # iterate through the handfuls
        split = re.split('d', x)  # separate the numbers in the dice call from the d.
        dice_count = int(split[0])  # number of dice to roll is the number left of the d.
        dice_size = int(split[1])  # die size is the number right of the d.
        die_rolls = []  # list recording each roll

        rolls_sum = 0  # sum of all the rolls in this handful.

        if dice_count > 31: return f'That\'s a few dice too many, sir. I can\'t hold that many d{dice_size} at once.' \
                                   f'\nMy hands are so very small, and my arms so terribly weak. ' \
                                   f'My deepest apologies, sir.'

        while dice_count > 0:
            roll = random.randint(1, dice_size)  # roll a die.
            die_rolls.append(roll)  # add a roll to die_rolls.
            rolls_sum += roll  # add THAT^ die roll to the sum.
            dice_count -= 1  # count down once for each die rolled.

        die_rolls.sort()  # sort the rolls.
        display += row.format(dice_size, rolls_sum, die_rolls.pop())  # add row to display string.
        while len(die_rolls) > 0:  # add each die roll to the display string.
            display += '{:>4}'.format(str(die_rolls.pop()))

        rolls_super_sum += rolls_sum

    display += '\n{:>10}  | TOTAL```'.format(rolls_super_sum)
    return display
