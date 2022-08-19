from commandogotchi import Commandogotchi
import game_functions as gf


def create_start_menu():
    """Create a starting menu for the game."""
    # Create a menu with choices for players.
    print("*" * 34)
    print()
    print("       Commandogotchi       ")
    print("--A Command Line Tamagochi--")
    print()
    print("*" * 34)
    print()
    print("Choose an option by entering 1, 2, or 3.")
    print(">>> 1. Continue")
    print(">>> 2. New Game")
    print(">>> 3. Hall of Fame")
    print()


def start_menu_selections():
    """Option (1) allows a user to continue a previously started game.
    Option (2) allows a user to start a new game.
    Option (3) allows a user to view the Hall of Fame."""

    # User
    menu_choice = input(">>> ")
    print(f"You chose option {menu_choice}")

    if int(menu_choice) == 1:
        # insert code here to get a new game running.
    if int(menu_choice) == 2:
        # fix this: Need a loop, not a function within a function.
        def choose_a_name():
            chosen_name = input("Enter a name for your commandogotchi: ")
            confirm_name = input(f"Is ""{chosen_name}"" correct? (y/n):")
            if confirm_name ==
        cogo = gf.create_commandogotchi(chosen_name)
    else:
        pass


# Create an instance of a commandogotchi.
# Cogo is short for 'commandogotchi'.
def create_commandogotchi(chosen_name):
    cogo = Commandogotchi(chosen_name)
    return cogo
