import json
import datetime
import os

def loadcsv(fname : str) :
    '''Загрузка справочника из csv-файла'''
    outlist = []
    with open(fname, 'r', encoding='UTF-8') as fcsv :
        tmpread = fcsv.read().splitlines()
        for line in tmpread :
            outlist.append(tuple(line.split(';')))
    return outlist

def exportcsv(fname: str, gd : list) :
    '''Записывет список в csv-файл'''
    with open(fname, 'w', encoding='UTF-8') as recfile :
        for element in gd :
            recfile.write(';'.join(element) + '\r')

def exportjson(fname : str, gd : list) :
    '''Записывет список в json-файл'''
    # Сначала формируем словарь
    phonebook = {}
    counter = 1
    for contact in gd :
        fcount = 1
        cortege = {}
        for field in contact :
            cortege['f'+str(fcount)] = field
            fcount += 1
             
        phonebook['rec'+str(counter)] = cortege
        counter += 1
    # Теперь записываем всё в json
    with open(fname,'w', encoding='UTF-8') as recfile :
        json.dump(phonebook, recfile)

def importjson(fname : str) :
    '''Импорт контактов из указанного JSON-файла'''
    lst = []
    # Читаем из json
    with open(fname,'r',encoding='UTF-8') as readfile :
        phonebook = json.load(readfile)
    tmplst = phonebook.values()
    
    for contact in tmplst :
        lst.append(tuple(contact.values()))

    return lst
   
def makebackup() :
    '''Создаёт backup файла phonebook.csv'''
    now = str(datetime.datetime.now())
    now = now[:now.find('.')]
    now = now.replace('-','').replace(':','').replace(' ','_')
    if os.path.exists('phonebook.csv') :
        bckp = loadcsv('phonebook.csv')
        exportcsv(now + '.backup',bckp)

def logfile(oper : int) :
    '''Запись действий в log'''
    now = datetime.datetime.now()
    with open('phonebook.log','a') as log :
        if oper == -1 :
            log.write(f'{now} - Справочник запущен\r')
        elif oper == -2 :
            log.write(f'{now} - Справочник по умолчанию загружен\r')
        elif oper == -3 :
            log.write(f'{now} - Справочник по умолчанию не загружен\r')
        elif oper == 1 :
            log.write(f'{now} - Добавлена запись\r')
        elif oper == 2 :
            log.write(f'{now} - Удалена запись\r')
        elif oper == 3 :
            log.write(f'{now} - Произведен поиск\r')
        elif oper == 4 :
            log.write(f'{now} - Редактирование записи\r')
        elif oper == 5 :
            log.write(f'{now} - Справочник экспортирован\r')
        elif oper == 6 :
            log.write(f'{now} - Справочник загружен\r')
        elif oper == 0 :
            log.write(f'{now} - Работа завершена\r')



            
    
