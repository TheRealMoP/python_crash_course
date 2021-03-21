from common.format_utils import get_formatted_name
from classes.survey import AnonimousSurvey
class C11Testing():        
    
    def __init__(self):
        print("\n*** Chapter 11: TESTING ***")
        self.run_survey()
    
    def run_name_formatting(self):  
        print("Enter 'q' to quit\n")
        while True:
            first = input("First name: ")
            if first == "q":
                break

            last = input("Last name: ")
            if last == "q":
                break

            print(get_formatted_name(first, last))

    def run_survey(self):
        question = "What was your first language?"
        survey = AnonimousSurvey(question)

        print("Enter 'q' to quit\n")
        print(survey.show_question())
        while True:
            answer = input("Language: ")
            if answer == "q":
                break
            survey.store_answer(answer)

        survey.show_results()