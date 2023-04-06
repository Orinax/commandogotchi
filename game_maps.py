from itertools import product




def grid(x, y):
    return list(product(range(x), repeat=y))


def get_number_columns(list):
    available_columns = list[-1][0] + 1
    number = 0
    new_list = []
    for item in list:
        if item[0] == number:
            new_list.append(item)
    return new_list

       # print(new_list)
#    for item in list:
#        for i in range(available_columns):
#            if item[0] == i:
#                print(f"{i} is {item}")
#    return available_columns
