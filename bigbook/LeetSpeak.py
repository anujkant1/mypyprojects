"""Leetspeak
Translates English messages into l33t5p34]<."""

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    print('''L3375P34]< (leetspeek)

Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetSpeak(english)
    pass


def englishToLeetSpeak(message):
    """Convert the English string in message and return leetspeak."""
    # Make sure all the keys in 'charMapping' are lowercase.
    charMapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']}
    leetspeak = ''
    for char in message:  # Check each character:
        # There is a 70& chance we change the character to leetspeak.
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # Don't translate this character:
            leetspeak = leetspeak + char
    return leetspeak


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
