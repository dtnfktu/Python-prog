import random

#   Задаём список случайных чисел и показываем его
lst = [random.randint(1,100) for i in range(10)]
print('List :')
print(lst)

# Нумеруем элементы и отсеиваем чётные индексы
lt = list(filter(lambda x: x[0] % 2 != 0, list(enumerate(lst,start=0))))

# Суммируем элементы и показываем её
print(f'Sum of odd elements = {sum(list(x[1] for x in lt))}')


odd_list = [x for x in range(1, len(lst), 2)]
print(odd_list)
out = [lst[odd_list]]
print(odd_list)