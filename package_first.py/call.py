class Human :
    pass

class Student(Human):

    name : str = ""
    age : str = ""
    adress : str = ""

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f" name : (self . name), age:(selg . age), Adress : (selkf . adress)"
    

obj_or_instance = Student()
print(obj_or_instance)