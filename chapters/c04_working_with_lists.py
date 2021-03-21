class C04WorkingWithLists(object):
    def __init__(self):        
        print("\n*** Chapter 4: Working with Lists ***")
               
        fruits_de = ['apfel', 'orange', 'banane', 'pfirsich']
        fruits_es = ['manzana', 'naranja', 'plátano', 'durazno']

        for fruit in fruits_de:
            print(fruit)

        for value in range(1,5):
            print(value)

        print(list(range(1,5)))
        print(list(range(2,10,2)))

        for value in range(2,11):
            print(f"{value}² = {value**2}")


        digits = [2,5,23,133,56,43,7]
        print(f'min: {min(digits)}')
        print(f'max: {max(digits)}')
        print(f'max: {sum(digits)}')

        # List comprehention: fügt den berechneten Wert (value²) der Liste hinzu
        squares = [value**2 for value in range(2, 11)]
        print(squares)

        # slicing
        print(fruits_de[1:3])
        print(fruits_de[:3])
        print(fruits_de[2:])
        print(fruits_de[-3:])
        print(fruits_de[:-3])

        for fruit in fruits_de[2:]:
            print(fruit)

        # copying a list by slicing
        fruits_copy = fruits_de[:]
        fruits_de.pop(2)
        print(fruits_copy)
        print(fruits_de)

        # tuple
        dimensions = (1080, 1920)
        print(dimensions)

        print('')