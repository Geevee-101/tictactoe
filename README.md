# Tic-Tac-Toe
A text-based version of Tic-Tac-Toe with a simple enemy AI for the player to fight against. Made in Python.

# Project Description
The AI has three difficulties to choose from: Easy, Medium, and Impossible. Easy is meant to simulate a player who does not know what they are doing. Medium simulates a competent player; it will block you if you try to win in a straight forward manner. Impossible simulates an expert player who cannot be defeated. It is capable of checking for opportunities to make a two-move win tactic before proceeding to set up the move.

To understand all the strategies of the game, I referred to a How-To wiki. From there I broke down the strategies into code that makes up the enemy AI. I noticed that the moves taken depend on the move number hence the moves taken by the computer revolve around what move number it is. You may see the result of this coding in enemy_ai.py.

The main.py contains the interface with the player and also functions that help verify any inputs.

The check_win.py is used by main.py to check if any player has won. It is also used by enemy_ai.py to predict possible wins.

The player.py contains the class for human players and art.py contains the ASCII art of the game title.

Addtionally you can also battle against another player (local).

# Installation
It's a simple app that only requires you to dump all the files into the same folder and run from main.py.
