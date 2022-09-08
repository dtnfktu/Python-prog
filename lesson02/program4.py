import time

t = (time.time_ns() % 1000) % 256

def GetRandomNumber(a, b):
    #return time.time_ns()
    #return a + int((time.time() - int(time.time())) * (10 ** 10)) % (b - a)
    global t 
    t = a + ((1664525 * t + 1013904223) % (2 ** 32)) % (b - a)
    return t
    
#print(time.time_ns() ^ 1024)
list = [GetRandomNumber(0,100) for i in range(100)]
print('Unsorted sequence of random numbers:')
print(list)
list.sort()
print('Sorted sequence of random numbers:')
print(list)

# for i in range(100):
#     print(GetRandomNumber(1,100))
