import random

n = 9

lst = [random.randint(1, 10) for i in range(n)]
print(lst)

mul = [lst[i] * lst[len(lst) - i - 1] for i in range(len(lst)//2)]

print(mul)