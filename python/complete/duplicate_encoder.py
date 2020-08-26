import unittest

###this problem consist in transformin every letter in a word 
### into parentheses, putting ( if the letter only appears one time and ) 
### if it appears more than once


def duplicate_encoder(word_o):
    ###mine solution
    frequency = {}
    print(word_o)

    #casefonding the array to avoid uppper letters
    word = word_o.casefold()
    print(word)

    #computing the frequency of every letter in word_o
    for i in range(len(word)):
        if word[i] in frequency.keys():
            frequency[word[i]] += 1
        else:
            frequency[word[i]] = 1

    #inserting ) if the frequency is bigger to one or ( if it is not
    new_array = ""
    for i in range(len(word)):
        if frequency[word[i]] > 1:
            new_array += ")"
        else:
            new_array += "("

    return new_array
    

class test(unittest.TestCase):
    def test_duplicate_encoder(self):
        word = "Success"
        self.assertEqual(duplicate_encoder(word), ")())())")


if __name__ == "__main__":
    unittest.main()