from question_model import Quetion
from data import question_data
from quiz_brain import QuizBrain 

question_bank = []
for x in question_data:
    user = Quetion(x["text"],x["answer"])
    question_bank.append(user)

quiz = QuizBrain(question_bank)
quiz.next_quetion()
# print(question_bank)  

while quiz.still_has_questions():
    quiz.next_quetion()
    
print("You have completed the quiz")
print(f"Your final score was {quiz.score}" )