import unittest
from parse_log import parse_log, convert_hour
import os

class test_parse(unittest.TestCase):

    def test_parse_log(self):
        self.assertEqual(parse_log("09:20-11:00 Introduction"), "Introduction              100 minutes   10%")
        self.assertEqual(parse_log("09:30-10:30 Lists and Tuples"), "Lists and Tuples           60 minutes    6%")
        self.assertEqual(convert_hour("09:20","11:00"),"100 minutes")
        self.assertEqual(convert_hour("09:30","10:30"), "60 minutes")



if __name__ == '__main__':
    unittest.main()
