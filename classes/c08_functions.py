from classes.mixed_module import random_number

class C08Functions(object):
    def __init__(self):
        print("\n*** Chapter 8: FUNCTIONS ***")

        self.describe_pet("dog", "Tuzik")
        self.describe_pet(name='marusja', type='cow', good_boy=False)

        self.my_cars("Audi", "BMW", "Porsche")
        self.my_cars_limited(2, "Audi", "BMW", "Porsche", "Lada")

        print(self.build_user("Anna", "Bananna", size="75D", hair="blonde"))

        num = random_number(1, 100, 1)
        print(f"Random number: {num}")


    def describe_pet(self, type, name, good_boy=True):
        print(f"My {type} has a name {name}", end=' ')
        if (good_boy):
            print(':-)')
        else:
            print(':-(')

    # unendlich viele argumente (arbitary)
    def my_cars(self, *cars):
        print(f"You own {len(cars)} cars")
        print(cars)

    # mixed arguments: positional & arbitary
    def my_cars_limited(self, max_cars, *cars):
        print(f"You can own max {max_cars} cars")
        print(cars[0:int(max_cars)])
        
    # mit ** wird eine leere Dictionary angelegt
    def build_user(self, first, last, **user_info):
        user_info["first"] = first
        user_info["last"] = last
        return user_info
