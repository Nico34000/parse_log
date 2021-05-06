import unittest
from parse_log import convert_hour


class test_parse(unittest.TestCase):

    def test_convert_hour(self):
        self.assertEqual(convert_hour("09:20", "11:00"), 100)
        self.assertEqual(convert_hour("09:30", "10:30"), 60)
        self.assertEqual(convert_hour("08:00", "8:30"), 30)
        self.assertNotEqual(convert_hour("12:00", "14:00"), 300)

    def test_parse_log(self):
        pass
    #     self.assertEqual(parse_log("09:20-11:00 Introduction"), "Introduction              100 minutes   10%")
    #     self.assertEqual(parse_log("09:30-10:30 Lists and Tuples"), "Lists and Tuples           60 minutes    6%")


if __name__ == '__main__':
    unittest.main()
