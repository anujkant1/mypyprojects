"""Dice Math
A flashcard addition game where you sum the total on random dice rolls."""

import random
import time

# Ser up the constants:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom

# The duration is in seconds:
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 1


# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)
D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)
D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)
D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)
D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)
D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)
D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)
D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)
D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)


ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print(f'''Dice Math

Add up the sides of all the dice displayed on the screen.
You have {QUIZ_DURATION} seconds to answer as many as possible. You get {REWARD}
points for each correct answer and lose {PENALTY} point for each
incorrect one.''')
input('Press Enter to begin... ')

# Keep track of how many answers were correct and incorrect:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:  # Main game loop.
    # Come up with the dice to display:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        dice = random.choice(ALL_DICE)
        # dice[0] contains the list of strings of the dice face:
        diceFaces.append(dice[0])
        # dice[1] contains the integer number of the pips on the face:
        sumAnswer += dice[1]

    # Contains (x, y) tuples of the top-left corner of each dice.
    topLeftDiceCorners = []

    # Figure out where dice should go:
    for i in range(len(diceFaces)):
        while True:
            # Find a random place on the canvas to put the dice:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Get the x, y coordinates for all four corners:
            #      left
            #      v
            # top > +-------+ ^
            #      | O     | |
            #      |   O   | DICE_HEIGHT (5)
            #      |     O | |
            #      +-------+ v
            #      <------->
            #      DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # Check if the dice overlaps with previous dice.
            overlaps = False
            for prevDiceLeft, prevDiceTop in topLeftDiceCorners:
                prevDiceRight = prevDiceLeft + DICE_WIDTH
                prevDiceBottom = prevDiceTop + DICE_HEIGHT
                # Check each corner of this dice to see if it is inside
                # of the are of the previous dice:
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDiceLeft <= cornerX < prevDiceRight
                            and prevDiceTop <= cornerY < prevDiceBottom):
                        overlaps = True
            if not overlaps:
                # It doesn't overlap, so we can put it here:
                topLeftDiceCorners.append((left, top))
                break

    # Draw the dice on the canvas:

    # Keys are (x, y) tuples of ints, values the character at that
    # position on the canvas:
    canvas = {}
    # Loop over each dice:
    for i, (diceLeft, diceTop) in enumerate(topLeftDiceCorners):
        # Loop over each character in the dice's face:
        diceFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # Copy this character to the correct place on the canvas:
                canvasX = diceLeft + dx
                canvasY = diceTop + dy
                # Note that in diceFace, a list of strings, the x and y
                # are swapped:
                canvas[(canvasX, canvasY)] = diceFace[dy][dx]

    # Display the canvas on the screen:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # Print a newline.

    # Let the player enter their answer:
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print(f'Incorrect, the answer is {sumAnswer}')
        time.sleep(2)
        incorrectAnswers += 1

# Display the final score:
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print(f'Correct:   {correctAnswers}')
print(f'Incorrect: {incorrectAnswers}')
print(f'Score:     {score}')
