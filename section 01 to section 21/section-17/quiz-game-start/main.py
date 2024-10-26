from crayons import green, red, yellow, blue, magenta, cyan
from time import sleep
from os import system
from art import logo
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

system("cls")
print(logo)
sleep(0.5)
print(cyan("Welcome to The Quiz Game!\n", bold=True))

question_bank = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

sleep(0.5)
print(f"You've completed the quiz!!!")
sleep(0.5)
print("Your final score was: ", end=" ")
print(f"{green(quiz.score)}/{yellow(quiz.question_number)}")
