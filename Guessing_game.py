
# NUMBER GUESSING GAME

import random

rounds = 0
score = 0


def restart():      # Restarts the game after a game over or because of invalid input
    global rounds
    rounds = 0      # Clears the saved rounds
    global score
    score = 0       # Clears the saved score
    start()
    return


def guessing_game_very_easy():      # This is the very easy mode
    global rounds
    rounds = rounds + 1     # Counts the rounds in the game
    print("\nRound " + str(rounds) + ":")

    numbers = range(30)
    chosen_numbers = random.sample(numbers, 2)      # Chooses x amount of random numbers depending on the difficulty.
    print(chosen_numbers)
    secret_number = random.choice(chosen_numbers)
    guess = input("\nGuess the number:\n")
    if str(guess) == str(secret_number):        # Function for the correct guess
        print("Correct!")
        global score
        score = score + 1       # Counts the number of correct guesses from the user
        return guessing_game_very_easy()

    else:
        print("Wrong!")
        print("\nGame Over")        # Game over message
        print("You scored: " + str(score))
        if input("\nPlay again? (y)\n>>> ") == "y":     # Option to play again after game over
            restart()
        else:
            return


def guessing_game_easy():       # This is the easy mode
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
        if input("\nPlay again? (y)\n>>> ") == "y":     # Option to play again after game over
            restart()
        else:
            return



def guessing_game_medium():         # This is the medium difficulty
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
        if input("\nPlay again? (y)\n>>> ") == "y":  # Option to play again after game over
            restart()
        else:
            return


def guessing_game_hard():           # This is the hard difficulty
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
        if input("\nPlay again? (y)\n>>> ") == "y":  # Option to play again after game over
            restart()
        else:
            return


# Selects the difficulty of the game
def start():
    print("Welcome to the number guessing game")
    difficulty = input("Select difficulty: Very easy (v), Easy (e), Medium (m), Hard (h)\n>>> ")

    if difficulty.lower() == "v":
        guessing_game_very_easy()

    elif difficulty.lower() == "e":
        guessing_game_easy()

    elif difficulty.lower() == "m":
        guessing_game_medium()

    elif difficulty.lower() == "h":
        guessing_game_hard()

        # Prints error in case of wrong input and asks for input again
    else:
        print("\nPlease enter a valid answer\n")
        restart()
        return


start()
