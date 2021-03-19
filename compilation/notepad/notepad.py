from tkinter import *
from tkinter import messagebox, filedialog


# f_menu = Frame(root, bg='#1F252A', height=40)
# f_menu.pack(fill=X)


# l_menu = Label(f_menu, text='Menu', bg='#2B3239', fg='#C6DEC1', font='Arial 10')
# l_menu.place(x=10, y=10)
#
#
# def add_str():
#     t.insert(END, 'Hello!')
#
#
# def del_str():
#     t.delete('2.6', '2.12')
#     # t.delete('1.0', END)
#
#
# def get_str():
#     print(t.get('1.0', END))
#
#
# btn_add = Button(root, text='Add', command=add_str).place(x=50, y=10)
# btn_def = Button(root, text='Delete', command=del_str).place(x=90, y=10)
# btn_get = Button(root, text='Get', command=get_str).place(x=140, y=10)

# main_menu.add_command(label='File')
# main_menu.add_command(label='About')

root = Tk()
root.geometry('300x400+500+400')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)


def about_program():  # Окно которое показует информацию приложения
    messagebox.showinfo(title='About notepad', message='Program Notepad Version 0.0.1')


def notepad_quit():  # Окно которое спрашивает, точно ли хотит выйти?
    answer = messagebox.askyesno(title='Exit', message='Quit Program?')

    if answer:  # True == Exit
        root.destroy()


def open_file():
    # Диалогое окно с предложением выбора файла(документа)
    file_path = filedialog.askopenfilename(
        title='Select file', filetypes=(
            ('Text document(*.txt)', '*.txt'),
            ('All files', '*.*')
        ),
    )
    if file_path:
        t.delete('1.0', END)  # Удаление текста в блокноте
        t.insert('1.0', open(file_path, encoding='utf-8').read())  # Добавление текста из файла в блокнот


def save_file():
    # Окно с сохранением файла
    file_path = filedialog.asksaveasfilename(
        title='Saved',
        filetypes=(
            ('Text document(*.txt)', '*.txt'),
            ('All files', '*.*'))
    )
    f = open(file_path, 'w', encoding='utf-8')  # Открытие/Создание файла на запись
    text = t.get('1.0', END)  # Получение всего написаного текста
    f.write(text)  # Запись текста
    f.close()  # Закрытие файла


# Словарь с темами
theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#C6DEC1", 'cursor': "#EDA756", "select_bg": '#4E5A65'
    },
    'light': {
        'text_bg': '#fff', 'text_fg': '#000', 'cursor': '#8000FF', 'select_bg': '#777'
    }
}


def change_theme(theme):  # Смена тем между темной и светлой
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


main_menu = Menu(root)
root.config(menu=main_menu)

# File
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=notepad_quit)

# Theme
theme_menu = Menu(main_menu, tearoff=0)

main_menu.add_cascade(label='Other', menu=theme_menu)
theme_menu.add_command(label='Wow')

theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu.add_cascade(label='Registration', menu=theme_menu_sub)
theme_menu_sub.add_command(label="Light Theme", command=lambda: change_theme('light'))
theme_menu_sub.add_command(label="Dark Theme", command=lambda: change_theme('dark'))

theme_menu.add_command(label='About program', command=about_program)


# t = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors["dark"]['text_fg'],
#          padx=5, pady=5,
#          wrap=WORD,
#          insertbackground=theme_colors['dark']['cursor'], selectbackground=theme_colors['dark']["select_bg"],
#          width=10, spacing3=10
#          )
# t.pack(fill=BOTH, expand=1, side=LEFT)

# Поле текста
t = Text(f_text, bg=theme_colors['light']['text_bg'], fg=theme_colors["light"]['text_fg'],
         padx=5, pady=5,
         wrap=WORD,
         insertbackground=theme_colors['light']['cursor'], selectbackground=theme_colors['light']["select_bg"],
         width=10, spacing3=10, font=('Courier New', 12)
         )
t.pack(fill=BOTH, expand=1, side=LEFT)

# Виджет Scrollbar
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)


root.mainloop()






