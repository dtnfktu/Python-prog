str = input('Enter the integer number >0 : ')
while not str.isdigit():
    str = input('Enter the integer number >0 : ')
n = int(str)

list = []
multiply = 1

for i in range(1, n + 1):
    multiply *= i
    list.append(multiply)
    
print('List 1 :', list)

list2 = []

for i in range(1, n + 1):
    mult = 1
    for j in range(1, i + 1):
        mult *= j
    list2.append(mult)

print('List 2 :', list2)