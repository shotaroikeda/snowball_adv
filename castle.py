import globalvalues
import os
import syscombat

def main():
    globalvalues.clearscreen()



    print "Test combat fight here"
    syscombat.Combat()

    print 'You have found yourself in front of a castle.'
    print 'There is a forest to your left, a castle in the front, and a brick wall to the right'
    print globalvalues.p1.getstatus()

    while True:

        choice = raw_input("> ")
        choice_lowercase = choice.lower()


        if '!option' in choice:
            print "left - go to forest\nfront - go to castle\nright - go to brick wall"
        elif '!status' in choice:
            print globalvalues.p1.getstatus()

        # Debug items
        elif '!spawn' in choice:
            print "spawning combat..."
            raw_input(globalvalues.cont_mssg)
            globalvalues.clearscreen()
            syscombat.Combat()
        elif '!shotaro' in choice:
            print "hey"
        elif '!heal' in choice:
            print "healing 100hp"
            globalvalues.p1.gethp(-100)
        elif '!run':
            print globalvalues.runcounter

        # To be added...
        elif 'l' in choice:
            pass        #go to forest
        elif 'f' in choice:
            pass        # go into castle
        elif 'r' in choice:
            pass        # go into
        else:
            print "Invalid choice, please try again."
