class AnonimousSurvey():
    """Collects anonimous answers to a survey question"""

    def __init__(self, question):
        """Initializing global storage"""
        self.question = question
        self.answers = []

    def show_question(self):
        print(self.question)

    def store_answer(self, answer):
        self.answers.append(answer)

    def show_results(self):
        print("Survey results:\n")

        for answer in self.answers:
            print(f" - {answer}")

