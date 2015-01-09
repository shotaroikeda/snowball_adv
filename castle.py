import globalvalues

def main():
    globalvalues.clearup

    print '\n\n\nYou have found yourself in front of a castle.'
    print 'There is a forest to your left, a castle in the front, and a brick wall to the right'
    print globalvalues.p1.getstatus()

    while True:
        choice = raw_input("> ")

        if 'l' or 'L' in choice:
            pass        #go to forest
        elif 'f' or 'F' in choice:
            pass        # go into castle
        elif 'r' or 'R' in choice:
            pass        # go into
        elif '!option' in choice:
            print "left - go to forest\nfront - go to castle\nright - go to brick wall"
        elif '!status' in choice:
            print globalvalues.p1.getstatus()
    
