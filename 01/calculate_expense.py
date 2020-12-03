import itertools

def add_em(a):
    sum = 0
    for item in list(a):
        sum = sum + int(item)
    return sum


def multiply_em(a):
    product = 1
    for item in list(a):
        product = product * int(item)
    return product


def get_values(size_of_set, expense_list):
    combinations = itertools.combinations(expense_list, size_of_set)
    for item in combinations:
        if add_em(item) == 2020:
            print(item)
            print(multiply_em(item))


def get_expense_list():
    with open('expense') as f:
        expense_list = f.read().splitlines()
    return expense_list


expense_list = get_expense_list()
get_values(2, expense_list)
get_values(3, expense_list)
