def lists_zip(list1, list2) :
    '''Cоздаёт список кортежей, состоящих из номера и языка, написанного большими буквами'''
    return list(zip(list1,  [x.upper() for x in list2]))

def filter_list(tuple_list : list) :
    '''Фильтрует список tuple_list следующим образом: если сумма очков слова имеет в делителях номер, 
    с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется.'''
    #tuple_list = tuple_list

    for i in range(len(tuple_list) - 1, 0, -1) :
        
        x = tuple_list[i]
        points = sum(list(map(ord, list(x[1]))))    # вычисляем сумму очков текущего кортежа
        
        if points % x[0] != 0 :
            tuple_list.remove(x)
        else :
            t = list(x)
            t[0] = points
            tuple_list[i] = tuple(t)

    return tuple_list


langs = ['python', 'C#', 'Java', 'C++', 'JavaScript', 'Go', 'Perl', 'Pascal']   # Задаём список АЯП
nums = [i for i in range(1, len(langs) + 1)]                                    # Задаём список номеров

print('Source list')
print(lists_zip(nums, langs))                       
print('Resulting list')
print(filter_list(lists_zip(nums, langs)))