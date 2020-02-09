from ClockIterator import ClockIterator
import unittest

class TestStr(unittest.TestCase):


    def test_first(self):
        self.assertEqual(ClockIterator().user_iter(1), "00:00")

    def test_six_tens(self):
        self.assertEqual(ClockIterator().user_iter(60), "00:59")

    def test_six_tens_and_a_one(self):
        self.assertEqual(ClockIterator().user_iter(61), "01:00")

    def test_one_thousand_four_hundreds_and_four_tens(self):
        self.assertEqual(ClockIterator().user_iter(1440), "23:59")

    def test_one_more_than_most(self):
        self.assertEqual(ClockIterator().user_iter(1441), "00:00")

if __name__ == "__main__":
    unittest.main()