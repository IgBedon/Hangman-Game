# CHANGING SPACES OF WORD
def change_spaces(spaces, word, index_attempt, attempt, wrong_attempt):
    # CASE LIST SPACE DON'T HAVE ITENS YET
    if(spaces == []):
        for letter in range(0, len(word)):
            spaces.append("_")
        print(" ".join(spaces))
        if(wrong_attempt != []):
            print(f"Wrong attempts: {wrong_attempt}")
        print("===========================================================================")
        return spaces
    
    # CASE INDEX LENGTH < 0 MEANS THAT THE LETTER ISN'T AT THE WORD 
    elif(len(index_attempt)<0):
        # Print items of list "spaces" with " "
        print(" ".join(spaces))   
        if(wrong_attempt != []):
            print(f"Wrong attempts: {wrong_attempt}")
        print("===========================================================================")
        return spaces 

    # CASE INDEX LENGTH > 0 MEANS THAT THE LETTER IS AT THE WORD 
    else:
        counter = 0
        # Capture the index of correct attempt and put the index in "space" list to change the value
        for element in index_attempt:
            spaces[element] = attempt
        # Print items of list "spaces" with " "
        print(" ".join(spaces))
        if(wrong_attempt != []):
            print(f"Wrong attempts: {wrong_attempt}")
        print("===========================================================================")
        return spaces
