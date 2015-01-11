import sys

while True:
    try:
        keypress = raw_input()
    except (KeyboardInterrupt, EOFError):
        print "ayy lmao"

    if keypress == 'ayy lmao':
        sys.exit()
