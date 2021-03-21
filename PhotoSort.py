import os
import time


path = 'C:/Users/User/Desktop/wall/anime-sunrise.jpg'
path_sys = 'C:/Users/User/Desktop/wall'

p = 'C:/Users/User/Desktop/wall/M-09_Y-2020'


for address, dirs, files in os.walk(path_sys):
    for file in files:

        path_file = os.path.join(path_sys, file)  # Путь к файлу

        named_tuple = time.localtime(os.path.getmtime(path_file))  # Получить struct_time
        time_string = time.strftime("M-%m_Y-%Y", named_tuple)  # Вывод месяц/год
        date_folder = os.path.join(path_sys, time_string)
        if not os.path.exists(date_folder):
            os.mkdir(date_folder)

        os.replace(path_file, os.path.join(date_folder, file))



