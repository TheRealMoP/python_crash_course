import unittest
from classes.survey import AnonimousSurvey

class TestSurvey(unittest.TestCase):
    """Tests for 'AnonimousSurvey' class"""

    def setUp(self):
        """Create survey, question and answers"""
        
        question = "What was your first language?"
        self.survey = AnonimousSurvey(question)
        self.answers = ["english", "german", "english", "russian"]


    def test_store_single_answer(self):
        self.survey.store_answer("russian")
        self.assertEqual(len(self.survey.answers), 1)
        self.assertIn("russian", self.survey.answers)

    def test_store_few_answers(self):
        for answer in self.answers:
            self.survey.store_answer(answer)

        self.assertCountEqual(self.answers, self.survey.answers)
        for i in range(0, len(self.answers) - 1):
            self.assertEqual(self.answers[i], self.survey.answers[i])