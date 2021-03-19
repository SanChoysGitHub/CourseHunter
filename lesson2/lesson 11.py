from tkinter import *

root = Tk()
root.geometry('300x300+600+400')

# l1 = Label(root, text='Hello world!', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# l1.place(x=0, y=0)
#
# l2 = Label(root, text='Wassup', bg='#000', fg='#fff', font=16)
# l2.place(relx=0.5, rely=0.5, anchor=CENTER)

# btn_sw = Button(root, text="SW", bg='#fff', fg='#000')
# btn_sw.place(relx=0, rely=0)
# btn_center = Button(root, text="CENTER", bg='#fff', fg='#000')
# btn_center.place(relx=0.5, rely=0.5, anchor=CENTER)
# btn_se = Button(root, text="SE", bg='#fff', fg='#000')
# btn_se.place(relx=1, rely=1, anchor=SE)

square = Label(root, bg='#000')
square.place(relx=0.5, rely=0.5, anchor=CENTER, relheight=0.7, relwidth=0.7)

root.mainloop()


