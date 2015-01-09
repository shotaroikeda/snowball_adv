#main game here

import globalvalues
import syschar
import sys
import castle
import os

globalvalues.clearscreen()

debug = 'I am stuck here'

def main():
    print "Hello!"
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
    globalvalues.clearscreen()
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



print "Welcome to snowball_adv.py!"
print "Here you will traverse the land of absolutely nothing."
print "\n\nWhen you are stuck, type \'!options\'. This will help you greatly."
main()
