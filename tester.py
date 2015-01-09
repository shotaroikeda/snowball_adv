import syschar

print "Please input a character name"

playername = raw_input("> ")
print "You have created ", playername


p1 = syschar.PlayerCharacter(playername)

print p1.getstatus()

print "You gained 10 exp!"
p1.addexp(10)

print p1.getstatus()

while p1.checkalive():
    try:
        dmg = int(raw_input("How much damage will you to yourself? "))
        p1.gethp(dmg)
        exp = int(raw_input("How much exp will you get? "))
        p1.addexp(exp)
    except ValueError:
        print "Please try again."
        continue
        
