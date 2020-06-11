###this problem consist in a function that given a number returns true or false if 
###the number is a prime number

import unittest
import math

#first solution: is a simple exhaustive enumeration solution
#O(n) --- not as bad, but the problem requires better efficiency
def is_a_prime_number_1(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    return False

#second solution: another exhaustive enumeration solution, but we reduced the n in a half
#O(n/2) --- Not as bad, but again linear
def is_a_prime_number_2(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    return False

#solution three: for this solution we will be iterating from 2 to teh square root ef the number
#O(sqrt(n)) --- we have reduced a lot the big O 
#that's enought efficiency
def is_a_prime_number_3(number, arg = math.sqrt):
    if number > 1:
        for i in range(2, int(arg(number)) + 1):
            if number % i == 0:
                return False
        return True
    return False

#there's anothers solution, is not much more faster than the last one, but should be faster
#O(?), honestly, i don't want to calculate the big O right now, good night
def is_a_prime_number_4(number, arg = math.sqrt):
    num_str = str(number)
    if number > 1:
        if num_str[len(num_str) - 1] == 2 or num_str[len(num_str) - 1] == 4 or num_str[len(num_str) - 1] == 5 or num_str[len(num_str) - 1] == 6 or num_str[len(num_str) - 1] == 8:
            return False
        for i in range(2, int(arg(number)) + 1):
            if number % i == 0:
                return False
        return True
    return False


##test --- don't give them too much time, they are all quite similar
class test(unittest.TestCase):
    def test_1(self):
        a = 4
        b = 13
        c = 23
        d = 20
        e = 10007
        self.assertEqual(is_a_prime_number_1(a), False)
        self.assertEqual(is_a_prime_number_1(b), True)
        self.assertEqual(is_a_prime_number_1(c), True)
        self.assertEqual(is_a_prime_number_1(d), False)
        self.assertEqual(is_a_prime_number_1(e), True)

    def test_2(self):
        a = 4
        b = 13
        c = 23
        d = 20
        e = 9973
        self.assertEqual(is_a_prime_number_2(a), False)
        self.assertEqual(is_a_prime_number_2(b), True)
        self.assertEqual(is_a_prime_number_2(c), True)
        self.assertEqual(is_a_prime_number_2(d), False)
        self.assertEqual(is_a_prime_number_2(e), True)

    def test_3(self):
        a = 4
        b = 13
        c = 23
        d = 20
        e = 9973
        self.assertEqual(is_a_prime_number_3(a), False)
        self.assertEqual(is_a_prime_number_3(b), True)
        self.assertEqual(is_a_prime_number_3(c), True)
        self.assertEqual(is_a_prime_number_3(d), False)
        self.assertEqual(is_a_prime_number_3(e), True)

    def test_3(self):
        pass
        a = 4
        b = 13
        c = 23
        d = 20
        e = 9973
        self.assertEqual(is_a_prime_number_3(a), False)
        self.assertEqual(is_a_prime_number_3(b), True)
        self.assertEqual(is_a_prime_number_3(c), True)
        self.assertEqual(is_a_prime_number_3(d), False)
        self.assertEqual(is_a_prime_number_3(e), True)

    def test_4(self):
        pass
        a = 4
        b = 13
        c = 23
        d = 20
        e = 9973
        self.assertEqual(is_a_prime_number_4(a), False)
        self.assertEqual(is_a_prime_number_4(b), True)
        self.assertEqual(is_a_prime_number_4(c), True)
        self.assertEqual(is_a_prime_number_4(d), False)
        self.assertEqual(is_a_prime_number_4(e), True)


if __name__ == "__main__":
    unittest.main()