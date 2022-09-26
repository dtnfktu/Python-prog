from asyncio.windows_events import NULL
import operator

def is_float_number(a):
    '''Ковертирует str в float. При ошибке выдаёт сообщение и возвращает слово None'''
    try:
        float(a)
        return float(a)
    except:
        print('Некорректный ввод данных :(')
        return 'None'

# Вещественные числа можно вводить и с точкой и с запятой
while True:
    point1 = tuple(map(is_float_number, input('Координаты точки 1 через пробел : ').replace(',','.').split(" ")))
    if not 'None' in point1 :
        break

while True:
    point2 = tuple(map(is_float_number, input('Координаты точки 2 через пробел : ').replace(',','.').split(" ")))
    if not 'None' in point2 :
        break

# Разность между соответствующими компонентами координат
res = tuple(map(operator.sub, point1, point2))
# Извлечение квадратного корня из суммы квадратов
res = sum(map(lambda x: x ** 2, res)) ** 0.5

print(point1,point2)
print(f'Расстояние между точками = {res:.4f}')
#print(NULL is False)