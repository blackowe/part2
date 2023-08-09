"""
Assignment: Group Project - Part 2
Course: CS362
Author: Erik Blackowicz
Description: Testing Suite for my_datetime()
"""

import unittest
from task2 import my_datetime


class TestFunction2(unittest.TestCase):
    """ Test suite for """

# min non-leap year tests
    def test_nonleap_1(self):
        """ 01-01-1970 00:00:00 """
        expected = "01-01-1970"
        self.assertEqual(my_datetime(0), expected)

    def test_nonleap_2(self):
        """ 12-31-1970 23:59:59 """
        expected = "12-31-1970"
        self.assertEqual(my_datetime(31535999), expected)

    def test_nonleap_3(self):
        """ 01-01-1971 00:00:00 """
        expected = "01-01-1971"
        self.assertEqual(my_datetime(31536000), expected)

# 'special' non-leap year tests
    def test_nonleap_4(self):
        """ 01-01-2100 00:00:00 """
        expected = "01-01-2100"
        self.assertEqual(my_datetime(4102444800), expected)

    def test_nonleap_5(self):
        """ 02-28-2100 23:59:59 """
        expected = "02-28-2100"
        self.assertEqual(my_datetime(4107542399), expected)

    def test_nonleap_6(self):
        """ 03-01-2100 00:00:00 """
        expected = "03-01-2100"
        self.assertEqual(my_datetime(4107542400), expected)

    def test_nonleap_7(self):
        """ 12-31-2100 23:59:59 """
        expected = "12-31-2100"
        self.assertEqual(my_datetime(4133980799), expected)

# max non-leap year tests
    def test_nonleap_8(self):
        """ 01-01-9999 00:00:00 """
        expected = "01-01-9999"
        self.assertEqual(my_datetime(253370764800), expected)

    def test_nonleap_9(self):
        """ 12-31-9999 23:59:59 """
        expected = "12-31-9999"
        self.assertEqual(my_datetime(253402300799), expected)

# min leap year tests
    def test_leap_1(self):
        """ 01-01-1972 00:00:00 """
        expected = "01-01-1972"
        self.assertEqual(my_datetime(63072000), expected)

    def test_leap_2(self):
        """ 02-28-1972 23:59:59 """
        expected = "02-28-1972"
        self.assertEqual(my_datetime(68169599), expected)

    def test_leap_3(self):
        """ 02-29-1972 00:00:00 """
        expected = "02-29-1972"
        self.assertEqual(my_datetime(68169600), expected)

    def test_leap_4(self):
        """ 02-29-1972 23:59:59 """
        expected = "02-29-1972"
        self.assertEqual(my_datetime(68255999), expected)

    def test_leap_5(self):
        """ 03-01-1972 00:00:00 """
        expected = "03-01-1972"
        self.assertEqual(my_datetime(68256000), expected)

    def test_leap_6(self):
        """ 12-31-1972 23:59:59 """
        expected = "12-31-1972"
        self.assertEqual(my_datetime(94694399), expected)

# max leap year boundaries
    def test_leap_7(self):
        """ 02-28-9996 23:59:59 """
        expected = "02-28-9996"
        self.assertEqual(my_datetime(253281167999), expected)

    def test_leap_8(self):
        """ 02-29-9996 00:00:00 """
        expected = "02-29-9996"
        self.assertEqual(my_datetime(253281168000), expected)

    def test_leap_9(self):
        """ 02-29-9996 23:59:59 """
        expected = "02-29-9996"
        self.assertEqual(my_datetime(253281254399), expected)

    def test_leap_10(self):
        """ 03-01-9996 00:00:00"""
        expected = "03-01-9996"
        self.assertEqual(my_datetime(253281254400), expected)

    def test_leap_11(self):
        """ 12-31-9996 23:59:59 """
        expected = "12-31-9996"
        self.assertEqual(my_datetime(253307692799), expected)

    def test_leap_12(self):
        """ 01-01-9997 00:00:00 """
        expected = "01-01-9997"
        self.assertEqual(my_datetime(253307692800), expected)


if __name__ == '__main__':

    unittest.main()
