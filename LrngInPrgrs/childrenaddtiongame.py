"""
Children's Addition Game
This game will ask children to add two numbers and then check if the answer is correct.
The twist is that it will ask if they are serious or want a funny answer."""

import random
import sys

def get_random_numbers():
    return random.randint(1, 9), random.randint(1, 9)

def get_child_response(num1, num2):
    print(f"What is {num1} + {num2}?")
    return input(">  ")

def get_response_type():
    print("Have you provided the actual answer or THE FUNNY answer?")
    print("Serious(s) of Funny(f)")
    return input("> ")

def check_serious_answer(num1, num2, child_response):
    if num1 + num2 == int(child_response):
        return "Your answer is actually correct!"
    else:
        return f"Sorry, the actually answer is {num1 + num2} and not {child_response}."
    
def check_funny_answer(num1, num2, child_response):
    if str(num1) + str(num2) == child_response:
        return "Your FUNNY answer is correct!"
    else:
        return f"Sorry, funny answer I was expecting was {num1}{num2}, so your funny answer {child_response} is not correct!"

def main():
    while True:
        try:
            num1, num2 = get_random_numbers()
            child_response = get_child_response(num1, num2)
            response = get_response_type()
            while True:  # Keep asking until they enter a valid response.
                if response.lower() == "s":
                    print(check_serious_answer(num1, num2, child_response))
                    break
                elif response.lower() == "f":
                    print(check_funny_answer(num1, num2, child_response))
                    break
                else:
                    print("It's either 's' or 'f' buddy. Try again.")
                    response = get_response_type()
            play_again = input("Do you want to play again? (y/n) > ")
            if play_again.lower() != "y":
                sys.exit()
        except ValueError:
            print("You have not provided a valid number. Please provide a number between 1 and 9.")
            continue
        except KeyboardInterrupt:
            print("\nYou have pressed Ctrl+C. Exiting the game.")
            sys.exit()
            

if __name__ == '__main__':
    main()