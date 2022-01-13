"""Clickbait Headlins Generator
A clickbait headlines generator for your soulless content farm website."""

from math import e
import random

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'Him', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania'
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Bos', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():
    print('Clickbait Headlines Generator')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break  # Exit the loop once a valid number is entered.

    print('\nHere are the headlines: \n')
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadLine()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadLine()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadLine()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadLine()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadLine()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadLine()
        elif clickbaitType == 7:
            headline = generateReasonWhyHeadLine()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadLine()

        print(f'\t{headline}')
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Goggle',
                             'Facesbook', 'Tweeter', 'Inshtagram'])
    when = random.choice(WHEN).lower()
    print(f'Post these to your {website} {when} or you\'re fired!')


# Each of these functions returns a different type of headline:
def generateAreMillennialsKillingHeadLine():
    noun = random.choice(NOUNS)
    return f'Are Millennials Killing the {noun} Industry?'


def generateWhatYouDontKnowHeadLine():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {pluralNoun} Could Kill You {when}'


def generateBigCompaniesHateHerHeadLine():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def generateYouWontBelieveHeadLine():
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    place = random.choice(PLACES)
    return f'You Won\'t Believe What This {state} {noun} Found in {pronoun} {place}'


def generateDontWantYouToKnowHeadLine():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return f'What {pluralNoun1} Don\'t Want You To Know About {pluralNoun2}'


def generateGiftIdeaHeadLine():
    number = random.randint(7, 15)
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    return f'{number} Gift Ideas to Give Your {noun} From {state}'


def generateReasonWhyHeadLine():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # Number2 should be no larger than number1
    number2 = random.randint(1, number1)

    return f'{number1} Reasons Why {pluralNoun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)'


def generateJobAutomatedHeadLine():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = POSSESSIVE_PRONOUNS[i]
    if pronoun1 == 'Their':
        return (f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong.')
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong.'


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
