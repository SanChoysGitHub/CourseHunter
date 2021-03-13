#
# print(' |Guess the number game| ')
#
#
# print()
#
# num = 14
# attempt = 0
#
# while True:
#     enter_num = int(input('\nEnter the number(integer): '))
#     attempt += 1
#     if num == enter_num:
#         print('You win!' f"It took you {attempt} tries")
#         break
#     elif num < enter_num:
#         print('Your number is less, try again!')
#
#     elif num > enter_num:
#         print('Your number is greater, try again!')
#
# print('\tYou are winning son?)0)))')

# ////////////////////////////////////
# l = [1, 2, 3]
# l2 = []
#
#
# def multiplication(l):
#     for i in l:
#         i *= 2
#         l2.append(i)
#
#
# print(multiplication(l))
# print(l2)
# -------------------------------------

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# l = [3, 6, 12]
# l2 = []
#
#
# def num_sum():
#     res = 0
#     for i in l:
#         l1 = i ** 2
#         res += l1
#         l2.append(l1)
#
#     print(res)
#
#
# num_sum()
#
# print(l2)
# -------------------------------------------

# ///////////////////////////////////////////
# time = [3, 6.4, 11.2, 4]
# time_all = []
#
#
# def time_sum(time):
#     time_sum1 = 0
#     for i in time:
#         num = i // 2
#         time_sum1 += num
#         time_all.append(num)
#     print(time_all)
#     print(time_sum1)
#
#
# time_sum([2, 3, 4])
# ______________________________________________

# //////////////////////////////////////////////////
# def limbo(s):
#
#     if ' ' in s:
#         return s.upper()
#     else:
#         return s.lower()
#
#
#
# print(limbo('HEllo woRld'))
# print(limbo('Hello,woRld'))
# ----------------------------------------------------
#
# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2))

# def get_sum(*args):
#     return sum(args)
#
# print(get_sum(1, 2, 3,))


# def func(**kwargs):
#     print(kwargs)
#
#
# func(a=1, b=5, c=20)

# def f(a, x, *args, **kwargs):
#     print(a)
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# f(1, 2, 3,  b='test', c='hi')

# import random
#
#
# def game():
#     ctn = 1
#     random_num = random.randint(1, 10)
#     while True:
#         enter = int(input('Введите цифру: '))
#         if enter == random_num:
#             print(f'You win! Твое к-лво попыток {ctn}')
#             again = input('Хотите ли вы повторить игру(y/n): ')
#             if again == 'y':
#                 game()
#             else:
#                 print('Ну как хочешь друг...')
#                 break
#         elif enter <= random_num:
#             print('Больше')
#             ctn += 1
#
#         elif enter >= random_num:
#             print('Меньше')
#             ctn += 1
#
# print('Игра Угадай число')
#
# start_game = input('У нас есть игра, не проотив ли ты в нее сыграть(y/n)?: ')
# if start_game == 'y':
#     game()
# else:
#     print('Фуу, ну ты и зануда!!!')











































