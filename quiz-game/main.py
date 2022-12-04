from data import question_data
from question_model import Question
import numpy

question_bank = []
for data in question_data:
    question = Question(data['text'], data['answer'])
    question_bank.append(question)
    
# print(question_bank[1].answer)




x = numpy.array([[[1,1,2], [2,3,3]], [[1,1,1], [1,1,1]]])
print(x.shape)
print(x)