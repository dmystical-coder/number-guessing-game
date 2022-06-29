# This module generates random
import random
# Include an ascii art as logo
from art import logo

print(logo)
# display an introductory msg to the user
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# prompt user to choose difficulty level
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
# prepare the number the user will guess and store in a variable
computer_guess = random.randint(1, 100)
# dependent on the difficulty level chosen, display the number of gusses available to the user
if (difficulty == 'easy'):
    print("You have 10 attempts to guess the number")
    # track the number of attempts remaining
    counter = 10

elif (difficulty == 'hard'):
    print("You have 5 attempts remaining to guess the number")
    # track the number of attempts remaining
    counter = 5

else:
    print("Wrong Input!")

while counter > 0:
    # prompt user to guess a number
    guess = int(input("Guess a number: "))
    counter -= 1
    # return correct if the user guess equals computer guess
    if (guess == computer_guess):
        print(
            f"You got it right! The number I was thinking of is {computer_guess}. \nThe End. ")
        break
    # display too high! if the user guess is higher than the computer guess
    elif (guess > computer_guess):
        print("Too high!")
    # display too low if the user guess is lower than the computer guess
    elif (guess < computer_guess):
        print("Too low!")
    else:
        print("Wrong input")
    # give feedback to the user
    if (counter != 0):
        print(f"Guess again, you have {counter} attempts remaining. ")
    else:
        print("You have exhausted your attempts and you Lose!\nThe End. ")