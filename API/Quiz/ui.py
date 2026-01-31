import tkinter as tk
from quiz_brain import QuizBrain
from question_model import Question

THEME_COLOR = "#375362"


class Quizinterface:
    def __init__(self,quiz=QuizBrain) -> None:
        self.quizbrain=quiz
        self.question=self.quizbrain.next_question()
        self.window = tk.Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.title("Quiz")
        false_img=tk.PhotoImage(file=r"images\false.png")
        true_img=tk.PhotoImage(file=r"images\true.png")
        self.score=0
        self.score=tk.Label(text=f"Score:{self.score}",bg=THEME_COLOR,fg="white",font=("Arial", 13, "bold"))
        self.score.grid(row=0, column=0, columnspan=2,sticky="ne",padx=20,pady=20)
        self.q_box=tk.Canvas(height=250, width=300)
        self.question_text=self.q_box.create_text(150,125,text=self.question,fill="black",width=280,font=("Arial",20,"italic"))
        self.q_box.grid(row=1,column=0,columnspan=2,pady=20)
        self.true_butt=tk.Button(image=true_img,highlightthickness=0)
        self.false_butt=tk.Button(image=false_img,highlightthickness=0)
        self.true_butt.grid(row=2, column=0,pady=10,sticky="w")
        self.false_butt.grid(row=2, column=1,pady=10,sticky="e")
        self.true_butt.config(command=self.right_button)
        self.false_butt.config(command=self.wrong_button)
        self.window.mainloop()

    def next_question(self):
        if (self.quizbrain.still_has_questions()):
            self.q_box.itemconfig(self.question_text,text=self.quizbrain.next_question())
            self.score.config(text=f"Score:{self.quizbrain.score}")
        else:
            self.score.config(text=f"Score:{self.quizbrain.score}")
            self.end()


    def end(self):
        self.q_box.itemconfig(self.question_text,text='Quiz is over')
        self.true_butt.config(command=self.window.destroy)
        self.false_butt.config(command=self.window.destroy)


    def right_button(self):
        self.quizbrain.check_answer("True")
        self.next_question()
    def wrong_button(self):
        self.quizbrain.check_answer("False")
        self.next_question()


if __name__== "__main__":
    def random_things():
        ques_list=[ Question(q_text=f"Question{i}", q_answer="True") for i in range (0,5)]
        return ques_list
    quiz=QuizBrain(random_things())
    ui=Quizinterface(quiz=quiz)
