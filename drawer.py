import random

def draw_word():
    words = []
    themes_list = []
    # Open txt to draw a theme and a word
    with open("themes_list", "r", encoding='utf-8') as arquivo:
        # Copy itens of txt theme to a python list
        for theme in arquivo:
            themes_list.append(theme.strip())
        # Draw a theme (name of an archive)
        drawn_theme = random.choice(themes_list)
        # Put the first letter uppercase
        print(f"Your word is a(n): {drawn_theme.title()}")

        # Draw a word
        with open(f"{drawn_theme}", "r") as arquivo:
            # Copy itens of txt theme to a python list
            for word in arquivo:
                words.append(word.strip())
            # Draw a word (inside of the drawn theme list)
            drawn_word = random.choice(words).upper()
            return drawn_word