def read_polynom(filename : str) :
    '''Считывает полином из файла и преобразует его в список (коэффициентов)'''
    with open(filename, 'r') as f:
        txt = f.read().replace(' = 0','')
    
    tmp = list(filter(lambda x: 'x' in x, txt.split(' ')))[0]

    len = int(tmp[tmp.find('^') + 1:])          # определяем степень полинома
    answer = [0 for i in range(0, len + 1)]     # задаём список коэффициентовб изначально все нули

    tmp = txt.split(' ')
    
    if tmp[0][0] == '-' :                       # определяем знак первого слагаемого
        sign = '-'
        tmp[0] = tmp[0][1:]
    else :
        sign = '+'        
    
    for element in tmp :
        if element in ('+','-') :
            sign = element
        else :
            if 'x^' in element :
                koef = element[0:element.find('x')] if element[0:element.find('x')] != '' else '1'
                powr = element[element.find('^') + 1:]
                
            elif 'x' in element :
                powr = '1'
                koef = element[0:element.find('x')] if element[0:element.find('x')] != '' else '1'
            
            else :
                powr = '0'
                koef = element
            answer[len - int(powr)] = int(sign + koef)
    
    return answer

def increase_list(lst : list, ln : int) :
    '''Вставляет нули в начало списка до достижения требуемой длины'''
    while len(lst) < ln :
        lst.insert(0, 0)

def write_polynom(polynom : list, filename : str) :
    '''Записываем полином в файл'''
    pwer = len(polynom) - 1
    
    pol_str = str(polynom[0]) + 'x^' + str(len(polynom) - 1)            # старший элемент полинома формируем отдельно

    for indx in range(1, len(polynom) - 2) :
        if polynom[indx] != 0 :
            el = (' + ' if polynom[indx] > 0 else ' - ') + str(abs(polynom[indx])) + 'x^'
            pol_str = pol_str +  el + str(len(polynom) - indx - 1)
     
    # предпоследний и последний элементы тоже формируются отдельно
    if polynom[len(polynom) - 2] != 0 :
        pol_str += (' + ' if polynom[len(polynom) - 2] > 0 else ' - ') + str(abs(polynom[len(polynom) - 2])) + 'x'

    if polynom[len(polynom) - 1] != 0 :
        pol_str += (' + ' if polynom[len(polynom) - 1] > 0 else ' - ') + str(abs(polynom[len(polynom) - 1]))

    with open(filename, 'w') as f :
        f.write(pol_str + ' = 0')


polynom1 = read_polynom('polynom1.txt')
polynom2 = read_polynom('polynom2.txt')

increase_list(polynom1, max(len(polynom1), len(polynom2)))
increase_list(polynom2, max(len(polynom1), len(polynom2)))

itog = [polynom1[i] + polynom2[i] for i in range(0, len(polynom1))]     # складываем полиномы

print(polynom1)
print(polynom2)
print(itog)

write_polynom(itog, 'polynom3.txt')