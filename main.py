from commandogotchi import Commandogotchi
import game_functions as gf


# Create an opening menu for Commandogotchi.
print("*" * 34)
print()
print("       Commandogotchi       ")
print("--A Command Line Tamagochi--")
print()
print("*" * 34)
print()
print("Choose an option by entering 1, 2, or 3.")
print(">>>1. Continue")
print(">>>2. New Game")
print(">>>3. Hall of Fame")
print()

menu_choice = input(">>>")
print(f"You chose option {menu_choice}")

if int(menu_choice) == 2:
    chosen_name = input("Enter a name for your commandogotchi: ")
    cogo = gf.create_commandogotchi(chosen_name)
else:
    pass

#print(cogo.name)
#print(cogo.age)
#print(cogo.happiness)
