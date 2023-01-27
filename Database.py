import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

Word = [

    ["Train Station", "Eki"],
    ["Hello(day)", "Konnichiwa"],
    ["Hello(Morning)", "Ohayo"],
    ["Meat", "Niku"],
    ["English", "Igirisu"]

]


def run_test(Questions):
    total_question = 0
    for i in Word:
        apa = Word[random.randint(0, 4)]
        question_prompts = [
            "How do you say " + apa[0].lower() + " in Japanese?"
        ]
        answer = input(question_prompts)
        if answer == apa[1].lower():
            total_question += 1
            print("Rätt")

run_test(Question)