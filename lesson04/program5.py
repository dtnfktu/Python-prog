def read_from_file(file_name : str) :
    '''Считывает текст из заданного файла и возвращает его типом str'''
    with open(file_name, 'r') as textfile :
        txt = textfile.read()

    return txt

def write_into_file(filename : str, txt : str) :
    '''Записывает текст в файл с заданным имененм'''
    with open(filename,'w') as outfile :
        outfile.write(txt)

def encode_rle(txt : str) :
    '''Сжимает текст с применением RLE алгоритма'''
    rle = []
    current_position = 1
    current_symbol = txt[0]
    current_count = 1

    while current_position < len(txt) :
        if txt[current_position] != current_symbol :
            if current_count != 1 :
                rle.append(str(current_count) + current_symbol)
            else :
                rle.append(current_symbol)
            current_symbol = txt[current_position]
            current_count = 1
        else :
            current_count += 1
        
        current_position += 1

    if current_count != 1 :
        rle.append(str(current_count))
    rle.append(current_symbol)

    return '|'.join(rle)

def decode_rle(txt : str) :
    '''Восстанавливает текст, сжатый по RLE'''
    symbols = txt.split('|')
    dectxt = ''

    for element in symbols :
        end_str = len(element) - 1
        curr_sym = element[end_str]                 # определяем текущий символ
        if end_str == 0 :
            curr_count = 1                          # определяем
        else :                                      # количество 
            curr_count = int(element[:end_str])     # его повторений

        for i in range(0, curr_count) :
            dectxt += curr_sym
    return dectxt

print('Open source file : ')
input_txt = read_from_file('opentext.txt')
print(input_txt)
print('Encrypt RLE :')
output_txt = encode_rle(input_txt)
print(output_txt)
write_into_file('closedtext.txt', output_txt)

print('RLE file : ')
input_txt = read_from_file('closedtext.txt')
print(input_txt)
print('Decoded RLE :')
output_txt = decode_rle(input_txt)
print(output_txt)