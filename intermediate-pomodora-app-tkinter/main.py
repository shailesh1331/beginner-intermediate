# Import the required modules
from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ''

# Timer reset function
def reset_timer():
    global reps, checks
    reps = 0
    checks = ''
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")

# Timer mechanism
def start_timer():
    global reps, checks
    if reps == 0:
        timer = WORK_MIN * 60
        count_down(timer)
        label.config(text="Work", fg=GREEN)
        reps += 1
    elif reps % 2 == 1:
        timer = SHORT_BREAK_MIN * 60
        count_down(timer)
        label.config(text="Break", fg=PINK)
        reps += 1
        checks += '✅'
        check_mark.config(text=checks)
    else:
        timer = LONG_BREAK_MIN * 60
        count_down(timer)
        label.config(text="Break", fg=RED)
        reps += 1

# Countdown mechanism
def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 23, 'bold'), bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(101, 112, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", fill='yellow', font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', bg=PINK, borderwidth=2, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=PINK, borderwidth=2, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, borderwidth=0, font=(FONT_NAME, 12), bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
