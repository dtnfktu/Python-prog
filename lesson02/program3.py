def ReverseNumber(num):
    ans = 0
    while num != 0:
        ans = ans * 10 + num % 10
        num //= 10
    return ans

str = input('Enter the integer number > 0 : ')
while not str.isdigit():
    str = input('Enter the integer number > 0 : ')
n = int(str)

while n != ReverseNumber(n):
    n += ReverseNumber(n)
    
print('Palindrome is :', n)