"""Guess the Number
Try to guess the secret number based on hints."""

import random


def askForGuess():
    while True:
        guess = input('> ')  # Enter the guess

        if guess.isdecimal():
            return int(guess)  # Convert string guess to an integer
        print('Please enter a number between 1 and 100.')


print('Guess the Number\n')
secretNumber = random.randint(1, 100)  # Select a randome number.
print('I am thinking of a number between 1 and 100.')

for i in range(10):  # Give the player 10 guesses.
    print(f'You have {10 - i} guesses left. Take a guess.')

    guess = askForGuess()
    if guess == secretNumber:
        break  # Break out of the for loop if the guess is correct.

    # Offer a hint:
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# Reveal the results:
if guess == secretNumber:
    print('Yay! You guessed my number!')
else:
    print(f'Game over. The number I was thinking of was {secretNumber}')