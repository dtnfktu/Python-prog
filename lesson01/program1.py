s = ''                                                      # проверка корректности
while (not s.isdigit()):                                    # вводимого значения -
    s = input('Введите день недели (число от 1 до 7) : ')   # принимается только целое неотрицательное число

week_day = int(s)

if week_day > 7:
    week_day %= 7

if week_day == 0:
    week_day = 7

print('Выходной день [', week_day, '] - ', end='')
if week_day in (6, 7):
    print('да')
else:
    print('нет')