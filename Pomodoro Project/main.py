import math
import tkinter
from tkinter import PhotoImage


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button_clicked():
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text,text= "00:00")
    timerLabel.config(text="Timer")
    checkButton.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_clicked():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps

    reps += 1
    if reps % 8 == 0:
        timerLabel.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timerLabel.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timerLabel.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count / 60)
    count_sec = int(count % 60)

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button_clicked()
        final = math.floor(reps / 2)
        mark = "✔" * final
        checkButton.config(text=mark, fg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timerLabel = tkinter.Label(text= "Timer",font= (FONT_NAME,40,"bold"),bg=YELLOW,fg= GREEN)
timerLabel.grid(column=2, row=1)

startButton = tkinter.Button(text="Start",highlightthickness=0,command=start_button_clicked)
startButton.grid(column=1, row=3)

checkButton = tkinter.Label(font= (FONT_NAME,16,"bold"),background=YELLOW,fg=GREEN)
checkButton.grid(column=2, row=4)

resetButton = tkinter.Button(text="Reset",highlightthickness=0,command=reset_button_clicked)
resetButton.grid(column=3, row=3)




tomato_image = tkinter.PhotoImage(file = "tomato.png")
canvas = tkinter.Canvas(width=230, height=230,bg = YELLOW,highlightthickness=0)
canvas.create_image(112, 115, image=tomato_image)
timer_text = canvas.create_text(115,130,text= "00:00",font= (FONT_NAME,30,"bold"),fill= "White")
canvas.grid(column=2, row=2)



window.mainloop()