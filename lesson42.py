# def hello():
#     return 'OMG MAN, are you crazy!'
#
#
# def super_func(func):
#     print('Hello. Im func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'OMG MAN, are you crazy!!!'
#
#
# test = hello
#
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code After')
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello, i am func "func_test"')


# test = my_decorator(func_test)
#
# test()

# func_test()

# def make_title(fn):
#     def wrapped():
#         title = fn()
#         title = title.capitalize()
#         title = title.replace(',', '')
#         return title
#     return wrapped
#
#
# @make_title
# def string():
#     return 'aFAfAF,WRfafww'
#
#
# print(string())
#
# def get_square(num):
#     return num ** 2
#
#
# print(get_square(5))

# get_square = lambda num: num ** 2
# print(get_square(10))

# print((lambda num: num ** 2)(7))

l = [1, 2, 3]
l2 = [3, 6, 9]


# def get_double(l):
#     return [i * 2 for i in l]

def get_double(l):
    return list(map(lambda x: x * 2, l))


print(get_double(l2))



