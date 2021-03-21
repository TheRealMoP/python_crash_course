import json
import common.file_ops as fops
import common.math_ops as mops
from chapters.c09_classes import C09Classes
from classes.student import StudentEncoder
from classes.human import Human, HumanEncoder
from common.mixed_module import random_date as rd

class C10FilesAndExceptions:

    def __init__(self):
        print("\n*** Chapter 10: FILES AND EXCEPTIONS ***")
        
        #path = "ressources\pi.txt"

        #print(fops.read_complete_file(path))
        #print('Selected lines: \n' + fops.read_certain_lines(path, [0,2]))
        #print('Lines as list:')  
        #print(fops.read_as_list(path))
        #content = fops.read_and_append(path)
        #print(f"{content} \nLength: {len(content)}")

        #long_pi = fops.read_and_append("ressources/pi_1mio.txt")
        
        #print(long_pi[:int(input('Anzahl Stellen: '))])
        #string_to_find = input("Inhalt durchsuchen nach: ")
        #position = long_pi.find(string_to_find)
        #if position != -1:
        #    print(f"Gesuchter string gefunden: {position}")
        #    print(f"...{long_pi[position-2:position+len(string_to_find)+2]}...")
        #else:
        #    print("Gesuchter string nicht gefunden")

        path_for_replacing_text = 'local/new_file.txt'
        fops.write_and_replace(path_for_replacing_text, "Ich bin neu hier!")

        #self.run_editor()

        json_obj = "local/json_obj.json"
        c09 = C09Classes()
        self.save_data(c09.students, json_obj)
        loadded_data = self.read_date(json_obj)
        print(loadded_data)
      
    def save_data(self, data, path):
        
        #with open(path, 'w') as file:
            #json.dumps(data, cls=StudentEncoder)

        #human1 = Human("male", rd())
        #human1.introduce_yourself()

        #jstring = json.dumps(human1, cls=HumanEncoder)
        numbers = [2, 3, 5, 7, 11, 13]

        with open(path, 'w') as f:
            json.dump([2, 3, 5, 7, 11, 13], f)

    def read_date(self, path):
        with open(path) as file:
            return json.load(file)

    def run_editor(self):        
        path_for_appending_text = 'local/appending_file.txt'
        cmd = "";       
        
        print("Welcome to my text editor. For help type --help or -h")
        while cmd != "--q":
            cmd = input(">> ")
            if (cmd == "--q"):
                print("Bye :-)")
                break

            if (cmd in ["--help", "-h"]):
                print(fops.read_complete_file("ressources/commands.txt"))
            elif (cmd == "--p"):
                print(fops.read_complete_file(path_for_appending_text))
            elif (cmd == "--clr"):
                fops.write_and_replace(path_for_appending_text, "")
            elif (cmd.startswith("--add")):
                xy = self.get_x_y_from_str(cmd)
                if (xy != None):
                    print(mops.add(xy[0], xy[1]))
            elif (cmd.startswith("--sub")):
                xy = self.get_x_y_from_str(cmd)
                if (xy != None):
                    print(mops.sub(xy[0], xy[1]))
            elif (cmd.startswith("--mul")):
                xy = self.get_x_y_from_str(cmd)
                if (xy != None):
                    print(mops.mul(xy[0], xy[1]))
            elif (cmd.startswith("--div")):
                xy = self.get_x_y_from_str(cmd)
                if (xy != None):
                    result = mops.div(xy[0], xy[1])
                    if result != None:
                        print(result)
            elif (cmd.startswith("--exp")):
                xy = self.get_x_y_from_str(cmd)
                if (xy != None):
                    print(mops.exp(xy[0], xy[1]))
            elif (cmd == "--cnt"):
                print(f"{fops.count_words(path_for_appending_text)} words")
            else:
                fops.write_and_append(path_for_appending_text, cmd, True)
    

    def get_x_y_from_str(self, str):
        ''' Format should be <str> <x> <y> '''
        splitted = str.rsplit(" ");
        if (len(splitted) != 3):
            print("Wrong format")
            return None
        
        if not splitted[1].isnumeric() or not splitted[2].isnumeric():
            print("At least one of arguments is not a number")
            return None

        return splitted[-2:]