class C02VariablesAndSimpleData(object):
    def __init__(self):
        print("\n*** Chapter 2: Variables and simple data ***")

        message = "Hello again!"
        print(message)

        message = "privet"
        print(message)

        name = "vasja pupkin"
        print(name.title())
        print(name.upper())
        print(name.lower())

        first_name = "vasja"
        last_name = "pupkin"
        full_name = f"{first_name} {last_name}"
        print(full_name.title())

        str_with_empty = ' Hello, my name is Vasja  '
        print(str_with_empty)
        print(str_with_empty.strip())
        print(str_with_empty.rstrip())
        print(str_with_empty.lstrip())

        print(2*3)
        print(2.0*3.0)
        print(2**3.0)
        print(0.2+0.1)

        long_number = 12_500_000_000
        print(long_number)

        a, b, c = 1, 2, 3

        print("a, b, c = "+f"{a}, {b}, {c}")

        # Es gibt keine echten Konstanten. Großbuchstaben signalisieren bloß, dass der Wert nicht verändert werden soll
        PSEUDO_CONTANT = 2021