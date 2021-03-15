from tkinter import *


root = Tk()
# root.geometry('250x250+1200+100')
root.title("Rainbow_Dash")


colors = {
    '#ff0000': 'Red',
    '#ff7d00': 'Orange',
    '#ffff00': 'Yellow',
    '#00ff00': 'Green',
    '#007dff': 'Cyan',
    '#0000ff': 'Blue',
    '#7d00ff': 'Purple',
}


class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


l = Label(root)
e = Entry(root, width=30, justify=CENTER)
l.pack()
e.pack()


for k, v in colors.items():
    MyButtons(root, v, k)

#
# def get_color(text_color, hex_color):
#     l['text'] = text_color
#     e.delete(0, END)
#     e.insert(0, hex_color)


# def color_orange():
#     l['text'] = 'Оранжевый'
#     e.delete(0, END)
#     e.insert(0, '#ff7d00')
#
#
# def color_yellow():
#     l['text'] = 'Желтый'
#     e.delete(0, END)
#     e.insert(0, '#ffff00')

# for k, v in colors.items():
#     Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)


# def red():
#     btn_red['text'] = 'red'
#
# def orange():
#     btn_orange['text'] = 'orange'
# def yellow():
#     btn_yellow['text'] = 'yellow'
#     btn_green['text'] = 'green'
#     btn_cyan['text'] = 'cyan'
#     btn_blue['text'] = 'blue'
#     btn_purple['text'] = 'purple'
#
#
# btn_red = Button(root, text='', bg='#ff0000', command=red)
# btn_red.pack(fill=X)
# btn_orange = Button(root, bg='#ff7d00', command=orange)
# btn_orange.pack(fill=X)
# btn_yellow = Button(root, bg='#ffff00', command=yellow)
# btn_yellow.pack(fill=X)
# btn_green = Button(root, bg='#00ff00', command=yellow)
# btn_green.pack(fill=X)
# btn_cyan = Button(root, bg='#007dff', command=yellow)
# btn_cyan.pack(fill=X)
# btn_blue = Button(root, bg='#0000ff', command=yellow)
# btn_blue.pack(fill=X)
# btn_purple = Button(root, bg='#7d00ff', command=yellow)
# btn_purple.pack(fill=X)


root.mainloop()


