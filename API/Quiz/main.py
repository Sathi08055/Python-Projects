
from quiz_brain import QuizBrain
from data import new_data
from ui import Quizinterface



if __name__ == "__main__" :
    ques_list=new_data()
    quiz = QuizBrain(ques_list)
    ui=Quizinterface(quiz=quiz)
