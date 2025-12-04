import tkinter

screen = tkinter.Tk()
screen.title("Mile to KM Converter")
screen.config(padx=30, pady=30)


def button_clicked():
    mile_input = entry.get()
    final_answer = round(float(mile_input) * 1.60934,2)
    answer.configure(text=str(final_answer))


entry = tkinter.Entry(width= 9)
entry.grid(column= 1, row= 0)


my_label = tkinter.Label(text="Miles")
my_label.grid(column= 2, row= 0)

is_equal = tkinter.Label(text="is equal to")
is_equal.grid(column= 0, row= 1)

answer = tkinter.Label(text = "0",font=("Arial", 9, "bold"))
answer.grid(column= 1, row= 1)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column= 2, row= 1)

calculate = tkinter.Button(text="Calculate",command=button_clicked)
calculate.grid(column= 1, row= 2)
screen.mainloop()