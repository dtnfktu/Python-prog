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

def inputdata(title : str, typ) :
    '''Ввод данных заданного типа'''
    while True :
        s = input(title)
        if type(s) == typ :
            break
    return typ(s)

def human_step(candiesnow : int, maxcands : int) :
    '''Очередной ход реального игрока. Возвращает количество взятых конфет на текущем шаге'''
    while True :
        hcandies = input_int('How much candies You take now? : ') 
        if hcandies in range(1, (maxcands if maxcands < candiesnow else candiesnow)+1) :
            break
    return hcandies

def machine_step(game : list) :
    '''Очередной ход ИИ'''
    if game[0] == 1 :
        choice_num = random.randint(1, (game[4] if game[4] < game[3] else game[3]))
    else :
        choice_num = game[3] if game[3] <= game[4] else game[4] - game[5] + 1
    return choice_num

def initgame(options : list) :
    '''Инициализация игры - ввод основных настроек'''
    #options[0] =  inputdata('Enter bot level (1 - Rookie, 2 - God)', int)
    options[0] = input_int('Enter level')
    options[1] =  inputdata('Enter Your name :', str)
    options[2] = player2 = 'Valera' if options[0] == 1 else 'Gennadiy Albertovich'
   
def nextplayer(cp : int) :
    '''Определяет какой игрок делатет очередной ход'''
    return 1 if cp == 2 else 2

def game() :
    '''Сама игра'''
    opt = [1, 'player1', 'player2', 150, 14, 14]
    initgame(opt)
        
    print(opt)

    candies = opt[3]
    oneturn = opt[4]
    curplayer = priority_selection()
    print('First step by ' + opt[curplayer])
    print('Begin')

    while candies > 0 :
        if curplayer == 1 :
            opt[5] = human_step(opt[3], opt[4])
            candies -= opt[5]
            print('Player ' + opt[curplayer] + ' take ' + str(opt[5]) + ' candies. ' + str(candies) + ' candies left.')
        else :
            opt[5] = machine_step(opt)
            candies -= opt[5]
            print('Player ' + opt[curplayer] + ' take ' + str(opt[5]) + ' candies. ' + str(candies) + ' candies left.')
        curplayer = nextplayer(curplayer)
    print('Game over')
    curplayer = nextplayer(curplayer)
    print(opt[curplayer] + ' win')


















# # Задаём режим игры: 1 - два игрока, 2 - игрок против бота
# game_mode = input_int('Select game mode (1 - Human vs Human, 2 - Human vs AI)', 2)
# player1 = 'Player 1'
# player2 = 'Player 2'

# # Задаём уровень бота: 1 - без логики, 2 - интеллектуальный
# if game_mode == 2 :
#     player2 = 'Compukter'
#     ai_mode = input_int('Select AI mode : 1 - Stupid, 2 - God', 1)

# # Задаём начальное количество конфет, по умолчанию 2021
# candies = input_int('Enter the initial number of candies', 2021)

# # Максимальное количество конфет за один ход, по умолчанию 28
# candy_in_one_turn = input_int('Enter max number of candies in one turn', 28)

# # Выбираем кто начинает
# current_player = priority_selection()
# print('First step Player' + str(current_player))
# print('------------------------------------------------------')
# print('Let the Game begin!')
# minus = 0
# while candies > 0 :
#     if current_player == 1 :
#         minus = human_step(player1)
#         candies -= minus
#         current_player = 2
#     else :
#         if game_mode == 1 :
#             minus = human_step(player2)
#             candies -= minus
#         else :
#             minus = machine_step(ai_mode, player2)
#             candies -= minus
#         current_player = 1
#     print(f'{candies} left')

# print('Game over...')
# print((player1 if current_player == 2 else player2) + ' win')