import syschar
import os
import sys

global p1
# p1 is an instance of syschar.PlayerCharacter.
# p1 will keep track of the player's statuses

global ai
# ai is an instance of syschar.EnemyCharacter or syschar.BossCharacter.
# Keeps track of enemy things DURING combat

global runcounter

# runcounter keeps track of how many times the player has run away from battle
# only counts consecutive runs
# hopefully will prevent players from running away from battle all the time
# resets only when the running away fails. (check syscombat.Combat.playerrun)

global cont_mssg
cont_mssg = "Press Enter to Continue..."
# Just a shortcut because I'm too lazy to type the message over and over

# Make sure you can clear the screen on all OSs
def clearscreen():
    try:
        os.system('cls')
    except NameError:
        os.system('clear')
def main():
    print "1. Start"
    print "2. Quit"

    namecheck = True

    while namecheck:
        choice = raw_input("> ")

        if "1" in choice:
            makechar()
            namecheck = False
        elif "2" in choice:
            sys.exit()
        elif "!option" in choice:
            print ("1 - Begin the game!\n2 - Quit the game.")
        else:
            print "Please try again."

def makechar():
    clearscreen()
    print "Get ready to explore the strange world!"
    print "However, before you begin, I would like to know your name...."

    name = raw_input("> ")

    #initialize p1 and runcounter to be used elsewhere
    global p1
    p1 = syschar.PlayerCharacter(name)
    global runcounter
    runcounter = 0
    
    print p1.getstatus()
    print "^ This is your status."
    print "\nYou can obtain this at any time in the game if you type: "
    print "\'!status\'"
    print "while in game."
    print "\nHave fun on your endevours and good luck!"

    raw_input(cont_mssg)

def gameover_combat():
    print "You have been defeated!"
    print "Better luck next time!"

    # Wait till user input to move on to main()
    raw_input(cont_mssg)
    sys.exit()
