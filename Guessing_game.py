
# NUMBER GUESSING GAME

import random

print("Welcome to the number guessing game")
difficulty = input("Select difficulty: Very easy (v), Easy (e), Medium (m), Hard (h)\n")
rounds = 0
score = 0


def guessing_game_very_easy():
    global rounds
    rounds = rounds + 1
    print("\nRound " + str(rounds) + ":")
    numbers = range(30)
    chosen_numbers = random.sample(numbers, 2)
    print(chosen_numbers)
    secret_number = random.choice(chosen_numbers)
    guess = input("\nGuess the number:\n")
    if str(guess) == str(secret_number):
        print("Correct!")
        global score
        score = score + 1
        return guessing_game_very_easy()

    else:
        print("Wrong!")
        print("\n\nGame Over")
        print("You scored: " + str(score))
        input("")


def guessing_game_easy():
    global rounds
    rounds = rounds + 1
    print("\nRound " + str(rounds) + ":")
    numbers = range(30)
    chosen_numbers = random.sample(numbers, 3)
    print(chosen_numbers)
    secret_number = random.choice(chosen_numbers)
    guess = input("\nGuess the number:\n")
    if str(guess) == str(secret_number):
        print("Correct!")
        global score
        score = score + 1
        return guessing_game_easy()

    else:
        print("Wrong!")
        print("\n\nGame Over")
        print("You scored: " + str(score))
        input("")


def guessing_game_medium():
    global rounds
    rounds = rounds + 1
    print("\nRound " + str(rounds) + ":")
    numbers = range(30)
    chosen_numbers = random.sample(numbers, 6)
    print(chosen_numbers)
    secret_number = random.choice(chosen_numbers)
    guess = input("\nGuess the number:\n")
    if str(guess) == str(secret_number):
        print("Correct!")
        global score
        score = score + 1
        return guessing_game_medium()

    else:
        print("Wrong!")
        print("\n\nGame Over")
        print("You scored: " + str(score))
        input("")


def guessing_game_hard():
    global rounds
    rounds = rounds + 1
    print("\nRound " + str(rounds) + ":")
    numbers = range(30)
    chosen_numbers = random.sample(numbers, 10)
    print(chosen_numbers)
    secret_number = random.choice(chosen_numbers)
    guess = input("\nGuess the number:\n")
    if str(guess) == str(secret_number):
        print("Correct!")
        global score
        score = score + 1
        return guessing_game_hard()

    else:
        print("Wrong!")
        print("\n\nGame Over")
        print("You scored: " + str(score))
        input("")


if difficulty.lower() == "v":
    guessing_game_very_easy()

elif difficulty.lower() == "e":
    guessing_game_easy()

elif difficulty.lower() == "m":
    guessing_game_medium()

elif difficulty.lower() == "h":
    guessing_game_hard()

else:
    print("Wrong letter")
