import random

computer_choice = random.randint(1,100)

while True:
    guess = int(input("Guess the number between 1 to 100: "))

    if guess == computer_choice:
        print("Congo!, You've guessed it right!")
        break
    elif guess < computer_choice:
        print("Too low, try again.")
    else:
        print("Too High, try again.")