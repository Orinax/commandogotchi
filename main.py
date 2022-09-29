from commandogotchi import Commandogotchi
import game_functions as gf
import game_messages as msg


gf.create_start_menu()
selected_option = gf.start_menu_selections()

if selected_option == 1:
    gf.continue_game()
elif selected_option == 2:
    gf.new_game(msg)
elif selected_option == 3:
    gf.view_hof()
