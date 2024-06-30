"""
Write a function to draw the pattern, where the value of ‘n’ will be taken from the user, for n=4, pattern will be 
1 
2 3 
4 5 6 
7 8 9 10
"""

current_number = 1

print("Enter a number between 1 and 10:")
n = int(input("> "))

for i in range(1, n+1):
    for j in range(i):
        print(current_number, end=" ")
        current_number += 1
    print()