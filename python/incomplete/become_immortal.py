import unittest
import numpy as np

###in this problem we have to calculate how much time will be given to
###the "Grandpatriarch" form the young "worshippers" following this rules:
###     1.the worshippers line up in a magical rectangle, of dimensions m and n
###     2.the worshippers can give time equal to the xor of the column and the row
###     3.the donation of time have a transmission loss (l, in seconds)
###     4.the transmission counter has a limit t, if the transmission of time 
###       is bigger it will restart

#problems:
#   1.create the magic ractange of dimensions m and n
#   2.calculate the values of how much time can give any worshippers
#   3.substract to every donation the transmission loss (ever will be bigger then 0)
#   4.calculate how much time will be given to the Grandpatriarch acording to t


##firts and easy implementig solution, but lot of inefficency --- O(m + 3 * m * n) = O(m * n)
def become_immortal_1(m, n , l , t):
    # 1.creating the magic rectange of dimensions m and n --- O(m)
    magic_rectangle = []
    for i in range(m):
        magic_rectangle.append([])

    # 2.asingning values to the magic rectangle --- O(m * n)
    for i in range(m):
        for j in range(n):
            magic_rectangle[i].append(i ^ j)

    # 3.substracting the transmission loss --- O(m * n)
    for i in range(m):
        for j in range(n):
            if magic_rectangle[i][j] > l:
                magic_rectangle[i][j] -= l
            else:
                magic_rectangle[i][j] = 0

    # 4.calculating the total of time --- O(m * n)
    total = 0
    for i in range(m):
        for j in range(n):
            if total > t:
                total -= t
            total += magic_rectangle[i][j]

    print(bin(total))
    return total


##second solution, a littel bit more efficient but still polinomial --- O(m * n)
def become_immortal_2(m , n , l , t):
    magic_rectangle = []
    total = 0
    for i in range(m):
        magic_rectangle.append([]) 
        for j in range(n):
            magic_rectangle[i].append(i ^ j)
            if magic_rectangle[i][j] > l:
                magic_rectangle[i][j] -= l
            else:
                magic_rectangle[i][j] = 0
            if total > t:
                total -= t
            total += magic_rectangle[i][j]

    return total



class test(unittest.TestCase):
    def test_1_find_the_missing_letter(self):
        result = become_immortal_2(8,5,1,100)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    """ unittest.main() """
    res = become_immortal_1(8, 8 , 1 , 100)
    print(res)