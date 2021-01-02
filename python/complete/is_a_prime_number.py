###this problem consist in a function that given a number returns true or false if 
###the number is a prime number

from itertools import permutations
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

#solution three: for this solution we will be iterating from 2 to the square root of the number
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
#edit: the big O should be equal to the last one
#O(sqrt(n))
def is_a_prime_number_4(number, arg = math.sqrt):
    num_str = str(number)
    if number > 1:
        #discard the options where the numbers end in 2, 4, 5, 6, 8, as long as a number ended in those can't be prime
        if num_str[len(num_str) - 1] == 2 or num_str[len(num_str) - 1] == 4 or num_str[len(num_str) - 1] == 5 or num_str[len(num_str) - 1] == 6 or num_str[len(num_str) - 1] == 8:
            return False
        for i in range(2, int(arg(number)) + 1):
            if number % i == 0:
                return False
        return True
    return False


##test --- don't give them too much time, they are all quite similar

#default unit test with some predefined test cases
def default_test(testcase, function):
    a = 4
    b = 13
    c = 23
    d = 20
    e = 10007
    testcase.assertEqual(function(a), False)
    testcase.assertEqual(function(b), True)
    testcase.assertEqual(function(c), True)
    testcase.assertEqual(function(d), False)
    testcase.assertEqual(function(e), True)

#test to ensure that all solutions give the same answer over a range(depth) of parameters
def equality_test(testcase, depth, *args):
    permuts = permutations(args, 2)
    for i in permuts:
        function1 = i[0]
        function2 = i[1]
        for j in range(depth):
            testcase.assertEqual(function1(j), function2(j))


class test(unittest.TestCase):
    #testing function 1
    def test_1(self):
        default_test(self, is_a_prime_number_1)

    #testing function 2
    def test_2(self):
        default_test(self, is_a_prime_number_2)

    #testing function 3
    def test_3(self):
        default_test(self, is_a_prime_number_3)

    #testing function 4
    def test_4(self):
        default_test(self, is_a_prime_number_4)

    #testing that all functios give the same answers
    def test_5(self):
        depth = 10000
        equality_test(self, depth, is_a_prime_number_1, is_a_prime_number_2, is_a_prime_number_3, is_a_prime_number_4)


if __name__ == "__main__":
    unittest.main()