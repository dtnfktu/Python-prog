import os
import random
from turtle import clear

def input_int(title  : str, default_value = None) :
    '''Вводим целое число'''
    str_title = title
    if default_value :
        str_title = str_title + ' [' + str(default_value) + ']'
    str_title = str_title + ' => '
    s = input(str_title)
    
    while not s.isdigit() :
        if (s == '') and (not default_value is None) :
            return default_value
        s = input(str_title)
        
    return int(s)

def priority_selection() :
    '''Жеребьёвка'''
    return random.randint(1, 2)

def human_step(player : str) :
    '''Очередной ход реального игрока. Возвращает количество взятых конфет на текущем шаге'''
    max_candies = candy_in_one_turn if candy_in_one_turn < candies else candies
    cnds = input_int(player + ', enter Your choice (1..' + str(max_candies) + ')')
    while not (cnds >= 1 and cnds <= max_candies) :
        cnds = input_int(player + ', enter Your choice (1..' + str(max_candies) + ')')
    return cnds

def machine_step(mode : int, player : str) :
    '''Очередной ход ИИ'''
    # для режима 1 - Stupid
    
    if mode == 1 :
        choice_num = random.randint(1, (candy_in_one_turn if candy_in_one_turn < candies else candies))
    else :
        if candies <= candy_in_one_turn :
            choice_num = candy_in_one_turn
        else :
            choice_num = candy_in_one_turn + 1 - minus
    print(player + ' choice => ' + str(choice_num))    
    
    return choice_num


# Задаём режим игры: 1 - два игрока, 2 - игрок против бота
game_mode = input_int('Select game mode (1 - Human vs Human, 2 - Human vs AI)', 2)
player1 = 'Player 1'
player2 = 'Player 2'

# Задаём уровень бота: 1 - без логики, 2 - интеллектуальный
if game_mode == 2 :
    player2 = 'Compukter'
    ai_mode = input_int('Select AI mode : 1 - Stupid, 2 - God', 1)

# Задаём начальное количество конфет, по умолчанию 2021
candies = input_int('Enter the initial number of candies', 2021)

# Максимальное количество конфет за один ход, по умолчанию 28
candy_in_one_turn = input_int('Enter max number of candies in one turn', 28)

# Выбираем кто начинает
current_player = priority_selection()
print('First step Player' + str(current_player))
print('------------------------------------------------------')
print('Let the Game begin!')
minus = 0
while candies > 0 :
    if current_player == 1 :
        minus = human_step(player1)
        candies -= minus
        current_player = 2
    else :
        if game_mode == 1 :
            minus = human_step(player2)
            candies -= minus
        else :
            minus = machine_step(ai_mode, player2)
            candies -= minus
        current_player = 1
    print(f'{candies} left')

print('Game over...')
print((player1 if current_player == 2 else player2) + ' win')