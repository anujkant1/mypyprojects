"""Trick Questions,
A quiz of several trick questions."""

import json
import random
import sys

# QUESTIONS is a list of dictionaries, each dictionary represents a
# trick question and its answer. The dictionary has the keys 'question'
# (which holds the text of the question), 'answer' (which holds the text
# of the answer), and 'accept' (which holds a list of strings that, if
# the player's answer contains any of, they've answered correctly).

with open('bigbook/addons/questions.json') as questions:
    data = questions.read()
QUESTIONS = json.loads(data)['QUESTIONS']

CORRECT_TEXT = ['Correct!', 'That is right.', "You're right.",
                'You got it.', 'Righto!']
INCORRECT_TEXT = ['Incorrect!', "Nope, that isn't it!", 'Nope.',
                  'Not quite', 'You missed it.']

print('''Trick Questions,

Can you figure out the answers to these trick questions?
(Enter QUIT to quit at any time.)
''')

input('Press Enter to begin...')
random.shuffle(QUESTIONS)
score = 0

for questionNumber, qa in enumerate(QUESTIONS):  # Main program loop.
    print('\n' * 60)  # "CLear" the screen.
    print('Question:', questionNumber + 1)
    print('Score:', score, '/', len(QUESTIONS))
    print('QUESTION:', qa['question'])
    response = input('   ANSWER:   ').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

    correct = False
    for acceptanceWord in qa['accept']:
        if acceptanceWord in response:
            correct = True

    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text, qa['answer'])
        score += 1
    else:
        text = random.choice(INCORRECT_TEXT)
        print(text, 'The answer is:', qa['answer'])
    response = input('Press Enter for the next question...').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

print("That's all the questions. Thanks for playing!")
