# from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme='elegance')
root.geometry('400x300+700+500')

ttk.Button(root, text="Button").pack(pady=10)
ttk.Entry(root).pack()

root.mainloop()

# s = ttk.Style()
# s.theme_use('clam')
# # print(s.theme_names(), s.theme_use())
# # s.configure('.', foreground="red")
# # s.configure('TButton', padding=3)
#
# # ttk.Button(root, text='Button1', width=21).pack(pady=10)
# # ttk.Button(root, text='Button2', width=21).pack(pady=10)
# # Button(root, text='Button3', padx=40, pady=5).pack()
# #
# # ttk.Entry(root).pack(pady=10)
# # Entry(root).pack()
#
#
# def choose(event):
#     print(select.current(), select.get())
#
#
# select = ttk.Combobox(root, values=['January', 'February', "March", 'April', 'May'])
# select.place(relx=0.5, rely=0.5, anchor=CENTER)
# select.current(0)
# select.bind("<<ComboboxSelected>>", choose)

# def open_win():
#     win = Toplevel()
#     win.geometry("200x100+1000+800")
#     win.overrideredirect(1)
#     win.grab_set()
#     l = Label(win, text="Hello from Toplevel", bg="#000", fg='#fff').pack(expand=1, fill=BOTH)
#     win.after(3000, lambda: win.destroy())
#
#
# Button(root, text="Open", command=open_win, padx=40, pady=5).place(relx=0.5, rely=0.5, anchor=CENTER)

