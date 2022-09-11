import random

def CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25): 
    ''' Метод создания списка заданной длины (по умолчанию ListLen = 10),
    заполненного случайными целыми числами в дапазоне от MinNum (по умолчания = 0)
    до MaxNum (по умолчанию = 25) включительно
    '''
    NewList = [random.randint(MinNum, MaxNum) for i in range(ListLen)]
    return NewList

def CountMultiplicationOfPairNumbers(AList):
    '''Подосчёт произведений пар списка AList
    '''
    res = []
    LeftIndex = 0
    RightIndex = len(AList) - 1
    while LeftIndex <= RightIndex:
        res.append(AList[LeftIndex] * AList[RightIndex])
        LeftIndex += 1
        RightIndex -= 1
    return res

List = CreateRandomList(ListLen = random.randint(1, 10))
print('Исходный список :')
print(List)

print('Произведения пар элементов исходного списка :')
print(CountMultiplicationOfPairNumbers(List))