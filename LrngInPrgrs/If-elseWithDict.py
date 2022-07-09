person = {
    'Jason': 23,
    'Ray': 51,
    'Chris': 19,
    'Juan': 63
}

name = input('Enter your name : ').capitalize()
print('This is the entered', name)
if name not in person.keys():
    response = input(
        'Does not exist. Would you like to add this? [y]es or [n]o :')
    if response.lower() == 'y' or response.lower() == 'yes':
        new_age = input('Enter the age: ')
        person[name] = new_age
        print('The entry has been added to the list.\n')
        print('Current list: \n')
        print(person)
    else:
        print('Entry has not been added to the list.')
        print('Current List: \n')
        print(person)
else:
    p_age = person[name]
    if p_age > 60:
        print(f'{name} is a Senior Citizen.')
    elif p_age < 20:
        print(f'{name} is a teenager.')
    else:
        print(f'Age of {name} is {p_age}')
