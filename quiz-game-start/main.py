from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_object = Question(question["question"], question["correct_answer"])
    question_bank.append(q_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nex_question()

print("You made it to the end!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.\n")
