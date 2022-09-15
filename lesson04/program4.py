def encrypt_text(txt : str, key : int) :
    '''Шифрует текст txt со сдвигом на key позиций'''
    text_out = ''
    for i in range(0, len(txt)) :
        text_out += chr(ord(txt[i]) + key)
    return text_out

def decrypt_text(txt : str, key : int) :
    '''Дешифрует текст txt со сдвигом на key позиций'''
    text_out = ''
    for i in range(0, len(txt)) :
        text_out += chr(ord(txt[i]) - key)
    return text_out


ttext = input('Enter text : ')
print(ttext)
enc_text = encrypt_text(ttext, 5)
print('Encrypted text : ' + enc_text)
print('Decrypted text : ' + decrypt_text(enc_text, 5))