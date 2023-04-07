# For testing
# Ask someone for the better way to test things out.
from game_maps import *

a = create_coordinates(5)
b = create_grid(a, create_row)
for list in b:
    print(list)
