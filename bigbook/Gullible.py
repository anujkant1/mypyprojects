"""Gullible
How to keep a gullible person busy for hours. (This is a joke program.)"""

print('Gullible')

while True:  # Main program loop.
    print('Do you want to know how to keep a gullible person busy for hours Y/N')
    response = input('> ')
    if response.lower().startswith('n'):
        break  # If "no", break out of this loop.
    if response.lower().startswith('y'):
        continue  # If "yes", continue to the start of this loop.
    print(f'{response} is not a valid yes/no response.')

print('Thank you. Have a nice day!')
