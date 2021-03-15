# def get_sum(a, b):
#     """
#     Возращает сумму аргументов: a and b.
#
#     :param a: Первый операнд
#     :type a: int
#     :param b: Второй операнд
#     :type b: int
#     :return: Return type int
#     """
#     return a + b


# print(get_sum(1, 2))

# a = 5


# def f():
#     a = 10
#     a += 1
#     print(a)
#
#
# f()

# def f():
#     global a
#     a += 1
#     print(a)
#
#
# print(a)
# f()
# print(a)
# /////////////////////////////////////////////
# l = [1, 2, 3]
#
#
# def f(l):
#     return [i * 2 for i in l]
#
#
# print(f(l))
# /////////////////////////////////////////
# l = [1, '2', 3,]
#
# def f2(l):
#     def get_mult(x):
#         return x * 2
#     return [get_mult(i) for i in l]
#
# print(f2(l))
# # _______________________________________
#
#
# def f3(l):
#     def get_mult(x):
#         if isinstance(x, int):
#             return x * 2
#     return [get_mult(i) for i in l if get_mult(i)]
# #
# #
# print(f3(l))
#
#
#
# def f4(l):
#     def get_mult(x):
#             return x * 2
#     return list(map(get_mult, l))
#
# print(f4(l))
# ---------------------------------------------------

arr = ['even', 4, 'even', 7, "even", 55, "even", 6, "even", 10, "odd",  3,  'even']

# -***********************************
# def odd_ball(arr):
#     s = arr.index('odd')
#     for x in arr:
#         if x == s:
#             return (x == s)
#         elif x != s:
#             s1 = x != s
#             continue
# -***********************************

# arr = ['even', 4, 'even', 7, "even", 55, "even", 6, "even", 10, "odd", 3,  'even']
#
#
# def odd_ball(arr):
#     s = arr.index('odd')


# print(odd_ball(arr))
# # print(odd_ball(['even', 4, 'even', 7, "even", 55, "even", 6, "even", 10,  3, "odd", 'even']))
# print(odd_ball([1, 233, 3, 'odd']))


# print(arr.index('odd'))

# s1 = 'Hello world'
#
# if ' ' in s1:
#     print("ssss")
# else:
#     print("dafdas1w1d1dw")

# ************************************************
# def add_ball(arr):
#     return arr.index('odd') in arr
#
# print(add_ball(arr))
# ************************************************

#
# n = list(range(1, 6))

# |||||||||||||||||||||||||||||||||||||||||||||||||||
# def find_sum(n):
#     # res = 0
#     # for i in range(n + 1):
#     #     if i % 3 == 0 or i % 5 == 0:
#     #         res += i
#     # return res
#     return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)
#
#
#
# print(find_sum(100))
#
# |||||||||||||||||||||||||||||||||||||||||||||||||||

# names = ["Ryan", "Kieran", "Mark", 'John', 'David', "Paul"]
# names1 = []
#
# #
# def len_names(names):
#     return [x for x in names if len(x) == 4]
#     # for x in names:
#     #     if len(x) == 4:
#     #         names1.append(x)
#     # return
#
#
#
#
# print(len_names(names))
# print(names1)



















