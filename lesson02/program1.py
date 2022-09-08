def IsFloatNumber(a):
    try:
        float(a)
        return True
    except:
        return False

# Пока не будет введено число цикл повтояертся
str = input('Enter the number: ').replace(',','.')          # меняем запятую на точку
while not IsFloatNumber(str):
    str = input('Enter the number: ').replace(',','.')

# Обрабатываем строку. Убираем минус и точку (если таковые были)
str = str.replace('-','').replace('.','')

summa = 0
for s in str:
    summa += int(s)

# получаем ответ по обработанной строке    
print('Sum from string =', summa)

# получаем ответ из числа
a = int(str)
summa = 0

while (a != 0):
    summa += a % 10
    a //= 10

print('Sum from int =', summa)