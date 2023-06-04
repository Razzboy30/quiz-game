class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        
    def next_quetion(self):
        current_quetion = self.question_list[self.question_number]
        self.question_number+= 1
        user_answer = input(f"Q.{self.question_number}: {current_quetion.text} (True/False)")
        self.check_answer(user_answer,current_quetion)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You are right!")
            self.score += 1
        else:
            print("Wrong")
        print(f"Correct answer is {correct_answer}")
        print(f"Current score is: {self.score}/{self.question_number}")
        print("\n")

