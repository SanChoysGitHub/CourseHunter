# import random
#
#
# def game():
#     res = 1
#     random_num = random.randint(1, 30)
#     while True:
#         your_num = int(input('Enter the number: '))
#         if your_num == random_num:
#             print(f'Ну ты крутой! Отгадал число за {res} попыток!')
#             again1 = input('Хочешь еще раз сыграть(y/n)?:')
#             if 'y' == again1:
#                 game()
#             else:
#                 print('Как хочешь...')
#                 break
#         elif your_num > random_num:
#             print('Меньше')
#             res += 1
#         elif your_num < random_num:
#             print('Больше')
#             res += 1
#
#
# start_game = input('Хочешь сыграть в игру(y/n)?:')
#
# if start_game == 'y':
#     game()
# else:
#     print('Тююю, ну как хочешь...')


import random  # Модуль


def game():  # Игра
    res = 1  # Хранение кол-во попыток
    random_num = random.randint(1, 2)  # Генерация рандомного числа в диапазоне
    while True:
        your_num = int(input('Enter the number: '))  # Ввод числа пользователем
        if your_num == random_num:  # Сравнение числа ввода и генерируемого
            print(f'Ну ты крутой! Отгадал число с {res} попытки!')  # Вывод выигрыша, Кол-во попыток
            again1 = input('Хочешь еще раз сыграть(y/n)?:')  # Предложение сыграть снова
            if 'y' == again1:
                game()  # Запуск игры при соглашение пользователя повторить
            else:
                print('Как хочешь...')
                break  # Конец игры
        elif your_num > random_num:  # Сравнение числа ввода и генерируемого
            print('Меньше')
            res += 1  # Прибавление к переменной кол-во попыток при не правильном ответе пользователем
        elif your_num < random_num:  # Сравнение числа ввода и генерируемого
            print('Больше')
            res += 1  # Прибавление к переменной кол-во попыток при не правильном ответе пользователем


start_game = input('Хочешь сыграть в игру(y/n)?:')  # Соглашение игрока начать или закончить игру

if start_game == 'y':
    game()  # Первый запуск игры
else:  # Конец игры
    print('Тююю, ну как хочешь...')

# import libs
# print(__name__)
# # print(libs.get_count('hello', 'l'))
# # print(libs.get_len('hello'))
#
# f = libs.get_count
#
#
# print(f('hello', 'l'))
#
#
# def get_sum(a, b):
#     return a + b
#
#
# d = get_sum
#
# print(d(1, 2))



























































































































































































































