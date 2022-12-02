from question_model import Question
from data import question_data

question_bank = []
for data in question_data:
    question = Question(data['text'], data['answer'])
    question_bank.append(question)
    
print(question_bank[1].answer)