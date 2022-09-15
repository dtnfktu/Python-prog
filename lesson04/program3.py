def read_from_file(file_path : str) :
    '''Считывает из файла строки и возвращает список'''
    res_list = []
    with open(file_path, 'r') as file :
        for line in file:
            res_list.append(line.replace('\n',''))   # Сразу убираем перенос строки \n

    return res_list

def write_into_file(file_path : str, list_str : str) :
    '''Записывает в файл строки, заданные списком'''
    with open(file_path, 'w') as file :
        file.writelines('\n'.join(list_str))

def upper_better_four(ls : list) :
    '''Ищет всех, у кого оценка больше 4 и переводит в верхний регистр'''
    for i in range(0,len(ls)) :
        index = len(ls[i]) - 1
        if int(ls[i][index]) > 4 :
            ls[i] = ls[i].upper()

lst = read_from_file('test.txt')
upper_better_four(lst)
write_into_file('test.txt', lst)
print('File was rewrited')