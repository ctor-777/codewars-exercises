import unittest

#Complete the solution so that the function will break up camel 
# casing, using a space between words.

#mi solution uwu.
def solution(input):
    if type(input) == str:
        input_list = list(input)
        spaces = []

        for ind, value in enumerate(input_list):
            if value.isupper():
                spaces.append(ind)

        diference = 0
        for i in spaces:
            input_list.insert(i + diference, " ")
            diference += 1
        return "".join(input_list)

    else:
        raise TypeError ('the expected parameter type is: string' ,f' you introduced a parameter of type: {type(input)} ')
        return None

#codewars soluion, as usual, much better than mine unu.
def solution_codewars(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

#test class.
class test(unittest.TestCase):
    def test_0(self):
        text = "helloWorld"
        result = solution(text)
        self.assertEqual(result, "hello World")

    def test_1(self):
        text = "camelCase"
        result = solution(text)
        self.assertEqual(result, "camel Case")

    def test_2(self):
        text = "breakCamelCase"
        result = solution(text)
        self.assertEqual(result, "break Camel Case")

    def test_0_codewars(self):
        text = "helloWorld"
        result = solution_codewars(text)
        self.assertEqual(result, "hello World")

    def test_1_codewars(self):
        text = "camelCase"
        result = solution_codewars(text)
        self.assertEqual(result, "camel Case")

    def test_2_codewars(self):
        text = "breakCamelCase"
        result = solution_codewars(text)
        self.assertEqual(result, "break Camel Case")

if __name__ == "__main__":
    unittest.main()