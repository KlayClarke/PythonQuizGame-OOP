class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print(f'You got it right!\nThe correct answer was: {current_question.answer}.\nYour current score is: '
                  f'{self.score}/{self.question_number}\n')
            return True
        else:
            print(f'You got it wrong!\nThe correct answer was: {current_question.answer}.\nYour current score is: '
                  f'{self.score}/{self.question_number}\n')
            return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def quiz_done(self):
        print(f'You\'ve completed the quiz.\nYour final score was {self.score}/{self.question_number}')
