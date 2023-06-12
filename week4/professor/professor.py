import random


def main():
    level = get_level()
    problems = generate_problems(level)
    score = 0
    for problem in problems:
        if ask_problem(*problem):
            score += 1
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) in [1, 2, 3]:
            return int(level)
        print("Invalid input. Please enter a number from 1 to 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def generate_problems(level):
    return [(generate_integer(level), generate_integer(level)) for _ in range(10)]


def ask_problem(x, y):
    answer = input(f"{x} + {y} = ")
    for _ in range(2):
        if answer.isdigit() and int(answer) == x + y:
            print("Correct!")
            return True
        print("EEE")
        answer = input("Try again: ")
    print(f"The correct answer is {x + y}.")
    return False


if __name__ == "__main__":
    main()
