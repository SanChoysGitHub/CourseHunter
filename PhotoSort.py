import os
import time


path = 'C:/Users/User/Desktop/wall/anime-sunrise.jpg'
path_sys = 'C:/Users/User/Desktop/wall/'

p = 'C:/Users/User/Desktop/wall/M-09_Y-2020'
#
# r = os.replace(path, p)


for address, dirs, files in os.walk(path_sys):
    for file in files:

        path_file = (path_sys + file)  # Путь к файлу

        named_tuple = time.localtime(os.path.getmtime(path_file))  # Получить struct_time
        time_string = time.strftime("M-%m_Y-%Y", named_tuple)  # Вывод месяц/год

        if time_string in (dir_1 for dir_1 in dirs):
            print(time_string, dirs)

            print('FileExistsError')
            os.replace(f"C:/Users/User/Desktop/wall/{file}", f'C:/Users/User/Desktop/wall/{time_string}/{file}')

            # try:
            #     dirs == time_string
            # except FileExistsError:
            #     print('FileExistsError')
            #     os.replace(f"C:/Users/User/Desktop/wall/{file}", f'C:/Users/User/Desktop/wall/{dirs}/{file}')
        elif dirs != time_string:
            # try:
            #     dirs != time_string
            # except FileNotFoundError:
            #     print("FileNotFoundError")
            #     os.mkdir(f'C:/Users/User/Desktop/wall/{time_string}')
            #     os.replace(f'C:/Users/User/Desktop/wall/{file}', f'C:/Users/User/Desktop/wall/{time_string}/{file}')
            try:
                create_f = os.mkdir(f'C:/Users/User/Desktop/wall/{time_string}')
            except FileExistsError:
                print('FileExistsError')
                os.replace(f"C:/Users/User/Desktop/wall/{file}", f'C:/Users/User/Desktop/wall/{time_string}/{file}')


            # for dir in dirs:
            #     print(dir)
            #     if time_string in dir:
            #         print(create_f)
            #         carry_over = os.replace(f'C:/Users/User/Desktop/wall/{file}', f'C:/Users/User/Desktop/wall/{dirs}/{file}')
        else:
            print('BLYAT')
