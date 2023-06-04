"""Ninety-Nine Bottles of Milk on the Wall
Print the full lyrics to one of the longest songs ever! Press
Ctrl-C to stop."""

import sys
import time

print('Ninety-Nine Bottles')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # This is the starting number of bottles.
PAUSE = 1

try:
    while bottles > 1:  # Keep looping and display the lyrics.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles -= 1  # Decrease the number of bottles by one.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()  # Print a newline.

    # Display the last stanza:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
