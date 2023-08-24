from tkinter import *


def calculate():
    new_data=int(input.get())
    result.config(text=f'{(new_data*1.6)}')




window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=100)
window.config(padx=20,pady=20)

input=Entry()
input.grid(row=0,column=1)

equal = Label(text="is equal to")
equal.grid(row=1,column=0)


#Labels
mile = Label(text="Mile")
mile.grid(row=0,column=2)

km= Label(text='Km')
km.grid(row=1,column=2)

result= Label(text='0')
result.grid(row=1,column=1)

button=Button(text="calculate",command=calculate)
button.grid(column=1,row=3)


window.mainloop()