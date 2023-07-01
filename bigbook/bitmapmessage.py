"""Bitmap Message
Displays a text message according to the provided bitmap image.
"""

import sys
bitmap = """
....................................................................
___________¶¶¶¶¶¶
_________¶¶______¶
________¶¶_______¶¶
_______¶¶_________¶¶
_______¶¶_________¶¶
_______¶___________¶
_______¶¶_________¶¶
_______¶¶_________¶
_______¶¶________¶¶
________¶¶_____¶¶¶
_________¶¶___¶¶¶
__________¶__¶¶_________________¶¶¶¶¶¶
__________¶¶¶¶_________________¶¶___¶¶¶¶
__________¶¶_____________¶¶¶¶¶¶¶¶¶¶____¶¶
__________¶¶____________¶¶¶¶¶¶__¶¶¶¶____¶
__________¶¶____________¶_____¶___¶¶____¶¶
__________¶¶___________¶_¶_____¶___¶_____¶
_________¶¶¶__________¶¶___¶____¶__¶¶____¶¶
_________¶¶¶__________¶_________¶__¶¶____¶¶
________¶¶¶¶__________¶¶¶_______¶_¶¶¶____¶¶
_______¶¶¶¶¶¶_________¶________¶¶¶¶_¶_____¶
_______¶¶___¶¶_________¶_____¶¶¶¶___¶¶____¶¶
________¶¶__¶¶_________¶¶¶¶¶¶¶_______¶____¶¶
________¶¶¶_¶¶____¶¶___¶____¶________¶¶____¶
___________¶_¶¶_¶¶¶¶¶¶¶____¶¶¶¶¶______¶¶___¶
____________¶_¶¶¶___¶¶_____¶¶¶¶¶¶______¶¶__¶
____________¶__¶____¶______¶____¶_______¶__¶
_____________¶__¶¶¶_¶¶___¶¶¶___¶¶_______¶¶_¶
____________¶¶¶__¶¶__¶¶¶¶¶____¶¶_________¶¶
__________¶¶_¶¶__¶¶__¶¶¶¶____¶¶¶________¶¶
_________¶¶___¶¶__¶¶¶____¶¶¶¶_¶
_______¶¶___¶¶_¶¶____¶¶¶¶¶¶¶_¶¶
______¶¶__¶¶¶___¶¶¶¶¶¶¶_____¶¶
____¶¶___¶¶¶_____¶¶________¶¶
___¶¶__¶¶¶_______¶¶_______¶¶
__¶¶¶¶¶¶_________¶________¶¶¶
_¶¶_¶¶__________¶¶__________¶¶
¶¶__¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶__¶¶________¶¶¶_¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶
¶¶¶¶¶_______¶¶¶¶_¶_¶_¶¶_¶_¶¶__¶__¶¶¶
¶¶¶¶______¶¶¶___¶¶_¶_¶¶_¶¶_¶¶_____¶¶
__________¶¶____¶_¶¶_____¶______¶¶¶
____________¶¶¶______________¶¶¶¶
___________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__________¶_________¶¶¶¶¶¶¶
_________¶_______¶¶¶¶_____¶¶
________¶¶___¶¶¶¶¶¶¶¶_____¶¶
________¶____¶¶¶____¶¶_____¶¶
________¶¶____¶¶_____¶¶_____¶
_________¶_____¶¶_____¶¶____¶¶
_________¶¶_____¶______¶¶____¶¶
__________¶¶____¶¶______¶¶¶___¶¶¶
___________¶¶____¶________¶¶____¶¶
____________¶____¶¶________¶¶____¶¶
____________¶¶___¶¶_________¶¶____¶¶
_____________¶¶___¶__________¶¶____¶¶
______________¶___¶___________¶¶____¶
______________¶¶__¶¶___________¶¶___¶¶
_______________¶¶¶¶¶¶___________¶¶___¶¶
_______________¶____¶¶___________¶¶__¶¶¶
_______________¶____¶¶____________¶¶¶__¶¶
_______________¶¶¶¶¶¶¶¶___________¶¶___¶¶¶¶
_____________¶¶¶¶¶____¶¶___________¶¶_¶¶__¶¶
____________¶¶¶¶¶____¶¶¶____________¶¶____¶¶
____________¶¶¶¶__¶¶¶¶¶____________¶¶¶¶__¶¶
___________¶¶__¶¶¶¶¶_______________¶¶¶¶__¶¶
__________¶¶¶¶¶¶¶¶___________________¶¶_¶¶
__________¶¶¶¶_______________________¶¶_¶¶
_____________________________________¶¶¶¶
...................................................................."""

print('Bitmap Message')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmacp:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ' or bit == '_':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()