from commandogotchi import Commandogotchi
import game_functions as gf


gf.create_start_menu()
selected_option = gf.start_menu_selections()

# Depending on the user's choice 'selected_option' will = either
# (1) a request to load a file?
# (2) a Commandogotchi object
# (3) a request to view the hall of fame

# Next, plan ahead for how to handle that, and then keep working
# on the track for option (2).
