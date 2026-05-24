import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

number = random.randint(1, 100)

while attempts > 0:

    print(f"You have {attempts} attempts remaining.")

    guess = int(input("Make a guess: "))

    if guess == number:
        print("You guessed the number!")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")

    attempts -= 1

    if attempts > 0:
        print("Guess again!")

if attempts == 0:
    print(f"You lost! The number was {number}")
