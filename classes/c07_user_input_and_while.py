class C07UserInputAndWhile(object):
    def __init__(self):
        print("\n*** Chapter 7: USER INPUT AND WHILE LOOPS ***")

        #self.name_and_age()               

        my_index = 0
        while(my_index <= 5):
            print(my_index)
            my_index += 1;

        candidates = ['Adam', 'Berta', 'Anna', 'Michael', 'Anna', 'Jessica', 'Zelda'];

        #new_users = self.register_users(sorted(candidates))
        #print("- New Users -")
        #print(new_users)

        self.delete_users(candidates, 'Anna')
        print(candidates)

    def delete_users(self, user_list, user_name):
        while(user_name in user_list):
            user_list.remove(user_name)

    def register_users(self, unregistered_users):
        registered_users = [];

        while(unregistered_users):
            candidate = unregistered_users.pop();
            answer = input(f"{candidate}, do you wanna join? (Y=Yes / N=No / Q=Quit)").upper()

            if (answer == "Q"):
                break

            if (answer == "N"):
                continue
        
            if (answer == "Y"):
                registered_users.append(candidate)
            else:
                print("What are you doIng?!")

        return registered_users;

    def name_and_age(self):
        user_name = "";
        while(user_name == ""):
            user_name = input("Tell me your name: ").strip()

        age = input("And now your age: ")
        
        print(f"Hello {user_name}!")

        if (int(age) < 18):
            print("Sorry, but you are too young for this shit")
        else:
            go_on = input("Are yout sure, you want to continue? (Y / N): ")
            if (go_on.upper() == "Y"):
                print("Cool! You've just sold your soul to the satan!")
            elif (go_on.upper() == "N"):
                print("OK.. Fuck you!")
            else:
                print("You are too stupid to ented Y or N! Fuck you!")