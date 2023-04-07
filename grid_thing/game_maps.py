from itertools import product


def create_coordinates(x, y=2):
    '''Create a list of tuples with coordinates x, y. (Actually you are getting
    the cartesian product of to variables, but by leaving the y or 'repeat'
    values at 2, you can use the cartesian product as a set of coordinates for
    a 2 dimensional map.'''
    return list(product(range(x), repeat=y))


def create_row(list, row_number):
    '''Take a list of tuples and create a new list of
    tuples that have the same [1] index.'''
    row = []
    for item in list:
        if item[1] == row_number:
            row.append(item)
    return row


def create_grid(list, create_row):
    '''Combine lists of tuples to display in a format that shows 2 dimensional
    map coordinates.'''
    row_number = 0
    available_rows = list[-1][1]

    grid = []
    for item in list:

        if item[1] < available_rows:
            created_row = create_row(list, row_number)
            if not created_row:
                pass
            else:
               # print(created_row)
                grid.append(created_row)
            row_number += 1
    return grid
