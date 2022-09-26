n = 8
# Используем цикл 
print([(-3) ** i for i in range(n)])
# Используем map
print(list(map(lambda x: (-3) ** x, range(n))))