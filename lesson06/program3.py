import operator

point1 = tuple(map(float, input('Координаты точки 1 через пробел : ').split(" ")))
point2 = tuple(map(float, input('Координаты точки 2 через пробел : ').split(" ")))

# Разность между соответствующими компонентами координат
res = tuple(map(operator.sub, point1, point2))
# Извлечение квадратного корня из суммы квадратов
res = sum(map(lambda x: x ** 2, res)) ** 0.5

print(f'Расстояние между точками = {res:.2f}')