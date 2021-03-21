from json import JSONEncoder
from classes.human import Human;


class Student(Human):
    """Represents a studend as a special kind of human"""

    def __init__(self, gender, birthdate, name, faculty, hobby = None):
        super().__init__(gender, birthdate)
        self.faculty = faculty
        self.name = name

        if hobby == None:
            if gender == 'male':
                self.hobby = 'Saufen'
            else:
                self.hobby = 'Brainfuck'
        else:
            self.hobby = hobby


    def introduce_yourself(self):
        print('\n---------------------------------------')
        print(f"Hi! My name is {self.name}")
        super().introduce_yourself()
        print(f"I study {self.faculty}. And I love {self.hobby}")
        print('---------------------------------------\n')


class StudentEncoder(JSONEncoder):
    def defaulf(self, o):
        return o.__dict__