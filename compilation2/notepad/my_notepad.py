from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.geometry('400x400+500+400')  # Размер окна. Его спавн
root.title('NotePad')

# Словарь с цветами для разных тем
theme_colors = {
    'dark': {
        'bg': '#333333', 'fg': '#C8C8C8', 'cursor': '#D2691E', 'select_bg': '#F4A460',
    },
    'light': {
        'bg': '#fff', 'fg': '#000', 'cursor': '#000080', 'select_bg': '#E6E6FA',
    }
}


#  Смена тем между свтлой и темной
def change_theme(theme):
    text_note['bg'] = theme_colors[theme]['bg']
    text_note['fg'] = theme_colors[theme]['fg']
    text_note['insertbackground'] = theme_colors[theme]['cursor']
    text_note['selectbackground'] = theme_colors[theme]['select_bg']

# ======================================================================================================
# Размер фона
# def font_size(font1):
#     print(font1)
#     text_note['font'] = fonts.index(font1)
# ======================================================================================================


def open_file():
    # Выбор файла
    change_file = filedialog.askopenfilename(
        title='SELECT FILE',
        filetypes=(
            ('Text document(*.txt)', '*.txt'),
            ('All files', '*.*')
        )
    )
    if change_file:
        text_note.delete('1.0', END)  # Удаление всего текста в notepad
        text_note.insert('1.0', open(change_file, encoding='utf-8').read())  # Добавления текста из выбранного файла


def save_file():
    # Выбор/Создание файла в котором сохраняем текст
    saved_file = filedialog.asksaveasfilename(
        title='SAVED',
        filetypes=(
            ('Text document(*.txt)', '*.txt'),
            ('All files', '*.*')
        )
    )
    if saved_file:
        f = open(saved_file, 'w', encoding='utf-8')
        text = text_note.get('1.0', END)
        f.write(text)
        f.close()
    else:
        messagebox.showerror(
            title='Why are you breaking my natural system, AAAAAAAAAAAA?',
            message='You need to select a file to save!'
        )

# ======================================================================================================
# def fonts():
#     type_fonts = ['Roboto', 'Terminal', 'Fixedsys', 'Modern', 'Calibri', 'Georgia', 'Times New Roman']
#     for font in type_fonts:
#
#         text_note['font'] = font
# ======================================================================================================


# О виджете
def about_app():
    messagebox.showinfo(title='ABOUT PROGRAM', message='Program Version 0.0.1')


# Выход из виджета
def app_quit():
    answer = messagebox.askyesno(title='EXIT', message='Do you want to go out?')
    if answer:
        root.destroy()


main_menu = Menu(root)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# File
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=app_quit)


# Fonts
fonts = ['Roboto', 'Terminal', 'Fixedsys', 'Modern', 'Calibri', 'Georgia', 'Times New Roman']

font_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Font...', menu=font_menu)
font_menu_sub = Menu(font_menu, tearoff=0)
font_menu.add_cascade(label='Font', menu=font_menu_sub)
font_menu_size = Menu(font_menu, tearoff=0)
font_menu.add_cascade(label='Size', menu=font_menu_size)
for num in range(1, 101):
    b = font_menu_size.add_command(label=f'Entry size {num}', command=lambda: font_size(100))
    # print(num, b)
for font in fonts:
    a = font_menu_sub.add_command(label=font,)
    # print(a)



# Theme
theme_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Other', menu=theme_menu)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu.add_cascade(label='Registration', menu=theme_menu_sub)
theme_menu_sub.add_command(label='Light', command=lambda: change_theme('light'))
theme_menu_sub.add_command(label='Dark', command=lambda: change_theme('dark'))
theme_menu.add_command(label='About', command=about_app)

# Создание поля для текста
text_note = Text(f_text, bg=theme_colors['light']['bg'], fg=theme_colors['light']['fg'],
                 insertbackground=theme_colors['light']['cursor'],
                 selectbackground=theme_colors['light']['select_bg'],
                 padx=9, pady=7, wrap=WORD,
                 font=('Fixedsys', 13),
                 width=10, spacing3=10
                 )
text_note.pack(fill=BOTH, expand=1, side=LEFT)

# Scroll
scroll = Scrollbar(f_text, command=text_note.yview)
scroll.pack(fill=Y, side=LEFT)
text_note.config(yscrollcommand=scroll.set)

root.mainloop()




