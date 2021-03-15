from tkinter import *


root = Tk()
root.geometry('600x400+900+600')


def clicked():
    print('Clicked')


# btn = Button(root, text="BRUH", command=clicked, font="Arial 30 italic")
# btn = Button(root, text="Кнопка", command=clicked, font=("Comic Sanc MS", 20))
btn = Button(root, text="Кнопка1\nКнопка2", justify="right")
btn.configure(width=20, height=5)
# btn['font'] = 'Arial 15'
btn.pack()


root.mainloop()













