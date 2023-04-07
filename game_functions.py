import commandogotchi as cg
import game_messages as msg



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


def new_game(msg, sleep):
    """This creates a new instance of a commandogotchi."""
    while True:
        chosen_name = input("Enter a name for your commandogotchi: ")
        confirm_name = input(f"Is {chosen_name} correct? (y/n):")
        if confirm_name == "y":
            # Instantiate the commandogotchi object.
            cogo = create_commandogotchi(chosen_name)
            # Call the message function to introduce new commandogotchi.
            msg.named_egg_msg(chosen_name)
            sleep(5)
            return cogo
            break
        elif confirm_name == "n":
            pass


def create_commandogotchi(chosen_name):
        # cogo is short for 'commandogotchi'.
        cogo = cg.Commandogotchi(chosen_name)
        return cogo


def view_hof():
    """This allows a user to view records of all commandogotchis that have
    been cared for in the past."""
    # insert code here to create or show a hall of fame.
    pass


def hatch_egg(cogo, ai, sleep):
    hatch_messages = ["A new egg! Cool! What will hatch from it?",
                      "Hmm, is hasn't hatched yet, but it should soon.",
                      "Oh look! The egg is moving!",
                      "There are cracks on the egg! Any minute now!",
                      "...",
                     ]
    for message in ai(hatch_messages):
        print(message)
        sleep(5)
    print(f"Look! {cogo.name} has hatched from an egg!")
