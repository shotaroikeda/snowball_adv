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
            globalvalues.ai = syschar.BossCharacter(level, hp, hp, strength, exp)

        # Start combat
        self.playerchoice()

    # Some classes for Player side
    def playerchoice(self):
        # Prompt the player what they would like to do...
        # Player will always attack first

        print "\nIt's your turn!\n"
        print "\nWhat would you like to do?"
        print " 1. Attack"
        print " 2. Defend"
        print " 3. Run\n"

        self.runsuccess = False

        while (globalvalues.p1.checkalive() and globalvalues.ai.checkalive()
                and not self.runsuccess):
            # Initialize self.playerdefend. Also serves as a reset after a turn
            # of combat
            self.playerdefend = False
            self.runfail = False

            choice = raw_input("> ")

            if '1' in choice:
                self.combat()
            elif '2' in choice:
                self.playerdefend = True
                self.combat()
            elif '3' in choice:
                self.playerrun()
            elif '!status' in choice:
                print globalvalues.p1.getstatus()
                print globalvalues.ai.getstatusf()
            elif '!option' in choice:
                print "\n1 - Attack the enemy\n2 - Defend against enemy attack"
                print "3 - Attempt to run away\n"

        # Runs only when one of the hp's hit 0
        if not globalvalues.p1.checkalive():
            # checking player's health comes first
            # because dead = dead, even if you defeat the enemy
            self.playerdefeated()

        # Same deal here
        elif not globalvalues.ai.checkalive():
            self.enemydefeated()

        # Run is successful
        else:
            None

        # Combat ends....
        raw_input(globalvalues.cont_mssg)
        globalvalues.clearscreen()

    def playerrawdmg(self):
        """
        Figures out what to do when the player attacks
        Passes values to dmgcalc then passes it to enemy's health
        """
        playerstr = globalvalues.p1.getstrength()
        # see combatvaluetable.xlsx to see some possible values of
        # playerrawdamage. Base formula is below:
        #
        rawdmg = int((playerstr - 4) * 102 * 0.32)

        # Things that will deviate the amount of damage done.
        level = globalvalues.p1.getlevel() - globalvalues.ai.getstatus()[0]
        modvalue = float(1 + level * 0.05)
        rngfactor = float(1 + float(random.randint(85, 105)) / 100)

        return int(rawdmg * modvalue * rngfactor)

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
        maxrange = runcount_math + int(level_diff * 0.3 * runcount_math)
        runmap = range(0, maxrange)

        # Use runmap to figure out if running away was successful
        if level_diff < 0:
            # You over power the opponent, automatically run away
            globalvalues.runcounter += 1
            print breakline
            print '\nYou have successfully run away!\n'
            self.runsuccess = True
        elif 0 == random.choice(runmap):
            globalvalues.runcounter += 1
            print '\nYou have successfully run away!\n'
            self.runsuccess = True
        else:
            globalvalues.runcounter = 0
            print '\nYou have failed to run away!\n'
            self.runfail = True
            self.combat()

    def playerdefeated(self):
        """
        Figures out what to do when the player is defeated
        """
        globalvalues.gameover_combat()

    # Some classes for enemyside
    def enemychoice(self):
        """RNGs the enemychoice and corresponding actions"""
        choice = random.randint(0, 10)
        # when choice is 0 to 3, the enemy will attack
        # when choice is 4 to 7, the enemy will defend
        # when choice is 8, the enemy will do nothing
        # when choice is 9, the enemy will do a super move

        #Create the Booleans first, they will also automatically 'reset' them
        self.enemyattack = False
        self.enemydefend = False
        self.enemysuper = False

        if choice == 1 or choice == 2 or choice == 3:
            self.enemyattack = True
        elif choice == 4 or choice == 5 or choice == 6:
            self.enemydefend = True
        elif choice == 7 or choice == 8:
            None
        else:
            self.enemysuper = True

    def enemyrawdmg(self):
        """Calculates the enemy damage"""

        enemystr = globalvalues.ai.getstatus()[3]
        # rngfactor will ensure that regular mobs won't absolutely crush you
        rngfactor = float(float(random.randint(45, 65)) / 100)
        level = (
                globalvalues.p1.getlevel()
                - globalvalues.ai.getstatus()[0]
                )
        lvlfactor = float(1 - level * 0.05)

        return int((enemystr) * 102 * 0.12 * rngfactor * lvlfactor)

    def combat(self):
        breakline = "-" * 86
        # Figure out what the enemy choice is
        self.enemychoice()

        # Set variables to be able to used locally without changing values
        enemyrawdmg = self.enemyrawdmg()
        playerrawdmg = self.playerrawdmg()

        if self.enemyattack:
            #Need another if statement to see if the player defended
            if self.playerdefend:
                #Calculate how much damage is done if player defends
                deffactor = float(float(random.randint(35, 55)) / 100)
                enemydmg = int(enemyrawdmg * deffactor)

                globalvalues.p1.gethp(enemydmg)
                print "\nYou have defended against the enemy attack!"
                print "You have taken %d damage. You would have taken %d." % (
                                                            enemydmg,
                                                            enemyrawdmg
                                                            )
            elif self.runfail:
                print "You will get twice for failing to run.\n"
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)

            else:
                # Calculate damage normally
                # Player does damage first
                globalvalues.ai.gethp(playerrawdmg)
                print "\nYou have done %d damage." % (playerrawdmg)

                # Enemy does damage
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)
        # If the enemy defends...
        elif self.enemydefend:
            # Need another if statement to check if everyone defended
            if self.playerdefend:
                print "\nBoth sides defended!!!\n"
            elif self.runfail:
                print "Luckily, the enemy has defended nothing."
            else:
                print "\nThe enemy defended."
                # Calculate damage when the only enemy defends
                deffactor = float(float(random.randint(45, 75)) / 100)
                globalvalues.ai.gethp(playerrawdmg * deffactor)
                print "\nYou have done %d damage." % (playerrawdmg * deffactor)
                print "You could have done %d damage." % (playerrawdmg)
        # If you just got unlucky and the enemy feels like destroying you
        elif self.enemysuper:
            print "\nThe enemy's super move!\n"
            superfactor = float(float(random.randint(150, 250)) / 100)
            enemyrawdmg *= superfactor
            # Check if player is defending
            if self.playerdefend:
                deffactor = float(float(random.randint(35, 55)) / 100)
                enemydmg = int(enemyrawdmg * deffactor)
                # Taking damage from the enemy
                globalvalues.p1.gethp(enemydmg)
                print "You have defended against the enemy super attack!\n"
                print "You have taken %d damage. You would have taken %d." % (
                                                            enemydmg,
                                                            enemyrawdmg
                                                            )
            elif self.runfail:
                print "It takes two strong swipes at you.\n"
                # Gets attacked twice
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)
            else:
                # When the player does not defend...
                print "\nYou will take a lot of damage...\n"

                # Calculate damage normally
                # Player does damage first
                globalvalues.ai.gethp(playerrawdmg)
                print "You have done %d damage." % (playerrawdmg)

                # Enemy does damage
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)
        # Enemy does nothing...
        else:
            print "\nI guess the enemy is too lazy to attack us today!\n"
            if self.playerdefend:
                print "You defended against nothing!"
            elif self.runfail:
                print "Seeing you try to run, it has attacked you!\n"
                globalvalues.p1.gethp(enemyrawdmg)
                print "You have taken %d damage." % (enemyrawdmg)
            else:
                # Player attacks, no consequences
                globalvalues.ai.gethp(playerrawdmg)
                print "You have done %d damage." % (playerrawdmg)

        # After combat has finished print both hp and then add a breakline
        print breakline
        print breakline
        print "\n\tYour HP: %d/%d\n" % (
                                        globalvalues.p1.gethp(),
                                        globalvalues.p1.getmaxhp()
                                        )
        enemystatus = globalvalues.ai.getstatus()
        print "\n\tEnemy HP: %d/%d\n" % (
                                        enemystatus[1],
                                        enemystatus[2]
                                        )
        print breakline
        print breakline

    def enemydefeated(self):
        """Gives player exp"""
        print "\nYou have defeated the enemy!\n"
        exp = globalvalues.ai.getstatus()[4]
        print "You got %d Experience!\n" % (exp)
        globalvalues.p1.addexp(exp)
