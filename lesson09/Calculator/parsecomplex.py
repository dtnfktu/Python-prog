def sum_num(a : tuple, b : tuple) :
    '''Принимает два комплексных числа, складывает и возвращает результат - кортеж'''
    return (a[0] + b[0], a[1] + b[1])

def sub_num(a : tuple, b : tuple) :
    '''Принимает два комплексных числа, возвращает кортеж - первое минус второе'''
    return (a[0] - b[0], a[1] - b[1])

def mul_num(a : tuple, b : tuple) :
    '''Принимает два комплексных числа, возвращает их произведение'''
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + b[0]*a[1])

def div_num(a : tuple, b: tuple) :
    '''Принимает два комплексных числа, возвращает результат деления первого на второе'''
    if b[0] == 0 and b[1] == 0 :
        return 'Ошибка! Деление на ноль!'
    return ((a[0]*b[0] + a[1]*b[1]) / (b[0]*b[0] + b[1]*b[1]), (b[0]*a[1] - a[0]*b[1]) / (b[0]*b[0] + b[1]*b[1]))

def checkstring(st : str) :
    '''Корректировка введенного выражения и проверка на корректность'''
    ans = st.replace(' ','')            # удаляем пробелы, если таковые имеются
    ans = ans.replace(',','.')          # меняем запятые на точки, если таковые есть
    ans = ans.replace('\\','/')         # левый слеш на правый, если такой вдруг есть
    for sym in ans :
        if not sym in ('+','-','*','/','.','(',')','0','1','2','3','4','5','6','7','8','9','[',']','i') :
            print('Введено некорректное выражение - в выражении присутствует недопустимый символ')
            return -1

    if len(list(filter(lambda x: x == '(',ans))) != len(list(filter(lambda x: x == ')',ans))) :
        print('Введено некорректное выражение - количество открывающих и закрывающих скобок не совпадает')
        return -1

    if len(list(filter(lambda x: x == '[',ans))) != len(list(filter(lambda x: x == ']',ans))) :
        print('Введено некорректное выражение - количество открывающих и закрывающих скобок не совпадает')
        return -1        
    return ans

def parse_complex(expr : str) :
    '''Переводит комплексное число из строки в кортеж'''
    # Если стандартная запись числа - a + bi
    if expr[0] == '-' :
        sign = '-'
        expr = expr[1:]
    else :
        sign = ''
    if ('+' in expr) or ('-' in expr) :
        i = 0
        re = sign
        # Вещественную часть выделяем
        while (expr[i] != '+') and (expr[i] != '-') :
            re = re + expr[i]
            i += 1
        # Теперь мнимую
        im = expr[i:len(expr) - 1]
        if (im == '+') or (im == '-') :
            im = im + '1'
        return (float(re), float(im))
    # Если только мнимая часть присутствует
    if 'i' in expr :
        re = '0'
        im = expr[:len(expr) - 1]
        return (float(re), float(im))
    # Если только вещественная часть присутствует
    return (float(expr), 0.0)

def parse_num(expr : str) :
    '''Переводит заданное выражение в список'''
    ans = []
    complx = ''
    indx = 0
    while indx < len(expr) :
        if expr[indx] != '[' :
            ans.append(expr[indx])
        else :
            indx += 1
            cmplx = ''
            while expr[indx] != ']' :
                cmplx += expr[indx]
                indx += 1
            ans.append(parse_complex(cmplx))
        indx += 1

    return ans

def primitive_oper(oper : list) :
    '''Выполняет операцию между двумя числами'''
    if oper[1] == '+' :
        return sum_num(oper[0], oper[2])
    if oper[1] == '-' :
        return sub_num(oper[0], oper[2])
    if oper[1] == '*' :
        return mul_num(oper[0], oper[2])
    if oper[1] == '/' :
        return div_num(oper[0], oper[2])

def mixed_operation(oper : list) :
    '''Обрабатывает смешанную операцию'''
    res = oper.copy()

    while ('*' in res) or ('/' in res) :
        # определяем что раньше - умножение или деление
        index1 = len(res) if not '*' in res else res.index('*')
        index2 = len(res) if not '/' in res else res.index('/')
        index_begin = min(index1, index2)
        tmp_num = primitive_oper(res[index_begin - 1:index_begin + 2])
        res = res[:index_begin - 1] + [tmp_num] + res[index_begin + 2 :]

    while ('+' in res) or ('-' in res) :
        # определяем что раньше - умножение или деление
        index1 = len(res) if not '+' in res else res.index('+')
        index2 = len(res) if not '-' in res else res.index('-')
        index_begin = min(index1, index2)
        tmp_num = primitive_oper(res[index_begin - 1:index_begin + 2])
        res = res[:index_begin - 1] + [tmp_num] + res[index_begin + 2 :]    

    return res[0]

def calculate(expr : str) :
    '''Вычисляем значение выражения'''

    number = parse_num(checkstring(expr))
    # Заменяем выражения в скобках на их значения
    while '(' in number :
        # Берём начало и конец выражения в скобках
        index_begin = len(number) - 1 - number[::-1].index('(')     # открывающая скобка
        index_end = index_begin + number[index_begin:].index(')')   # закрывающая скобка
        # Заменяем его на число - результат операции(й)
        tmp_num = mixed_operation(number[index_begin + 1:index_end])
        # Заменяем скобки числом в исходном выражении
        number = number[:index_begin] + [tmp_num] + number[index_end + 1:]
   
    answr = mixed_operation(number)                                 # <= Ответ уже здесь, но в виде кортежа
    re = str(answr[0]) if answr[0] != 0 else ''
    im = '' if answr[1] == 0 else (str(answr[1]) if answr[1] < 0 else '+' + str(answr[1])) + 'i'
    return re + im