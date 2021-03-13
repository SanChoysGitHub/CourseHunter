import re

# s = 'Это просто строка текста. А это ещё одна строка текста.'
# pattern = 'строка'
#
# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('NO MATCH')
#
# match = re.search(pattern, s)
# print(match)
# print(match.start())
# print(match.end())

# print(re.match(pattern, s))

# print(re.findall(pattern, s))

# print(re.split(r'\.', s))

s = '''This is string text.
Its one more string text.
Its one more with numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 45, 100
Its string with bla bla bla; ",", "@", "-"
a\\b\tc
test string'''

# pattern = r'\w+'
# pattern = r'\d '

# pattern = r'\w+'

# s1 = 'mail@mail.com'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

# mail@mail.com


def validate_email(email):
    return re.match(r'^.+@\w+\.[a-z]{2,6}$', email, re.IGNORECASE)


print(validate_email('mail@mail.com'))
print(validate_email('ivanov@bank'))
print(validate_email('mail@google.com.ua'))









