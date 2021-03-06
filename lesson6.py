# t1 = (1, 2, 3)
# l1 = [1, 2, 3]
# t1 = 1, 2, 3
# t1 = tuple((1, 2, 3))
# t1 = ()
# t1 = (1, 2, 3)
# t2 = [1, 2, 3]

# print(t1.__sizeof__())
# print(t2.__sizeof__())

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
#
#
# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print('No')
#
# print(type(t1))
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(f"'{i}'", end=' ')


# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
# t1[2][2] = 'new'
# t1[4].append('hello')
# print(t1, id(t1))

# t1 = (1, 2, 3)
# x, y, z = t1
#
# print(x, y, z)
# x = 1
# y = 2
#
# print(x, y)
# x, y = y, x
# print(x, y)

# words = ['мадам', 'топот', 'test', 'madam', 'word']
# # my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# my_str1 = ['А роза упала на лапу Азора']
# l = list(my_str1)
#
# p = l.index('р')
#
# del(l[p])

# for i in my_str1:
#     if 'р' in i:
#         del[i]
#     else:
#         l += i[::-1]

# print(l)
# l = ' Hello world'  # -------------------------
# l2 = l.replace(' ', '')
# print(l2)  # --------------------------

# words = ['мадам', 'топот', 'test', 'madam', 'word']
# l1 = []
# no_palindromes = []
#
# palindromes = [word for word in words if word == word[::-1]]
# print(l1)
# for word in words:
#
#     # print(l1)
#     if word == word[::-1]:
#         palindromes.append(word)
#     else:
#         no_palindromes.append(word)
# print(palindromes)
# print(no_palindromes)

# words = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# palindromes = []
# no_palindromes = []
#
# for word in words:
#     if ' ' in word:
#         s1 = word.replace(' ', '').lower()
#         if s1 == s1[::-1]:
#             palindromes.append(word)
#         else:
#             no_palindromes.append(word)
#     else:
#         print('')
# print(palindromes)
# print(no_palindromes)


# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = set('hello')
# s3 = {i for i in range(1, 11)}
# s4 = set()
# print(s)
# print(s2)
# print(s3)
# print(s4)
#
# nums = [1, 2, 2, 2, 3, 3, 9]
#
# nums2 = set(nums)
# print(nums2)

# a = set('abracadabra')
# b = set('alacazam')
#
# c = b - a
# d = a | b
# f = a ^ b
#
# print(a, b, c, d, f, sep='\n')


# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#
# for i in s:
#     print(i)

# d = {'fuck': 1, }
# product1 = {'title': 'Sony', 'price': 100}
# product2 = dict(title='IPhone', price=110)
#
# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['katy@gmail.com', 'Katy'],
#     ['john@gmail.com', 'John'],
# ]
#
# d_users = dict(users)
# print(users)
# print(d_users)
#
# print(d)
# print(product1)
# print(product2)
#
# users_t = (
#     ('bob@gmail.com', 'Bob'),
#     ('katy@gmail.com', 'Katy'),
#     ('john@gmail.com', 'John'),
# )
#
# t_users = dict(users_t)
# print(users_t)
# print(t_users)


# product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
# print(product3)

# nums = {i: i + 1 for i in range(1, 10)}
# print(nums)

product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title='IPhone', price=110)

# print(product1['title'])
# print(product2.get('title'))
# print(nums[1])

# for key in product1:
#     print(f'{key}: {product1[key]}')
#
#
# for key, value in product1.items():
#     print(key, value)

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'IPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90},
    {'title': 'Xiaomi', 'price': 50},
    {'title': 'Honor', 'price': 70},
]

print(products)

for product in products:
    print(product['title'], product['price'])

print(products[::-1])