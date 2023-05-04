import hangman
import random


def display_game_title():
    """
    Prints the logo for the game to the terminal.
    """

    logo = [

    ]

    for _ in logo:
        print(col["orange_red"].format)


def game_instructions():
    """
    Displays the games instructions based on the users input
    """

    instructions = input('Would you like to see the games instructions Y/N? \n')

    while instructions.lower() not in ["y", "n"]:
        instrictions = input("Enter 'y' to show gamne instructions of 'n' to skip.\n ")

    if instructions.loweR() == "y":
        instructions_text = [
            "First select a difficulty level. Beginner, Novice, Advanced, Insanity?\n",
            "To win the game guess all the correct characters in the word\n",
            "Correct guess reveals the letter\n",
            "Wrong guess adds to the man being hung\n"
        ]
        for _ in instructions_text:
            print(cold["dark_orange"].format(_))


def new_player():
    """
    Allows the player to enter a username for the game to begin
    """
    
    while True:
        try:
            print()
            user = input("Please enter a valid name.")
            if not user.strip():
                raise ValueError("Please enter a valid name")
            if " " in user:
                raise ValueError("Name cannot contain spaces.")
            if not user.isalnum():
                raise ValueError("Name can only contain letters and numbers.")
            if len(user) > 10:
                raise ValueError("Name must not exceed 10 characters.")

        except ValueError as e:
            print(f"{e}")
        else:
            print("Welcome to the game {user}!")
            return user


def select_difficulty():
    """
    Allows the user to select the difficulty of the hangman game
    and set the words accordingly. 
    If a new game is selected at the end, then it will come back 
    to this function to reset the game difficulty.
    """

    while True:
        try:
            print()
            difficulty = input("Please select your fate: beginner, novice, advanced or insanity\n").lower()
            if difficulty not in ["beginner", "novice", "advanced", "insanity"]:
                raise ValueError("There is a problem here, selected {diffulty} doesnt exist!\n Please select again.\n")
            break
        except ValueError as e:
            print(e)

    if difficulty == "beginner":
        return hangman.beginner
    elif difficulty == "novice":
        return hangman.novice
    elif difficulty == "advanced":
        return hangman.advanced
    else:
        return hangman.insanity


def select_random_word(word_list):
    """
    Chooses a random word from the list based on what level of 
    difficulty has been selected by the user.
    """

    word = random.choice(word_list)
    return word.lower()


def user_input(user_guess):
    """
    Checks the users input and returns the correct outcome based on if 
    the users guess is in the current word. 
    """

    while True:
        try:
            guess = input("Please take a guess:\n").lower()
            if len(guess) != 1:
                raise ValueError("Input Invalid. Please enter a single letter.")
            elif guess in user_guess:
                raise ValueError ("Sorry, you've' already tried that letter. Try again")
            elif not guess.isalpha():
                raise ValueError("Input is invalid. Please enter a letter.")
            else: 
                return guess
        except ValueError as e:
            print(e)


def update_game_word():
    """
    Updates the games word, based on the games selected word and users
    inputs.
    """


def game_won():
    """
    Checks if the game is won and returns a value based on if all the 
    correct letters have been guessed by the user.
    """


def display_current_game():
    """
    Displays the current state of the Hangman man. The current correct guesses
    and the current wrong guessed letters.
    """    


def game_running():
    """
    Runs the main game, calling all relevent functions
    """


def game_restart():
    """
    Restarts the game based on the users input. Going back to the 
    select difficulty function and running the game all over again.
    """


def main():
    """
    This function calls all other functions to allow the game 
    to be run more simply and easilly. Only calling one function to run 
    the game
    """
    display_game_title()

main()