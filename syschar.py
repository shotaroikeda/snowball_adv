# syschar.py
#
#
# syschar.py essentially calculates levels and stats based off of exp

import random
# random is used later to generate enemy values

maxlevel = 20

class PlayerCharacter(object):
    #PlayerCharacter creates a character for you. Creation of explicit
    #characters is possible
    def __init__(self, name='Player1', hp=100, exp=0, strength=5):
        """
        Initializes the class. Takes in (name, hp, exp).
        Defaults are name = 'Player1', hp = 100, exp = 0

        WARNING: hp is assigned to the current hp the player has, which means
        that it can potentially generate a character will less health or more
        health than maximum.
        """
        self.exp = exp
        self.charname = name
        self.currenthp = hp
        self.maxhp = hp
        self.playerstr = strength

    def getname(self):
        """
        Returns the character name. Set when initializing, cannot change
        without creating a new character.
        """
        return str(self.charname)

    def getexp(self, exp=0):
        """
        Returns what the current exp is. Optionally takes in (exp) which by
        default is 0.
        You can use this to add exp to the character. Will add 0 by default,
        which in turn will return the amount of exp the player currently has.
        Ex. PlayerCharacter.getexp(50) will add 50 exp to the character.

        addexp() also does the same thing but with more feedback.
        addexp() is much more preferred to this method.
        """
        self.addexp(exp)
        return int(self.exp)

    def getlevel(self):
         """getlevel will return a number which corresponds to the level"""
         level = int(self.exp / 100 + 1)

         #This part of the code will ensure that the maximum level will be
         #The maximum level, even if the exp goes above
         if level <= maxlevel:
             self.level = level
             return self.level

         else:
             self.level = maxlevel
             return self.level

    def getmaxhp(self, addhp=0):
        """
        gethp will return the number of maximum hp at the current level
        You can add more maxhp by adding a number as the argument.

        Ex. PlayerCharacter.getmaxhp(100) will add 100 to the maxhp
        WARNING: It will not heal the character. IF the player has 100/100 hp,
        adding 100 hp will make their health 100/200. Use gethp() to add health
        """

        # Calculates hp from what level they are to ensure accuracy

        self.maxhp += addhp
        return int(self.maxhp)

    def gethp(self, dmg=0):
        """
        gethp() will return the hp at the moment.
        Can be passed with an argument to make the player take damage.

        Ex. PlayerCharacter.gethp(50) would make the player lose 50 health.
        Ex. PlayerCharacter.gethp(-30) would make the player gain 30 health.
        """

        # Writes the currenthp to self.currenthp. Used later to determine
        # the current status
        self.currenthp -= dmg
        # Check to see if the hp now is greater than the maximum hp
        # Prevents hp from begin unreasonable like 500/300
        if self.currenthp > self.maxhp:
            self.currenthp = self.maxhp
        return int(self.currenthp)

    def getstrength(self, addstr=0):
        """
        getstrength() will return the current strength
        Passing an argument will make it add more strength.
        """
        self.playerstr += addstr
        return int(self.playerstr)

    def getstatus(self):
        """getstatus returns the current status of the character"""
        # This returns formatted text, instead of a list
        # This is to prevent reformatting over and over...
        return str(
            "\nCharacter Name: %s\n Level: %d\n HP: %d/%d\n Str: %d\n EXP: %d\n"
            % (self.getname(), self.getlevel(), self.gethp(),
            self.getmaxhp(), self.getstrength(), self.getexp()
                )
        )

    def checkalive(self):
        """checkalive returns True if the character is alive. Otherwise False"""

        if self.gethp() > 0:
            return True
        else:
            return False

    def addexp(self, num):
        """addexp allows adding exp to the character. If they level up they get
        a notification"""

        # Figure out if we leveled up or leveled down
        level_old = self.getlevel()
        self.exp += num
        level_new = self.getlevel()
        level_diff = level_new - level_old

        if level_diff > 0:
            print "\nYou have leveled up %d times!" % (level_diff)
            # Do this to add hp when leveling up, as opposed to subtracting
            self.gethp(level_diff * 100 * -1)
            self.getmaxhp(level_diff * 100)
            self.getstrength(level_diff)
            # Gain hp when leveling up
            print "\nNew Status: "
            print self.getstatus()
        elif level_diff < 0:
            print "\nYou have leveled down %d times..." % (level_diff)
            # You do not lose hp when you are leveling down...
            # except when your current hp > max hp
            # ie: 500/300
            self.getmaxhp(level_diff * 100)
            self.getstrength(level_diff)
            # just to check for correct hp value
            self.gethp()


