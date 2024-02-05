from time import sleep
from os import system
import design
import checker
import interaction
import drawer
import words_list

# Define process gamemode
def define_process(gamemode):
    if(gamemode == 1):
        process_singleplayer()
    elif(gamemode == 2):
        process_multiplayer()
    elif(gamemode == 3):
        words_list.add_word()
    elif(gamemode == 4):
        words_list.remove_word()
    else:
        exit()


def process_singleplayer():
    allowed_errors = 6
    wrong_attempts = []
    first_time = True
    # Drew a word existing in a .txt
    drawn_word = drawer.draw_word()
    # Defining the spaces of the word
    spaces = design.drawing(allowed_errors, drawn_word)
    # Start the game process
    while (allowed_errors >= 0):
        # Do that if isn't the first time
        if (not first_time):
            # Update spaces with letters changed (or not)
            spaces = design.drawing(allowed_errors, drawn_word, spaces, index_attempt, attempt, wrong_attempts)
            # Check if the word have blank spaces
            if (allowed_errors > 0):
                try:
                    # The code continues
                    spaces.index('_')
                except:
                    # The code finish and restart
                    print("You won! Congratulation! :)")
                    print(f"The word was: {drawn_word}")
                    print(f"Restarting")
                    spaces.clear()
                    sleep(3)
                    system('cls')
                    return
                # Ask for a letter if isn't the first time
                attempt = input("Type a letter so we can check if it's in the word: \n").upper()
                index_attempt, allowed_errors, wrong_attempts = checker.check_attempt(drawn_word, allowed_errors, spaces, attempt, wrong_attempts)
            else:
                allowed_errors -= 1
        # Ask for a letter if isn't the first time
        else:
            attempt = input("Type a letter so we can check if it's in the word: \n").upper()
            index_attempt, allowed_errors, wrong_attempts = checker.check_attempt(drawn_word, allowed_errors, spaces, attempt, wrong_attempts)
            first_time = False


def process_multiplayer():
    word = interaction.set_word_hint()
    allowed_errors = 6
    wrong_attempts = []
    first_time = True
    # Defining the spaces of the word
    spaces = design.drawing(allowed_errors, word)
    while(allowed_errors>=0):
        # Do that if isn't the first time
        if(not first_time):
            # Update spaces with letters changed (or not)
            spaces = design.drawing(allowed_errors, word, spaces, index_attempt, attempt, wrong_attempts)
            # Check if the word have blank spaces
            if(allowed_errors>0):
                #Try to capture an Error
                try:
                    # The code continues
                    spaces.index('_')
                except:
                    # The code finish and restart
                    print("You won! Congratulation! :)")
                    print(f"The word was: {word}")
                    print(f"Restarting")
                    # Clean the list for the next game
                    spaces.clear()
                    sleep(3)
                    system('cls')
                    return
                # Ask for a letter if isn't the first time
                attempt = input("Type a letter so we can check if it's in the word: \n").upper()
                # Check if the attempt was correct
                index_attempt, allowed_errors, wrong_attempts = checker.check_attempt(word, allowed_errors, spaces, attempt, wrong_attempts)
            else:
                allowed_errors-=1
        # Ask for a letter if isn't the first time
        else:
            attempt = input("Type a letter so we can check if it's in the word: \n").upper()
            # Check if the attempt was correct
            index_attempt, allowed_errors, wrong_attempts = checker.check_attempt(word, allowed_errors, spaces, attempt, wrong_attempts)
            first_time = False

