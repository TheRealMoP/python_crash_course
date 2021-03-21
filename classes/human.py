import datetime
from json import JSONEncoder

class Human:

    def __init__(self, gender, birthdate):
        self.gender = gender
        self.birthdate = birthdate
        self.planet = 'Earth'

    def introduce_yourself(self):
        print(f"I am {self.gender} and i am {self.get_age()} years old. I come from {self.planet}")

    def get_age(self):
        return (datetime.date.today().year - self.birthdate.year)
    
    def change_gender(self, new_gender, reprint = False):
        self.gender = new_gender
        if reprint:
            print('** Gender changed **')
            self.introduce_yourself()

class HumanEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__