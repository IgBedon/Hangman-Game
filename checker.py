from time import sleep


# Check attempt
def check_attempt(word, allowed_errors, spaces, attempt, wrong_attempt):
    counter = 0
    index_attempt = []
    # Using find() to check if we have a letter in the word
    index_find = word.find(attempt)
    try:
        # The letter haven't been attempted yet, index will return an error and go to except to add or not
        if(index_find>=0):
            spaces.index(attempt)
        # The letter have already been attempted
        else:
            wrong_attempt.index(attempt)
        print("\n----------> This letter was already entered! Try another letter <----------")
        return index_attempt, allowed_errors, wrong_attempt
    except:
        # Put the letter in the right space
        if(index_find>=0):
            for letter in range(0, len(word)):
                if(word[counter]==attempt):
                    index_attempt.append(counter)
                counter+=1

            print(f"\nYou're correct! This letter ({attempt}) is in the word! \nAllowed errors: {allowed_errors}")
            return index_attempt, allowed_errors, wrong_attempt
        # Say that the letter is wrong
        else:
            allowed_errors-=1
            print(f"\nYou're wrong! This letter ({attempt}) isn't in the word! \nAllowed errors: {allowed_errors}")
            wrong_attempt.append(attempt)
            return index_attempt, allowed_errors, wrong_attempt


def check_gamemode(gamemode):
    match gamemode:
        case 1:
            print("Nice, let's play singleplayer mode!")
            return 1
        case 2:
            print("Nice, let's play multiplayer mode!")
            return 2
        case 3:
            print("Well, let's ADD some word! :)")
            return 3
        case 4:
            print("Well, let's REMOVE some word! :)")
            return 4
        case 5:
            print("Oh, okay... Maybe we can play next time! :)")
            return 5
        

def check_list(choice):
    match choice:
        case 1:
            print("\nFruit selected!")
            return "fruit"
        case 2:
            print("\nCountry selected!")
            return "country"
        case 3:
            print("\nObject selected!")
            return "object"
        case 4:
            print("\nAnimal selected!")
            return "animal"


def check_add_word(entered_word, list_name):
    list_words = []
    # Open words list
    with open(f"{list_name}", "r", encoding='utf-8') as arquivo:
        # Copy words to a python list
        for line in arquivo:
            list_words.append(line.strip())
        # Check if the word is already in the list
        number_appears = list_words.count(entered_word)
        if(number_appears == 0):
            return True
        else:
            print("This word is already added! Returning to menu...\n")
            sleep(3)
            return False
        

def check_remove_word(entered_word, list_name):
    list_words = []
    # Open words list
    with open(f"{list_name}", "r", encoding='utf-8') as arquivo:
        # Copy words to a python list
        for line in arquivo:
            list_words.append(line.strip())
        # Check if the word is in the list
        number_appears = list_words.count(entered_word)
        if(number_appears == 0):
            print("This word isn't in list! Returning to menu...\n")
            sleep(3)
            return False
        else:
            return True