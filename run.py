
import hangman
import random


def display_game_title():
    """
    Prints the logo for the game to the terminal.
    """

    logo = [

    ]

def game_instructions():
    """
    Displays the games instructions based on the users input
    """

    instructions = input('Would you like to see the games instructions Y/N? \n')

    instructions_text = [
        "First select a difficulty level. Beginner, Novice, Advanced, Insanity?\n",
        "To win the game guess all the correct characters in the word\n",
        "Correct guess reveals the letter\n",
        "Wrong guess adds to the man being hung\n"
    ]


def new_player():
    """
    Allows the player to enter a username for the game to begin
    """


def select_difficulty():
    """
    Allows the user to select the difficulty of the hangman game
    and set the words accordingly. 
    If a new game is selected at the end, then it will come back 
    to this function to reset the game difficulty.
    """


def select_random_word():
    """
    Chooses a random word from the list based on what level of 
    difficulty has been selected by the user.
    """


def user_input():
    """
    Checks the users input and returns the correct outcome based on if 
    the users guess is in the current word. 
    """


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