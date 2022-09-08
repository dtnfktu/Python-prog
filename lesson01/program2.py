count = 2 ** 3              # количество комбинаций значений переменных

for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            ans = (not (x or y or z)) == (not x and not y and not z)
            print('x =', x, 'y =', y,'z =', z, ', Результат =', ans)
            print('---------------------')
            if ans:
                count -= 1

if count == 0:              # количество комбинаций с результатом False
    print("Равенство верно!")
else:
    print("Равенство неверно!")