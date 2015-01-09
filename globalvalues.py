import syschar

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
