from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time


API_KEY = '067c5d096347c68757bbf5f40ade5169'
API_URL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=067c5d096347c68757bbf5f40ade5169'


# Словарь с темами
theme_colors = {
    "dark": {
        "label_main_bg": "#2F3136",
        "button_send_bg": "#808080",
        'entry_bg': "#37393d",
        "label_low_bg": '#37393d',
        'font_fg': '#fff',
        'frame_bg': '#494949',
    },
    'light': {
        'label_main_bg': '#FFFFFF',
        'button_send_bg': '#FFFAFA',
        'entry_bg': '#F5FFFA',
        'label_low_bg': '#F5FFFA',
        'font_fg': '#000',
        'frame_bg': '#FFE4E1',
    }
}

languages = {
    "en": {
        'btn_req': 'Weather request',
#         'result': {'m': f"Location: ,  ",
#                    "t": f"\nTemperature:  °C ",
#                    "h": f"\nHumidity: % ",
#                    "ws": f"\nWind speed:  м/c ",
#                    "w": f"\nWeather: ",
#                    "sr": f"\nSunrise: ",
#                    "sn": f"\nSunset: ",
#                    },
    },
    "ru": {
        'btn_req': 'Запрос погоды',
#         'result': {'m': f"Местоположение: ,  ",
#                    "t": f"\nТемпература:  °C ",
#                    "h": f"\nВлажность: % ",
#                    "ws": f"\nСкорость ветра:  м/c ",
#                    "w": f"\nПогодные условия: ",
#                    "sr": f"\nВосход: ",
#                    "sn": f"\nЗакат "
#                    },
    },
    'ua': {
        'btn_req': 'Запит погоди',

    }
}


def change_theme(theme):
    main_label['bg'] = theme_colors[theme]['label_main_bg']
    button_send['bg'] = theme_colors[theme]['button_send_bg']
    label_low['bg'] = theme_colors[theme]['label_low_bg']
    label_low['fg'] = theme_colors[theme]['font_fg']
    button_send['fg'] = theme_colors[theme]['font_fg']
    entry['bg'] = theme_colors[theme]['entry_bg']
    entry['fg'] = theme_colors[theme]['font_fg']
    lower_frame['bg'] = theme_colors[theme]['frame_bg']


def change_lang(lang):
    button_send['text'] = languages[lang]['btn_req']
    # label_low['text'] = languages[lang]['result']


def print_weather(weather):

    try:
        city = weather['city']['name']
        country = weather['city']['country']
        temp = weather['list'][0]['main']['temp']
        temp_min = weather['list'][0]['main']['temp_min']
        temp_max = weather['list'][0]['main']['temp_max']
        humidity = weather['list'][0]['main']['humidity']
        wind = weather['list'][0]['wind']['speed']
        desc = weather['list'][0]['weather'][0]['description']
        sunrise_ts = weather['city']['sunrise']
        sunset_ts = weather['city']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
        sunset = time.strftime('%H:%M:%S', sunset_struct_time)
        return f"Местоположение: {city}, {country}\n" \
                f"\nТемпература: {temp}°C" \
                f"\nМин: {temp_min} °C    Макс: {temp_max} °C\n" \
                f"\nВлажность: {humidity}%" \
                f"\nСкорость ветра: {wind} м/c\n" \
                f"\nПогодные условия: {desc}\n" \
                f"\nВосход: {sunrise}" \
                f"\nЗакат {sunset}"
    except:
        return "Ошибка получения данных..."


def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning("WARNING", " Введите запрос в формате city, country_code")
    else:
        params = {
            "appid": API_KEY,
            "q": entry.get(),
            "units": 'metric',
            'lang': 'ru'
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()

        label_low['text'] = print_weather(weather)



root = Tk()
root.geometry("500x400+700+300")
root.resizable(0, 0)

# Menu
main_menu = Menu(root)
root.config(menu=main_menu)

# Settings
settings_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Settings', menu=settings_menu)

# Theme
settings_menu_theme = Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label='Theme', menu=settings_menu_theme)
settings_menu_theme.add_command(label='Dark', command=lambda: change_theme('dark'))
settings_menu_theme.add_command(label='Light', command=lambda: change_theme('light'))

# Lang
settings_menu_lang = Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label='Lang', menu=settings_menu_lang)
settings_menu_lang.add_command(label='EN', command=lambda: change_lang('en'))
settings_menu_lang.add_command(label='UA', command=lambda: change_lang('ua'))
settings_menu_lang.add_command(label='RU', command=lambda: change_lang('ru'))


# s = ttk.Style()
# s.configure("", padding=5, font="Arial 11")

frame = Frame(root)
frame.pack(fill=BOTH)

main_label = Label(frame, background=theme_colors['light']['label_main_bg'])
main_label.pack(fill=BOTH, ipady=400)

top_frame = Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')


entry = Entry(top_frame,
              bg=theme_colors['light']['entry_bg'],
              fg=theme_colors['light']['font_fg']
              )
entry.place(relwidth=0.7, relheight=1)

button_send = Button(top_frame,
                     background=theme_colors['light']['button_send_bg'],
                     text=languages['en']['btn_req'],
                     fg=theme_colors['light']['font_fg'], font="Arial 11",
                     command=get_weather
                     )
button_send.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = Frame(root, bg=theme_colors['light']['frame_bg'])
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label_low = Label(
    lower_frame,
    bg=theme_colors['light']['label_low_bg'],
    fg=theme_colors['light']['font_fg'], font=('Arial 12 bold'), anchor=NW, justify=LEFT
)
label_low.pack(fill=BOTH, side=LEFT, ipadx=400, padx=2, pady=2)

entry.bind("<Return>", get_weather)


root.mainloop()


# city = weather['city']['name']
# country = weather['city']['country']
# temp = i['main']['temp']
# temp_min = i['main']['temp_min']
# temp_max = i['main']['temp_max']
# press = i['main']['pressure']
# humidity = i['main']['humidity']
# # wind = i['wind']['speed']
# desc = i['weather'][0]['description']
# # sunrise_ts = i['sys']['sunrise']
# # sunset_ts = i['sys']['sunset']
# # sunrise_struct_time = time.localtime(sunrise_ts)
# # sunset_struct_time = time.localtime(sunset_ts)
# # sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
# # sunset = time.strftime('%H:%M:%S', sunset_struct_time)


# f"Местоположение: {city}, {country} " \
# f"\nТемпература: {temp} °C " \
# f"\nВлажность: {humidity}% " \
# f"\nСкорость ветра: {wind} м/c " \
# f"\nПогодные условия: {desc}" \
# f"\nВосход: {sunrise}" \
# f"\nЗакат {sunset}"
