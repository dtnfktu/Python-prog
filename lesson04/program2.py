from operator import index
import random


def create_list(min_num : int, max_num : int, len_num : int) :
    '''Создаёт случайную последовательность целых чисел'''
    return [random.randint(min_num, max_num) for i in range(len_num)]

def analise_list(nums : list) :
    ''' Возвращает список неповторяющихся элементов,
    из которых состоит последовательность nums'''
    out_list = nums.copy()
    out_list.sort()

    current_index = 0
    while current_index < len(out_list) - 1 :
        if out_list[current_index] == out_list[current_index + 1] :
            out_list.pop(current_index + 1)
        else :
            current_index += 1

    return out_list

lst = create_list(1, 15, 25)
print('Primary list :')
print(lst)
print('List of numbers :')
print(analise_list(lst))