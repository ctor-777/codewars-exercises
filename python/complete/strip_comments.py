import unittest

#Complete the solution so that it strips all text that follows any of a 
# set of comment markers passed in. Any whitespace at the end of the line 
# should also be stripped out.

#Example:
#Given an input string of:
#   apples, pears # and bananas
#   grapes
#   bananas !apples
#The output expected would be:
#   apples, pears
#   grapes
#   bananas


#here's mi solution, not as bad but there are better ones.
def solution(text, markers):
    lines = text.split("\n")
    striped_lines = []
    final = ""
    for line in lines:
        expression = False
        for letter in line:
            if letter in markers:
                expression = True
                ind = line.index(letter)
                break

        if expression:
            striped_lines.append(line[:ind].strip()) 
        else:
            striped_lines.append(line.strip())

    return "\n".join(striped_lines)

#like this one i found in codewars, really good in my opinion :).
def solution_codewars(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

#test class.
class test(unittest.TestCase):
    def test_mine_0(self):
        string = "apples, pears # and bananas\ngrapes\nbananas !apples"
        markers = ["#", "!"]
        result = solution(string, markers)
        self.assertEqual(result, "apples, pears\ngrapes\nbananas" )

    def test_mine_1(self):
        string = "apples, pears # and bananas\ngrapes\nbananas #!apples"
        markers = ["#", "!"]
        result = solution(string, markers)
        self.assertEqual(result, "apples, pears\ngrapes\nbananas")

    def test_codewars_0(self):
        string = "apples, pears # and bananas\ngrapes\nbananas !apples"
        markers = ["#", "!"]
        result = solution_codewars(string, markers)
        self.assertEqual(result, "apples, pears\ngrapes\nbananas" )

    def test_codewars_1(self):
        string = "apples, pears # and bananas\ngrapes\nbananas #!apples"
        markers = ["#", "!"]
        result = solution_codewars(string, markers)
        self.assertEqual(result, "apples, pears\ngrapes\nbananas")

if __name__ == "__main__":
    unittest.main()