import random

def CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25): 
    ''' Метод формирует список случайных вещественных чисел
    '''
    NewList = [round(random.random() + random.randint(MinNum, MaxNum), 3) for i in range(ListLen)]
    return NewList

def GetMaxFractionalPart(List):
    '''Поиск максимальной дробной части среди элементов списка
    '''
    max = List[0] - int(List[0])
    
    for i in range(1, len(List)):
        t = List[i] - int(List[i])
        if max < t:
            max = t
    
    return max

def GetMinFractionalPart(List):
    '''Поиск минимальной дробной части среди элементов списка
    '''
    min = List[0] - int(List[0])

    for i in range(1, len(List)):
        t = List[i] - int(List[i])
        if min > t:
            min = t
    
    return min    

AList = CreateRandomList()
print(AList)

print(f'Max = {GetMaxFractionalPart(AList):.3f}, Min = {GetMinFractionalPart(AList):.3f}')
print('Max - Min = {:.3f}'.format(GetMaxFractionalPart(AList)-GetMinFractionalPart(AList)))