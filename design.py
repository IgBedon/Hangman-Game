import word_spaces

# Here I'm doing the design part
def drawing(allowed_errors, word, spaces=[], index_attempt=[], attempt='', wrong_attempt=[]):
    if(allowed_errors == 6):
        print("________ ")
        print("|    | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif(allowed_errors == 5):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("| ")
        print("| ")
        print("| ")
    elif(allowed_errors == 4):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|    | ")
        print("| ")
        print("| ")
    elif(allowed_errors == 3):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /| ")
        print("| ")
        print("| ")
    elif(allowed_errors == 2):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    ")
        print("| ")
    elif(allowed_errors == 1):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|   /")
        print("| ")
    else:
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|   //")
        print("| ")
        print("Oh no! Your attempts are over! Finishing... :(")
        print(f"The word was: {word} \n")
        spaces.clear()
        return
    # I'm calling the method to change the spaces of the word
    return word_spaces.change_spaces(spaces, word, index_attempt, attempt, wrong_attempt)
