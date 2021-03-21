"""Some functions to read, format and print names"""

def get_formatted_name(first, last, middle = ""):
    if middle == "":
        return f"{last.title()}, {first.title()}"
    
    return f"{last.title()}, {first.title()} {middle.title()}"