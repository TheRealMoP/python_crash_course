import sys

class C06Dictionaries(object):
    def __init__(self):
        print("\n*** Chapter 6: Dictionaries ***")

        fruit_apple = {'color' : 'green', 'taste' : 'sour'}
        print("color: " + fruit_apple['color'])
        print("taste: " + fruit_apple['taste'])

        fruit_apple['price'] = 'moderate'
        print("price: " + fruit_apple['price'])
        del fruit_apple['price']
        print(fruit_apple)

        fav_colors = {
            'michael' : 'green',
            'jessy' : 'black',
            'vasja' : 'white', # comma is a good practice
            }

        try:
           print('thomas loves ' + fav_colors['thomas'])
        except KeyError:
           print('thomas loves ' + fav_colors.get('thomas', 'kein thomas hier!'))

        
        try:
           print('jessy loves ' + fav_colors['jessy'])
        except KeyError:
           print('jessy loves ' + fav_colors.get('jessy', 'kein thomas hier!'))

        for key, value in fav_colors.items():
            print(f"{key} loves {value}")

        print("- All Names - ")
        for key in fav_colors.keys():
            print(key)

        fruit_orange = {'color' : 'orange', 'taste:' : 'sour'}
        fruit_banana = {'color' : 'yellow', 'taste:' : 'sweet'}

        fruits = [fruit_apple, fruit_banana, fruit_orange]

        # name der variable bekommen
        #print(f'{fruit_apple=}'.split('=')[0]) 
        print(fruits)

        jessy = {
            'gender' : 'girl',
            'fruits' : [fruit_apple, fruit_orange],
            }

        print(jessy)

        people = {
            'michael' : {
                'gender' : 'male',
                'age' : 17,
                },
            
            'anna' : {
                'gender' : 'female',
                'age' : 22,
                }
            }

        for person, properties in people.items():
            print(person.title() + ':')

            for key, value in properties.items():
                print(f"\t{key}: {value}")