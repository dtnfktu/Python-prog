def DecToBin(dec):
    '''Перевод целого числа из десятичной системы счисления в двоичную
    '''
    bin = ''
    while True:
        bin = str(dec % 2) + bin
        dec //= 2
        if dec == 0:
            break
    
    return bin

st = input('Введите целое неотрицательное число : ')
while not st.isdigit():
    st = input('Введите целое неотрицательное число : ')

num = int(st)

print('Двоичное представление числа : ', DecToBin(num))