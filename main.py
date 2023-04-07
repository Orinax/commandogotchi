from commandogotchi import Commandogotchi
import game_functions as gf
import game_messages as msg
from alive_progress import alive_it as ai
from time import sleep


gf.create_start_menu()
selected_option = gf.start_menu_selections()

if selected_option == 1:
    gf.continue_game()
elif selected_option == 2:
    cogo = gf.new_game(msg, sleep)
    gf.hatch_egg(cogo, ai, sleep)
elif selected_option == 3:
    gf.view_hof()
