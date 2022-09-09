import time

t = time.time_ns() // 1000

def GetRandomNumber(a, b):
    global t 
    t = (1664525 * t + 1013904223) % (2 ** 32)
    return a + t % (b - a)
    
list_len = 25
list = [GetRandomNumber(1, 50) for i in range(list_len)]
print('Unsorted sequence of random numbers:')
print(list)

list.sort()
print('Sorted sequence of random numbers:')
print(list) 