
""" simple mathematical functions """


def to_float(str):
    try: 
        return float(str)
    except ValueError:
        pass

def add(x, y):
    return to_float(x) + to_float(y)

def sub(x, y):
    return to_float(x) - to_float(y)

def mul(x, y):
    return to_float(x) * to_float(y)

def div(x, y):
    try:
        return to_float(x) / to_float(y)
    except ZeroDivisionError:
        print("You are  not Chuck Norris! You can't divide by zero!")

def exp(x, y):
    return to_float(x) ** to_float(y)