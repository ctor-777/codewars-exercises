import unittest

#Given an array (arr) as an argument complete the function countSmileys that 
# should return the total number of smiling faces.

#Rules for a smiling face:
# 1.Each smiley face must contain a valid pair of eyes. Eyes can be marked 
#   as : or ;
# 2.A smiley face can have a nose but it does not have to. Valid characters 
#   for a nose are - or ~
# 3.Every smiling face must have a smiling mouth that should be marked 
#   with either ) or D

#No additional characters are allowed except for those mentioned.
#Valid smiley face examples: :) :D ;-D :~)
#Invalid smiley faces: ;( :> :} :]

#first attempt, works and i thik is the most efficient we can get.
def smiley(faces):
    num_smileys = 0

    valid_eyes = [":", ";"]
    valid_noses = ["-", "~"]
    valid_mouths = [")", "D"]

    for i in faces:
        if i[0] in valid_eyes:
            if i[1] in valid_noses and len(i) == 3:
                if i[2] in valid_mouths:
                    num_smileys += 1
            if i[1] in valid_mouths:
                num_smileys += 1

    return num_smileys

#test class.
class testing(unittest.TestCase):
    def test_0(self):
        faces = []
        result = smiley(faces)
        self.assertEqual(result, 0)

    def test_1(self):
        faces = [':D',':~)',';~D',':)']
        result = smiley(faces)
        self.assertEqual(result, 4)

    def test_2(self):
        faces = [':)',':(',':D',':O',':;']
        result = smiley(faces)
        self.assertEqual(result, 2)

    def test_3(self):
        faces = [';]', ':[', ';*', ':$', ';-D']
        result = smiley(faces)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()

