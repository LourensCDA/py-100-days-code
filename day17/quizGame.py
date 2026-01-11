from data import question_data_api
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []

for question in question_data_api:
    questionBank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(questionBank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"End of Quiz.\nYour final score is: {quiz.score} / {quiz.question_number}")
