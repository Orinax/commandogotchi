import commandogotchi as cg


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

    # Ask the user to choose a menu option.
    menu_choice = input(">>> ")
    print(f"You chose option {menu_choice}")
    return int(menu_choice)


# Choosing 1 will load a file? that will continue a save?
def continue_game():
    """This will continue a previously started game."""
    pass
    # insert code here to continue a previously started game.


def new_game():
    """This creates a new instance of a commandogotchi."""
    while True:
        chosen_name = input("Enter a name for your commandogotchi: ")
        confirm_name = input(f"Is {chosen_name} correct? (y/n):")
        if confirm_name == "y":
            # cogo is short for 'commandogotchi'.
            cogo = cg.Commandogotchi(chosen_name)
            print(f'''
                  Congratulations! {chosen_name} will hatch from an egg
                  soon. Please take good care of {chosen_name} and do not
                  let {chosen_name} die.
                  ''')
            return cogo
            break
        elif confirm_name == "n":
            pass


def view_hof():
    """This allows a user to view records of all commandogotchis that have
    been cared for in the past."""
    # insert code here to create or show a hall of fame.
    pass
