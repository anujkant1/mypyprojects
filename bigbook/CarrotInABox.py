"""Carrot in a Box
A silly bluffing game between two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it."""

import random

print('''Carrot in a Box

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The fist player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')

input('Please Enter to begin...')

p1Name = input('Player 1, please enter your name: ').capitalize()
p2Name = input('Player 2, please enter your name: ').capitalize()
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |  GOLDEN | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLDEN box in front of you')
print()
print(p1Name + ', you will get to look into your box.', end=' ')
print(p2Name.upper() + ', close your eyes and don\'t look!!!!')
print()
input('When ' + p2Name + ' has closed their eyes, press Enter... ')
print()

print(p1Name + ' here is the inside of your box:')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |  GOLDEN | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (carrot!)''')
    print(playerNames)

else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |  GOLDEN | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(no carrot!)''')
    print(playerNames)

input('Press Enter to continue...')

print('\n' * 100)  # Clear the screen by printing several newlines.
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press enter to continue...')

print()
print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
print('1. There is a carrot in my box.')
print('2. There is not a carrot in my box.')
print()
input('Then press Enter to continue...')

print()
print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or (response.startswith('N'))):
        print(p2Name + ', please enter "YES" or "NO".')
    else:
        break

firstBox = '  RED '  # Note the spaces for aligning text in the box.
secondBox = 'GOLDEN'

if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print(''' HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
| {}  | |  | {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Press Enter to reveal the winner...')
print()

if carrotInFirstBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
| {}  | |  | {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
| {}  | |  | {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)

# This modification made possible through the 'carrotInFirstBox' variable
if carrotInFirstBox:
    print(p1Name + ' is the winner!')
else:
    print(p2Name + ' is the winner!')

print('Thanks for playing!')
