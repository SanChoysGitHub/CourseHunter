from tkinter import *

root = Tk()
root.geometry('600x700+700+500')

l = Label(root,
          text='Text in string 1\n'
               'String 2\n'
               'String 3\n'
               'String 4\n'
               'String 5',
          bg="black",
          fg="green",
          font=("Comic Sans MS", 10, "bold"),
          justify=LEFT,
          width=40,
          height=10,
          anchor=NW
          )
img = PhotoImage(file='python.png')
l_logo = Label(root, image=img)
l_logo.pack()


l.pack()

root.mainloop()









