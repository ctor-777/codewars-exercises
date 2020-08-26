import unittest

#coding challenge moved to useful because of her interesant properties in
# projects, aniway some parts can be documented as a normal coding challenge 

#first working attempt, i don't really care a lot of efficiency because 
# i honestly don't think can be better than linear big O, the improvements
# are only aesthetic and readability.
#O(n)
def same_structure_as(originals,others):
    """given two list return true if the structure of both are equal or 
    false if it aren't
    
    parameters:
        originals (list): the first list to compare
        others (list): the second list to compare
        
    return:
        bool: true if both structures are equal False if not
    """
    
    #verifying that they both are true and returning false if they aren't
    if type(originals) != list or type(others) != list: 
        return False

    #verifying that both lengths are equal  and returning false if they aren't
    if len(originals) != len(others):                   
        return False    

    #verifying that the lengths of both are different of 0, we have 
    # verified that the length of both are equal before, so using the length 
    # of originals is equal to use both lengths.
    if len(originals) != 0:
        
        for original, other in zip(originals, others):
            if type(original) == list and type(other) == list:
                if not same_structure_as(original, other):
                    return False
            elif not type(original) != list or not type(other) != list:
                return False
    return True

#test cases.
class tests(unittest.TestCase):
    def test_1(self):
        original = [1 ,[1 ,1]]
        other = [2 ,[2 ,2]]
        result = same_structure_as(original, other)
        assert result == True

    def test_2(self):
        original = [1 ,[1 ,1]]
        other = [[2 ,2] ,2]
        result = same_structure_as(original, other)
        assert result == False

    def test_3(self):
        original = [[[]],[]]
        other = [[[]],[]]
        result = same_structure_as(original, other)
        assert result == True

    def test_4(self):
        original = [[[]],[]]
        other = [[],[[]]]
        result = same_structure_as(original, other)
        assert result == False

    def test_5(self):
        original = [1 ,1 ,[1 ,1, [1 ,1, [1 ,1 ,[1,1] ,1] ,1] ,1] ,1]
        other = [2 ,2 ,[2 ,2 ,[2 ,2 ,[2 ,2 ,[2 ,2] ,2] ,2] ,2] ,2]
        result = same_structure_as(original, other)
        assert result == True

    def test_6(self):
        original = [1,[1,1], 1, [1,1,[1,1,1]], [1,1,[1,1,[1,1,1,[1,[1,1,1]]]]]]
        other = [2,2,[2,2,[2,2,[2,2,[2,2],2],2],2],2]
        result = same_structure_as(original, other)
        assert result == False

    def test_7(self):
        original = [1 ,'[' ,']' ,4]
        other = ['1',2 ,3 ,'4']
        result = same_structure_as(original, other)
        assert result == True

if __name__ == "__main__":
    unittest.main()