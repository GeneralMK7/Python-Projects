import tkinter
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.answer = "False"
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quiz GUI")
        self.window.minsize(400, 500)
        self.window.config(bg=THEME_COLOR)
        self.score_label = tkinter.Label(text= f"Score: {self.quiz.score}",font=("Arial", 14),bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0)

        self.canvas = tkinter.Canvas(width=350, height=250,highlightthickness=0,bg="white")
        self.question_text = self.canvas.create_text(
            175,
            125,
            text="",
            width=330,
            font=("Arial",12,"italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1,columnspan=2,padx=50,pady=40)

        image_right = tkinter.PhotoImage(file="images/true.png")
        self.right_button = tkinter.Button(image=image_right, highlightthickness=0, command=self.right_button_clicked)
        self.right_button.grid(column=0, row=2)

        image_wrong = tkinter.PhotoImage(file="images/false.png")
        self.wrong_button = tkinter.Button(image=image_wrong, highlightthickness=0, command=self.wrong_button_clicked)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()


    def next_question(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Your final score: {self.quiz.score}",font=("Arial", 18,"bold"))
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    # noinspection PyTypeChecker
    def check_answer_for_question(self,answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.update_score()
        self.window.after(1000, self.next_question)

    def right_button_clicked(self):
        self.answer = "True"
        self.check_answer_for_question(self.answer)

    def wrong_button_clicked(self):
        self.answer = "False"
        self.check_answer_for_question(self.answer)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
