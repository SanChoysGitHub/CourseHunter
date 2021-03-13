import os
from os.path import join, getsize

folder = []
for i in os.walk('folder'):
    folder.append(i)

print(folder)

for address, dirs, files in folder:
    for file in files:
        print(address + '\\' + file)

n = 1


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(997))



