class EnemyCharacter(object):
    # Might have been more efficient to have inherited the PlayerCharacter class
    def __init__(self, playerlevel):
        """creates a new instance of EnemyCharacter"""
        self.playerlevel = playerlevel
        self.generator()

    def generator(self):
        """returns a list containing information about the enemy character"""
        # This is returned as a list as opposed to PlayerCharacter.getstatus()
        return [
                self.levelgenerator(),
                self.hpgenerator(), self.strgenerator(),
                self.expgenerator()
                ]

    def levelgenerator(self):
        """returns an integer, representing the enemy level"""
        # Prevent negative levels from occuring!
        if self.playerlevel <= 1:
            self.enemylevel = int(random.randint(self.playerlevel + 1))

        elif self.playerlevel == maxlevel:
            self.enemylevel = int(random.randint(
                                            self.playerlevel - 2,
                                            self.playerlevel + 1
                                            ))
        else:
            self.enemylevel = int(random.randint(
                                            self.playerlevel - 2,
                                            self.playerlevel + 2
                                            ))
        return self.enemylevel

    def hpgenerator(self):
        """returns an integer, representing the enemy's max hp"""
        #Make sure we don't get a negative hp here.
        if self.playerlevel <= 2:
            maxhp_low = (self.playerlevel) * 50
        else:
            maxhp_low = (int(self.playerlevel) - 2) * 100
        maxhp_high = (int(self.playerlevel) + 2) * 100

        self.maxhp = int(random.randrange(maxhp_low, maxhp_high, 50))
        self.currenthp = self.maxhp
        return self.maxhp

    def strgenerator(self):
        """returns an integer, representing the enemy's strength"""
        #Limitations to how overpowered the enemy character can be...
        if self.maxhp >= self.playerlevel * 100:
            maxstr = int(self.playerlevel + 6)
            minstr = int(self.playerlevel + 1)
        elif self.maxhp < self.playerlevel * 100:
            maxstr = int(self.playerlevel + 10)
            minstr = int(self.playerlevel + 5)
        self.enemystr = int(random.randint(minstr, maxstr))
        return self.enemystr

    def gethp(self, dmg=0):
        """Same as the one in PlayerCharacter."""
        self.currenthp -= dmg
        return int(self.currenthp)

    def getdifficulty(self):
        """
        Returns how potentially difficult the enemy can be.
        Used to calculate exp returns
        """
        levelexp = self.enemylevel * 100
        hpexp = self.maxhp
        strexp = (self.enemystr - 4) * 100
        #Take the average of all of them...
        #hopefully returns a resonable amt of exp accurate to player
        return int(levelexp/3 + hpexp/3 + strexp/3)

    def expgenerator(self):
        """
        returns the amount of exp the player should get if they defeat
        the monster
        """
        # Banking on the fact that exp is an accurate way to determine the
        # "True Difficulty" of the enemies...
        playerexp = self.playerlevel * 100
        enemyexp = self.getdifficulty()

        if playerexp > enemyexp:
            #should get smaller amount of exp, fighting an easier monster
            #factor in how strong the enemy is in calcuations
            return int(enemyexp * 0.35 / self.enemylevel)

        elif playerexp <= enemyexp:
            #should get larger amount of exp, fighting stronger monster
            #factor in how strong the enemy is to the calculations
            returnedexp = (enemyexp * 0.8 - playerexp * 0.7) * 0.4
            return int(returnedexp)

    def getstatus(self):
        """
        returns the status of the monster in a list.
        [level of enemy, current hp, max hp, strength, how much exp]
        """
        return [
                int(self.enemylevel), self.gethp(),
                int(self.maxhp), int(self.enemystr),
                self.expgenerator()
                ]
                

    def checkalive(self):
        """
        Returns True if the monster is alive. Otherwise returns false
        """
        # Same as PlayerCharacter basically....
        if self.gethp() <= 0:
            return False
        else:
            return True

class BossCharacter(EnemyCharacter):
    # Inherits ALOT from EnemyCharacter.
    def __init__(self, level, hp, strength, exp):
        self.enemylevel = level
        self.maxhp = hp
        self.currenthp = hp
        self.enemystr = strength
        self.exp = exp

    def expgenerator(self):
        """
        Returns how much exp the player should receive upon defeating the boss.
        Look at the source code for more info.
        """
        # The amount of exp gained should be constant.
        # No need to return exp here
        return int(self.exp)
