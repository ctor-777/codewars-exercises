import unittest
import sys
sys.setrecursionlimit(1000000000)

###this problme consist in given a string reverse them, then take the 
###first letter, reverse the rest of letters and so on
###ex:
###     012345 --> 543210 --> 501234 --> 504321 --> ... --> 504132

#that first function reverse a given string
def reversing_str(string_in):
    return string_in[len(string_in)::-1]

#this function do the logic before explained
def reversing_fun(string_in):
    if len(string_in) > 1:
        reversed_str = reversing_str(string_in)
        return reversed_str[0] + reversing_fun(reversed_str[1::])
    return string_in


class test(unittest.TestCase):
    def test_1(self):
        a = "012345"
        self.assertEqual(reversing_fun(a), "504132")


if __name__ == "__main__":
    unittest.main()