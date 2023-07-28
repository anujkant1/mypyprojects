"""Soraban Japanese Abacus,
A simulation of a Japanese abacus calculator tool.
More info at: https://en.wikipedia.org/wiki/Soroban"""

import sys

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban - The Japanese Abacus')
    print()

    abacusNumber = 0  # This is the number represented on the abacus.

    add_dict = {
        'q': 1000000000, 'w': 100000000, 'e': 10000000, 'r': 1000000,
        't': 100000, 'y': 10000, 'u': 1000, 'i': 100, 'o': 10, 'p': 1
    }

    subtract_dict = {
        'a': 1000000000, 's': 100000000, 'd': 10000000, 'f': 1000000,
        'g': 100000, 'h': 10000, 'j': 1000, 'k': 100, 'l': 10, ';': 1
    }

    while True:  # Main program loop.
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            # Quit the program:
            sys.exit()
        elif commands.isdecimal():
            # Set the abacus number:
            abacusNumber = int(commands)
        else:
            # Handle increment/decrement commands:
            for letter in commands:
                if letter in add_dict:
                    abacusNumber += add_dict[letter]
                elif letter in subtract_dict:
                    abacusNumber -= subtract_dict[letter]

        # The abacus can't show negative numbers:
        if abacusNumber < 0:
            abacusNumber = 0  # Change any negative numbers to 0.
        # The abacus can't show numbers larger than 9999999999:
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    hasBead = []  # Contains a True or False for each bead position.

    # Top heaven row has a bead for digits 0, 1, 2, 3, and 4.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01234')

    # Bottom heaven row has a bead for digits 5, 6, 7, 8, and 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '56789')

    # 1st (topmost) earth row has a bead for all digits except 0.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '123456789')

    # 2nd earth row has a bead for digits 2, 3, 4, 7, 8, and 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '234789')

    # 3rd earth row has a bead for digits 0, 3, 4, 5, 8, and 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '034589')

    # 4th earth row has a bead for digits 0, 1, 4, 5, 6, and 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '014569')

    # 5th earth row has a bead for digits 0, 1, 2, 5, 6, and 7.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '012567')

    # 6th earth row has a bead for digits 0, 1, 2, 3, 5, 6, 7, and 8.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01235678')

    # Convert these True or False values into O or | characters.
    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    # Draw the abacus with the O/| characters.
    chars = abacusChar + numberList
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def displayControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == '__main__':
    main()
