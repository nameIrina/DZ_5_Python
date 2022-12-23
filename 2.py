#Д/3 5
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'абв'
# my_str = input("Введите текст пробел: ") 
# no_text = " "
# for char in my_str:
#    if char not in text:
#        no_text = no_text + char
# print(f'Результат:{no_text}')

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# a) Добавьте игру против бота
# from random import randint
# def input_dat(name):
#     i = int(input(f"{name}, возьмете конфету от 1 до 28: "))
#     while i < 1 or i > 28:
#         i = int(input(f"{name}, введите корректное количество конфет: "))
#     return i
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# player1 = input("Введите имя 1 игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0 
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1,29)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# b) Подумайте как наделить бота ""интеллектом""
# from random import randint
# def input_dat(name):
#     i = int(input(f"{name}, возьмете конфету от 1 до 28: "))
#     while i < 1 or i > 28:
#         i = int(input(f"{name}, введите корректное количество конфет: "))
#     return i
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# def bot_calc(value):
#     k = randint(1, 29)
#     while value-k <= 28 and value > 29:
#         k = randint(1, 29)
#     return k
# player1 = input("Введите имя 1 игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0 
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1, 10))
# def design_board(board):
#     print('-' * 12)
#     for i in range(3):
#         print('|', board[0 + i * 3],'|', board[1 + i * 3], '|', board[2 + i * 3], '|')
#         print('-' * 12)
# def choice(tic_tac_toe):
#     valid = False
#     while not valid:
#         player_index = input(f'Xод {tic_tac_toe}, выберите ячейку:')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Что то не то нажали')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index - 1] = tic_tac_toe
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Попробуй еще раз ')
# def victory_check(board):
#     victory = ((0, 1, 2) , (3 ,4, 5) , (6, 7, 8),
#                (0, 3, 6) , (1, 4, 7) , (2, 5, 8),
#                (0, 4, 8) , (2, 4, 6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False
# def game(board):
#     counter = 0
#     vic = False
#     while not vic:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('O')
#         counter += 1
#         if counter > 4:
#             ttt_win = victory_check(board)
#             if ttt_win:
#                 print(ttt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('text_for_RLE.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('text_for_RLE.txt', 'r') as file:
#     my_text = file.readline()
#     text_compression = my_text.split()
#     print(my_text)

# def coding(txt):
#     count = 1
#     result = ' '
#     for i in range(len(txt) -1):
#         if txt[i] == txt[i + 1]:
#             count += 1
#         else:
#             result = result + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt) -2] != txt[ -1]):
#         result = result + str(count) + txt[ -1]
#     return result
# def decoding(txt):
#     number = ' '
#     result = ' '
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             result = result + txt[i] * int(number)
#             number = ' '
#     return result

# text_compression = coding(my_text)
# with open('text_compression_RLE.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compression}')
# print(text_compression)