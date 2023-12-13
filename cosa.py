class Student:

    def __init__(self, aName='Leo', anAge=22):
        self.Name = aName
        self.Age = anAge
        
    def __str__(self):
        answ = ""
        # answ += repr(self) + '\n\t'  # CAN TOGGLE THIS
        answ += str(vars(obj))
        return answ
    
obj = Student("luis", 44)
print(obj)
