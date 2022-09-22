from itertools import count
import random


def clear_game_field() :
    '''Возвращает пустое игровое поле 3х3'''
    return [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def draw_field() :
    '''Выводит текущее игровое поле в консоль'''
    for i in (0,1,2) :
        for j in (0,1,2) :
            print(' ' + game_field[i][j] + ' ', end= '')
            print('|' if j < 2 else '', end='')
        print('\n------------' if i < 2 else '')

def set_field(row, col, tictactoe) :
    '''Вносит Х или 0 в заданную ячейку'''
    if  game_field[row][col] == ' ' :
        game_field[row][col] = tictactoe
        return True
    else :
        print('The cell is occupied, select another one')
        return False

def select_cell() :
    '''Выбираем координаты ячейки, которую следует заполнить'''
    row = int(input('Select row (1..3) : ')) - 1
    col = int(input('Select col (1..3) : ')) - 1
    return [row, col]

def select_cell_bot() :
    '''Автоматический выбор пустой ячейки'''
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while game_field[row][col] != ' ' :
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return [row, col]

def game_over() :
    '''Проверка на конец игры'''
    # проверка на заполнение игрового поля
    if not ' ' in [x for l in game_field for x in l] :
        return True
    # проверка по строкам
    for rows in game_field :
        for sign in signs :
            if rows.count(sign) == 3 :
                return True
    # проверка по столбцам
    for sign in signs :
        for j in (0,1,2) :
            if [game_field[i][j] for i in (0,1,2)].count(sign) == 3 :
                return True
    # проверка по диагоналям
    for sign in signs :
        if sign == game_field[1][1] == game_field[2][2] == game_field[0][0] :
            return True
        if sign == game_field[0][2] == game_field[2][2] == game_field[2][0] :
            return True
    return False
    
def sign_selection() :
    '''Случайным образом определяется чьи крестики, чьи нолики'''
    if random.randint(0, 2) == 0 :
        print('You play by Zeros now')
        return ['0', 'X']
    else :
        print('You play by Crosses now')
        return ['X', '0']

# Инициализация игры
player2 = int(input('Chose player 2 (1 - human, 2 - computer) :'))
game_field = clear_game_field()
signs = sign_selection()
current_player = 1 if signs[0] == 'X' else 2
draw_field()

# Сама игра
while not game_over() :
    print('It''s a move now by ' + signs[current_player - 1])
    if current_player == 1 :
        current_cell = select_cell() 
        while not set_field(current_cell[0], current_cell[1], signs[current_player - 1]) :
            current_cell = select_cell() 
        current_player = 2
    else :
        if player2 == 1 :
            current_cell = select_cell() 
            while not set_field(current_cell[0], current_cell[1], signs[current_player - 1]) :
                current_cell = select_cell() 
        else :
            current_cell = select_cell_bot()
            set_field(current_cell[0], current_cell[1], signs[current_player - 1])
        current_player = 1
    draw_field()

print('Game over')
if ' ' in [x for l in game_field for x in l] :
    print('Player ' + str(1 if current_player == 2 else 1) + ' win')
else :
    print('There are no winners')