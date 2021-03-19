from tkinter import *

root = Tk()
root.geometry("600x400+700+500")
root.title('Calculator')


def sum():
    first_number = int(input('Enter 1 num: '))
    second_number = int(input('Enter 2 num: '))
    if btn['text'] == '+':
        btn['text'] = first_number + second_number
    if btn['text'] == '-':
        btn['text'] = first_number - second_number
    if btn['text'] == '/':
        btn['text'] = first_number / second_number
    if btn['text'] == '*':
        btn['text'] = first_number * second_number


def btn():
    btn = Button(root, text='+', command=sum)
    btn.pack()

btn()
root.mainloop()







