# Считываем текст из файла.
with open('testin.txt','r') as f :
    txt = f.read()
txt = txt.replace('\n',' ')

answer = list(filter(lambda x: not 'абв' in x, txt.split(' ')))

with open('testout.txt','w') as f :
    f.write(' '.join(answer))
print('Your answer in textout.txt')