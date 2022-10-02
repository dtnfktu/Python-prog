import database as db
import dbfiles as fl
import menu
import os

fl.logfile(-1)
if os.path.exists('phonebook.csv') :
    guide = fl.loadcsv('phonebook.csv')
    fl.logfile(-2)
else :
    guide = []
    fl.logfile(-3)
backup = False
while True :
    key = db.printtable(guide)
    fl.logfile(key)
    if key == 0 :
        break
    elif key == 1 :
        guide.append(menu.inputrec())
        backup = True
    elif key == 2 :
        guide.pop(menu.delrec() - 1)
        backup = True
    elif key == 3 :
        db.printtable(menu.searchrec(guide),False)
    elif key == 4 :
        menu.editrec(guide)
        backup = True
    elif key == 5 :
        menu.exportdata(guide)
    elif key == 6 :
        guide = menu.importdata()

# Создаём backup, если были изменения
if backup :
    fl.makebackup()
    fl.exportcsv('phonebook.csv', guide)
print('Работа завершена')