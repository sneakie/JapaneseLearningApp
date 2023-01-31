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
    asked_question = [

    ]
    while total_question < 5:
        apa = Word[random.randint(0, 4)]
        count = asked_question.count(apa)
        if count >= 1:
            continue
        else:
            question_prompts = [
            "How do you say " + apa[0].lower() + " in Japanese?"
        ]
            answer = input(question_prompts)
            asked_question.append(apa)
            if answer.lower() == apa[1].lower():
                total_question += 1
                right_question += 1
                print("Rätt")
            else:
                print("Fel")
                total_question += 1
    print("You had " + str(right_question) + " out of " + str(total_question) + " questions correct")
    print(asked_question)

run_test(Question)