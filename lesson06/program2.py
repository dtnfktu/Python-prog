import random

#   Задаём список случайных чисел и показываем его
lst = [random.randint(1,100) for i in range(10)]
print(f'Исходный список:\n{lst}')

# Oтсеиваем с чётными индексами
st = list(filter(lambda x: lst.index(x) %2 != 0, lst))

# Суммируем элементы и показываем
print(f'Сумма элементов на нечётных позициях = {sum(st)}')