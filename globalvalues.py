import syschar
import os

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
# resets only when the enemy is defeated. (check syscombat.Combat.enemydefeated)

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

    while True:
        choice = raw_input("> ")

        if "1" in choice:
            makechar()
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

    globalvalues.p1 = syschar.PlayerCharacter(name)
    print globalvalues.p1.getstatus()
    print "^ This is your status."
    print "\nYou can obtain this at any time in the game if you type: "
    print "\'!status\'"
    print "while in game."
    print "\nHave fun on your endevours and good luck!"

    raw_input(globalvalues.cont_mssg)

    castle.main()

def gameover_combat():
    print "You have been defeated!"
    print "Better luck next time!"

    # Wait till user input to move on to main()
    raw_input(cont_mssg)
    main()
