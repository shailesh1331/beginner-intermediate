import tkinter
from tkinter import Tk

# def yo():
#     func.config(text="Button got Clicked!")


window=Tk()
window.title('My first GUI program!')
window.minsize(width=500,height=300)


my_lable=tkinter.Label(text='Hello')
my_lable.pack()


def pressed():
    new_text=entry.get()
    print(my_lable.config(text=f'{new_text}'))

button=tkinter.Button(text='click me',command=pressed)
button.pack()

entry=tkinter.Entry()
entry.pack()







window.mainloop()

# def add(*args):
#     total=0
#     for n in args:
#         total+=n
#     return total
#
# print(add(10,14,43,546,))
#

