from classes.human import Human
from classes.student import Student
from common.mixed_module import random_date as rd, pick_random as ran

class C09Classes:
    def __init__(self):
        print("\n*** Chapter 9: CLASSES ***")

        self.students = []
        #self.run()
        self.create_students()


    def run(self):
        step = ''

        while(step != 'q'):         

            human_01 = Human('male', rd());
            human_01.introduce_yourself()

            human_02 = Human('divers', rd());
            human_02.planet = 'Jupiter'
            human_02.introduce_yourself()

            human_01.change_gender('trans', True)

            stud_chosen = ran(self.students)
            print(f"{stud_chosen.name}, you are the choosen one!")

            step = input("'q' for exit: ")


    def create_students(self):
        stud_01 = Student('male', rd(), 'Vasilij', 'Informatics', 'Rumnerden')
        self.students.append(stud_01)

        stud_02 = Student('male', rd(), 'Ivan', 'Economics')
        self.students.append(stud_02)

        stud_03 = Student('female', rd(), 'Olga', 'Arts')
        self.students.append(stud_03)

        #for stud in self.students:
        #    stud.introduce_yourself()