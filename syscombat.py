#this manages combat

import syschar
import globalvalues
import random

class Combat(object):
    # Combat should flow like this:
    # 1. playerchoice()
    # 2. calls whatever the player choice is
    # 3. enemychoice()
    # 4. calls whatever the enemychoice is

    def __init__(self, boss=False, level=None, hp=None, strength=None, exp=None):
        """When called, creates a new instance of combat."""
        # Generates an enemy unless otherwise specified
        # Good for set in game bosses.
        if boss == False:
            #initialize the enemy
            globalvalues.ai = syschar.EnemyCharacter(globalvalues.p1.getlevel())
        else:
            #read enemy values...
            globalvalues.ai = [level, hp, hp, strength, exp]

    # Some classes for Player side
    def playerchoice(self):
        # Prompt the player what they would like to do...
        # Player will always attack first

        print "\nIt's your turn!\n"
        print "\nWhat would you like to do?"
        print " 1. Attack"
        print " 2. Defend"
        print " 3. Run"

        while globalvalues.p1.checkalive() or globalvalues.ai.checkalive():

            choice = raw_input("> ")

            if '1' in choice:
                self.playerattack()
            elif '2' in choice:
                self.playerdefend()
            elif '3' in choice:
                self.playerrun()
            elif '!status' in choice:
                print globalvalues.p1.getstatus()
            elif '!option' in choice:
                print "1 - Attack the enemy\n2 - Defend against enemy attack"
                print "3 - Attempt to run away"
        # Runs only when one of the hp's hit 0
        if not globalvalues.p1.checkalive():
            # checking player's health comes first
            # because dead = dead, even if you defeat the enemy
            self.playerdefeated()

        # Same deal here
        elif not globalvalues.ai.checkalive():
            self.enemydefeated()

    def playerattack(self):
        """
        Figures out what to do when the player attacks
        Passes values to dmgcalc then passes it to enemy's health
        """
        playerstr = globalvalues.p1.getstrength()
        # see combatvaluetable.xlsx to see some possible values of
        # self.playerrawdamage
        self.playerrawdamage = int((playerstr - 4) * 102 * 0.32)

        self.combat()


    def playerdefend(self):
        """
        Figures out what to do when the player defends
        """
        # Player is defending!
        self.playerdefend == True

        self.combat()

    def playerrun(self):
        """
        Figures out what to do when the player runs
        """
        # Calculating level difference. enemyinfo[0] returns level
        p1level = globalvalues.p1.getlevel()
        enemyinfo = globalvalues.ai.getstatus()
        level_diff = enemyinfo[0] - p1level

        # Generate the sequence used to determine if runnable
        runcount_math = int(globalvalues.runcounter * 0.8 + 1)
        maxrange = runcount_math + int(level_diff * 0.3 * roundcount_math)
        runmap = range(0, maxrange)

        # Use runmap to figure out if running away was successful
        if level_diff < 0:
            # You over power the opponent, automatically run away
            globalvalues.runcounter += 1
            print 'You have successfully run away!'
        elif 0 == random.choice(runmap):
            globalvalues.runcounter += 1
            print 'You have successfully run away!'
        else:
            globalvalues.runcounter = 0
            print 'You have failed to run away'

    def playerdefeated(self):
        """
        Figures out what to do when the player is defeated
        """
        globalvalues.gameover_combat()

    # Some classes for enemyside
    def enemychoice(self):
        #
        choice = random.randint(0, 10)



    def enemydefeated(self):
        pass
    def dmgcalc(self, attackerlvl, attackerstr, defenderlvl, defenderhp):
