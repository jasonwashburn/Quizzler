from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 14, "normal")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        # Main Window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score Label
        self.score_label = Label(text="Score: 0", font=SCORE_FONT, fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        # Main Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        q_text = quiz.next_question()
        self.question_text = self.canvas.create_text(150, 125, font=FONT, text=q_text, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Buttons
        true_button_img = PhotoImage(file="images/true.gif")
        self.true_btn = Button(image=true_button_img, borderwidth=0, highlightbackground=THEME_COLOR,
                               highlightthickness=0)
        self.true_btn.grid(column=0, row=2, padx=20, pady=20)
        false_button_img = PhotoImage(file="images/false.gif")
        self.false_btn = Button(image=false_button_img, borderwidth=0, highlightbackground=THEME_COLOR,
                                highlightthickness=0)
        self.false_btn.grid(column=1, row=2, padx=20, pady=20)

        # Start main loop
        self.window.mainloop()