import introduct
import interaction
import process

# Hangman game - Challenge
continue_playing = True
# Show rules
introduct.show_rules()
# Start the interaction with the game
while(continue_playing):
    # Return the gamemode selected
    gamemode = interaction.get_choice()
    # Do the process part
    process.define_process(gamemode)
