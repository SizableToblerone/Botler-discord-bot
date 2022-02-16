# Botler
My Discord bot.

Botler is a hobby project I'm making, primarily with the objective of measuring (and improving) my Python abilities.
He's based in the *discord.py* API.

__Commands:__

*"Botler, do you think...?"*
- 8ball command. The user includes a question after "think," and Botler will provide a positive or negative response. 

*Botler, roll me 4d6, 5d8, and 2d4."*
- When Botler notices '*X*d*Y*' formats in your message, he will parse the message as a dice rolling command, where *X* is the number of dice to roll, and *Y* the range of the dice. If the message contains multiple '*X*d*Y*' items, Botler will roll them all. He will display all individual dice rolls, and the total sum.  


*Botler, roll me a d20.* 
- If you ask Botler for "1d20," he'll use the previous command. But if you commit the 1, he'll use this dedicated d20 roller instead, returning your result with a polite sentence instead of a table of rolls. 

