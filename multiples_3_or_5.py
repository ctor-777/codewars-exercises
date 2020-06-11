###this problem consist in doing a funcion that will give you the multiples of 3 and 5
###under the given number, adn finally sum all the relusts
import unittest


#solution 1: a exhaustive enumeration algorithm
#O(n) is a really good answer, but i think i can do it better
def multiples_3_or_5_1(n):
    results = []
    for i in range(1, n):
        if i % 3 == 0:
            if i not in results:
                results.append(i)

        if i % 5 == 0:
            if i not in results:
                results.append(i)

    return sum(results)

#solution 2: in this case we only do the necessary operation,
#not measure all the posibilities in n
#O(log n)?, i don't really know, but should be faster
def multiples_3_or_5_2(n):
    ran = range(1, (n // 3) + 1)
    results = []
    print(ran)
    for i in ran:
        if 3 * i not in results and 3 * i < n:
            results.append(3 * i)
        if 5 * i not in results and 5 * i < n:
            results.append(5 * i)
    return sum(results)

class test(unittest.TestCase):
    def test_1(self):
        
        res = multiples_3_or_5_1(10)
        self.assertEqual(res, 23)

    def test_2(self):
        
        res = multiples_3_or_5_2(10)
        self.assertEqual(res, 23)

if __name__ == "__main__":
    unittest.main()