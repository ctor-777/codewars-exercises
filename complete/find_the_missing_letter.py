###this chalenge consist in writing a method that takes an array of 
###consecutive letters and return the missing letter
# problems:
# 1.identify in wich part of the alphabet qe start
# 2.identify wich letter is missing

#dependencies
import unittest
import string



def find_the_missing_letter(chars):
    ###mine solution
    #strart getting the alphabet and finding in them the position fo the 
    #first letter of chars
    alphabet = string.ascii_letters
    start = alphabet.index(chars[0])

    #finding the missing letter
    for i in range(len(chars)):
        if chars[i] != alphabet[start + i]:
            return alphabet[start + i]


##test class
class test(unittest.TestCase):
    def test_1_find_the_missing_letter(self):
        a = ['a','b','c','d','f']
        result = find_the_missing_letter(a)
        self.assertEqual(result, 'e')

    def test_2_find_the_missing_letter(self):
        b = ['O','Q','R','S']
        result = find_the_missing_letter(b)
        self.assertEqual(result, 'P')



if __name__ =="__main__":
    unittest.main()