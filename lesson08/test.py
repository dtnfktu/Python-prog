from base64 import encode
from imp import reload
import json
import datetime

# with open('test.json','r') as f :
#     data = json.loads('test.json')
# #print(data)
# data = {'contact1':{
#                     'fname' : 'Ivanov',
#                     'sname' : 'Petro' ,
#                     'phnum' : '89898',
#                     'other' : 'okay'
#                 },
#         'contact2': {
#                     'fname' : 'Petrov',
#                     'sname' : 'Ivan' ,
#                     'phnum' : '56456',
#                     'other' : 'okay-2'
#                 }                
#         }
# print(data)
# print(data.keys())
            
# with open('test.json','w') as f :
#     json.dump(data,f)

# with open('test.json','r') as f :
#     s = json.load(f)
# d1 = s.get('contact1')
# print(d1)
# print(list(d1.values()))
#print(s.get('contact2'))

# now = str(datetime.datetime.now())
# now = now[:now.find('.')]
# now = now.replace('-','').replace(':','').replace(' ','_')
# print(now)

import sys
import os
os.system('echo off')
os.system('chcp 65001')
print('Слово : ',end ='')
input()
os.system('chcp 1251')
st = input()
print(st)
os.system('chcp 65001')
