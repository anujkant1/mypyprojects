"""Sound Mimic,
A pattern-matching game with sounds. Try to memorize an increasingly
longer and longer pattern of letters. Inpired by the electronic game
Simon."""

import random
import sys
import time


try:
    import playsound
except ImportError:
    print('''
The playsound module needs to be installed to run this
program. On Windows, open a Command Prompt and run:
pip install playsound
On macOS and Linux, open a Terminal and run
pip3 install playsound''')
    sys.exit()

print('''Sound Mimic,
Try to memorize a pattern of A S D F letters (each with it's own sound)
as it gets longer and longer.''')

input('Press Enter to begin...')

pattern = ''
sound_path = sys.path[0] + '/addons/'
while True:
    print('\n' * 60)  # Clear the screen by printing several newlines.

    # Add a random letter to the pattern:
    pattern += random.choice('ASDF')

    # Display the pattern (and play their sounds):
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound(sound_path + 'sound' + letter + '.wav')

    time.sleep(1)  # Add a slight pause at the end.
    print('\n' * 60)  # Clear the screen by printing several newlines.

    # Let the player enter the pattern:
    print('Enter the pattern:')
    response = input('> ').upper()

    if response != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        playsound.playsound(sound_path + 'sound' + letter + '.wav')

    if response != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)
