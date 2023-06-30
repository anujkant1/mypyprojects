"""Rainbow,
Shows a simple rainbow animation. Press Ctrl-C to stop."""

import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

print('Rainbow')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.

try:
    while True:  # Main program loop.
        print(' ' * indent, end='')
        bext.fg('purple')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('red')
        print('##')

        if indentIncreasing:
            # Increase the number of spaces:
            indent += 1
            if indent == 60:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True

        time.sleep(0.02)  # Add a slight pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
