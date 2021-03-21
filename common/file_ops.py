"""functions to read/write files"""


def read_complete_file(path):
    with open(path) as file:
        return file.read()

def read_certain_lines(path, lines):
    line_nr = 0
    content = ''

    with open(path) as file:
        for line in file:
            if line_nr in lines:
                content += line
            line_nr += 1

        return content

def read_as_list(path):
    with open(path) as file:
        return file.readlines()

def read_and_append(path):
    content = ''
    with open(path) as file:
        for line in file:
            content += line.strip()

    return content

def write_and_replace(path, str):
    with open(path, 'w') as file:
        file.write(str)

        
def write_and_append(path, str, in_new_line):
    with open(path, 'a') as file:
        if in_new_line:
            file.write(f"\n{str}")
        else:
            file.write(str)

def count_words(path):
    """ Counts approximate number of words """
    try:
        with open(path, encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File '{path}' could not be found")
    else:
        words = contents.split()
        return len(words)