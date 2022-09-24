num = input('Введите искомое число :')
lst = ['Здесь нет','Здесь есть число 123','Здесь тоже 3214 есть','Здесь опять нету','456 А здесь есть 789']

#print(list(map(str, [x for x in range(0,10)])))

# for element in lst:
#     res = sum(list(map(lambda x: x in list(map(str, [x for x in range(0,10)])), list(element))))
#     print(res)

print(num in '\n'.join(lst))