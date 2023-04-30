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

def main():
    """
    This function calls all other functions to allow the game 
    to be run more simply and easilly. Only calling one function to run 
    the game
    """
    display_game_title()

main()