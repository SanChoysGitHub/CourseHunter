# f = open('file.txt', encoding='utf-8')

# text = f.read(2)
# text2 = f.read(8)
# print(f.encoding)

# text = f.read()
# f.close()
# print(text)


# print(text2)
# ***************************************
# lines = ['Новая строка 1', 'Новая строка 2']
#
# f = open('file.txt', 'a', encoding='utf-8')
# # for i in lines:
# #     f.write(i + '\n')
# f.writelines(f'{i}\n' for i in lines)
#
# f.close()
# *****************************************
# f = open('file.txt', 'r', encoding='utf-8')
#
# print(f.readline())
# ****************************************
lines = ['Hello ', 'mazafaka']

f = open('file1.txt', 'w', encoding='utf-8')

f.writelines(f'{i}' for i in lines)


