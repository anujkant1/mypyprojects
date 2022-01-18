"""Deep Cave
An animation of a deep cave that goes forever into the earth."""


import random
import sys
import time

# Set up the constants:
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10


while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + ('.' * gapWidth) + ('#' * rightWidth))

    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, exit the program.

    # Adjust the left side width:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1  # Decrease the left side width.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth += 1  # Increase the left side width.
    else:
        pass  # Do nothing; no change in left side width.

    # Adjust the gapWidth:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth -= 1  # Decrease the gap width.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth += 1  # Increase the gap width.
    else:
        pass  # Do nothing; no change in gap width
