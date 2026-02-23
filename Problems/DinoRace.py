"""
Given two datasets:
1. Containing the dinosaur names, their leg lengths and their dietary needs
2. Containing the dinosaur names, their stride length and their postures

Provide a formula for calculating the speed of the dinosaurs.
Print them in the order of fastest to slowest.

Formula:
g = 9.8
speed_of_dino = ((stride_length / leg_length) - 1) * sqrt(leg_length) * g
"""

import csv
from math import sqrt


dino_dict = {}

with open('Problems/data/dataset1.csv', 'r') as dataset1:
    csv_data1 = csv.DictReader(dataset1)
    for row in csv_data1:
        dino_dict[row['NAME']] = {
            'LEG_LENGTH': float(row['LEG_LENGTH'])
        }
    
with open('Problems/data/dataset2.csv', 'r') as dataset2:
    csv_data2 = csv.DictReader(dataset2)
    for row in csv_data2:
        if row['NAME'] in dino_dict:
            dino_dict[row['NAME']].update({
                'STRIDE_LENGTH': float(row['STRIDE_LENGTH']),
                'STANCE': row['STANCE']
            })
# speed_of_dino = ((stride_length / leg_length) - 1) * sqrt(leg_length) * g
bipedal_dinos = []
g = 9.8
for key, value in dino_dict.items():
    STRIDE_LENGTH = value.get('STRIDE_LENGTH')
    LEG_LENGTH = value.get('LEG_LENGTH')
    if value.get('STANCE') == 'bipedal':
        speed = (((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH) * g)
        bipedal_dinos.append((key, speed))

fastest_dinos = sorted(bipedal_dinos, key=lambda x: x[1], reverse=True)
for dino in fastest_dinos:
    print(dino[0])