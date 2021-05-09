import unittest
from parse_log import convert_hour, total_time


class test_parse(unittest.TestCase):

    def test_convert_hour(self):
        self.assertEqual(convert_hour("09:20", "11:00"), 100)
        self.assertEqual(convert_hour("09:30", "10:30"), 60)
        self.assertEqual(convert_hour("08:00", "8:30"), 30)
        self.assertNotEqual(convert_hour("12:00", "14:00"), 300)

    def test_total_time_(self):
        self.assertEqual(total_time({1, 2, 3}), 6)
        self.assertEqual(total_time({100, 42, 3}), 145)
        self.assertEqual(total_time([1]), 1)
        self.assertNotEqual(total_time([4, 13, 4]), 43)
        self.assertEqual(total_time(["ffkfk"]), "Incorrect value")
        self.assertEqual(total_time([""]), "Incorrect value")
        self.assertEqual(total_time([]), 0)
        self.assertEqual(total_time({"ffkfk"}), "Incorrect value")


if __name__ == '__main__':
    unittest.main()
