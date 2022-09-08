x = float(input('Введите значение х : '))
y = float(input('Введите значение y : '))

if x == 0 and y == 0:
    print('Центр координатной плоскости')
elif x == 0:
    print('На оси Ох')
elif y == 0:
    print('На оси Оу')
elif x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)