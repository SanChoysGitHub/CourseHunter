from tkinter import *
import time


root = Tk()
root.geometry('600x400+700+600')
root.title('Counter')


def check_time():
    btn_time['text'] = time.strftime('%h:%M:%S')
    # print(time)


clicks = 0


def counter():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')


btn_time = Button(root, text='Check time', command=check_time)
btn_time.pack()


btn_cnt = Button(root, text='Counter', command=counter)
btn_cnt.pack(fill=X)


root.mainloop()








