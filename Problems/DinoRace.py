import csv
import math

dino_dict = {}

with open('Problems/dataset1.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dino_dict[row['NAME']] = {
            'LEG_LENGTH': float(row['LEG_LENGTH']),
            'DIET': row['DIET']
        }

with open('Problems/dataset2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['NAME'] in dino_dict:
            dino_dict[row['NAME']].update({
                'STRIDE_LENGTH': float(row['STRIDE_LENGTH']),
                'STANCE': row['STANCE']
            })

bipedal_dinos = []
g = 9.8
for name, data in dino_dict.items():
    if data.get('STANCE') == 'bipedal':
        speed = ((data['STRIDE_LENGTH'] / data['LEG_LENGTH']) - 1) * math.sqrt(data['LEG_LENGTH'] * g)
        bipedal_dinos.append((name, speed))

# Define a function to extract the speed for sorting
def get_speed(dino):
    return dino[1]

# Sort the bipedal dinosaurs by speed in descending order
bipedal_dinos.sort(key=get_speed, reverse=True)

# Print the names of the bipedal dinosaurs from fastest to slowest
for dinosaur in bipedal_dinos:
    print(dinosaur[0])