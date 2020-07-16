# 1st import unittest
import unittest

# 2nd import class
from survey import AnonymousSurvey

# 3rd create a a child class of a unittest
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    # 4th use setUp so you can instiated class once and re-use for tests
    # *setUp method is inherited from unittest.TestCase
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
