

import random

print("Number guessing game")

number = random.randint(1, 9)

# number of chances to be given to the user to guess the number
# or it is the inputs given by user into input box here number of chances are 5
chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:

    guess = int(input("Your guess (between 1 and 9): "))

    if guess == number:
        print("Congratulation! You won the game!")
        break

    # Check if the user entered number is smaller than the generated number
    elif guess < number:
        print("Your guess was too low. Guess a number higher than ", guess)

    # The user entered number is greater than the generated number
    else:
        print("Your guess was too high: Guess a number lower than ", guess)

    chances += 1


if not chances < 5:
    print("You lose :( The number was ", number)
