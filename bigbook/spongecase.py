"""sPoNgEcAsE
Translates English messages into sPOnGEtExT."""

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    """Run the Spongetext program."""
    print('''sPoNgEcAsE

eNtEr YoUr MeSsAgE:''')
    spongetext = englishToSpongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOPiEd SpOnGeTeXT tO cLiPbOaRd.)')
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def englishToSpongecase(message):
    """Return the spongetext form of the given string."""
    spongeText = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongeText += character
            continue

        if useUpper:
            spongeText += character.upper()
        else:
            spongeText += character.lower()

        # Flip the case, 90% of the time.
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Flip the case.
    return spongeText


# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
