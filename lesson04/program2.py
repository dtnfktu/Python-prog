import random


def create_list() :
    return [random.randint(10) for i in range(0,20)]

lst = create_list()
print(lst)