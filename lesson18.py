from tkinter import *
import time

root = Tk()
root.geometry('400x300+700+500')


def f_event(event, key):
    print(event, key)


colors = {
    "Left click": "#fff",
    "Middle click": "#000",
    "Right click": "#666",
}


def get_color(key):
    if key == "Left click":
        l['bg'] = colors['Left click']
    if key == "Middle click":
        l['bg'] = colors['Middle click']
    if key == "Right click":
        l['bg'] = colors['Right click']




e = Entry(root, justify=CENTER, font="Arial 15")
e.pack(fill=X, expand=1, padx=10, ipady=10)
e.bind("<Button-1>", lambda event, key="Left click": get_color(key))
e.bind("<Button-2>", lambda event, key="Middle click": get_color(key))
e.bind("<Button-3>", lambda event, key="Right click": get_color(key))
e.bind("<FocusIn>", lambda event, key="Focus": f_event(event, key))

l = Label(root, bg="blue")
l.pack(fill=X)

root.mainloop()

# def tick():
#     watch.after(200, tick)
#     watch['text'] = time.strftime('%H:%M:%S')
#
# watch = Label(root, font='Arial 70')
# watch.pack()
# tick()
