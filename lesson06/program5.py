import random

n = 9

lst = [random.randint(1, 10) for i in range(n)]
print(f'Исходный список :\n{lst}')

multi_list = [lst[i] * lst[len(lst) - 1 - i] for i in range(round(len(lst)/2 + 0.1))]
# Пояснение. Если просто округлять, то 2.5 -> 2, 4.5 -> 4 etc, Особенность питона...
# При увеличении на 0.1 гарантировано при чётном количестве - округление в меньшую сторону
# при нечётном - в бОльшую
print(f'Полученный список:\n{multi_list}')