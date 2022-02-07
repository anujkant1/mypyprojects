"""Fibonacci Sequence
Calculates numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13..."""

import sys

print('''Fibonacci Sequence

The Fibonacci Sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

while True:  # Main program loop.
    while True:  # Keep asking until the user enters valid input.
        print('Enter the Nth Fibonacci number you wist to')
        print('calculate (such as 5, 50, 1000, 9999) or QUIT:')
        response = input('> ')

        if response.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # Exit the loop when we have a valid number.

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # Handle the special cases if the user entered '1' or '2':
    if nth == 1:
        print('0')
        print()
        print('THe #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2')

    # Display warning if the user entered a large number:
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done. Press Ctrl-C.')
        print('Press Enter to begin...')

    # Calculate the Nth Fibonacci series:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # Display the first two Fibonacci numbers.

    # Display all the later numbers of the Fibonacci sequence:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # Display the next number in the sequence:
        print(nextNumber, end='')

        # Check if we've found the Nth number the user wants:
        if fibNumbersCalculated == nth:
            print()
            print()
            print(
                f'The #{fibNumbersCalculated} Fibonacci number is {nextNumber}', sep='')
            break

        # Print a comma in between the sequence numbers:
        print(', ', end='')

        # Shift the last two numbers:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
