class C05IfSatements(object):
    def __init__(self):
        print("\n*** Chapter 5: If Statements ***")

        fruits_de = ['apfel', 'orange', 'banane', 'pfirsich']
        for fruit in fruits_de:
            if len(fruit) >= 7:
                print(f" long named ({len(fruit)}): {fruit.upper()}")
            else:
                print(f"short named ({len(fruit)}): {fruit.upper()}")


        for fruit in fruits_de:
            if (len(fruit) <= 6 and fruit.startswith('a')):
                print(f"fruit found: {fruit}")

        
        fruits_minimized = ['orange', 'pfirsich']

        for fruit in fruits_de:
            if (fruit in fruits_minimized):
                print(f"{fruit.upper()} is in the minimized list")


        for fruit in fruits_de:
            if (fruit not in fruits_minimized):
                print(f"{fruit.upper()} is missing :-/")

        for fruit in fruits_de:
            if (fruit.startswith('a')):
                print(f"{fruit.upper()} is an A-fruit")
            elif (len(fruit) > 6):
                print(f"{fruit.upper()} is a Long-named-fruit")
            else:
                print(f"{fruit.upper()} is an obvious one")
