BACKGROUND_COLOR = "#B1DDC6"
import tkinter as tk
import pandas, random

#$----------------------------------DATA FILES-------------------------------------------$#
data_file = pandas.read_csv("data/french_words.csv")
french_word = ""
english_word = ""
index_word = 0
try:
    open("data/words_to_learn.txt")
except FileNotFoundError:
    data_file.to_csv("data/words_to_learn.csv",index=False)

#$--------------------------------BUTTON RESPONSES----------------------------------------$#
def next_word():
    global french_word, english_word,index_word,data_file
    index_word = random.randint(0, len(data_file) - 1)
    french_word = data_file.French[index_word]
    english_word = data_file.English[index_word]

def give_answer(answer):
    global index_word, data_file
    data_file = data_file[data_file["French"] != french_word]
    data_file.to_csv("data/words_to_learn.csv", index=False)
    card_front.itemconfig(language,text= "English",fill= "white")
    card_front.itemconfig(canvas_text,text= f"{answer}",fill="white")
    card_front.itemconfig(card_background, image=image_back)

def button_clicked():
    global french_word, english_word,flip_timer
    window.after_cancel(str(flip_timer))
    next_word()
    card_front.itemconfig(card_background,image= image_front)
    card_front.itemconfig(language,text="French",fill= "black")
    card_front.itemconfig(canvas_text,text= french_word,fill="black")

    flip_timer = window.after(3000, give_answer,english_word)


#$------------------------------------UI SETUP--------------------------------------------$#
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=40, pady=20)

image_front = tk.PhotoImage(file="images/card_front.png")
card_front = tk.Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card_front.create_image(400,300,image=image_front)
image_back = tk.PhotoImage(file="images/card_back.png")
language = card_front.create_text(400,180,text="",font=("Arial",25,"italic"),fill="black")
canvas_text = card_front.create_text(400,280,text="",font=("Arial",40,"bold"),fill="black")
card_front.grid(row=0, column=0,columnspan=2)


image_right = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(window,image= image_right,highlightthickness=0,borderwidth=0,command=button_clicked)
right_button.grid(row=1,column=1)


image_wrong = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(window,image= image_wrong,highlightthickness=0,borderwidth=0,command=button_clicked)
wrong_button.grid(row=1,column=0)

flip_timer = 0
button_clicked()

window.mainloop()
