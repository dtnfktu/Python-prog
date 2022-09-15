def encrypt_text(txt : str, key : int) :
    '''Шифрует текст txt со сдвигом на key позиций'''
    text_out = ''
    for i in range(0, len(txt)) :
        text_out += chr(ord(txt[i]) + key)
    return text_out

def write_into_file(file_path : str, txt : str) :
    '''Записывает текст в файл'''
    with open(file_path, 'w') as file :
        file.write(txt)

def decrypt_text_from_file(filename : str) :
    sk = input('Enter key : ')
    while not sk.isdigit() :
        sk = input('Enter key')
    key = int(sk)

    with open(filename,'r') as sourcefile :
        txt = sourcefile.read()

    return encrypt_text(txt, -key)


ttext = input('Enter text : ')
enc_text = encrypt_text(ttext, 5)
write_into_file('caesar.txt', enc_text)
print(decrypt_text_from_file('caesar.txt'))