# 1st import unittest
import unittest

# 2nd import whatever you're testing
from name_function import get_formatted_name

# 3rd create a class using the unittest you are interested in
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')

        # 4th use the test condition from the inheritance
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')

        # 4th use the test condition from the inheritance    
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# 5th run test
if __name__ == '__main__': # variable __name__ is set when program is ran
    unittest.main()        # we call unittest.main() which runs the test case
