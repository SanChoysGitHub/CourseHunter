from datetime import date, datetime, timedelta
import locale

# date
# today = date.today()
# print(today)  # 2019-07-10
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())

# datetime
# now = datetime.now()
# now2 = datetime.now()

# print(now)

# ****************************************
# locale.setlocale(locale.LC_ALL, 'ru-RU')
#
# now = datetime.now()
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime("%c"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))
# ________________________________________________


now = datetime.today()
d1 = now + timedelta(days=1, hours=2, minutes=10)

print(now.strftime('%c'))
print(d1.strftime('%c'))













































