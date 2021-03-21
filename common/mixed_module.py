from random import randrange
from random import choice
from datetime import date


def random_number(min, max, step = 1):
    return randrange(min, max, step)

def random_date():
    return date(random_number(0, 2021), random_number(1, 12), random_number(1, 30))

def pick_random(lst):
    return choice(lst)