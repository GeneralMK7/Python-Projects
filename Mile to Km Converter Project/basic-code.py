import tkinter

def button_clicked():
    print("Button got clicked")
    input_text = entry.get()
    my_label.config(text= input_text)


screen = tkinter.Tk()
screen.title("My First GUI Program")
screen.minsize(width=500, height=300)
screen.config(padx=20, pady=20)

my_label = tkinter.Label(text="This is my label", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

button = tkinter.Button(text="Click Me")
button.grid(column=1, row=1)


entry = tkinter.Entry(width=10)
entry.grid(column=3, row=3)


screen.mainloop()
