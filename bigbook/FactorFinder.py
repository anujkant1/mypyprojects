"""Factor Finder
Finds all the factors of a number."""

import math
import sys

print('''Factor Finder

A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say 26 has four factors: 1, 2, 13, 26.

If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.

Can you discover some prime numbers?
''')

while True:  # Main program loop.
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of number:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # If there's no remainder, it's a factor.
            factors.append(i)
            print(factors)
            factors.append(number // i)
            print(factors)

    # Convert to a set to get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    # Display the results:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print('. '.join(factors))
