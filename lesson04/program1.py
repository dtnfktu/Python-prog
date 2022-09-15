def input_int() :
    '''Ввод целого положительного числа'''
    st = input('Enter integer positive number : ')
    while not st.isdigit() or st == '0' :
        st = input('Enter integer positive number : ')
    return int(st)

def prime_numbers(lim):
    ''' Возвращает список простых чисел от 2 до lim включительно'''
    nums = [i for i in range(3, lim + 1, 2)]
 
    indexlist = []
    index = 0
    while (index < len(nums)):

        for i in range(index + 1, len(nums)):
            if nums[i] % nums[index] == 0:
                indexlist.append(i)

        index += 1

    indexlist.sort(reverse=True)
    
    index = 0
    while index < len(indexlist):
        sindex = index + 1
        while sindex < len(indexlist) and indexlist[index] == indexlist[sindex]:
            indexlist.pop(sindex)
        index += 1

    for i in range(len(indexlist)):
        nums.pop(indexlist[i])

    return [2] + nums

def list_of_multipliers(n):
    '''Возвращает список простых множителей числа n'''
    lst = prime_numbers(n // 2)

    res_list = []
    for i in lst :
        if n % i == 0:
            res_list.append(i)

    return res_list

n = input_int()
print('Prime factors of a number : ', list_of_multipliers(n))