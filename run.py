import hangman
import random


def display_game_title():
    """
    Prints the logo for the game to the terminal.
    """

    logo = ["Welcome to Hangman!"]

    for _ in logo:
        print(logo)


def game_instructions():
    """
    Displays the games instructions based on the users input
    """

    instructions = input('Would you like to see the games instructions Y/N? \n')

    while instructions.lower() not in ["y", "n"]:
        instructions = input("Enter 'y' to show gamne instructions of 'n' to skip.\n ")

    if instructions.lower() == "y":
        instructions_text = [
            "First select a difficulty level. Beginner, Novice, Advanced, Insanity?\n",
            "To win the game guess all the correct characters in the word\n",
            "Correct guess reveals the letter\n",
            "Wrong guess adds to the man being hung\n"
        ]
        for _ in instructions_text:
            print("Lets Get Started")
            break


def new_player():
    """
    Allows the player to enter a username for the game to begin
    """

    while True:
        try:
            print()
            user = input("Please enter a valid name: \n")
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
            print(f"Welcome to the game {user}!")
            return user


def select_difficulty():
    """
    Allows the user to select the difficulty 
    of the hangman game
and set the words accordingly.
    If a new game is selected at the end, then it will come back
    to this function to reset the game difficulty.
    """

    while True:
        try:
            print()
            difficulty = input("Please select your fate: beginner, novice, advanced or insanity\n").lower()
            if difficulty not in ["beginner", "novice", "advanced", "insanity"]:
                raise ValueError(f"There is a problem here, selected {difficulty} difficulty doesnt exist!\nPlease select again.")
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
    Checks the users input and returns the 
    correct outcome based on if the users 
    guess is in the current word.
    """

    while True:
        try:
            guess = input("Please take a guess:\n").lower()
            if len(guess) != 1:
                raise ValueError(f"{guess} is invalid. Please enter a single letter.")
            elif guess in user_guess:
                raise ValueError(f"Sorry, you've' already tried {guess} before. Try again")
            elif not guess.isalpha():
                raise ValueError(f"{guess} is invalid. Please enter a letter.")
            else:
                return guess
        except ValueError as e:
            print(e)


def update_game_word(guess, selected_word, hidden_word):
    """
    Updates the games word, based on the games 
    selected word and users inputs.
    """

    if guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                hidden_word[i] = guess
    return hidden_word


def game_won(hidden_word):
    """
    Checks if the game is won and returns a value 
    based on if all the correct letters have been 
    guessed by the user.
    """

    return "_" not in hidden_word


def display_current_game(wrong_guess, user_guess, hidden_word):
    """
    Displays the current state of the Hangman man. 
    The current correct guesses and the current 
    wrong guessed letters.
    """

    print(hangman.hangman_state[wrong_guess])
    print(f"Guessed Letters: { ', '.join(user_guess)}")
    print(" ".join(hidden_word))


def game_running(user):
    """
    Runs the main game, selecting a random word from the words 
    avalible in the hang man file.
    Checking the users input and reacting based on the input
    Checking if the game is won or lost and printing,
    relevent messages.
    """

    word_list = select_difficulty()
    secret_word = select_random_word(word_list)
    hidden_word = ["_" for _ in secret_word]
    print(" ".join(hidden_word))

    wrong_guess = 0
    user_guess = []

    while not game_won(hidden_word) and wrong_guess < 6:
        guess = user_input(user_guess)
        user_guess.append(guess)

        if guess in secret_word:
            print('Correct!')
            hidden_word = update_game_word(guess, secret_word, hidden_word)
        else:
            print("Incorrect!")
            wrong_guess += 1

        display_current_game(wrong_guess, user_guess, hidden_word)

        if wrong_guess == 5 and not game_won(hidden_word):
            print(f"Final Chance {user.upper()}!\n")

    if game_won(hidden_word):
        print()
        print("You've beaten the hangmans noose\n")
        print(f"Your name is clear {user.capitalize()}\n")
        print("You are free to go!\n")
    else:
        print()
        print("The word was:", secret_word.upper())
        print(f"\nYou've lost to the hangman. Better luck next time {user.capitalize()}\n")

    if not game_restart():
        print('why no work')


def game_restart():
    """
    Restarts the game based on the users input. Going back to the
    select difficulty function and running the game all over again.
    """

    while True:
        try:
            user_play_again = input("Would you like to play again? 'Y' or 'N'\n").lower()
            if user_play_again not in ['y', 'n']:
                raise ValueError("Input invalid. Please enter 'Y' or 'N'\n")
            break
        except ValueError as e:
            print(e)

    if user_play_again == 'y':
        main()
        return True
    elif user_play_again == 'n':
        return False


def main():
    """
    This function calls all other functions to allow the game
    to be run more simply and easilly. Only calling one function to run
    the game
    """
    display_game_title()
    print('\nThis is your chance to see if you have what it takes,')
    print('To beat the Gallows! And survive your fate.')
    print('Are you ready to play? Lets get going!\n')
    game_instructions()
    user = new_player()
    game_running(user)


main()
