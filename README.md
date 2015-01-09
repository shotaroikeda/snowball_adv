# snowball_adv
A primitive RPG on command line. Features combat using OoP across multiple files, which is the main objective of this project. See readme.md for more details

# How to run the game
Make sure you have python 2.7.x installed. This will only run on python 2.7.x.
When you have the game downloaded, run your terminal program. (ie Windows Powershell, Terminal, etc.)
cd into the game directory, then run snowball_adv.py

# Table of contents:
  1. General Overview
  2. File contents and what they do
    I. globalvalues.py
    II. syschar.py
    III. combat.py
    IV. snowball_adv.py
    V. Any other files
  3. Organization (see here if you want to add levels to the game)
  4. Changelog
  5. Future Addons

1. General Overview:

  Welcome to the world of snowball_adv.py! In this world you will be adverturing in the land of nowhere. The game is all done on through the command line, which means no GUI. Unlike traditional zork variants however, this game features a primitive form of combat. Hopefully we will be able to extend our knowledge and experience from the game to create a more complex one later.

  This is the first project I have done (as well as most main contributors). So the code may not be the best it could be, there will be some bad memory management and mediocre code. As we get better at it, we may have mass revisions and cleanups of the code.

2. File contents and what they do

  I. globalvalues.py:
    This file manages the global instances and variables created, such as the instance for the player. Especially when creating levels (see organization for more details), having instances created within specific parts of the game makes the code a little sloppy and causes some weird import loops.
    Ex. One file creates the instance, which means that all the other files must be importing that one. However, that file will be imported across other places to keep the organization better. This causes an infinite loop of imports that basically makes the python say "No"

  II. syschar.py
    This file managaes all the generation/character management in game. The code here is relatively sloppy, which should be cleaned up a lot more soon.

  III. combat.py
    This file manages all the combat management. This should be called everytime there is combat required.

  IV. snowball_adv.py
    This is the "starting point" of the game. This is the file will be run to begin the game.

  V. Any other files
    These should be the level files. Each "location" will have it's own individual file associated with them.
    All files should be importing syschar, globalvalues, and combat.

3. Organization
  Each individual level will have it's own .py file. No other organization planned at this time

4. Changelog
  Not formally released yet.

5. Future addons(?)
  A primative inventory management would be really cool to script in. Obviously the full fledged game. Save data???
