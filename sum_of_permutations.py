###this problem consists in create a finction that given a number sum all the permutations
###with the same digits
###ex:
###     sum_of_permutations(123) --- 123 + 132 + 213 + 231 + 312 + 321 = 1332

import unittest
from itertools import permutations

def sum_of_permutations_1(number):
    list_of_numbers = [int(i) for i in str(number)]
    perm = permutations(list_of_numbers, len(list_of_numbers))
    list_of_permutations = []
    for i in range(len(list(perm))):
        list_of_permutations.append('')
        for j in range(len(list(perm)[i])):
            list_of_permutations[i].join(perm[i][j])

    print(list_of_permutations)

class test(unittest.TestCase):
    def test_1(self):
        pass

if __name__ == "__main__":

    sum_of_permutations_1(123)