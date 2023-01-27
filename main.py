import random
from Database import Word

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def run_test(Questions):
    total_question = 0
    right_question = 0
    wrong_question = 0
    while total_question < 5:
    #for i in Word:
        apa = Word[random.randint(0, 4)]
        question_prompts = [
            "How do you say " + apa[0].lower() + " in Japanese?"
        ]
        answer = input(question_prompts)
        if answer.lower() == apa[1].lower():
            total_question += 1
            right_question += 1
            print("Rätt")
        else:
            print("Fel")
            wrong_question += 1
            total_question += 1
    print("You had " + str(right_question) + " out of " + str(total_question) + " questions correct")

run_test(Question)