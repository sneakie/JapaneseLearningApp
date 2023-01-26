import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

Word = [

    ["Train Station", "Eki"],
    ["Hello(day)", "Konnichiwa"],
    ["Hello(Morning)", "Ohayo"]

]

apa = Word[random.randint(0, 2)]

question_prompts = [

    "How do you say " + apa[0] + " in Japanese?"
]

def run_test(Questions):

    score = 0
    answer = input(question_prompts)
    if answer == apa[1]:
        print("Rätt")
    else:
        print("Fel")

run_test(Question)