# from commandogotchi import Commandogotchi as cg
import game_functions as gf
# import game_messages as msg
from alive_progress import alive_it as ai
from time import sleep


gf.create_start_menu()
selected_option = gf.start_menu_selections()

if selected_option == 1:
    gf.continue_game()
elif selected_option == 2:
    cogo = gf.new_game(sleep)
    gf.hatch_egg(cogo, ai, sleep)
    # Now that an egg has hatched, make it possible for the user to find out
    # informatino about the commandogotchi. i.e. Enter the main game loop.
elif selected_option == 3:
    gf.view_hof()
else:
    pass


while True:

    gf.check_cogo_stats(cogo)
