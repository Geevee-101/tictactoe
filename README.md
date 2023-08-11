# Tic-Tac-Toe
A text-based version of Tic-Tac-Toe made in Python.

# Project Description
I wanted to make a Tic-Tac-Toe game with an enemy AI for the player to fight against. The AI should be impossible defeat, as how a game of Tic-Tac-Toe is when played between two expert players.

To understand all the strategies of the game, I refered to a How-To wiki. From there I broke down the strategies into code that makes up the enemy AI.
I noticed that the moves taken depend on the round hence the moves taken by the computer revolves around what round it is.
Besides that, the enemy AI is capable of checking for oppurtunities to make a two move win tactic before proceeding to setup the move.
The AI will also check if the player is about to win and proceed to block.
You may see the result of this coding in enemy_ai.py.

The main.py contains the interface with the player and also functions that help verify any inputs.

The check_win.py while that is used by main.py to check if any player has won. It is also used by enemy_ai to predict possible wins.

The player.py contains the class for the players and art.py contains the ASCII art of the game title.

# Installation
It's a simple app that only requires you to dump all the files into the same folder and run from main.py.


