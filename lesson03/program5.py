def Fibonacci(n):
    ''' Метод формирует последовательность Фибоначчи + негаФибоначчи
    двумя циклами: первый - правую часть, второй - левую
    '''
 
    if n == 0:          # Костыль
        return []       # для n = 0
    
    f1 = 0
    f2 = 1
    lst = [f1, f2]

    # Формируем правую (положительную) часть
    for i in range(2, n + 1):
        lst.append(f1 + f2)
        f1 = f2
        f2 = lst[i]
    
    f1 = lst[0]
    f2 = lst[1]
    
    #Формируем левую (положительно-отрицательную часть)
    for i in range(1, n + 1):
        lst.insert(0, f2 - f1)
        f2 = f1
        f1 = lst[0]
    
    return lst

def RecFibonacci(k):
    '''Рекурсивный поиск k-го числа Фибоначчи
    '''
    if k == 1 or k == 2:
        return 1
    
    return RecFibonacci(k - 2) + RecFibonacci(k - 1)

def RecNegaFibonacci(k):
    '''Рекурсивный поиск k-го числа негаФибоначчи
    '''
    if k == -1:
        return 1    
    if k == -2:
        return -1
    
    return RecNegaFibonacci(k + 2) - RecNegaFibonacci(k + 1)    

def RecFibonacciList(n):
    '''Метод форимрует последовательность Фибоначчи + негаФибоначчи
    используя функции рекурсивного нахождения k-го числа последовательности
    '''
    ls = []

    if n == 0:          # Костыль
        return ls       # для n = 0

    for i in range(-n, 0):
        ls.append(RecNegaFibonacci(i))

    ls.append(0)

    for i in range(1, n + 1):
        ls.append(RecFibonacci(i))

    return ls

st = input('Введите целое неотрицательное число : ')
while not st.isdigit():
    st = input('Введите целое неотрицательное число : ')

print('Последовательность Фибоначчи/негаФибоначчи (цикл):')
print(Fibonacci(int(st)))

print('Последовательность Фибоначчи/негаФибоначчи (рекурсия):')
print(RecFibonacciList(int(st)))