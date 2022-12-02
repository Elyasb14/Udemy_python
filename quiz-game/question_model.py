class Question:
    
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
        
newq = Question('3+3=6', 'True')
print(newq.text)