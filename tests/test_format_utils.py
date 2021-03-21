import unittest
from common.format_utils import get_formatted_name as fname

class TestFormatUtils(unittest.TestCase):
    """Tests for 'format_utils.py"""

    def test_first_last_name(self):
        """Do name like 'Müller, Thomas' work?"""
        fullname = fname("thomas", "müller")
        self.assertEqual(fullname, "Müller, Thomas")
       

    def test_first_middle_last_name(self):
        """Do name like 'Müller, Thomas' work?"""
                
        fullname = fname("thomas", "müller", "ivanovitsch")
        self.assertEqual(fullname, "Müller, Thomas Ivanovitsch")


    if __name__ == '__main__':
        unittest.main()