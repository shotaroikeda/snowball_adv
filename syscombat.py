#this manages combat

import syschar
import globalvalues

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

        elif not globalvalues.ai.checkalive():
            self.enemydefeated()

    def playerattack(self):
        """
        Figures out what to do when the player attacks
        Passes values to dmgcalc then passes it to enemy's health
        """
        playerstr = globalvalues.p1.getstrength()
        self.playerrawdamage = int((playerstr - 4) * 102 * 0.32)

        self.combat()


    def playerdefend(self):
        """
        Figures out what to do when the player defends
        """
        self.playerdefend == True

        self.combat()

    def playerrun(self):
        """
        Figures out what to do when the player runs
        """
        

    def playerdefeated(self):
        """
        Figures out what to do when the player is defeated
        """
        pass

    # Some classes for enemyside
    def enemychoice(self):
        pass

    def enemydefeated(self):
        pass
    def dmgcalc(self, attackerlvl, attackerstr, defenderlvl, defenderhp):


    def fight(self, )
