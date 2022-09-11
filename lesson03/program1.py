import random

def CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25): 
    ''' Метод создания списка заданной длины (по умолчанию ListLen = 10),
    заполненного случайными целыми числами в дапазоне от MinNum (по умолчания = 0)
    до MaxNum (по умолчанию = 25) включительно
    '''
    NewList = [random.randint(MinNum, MaxNum + 1) for i in range(ListLen)]
    return NewList

def GetSumInOddPosition(AList):
    '''Метод подсчета сумм элементов заданного списка AList,
    стоящих на нечётных позициях
    '''
    summa = 0
    range_len = len(AList)
    
    for i in range(1, range_len, 2):
        summa += AList[i]

    return summa


List = CreateRandomList()
print('Рассматриваемая последовательность целых чисел:')
print(List)

print('Сумма элементов на нечетных позициях =', GetSumInOddPosition(List))
