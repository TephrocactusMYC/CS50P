import random

while True:
    level = input("Level: ")
    if level.isdigit() and int(level) > 0:
        level = int(level)
        break
    else:
        print("Invalid level. Please enter a positive integer.")

random_num = random.randint(1, level)

while True:
    guess = input("Guess: ")
    if guess.isdigit() and int(guess) > 0:
        guess = int(guess)
        if guess < random_num:
            print("Too small!")
        elif guess > random_num:
            print("Too large!")
        else:
            print("Just right!")
            break
    else:
        print("Invalid guess. Please enter a positive integer.")
