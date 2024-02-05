import random
from time import sleep
import checker

# Show list of themes
def show_lists():
    themes_list = []
    print("We have these themes here:")
    counter = 0
    # Open theme list
    with open("themes_list", "r", encoding='utf-8') as arquivo:
        # Print themes
        for theme in arquivo:
            themes_list.append(theme.strip())
            print(f"{counter+1} -> {theme}", end="")
            counter+=1


# Show list of words
def show_words(list_name):
    words_list = []
    print("We have these words added here:")
    # Open words list
    with open(f"{list_name}", "r", encoding='utf-8') as arquivo:
        # Print words in some theme
        for word in arquivo:
            words_list.append(word.strip())
            print(f"-> {word.title()}", end="")


def add_word():
    # Show list of themes
    show_lists()
    try:
        choice = int(input("\nDo you want to add a word in which theme (Enter the number)?\n"))
        # Check if choice is valid
        list_name = checker.check_list(choice)
        # Open words list
        with open(f"{list_name}", "a", encoding='utf-8') as arquivo:
            # Show list of words
            show_words(list_name)
            entered_word = input("\nEnter the new word: \n").lower()
            # Check if the word is already added
            valid = checker.check_add_word(entered_word, list_name)
            if(valid):
                arquivo.write(f"{entered_word}\n")
                print("Word added! Returning to menu...")
                sleep(3)
    except:
        print("Invalid value!")


def remove_word():
    # Show list of themes
    show_lists()
    original_list = []
    try:
        choice = int(input("\nDo you want to remove a word in which theme (Enter the number)?\n"))
        # Check if choice is valid
        list_name = checker.check_list(choice)
        with open(f"{list_name}", "r", encoding='utf-8') as arquivo:
            # Show list of words
            show_words(list_name)
            #Copy itens from txt to a python list
            for line in arquivo:
                original_list.append(line.strip())
            entered_word = input("\nEnter the word to remove: \n").lower()
            # Check if the word is in the list
            valid = checker.check_remove_word(entered_word, list_name)
            if(valid):
                original_list.remove(entered_word)

                # Rewrite the list in a txt
                with open(f"{list_name}", "w", encoding='utf-8') as arquivo:
                    for line in original_list:
                        arquivo.write(f"{line}\n")
                    print("Word removed! Returning to menu...")
                    sleep(3)
    except:
        print("Invalid value!")