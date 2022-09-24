import os

def second_sub(string_list : list, sub_string : str):
    '''Определяет индекс второго вхождения строки в списке'''
    filtered_list = list(filter(lambda element: sub_string in element, list(enumerate(string_list,start=0))))

    return - 1 if len(filtered_list) < 2 else filtered_list[1][0]

def print_answer(lst : list, substr : str) :
    '''Получает результат и выводит в консоль'''
    print('List =>', lst, f'=> Finding : \'{substr}\' => Answer :',second_sub(lst, substr))

# Для корректного отображения кириллицы в Windows
os.system('chcp 65001')
# Тесты из задания
print_answer(["qwe", "asd", "zxc", "qwe", "ertqwe"], 'qwe')
print_answer( ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], 'йцу')
print_answer(["йцу", "фыв", "ячс", "цук", "йцукен"], 'йцу')
print_answer(["123", "234", 123, "567"], '123')
print_answer([], '123')