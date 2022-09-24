import random

#   Задаём список случайных чисел и показываем его
lst = [random.randint(1,100) for i in range(10)]
print(f'Исходный список:\n{lst}')

# Нумеруем элементы и отсеиваем с чётными индексами
lt = list(filter(lambda x: x[0] % 2 != 0, list(enumerate(lst,start=0))))

# Суммируем элементы и показываем
print(f'Сумма элементов на нечётных позициях = {sum(list(x[1] for x in lt))}')