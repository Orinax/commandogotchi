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

    # Choosing 1 will load a file? that will continue a save?
    if int(menu_choice) == 1:
        # insert code here to continue a previously started game.
        pass
    # Choosing 2 will create a new instance of a commandogotchi.
    elif int(menu_choice) == 2:
        # Maybe clean this up later and put it all in a function?
        while True:
            chosen_name = input("Enter a name for your commandogotchi: ")
            confirm_name = input(f"Is {chosen_name} correct? (y/n):")
            if confirm_name == "y":
                # cogo is short for 'commandogotchi'.
                cogo = cg.Commandogotchi(chosen_name)
                return cogo
                break
            elif confirm_name == "n":
                pass
    # Choosing 3 will open a hall of fame to show stats from games past.
    elif int(menu_choice) == 3:
        # insert code here to create or show a hall of fame.
        pass


# Create an instance of a commandogotchi.
# Cogo is short for 'commandogotchi'.
# def create_commandogotchi(chosen_name):
#    cg.Commandogotchi(chosen_name)
