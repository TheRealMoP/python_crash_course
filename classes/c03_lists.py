class C03Lists(object):

    def __init__(self, *args, **kwargs):
        print("\n*** Chapter 3: Lists ***")

        fruits_de = ['apfel', 'orange', 'banane', 'pfirsich']
        fruits_es = ['manzana', 'naranja', 'plátano', 'durazno']
        print(fruits_de)
        print(fruits_es)

        # Mit index -1 wird das letzte Element ausgegeben, mit -2 das Vorletzte etc..
        print(fruits_de[-1])
        print(fruits_de[-2])

        print(f"Meine Lieblingsfrucht ist {fruits_de[1].title()}")
        print(f"Mi fruta favorita es la {fruits_es[1].title()}")
        
        fruits_de.append('pflaume')
        fruits_es.append('ciruela')
        print(fruits_de)
        print(fruits_es)

        fruits_de.insert(2, 'melone')
        fruits_es.insert(2, 'melón')
        print(fruits_de)
        print(fruits_es)

        del fruits_de[3]
        del fruits_es[3]
        print(fruits_de)
        print(fruits_es)

        popped_last_fruit_de = fruits_de.pop()
        popped_last_fruit_es = fruits_es.pop()
        popped_second_fruit_de = fruits_de.pop()
        popped_second_fruit_es = fruits_es.pop()

        print(popped_last_fruit_de)
        print(popped_last_fruit_es)
        print(popped_second_fruit_de)
        print(popped_second_fruit_es)

        fruits_de.remove('apfel')
        fruits_es.remove('manzana')
        print(fruits_de)
        print(fruits_es)
        
        cars = ['bmw', 'audi', 'porsche', 'mercedes']
        print(f"A list of cars with the length {len(cars)} was created")
        # temporäres Sortieren
        print(sorted(cars))
        cars_unchanged = cars.copy()
        cars.sort()
        print(cars)
        cars.sort(reverse=True)
        print(cars_unchanged)
        cars_unchanged.reverse()
        print(cars_unchanged)

