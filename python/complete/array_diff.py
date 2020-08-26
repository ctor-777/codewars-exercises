import unittest

###this problem consist in rastate to the array a the numbers present
###in b

def array_diff(a , b):
    ###mine solution
    #creates the list when we will store the frequency of b values in a 
    repeated = []
    for i in range(len(b)):
        repeated.append(0)

    #calculating the frequency of teh values if b in a, and soring them in repeated
    for i in range(len(b)):
        for x in range(len(a)):
            if b[i] == a[x]:
                repeated[i] += 1

    #whith the frequency removing the values of b in a
    for i in range(len(b)):
        for x in range(repeated[i]):
            #if the value we try to remove is not in the list will give the ValueError
            try:
                a.remove(b[i])
            except ValueError:
                break
    return a
    
    
def array_diff_better(a , b):
    ##the solution of codewars
    #much easier than mine :(
    return [i for i in a if i not in b]


class test(unittest.TestCase):
    def test_array_diff(self):
        a = [1,2, 2, 3,4,5,5,6,7]
        b = [2,5]
        self.assertEqual(array_diff(a,b), [1,3,4,6,7])

    def test_array_diff_better(self):
        a = [1,2, 2, 3,4,5,5,6,7]
        b = [2,5]
        self.assertEqual(array_diff_better(a,b), [1,3,4,6,7])


if __name__ == "__main__":
    unittest.main()