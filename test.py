import unittest
import sys
from parse_log import total_time, convert_hour,file_to_dict , open_file, parse_dict


class test_parse(unittest.TestCase):


    def test_open_file(self):
        result = ["09:20-11:00 Introduction\n",
                    "11:00-11:15 Exercises\n",
                    "11:15-11:35 Break"]
        self.assertIsInstance(open_file('planning.log'), list)
        self.assertIsNotNone(open_file('planning.log'))
        self.assertEqual(open_file('planning_test.log'), result)


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


    def test_file_to_dict(self):
        self.assertEqual(file_to_dict(["19:20-19:40 Test"]), {"Test": 20})
        self.assertEqual(file_to_dict(["00:00-03:00 Test2"]),{"Test2": 180})
        self.assertEqual(file_to_dict(["19:00-20:00 Test3","14:00-15:00 Test4"]),{"Test3": 60, "Test4":60})
        self.assertIsInstance(file_to_dict(["19:00-20:00 Test"]),(dict))
        

    def test_dict_parse(self):
        self.assertEqual(parse_dict({'Break': 65},"test.log"), 'Break                  65 minutes      100%')
        self.assertEqual(parse_dict({'Test': 100},"test.log"), 'Test                  100 minutes      100%')
        self.assertNotEqual(parse_dict({'Test': 100},"test.log"), 'Test 100 minutes 100%')



if __name__ == '__main__':
    unittest.main()
