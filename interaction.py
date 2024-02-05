from os import system
import checker

def get_choice():
    valid_number = False
    while(not valid_number):
        try:
            # Define the gamemode
            gamemode = int(input("You can chose Singleplayer [1], Multiplayer [2] or add [3] / remove [4] a word from Singleplayer's list (and you can exit if you enter [5]): \n"))
            if(0<gamemode<=5):
                valid_number = True
                # Check the gamemode chose and show the message for user
                return checker.check_gamemode(gamemode)
            else:
                print("Invalid number!")
        except:
            print("Invalid value!")


# Word and Hint (Multiplayer mode)
def set_word_hint():
    word = input("Enter a word to the Hangman Game: \n").upper()
    hint = input("Enter a hint about the word you chose: \n")
    system('cls')
    print("Well, let's play the game!")
    print(f"Hint about the word: {hint}")
    return word

