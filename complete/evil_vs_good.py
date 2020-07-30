import unittest
# Middle Earth is about to go to war. The forces of good 
# will have many battles with the forces of evil. Different races 
# will certainly be involved. Each race has a certain worth when 
# battling against others. On the side of good we have the following 
# races, with their associated worth:
#   Hobbits: 1
#   Men: 2
#   Elves: 3
#   Dwarves: 3
#   Eagles: 4
#   Wizards: 10
# On the side of evil we have:
#   Orcs: 1
#   Men: 2
#   Wargs: 2
#   Goblins: 2
#   Uruk Hai: 3
#   Trolls: 5
#   Wizards: 10
# if you add up the worth of the side of good and compare it with the 
# worth of the side of evil, the side with the larger worth will tend 
# to win.

# first attempt, lets see if is posible to improve
def goodVsEvil_v0(good, evil):
    good_list = good.split()
    evil_list = evil.split()

    GOOD_WORTH = [1,2,3,3,4,10]
    EVIL_WORTH = [1,2,2,2,3,5,10]

    good_worths = []
    for index, value in enumerate(good_list):
        good_worths.append(GOOD_WORTH[index] * value)
    
    evil_worths = []
    for index, value in enumerate(evil_list):
        evil_worths.append(EVIL_WORTH[index] * value)
    
    total_good = sum([int(i) for i in good_worths])
    total_evil = sum([int(i) for i in evil_worths])


    if total_good > total_evil:
        return "Battle Result: Good triumphs over Evil"
    elif total_good < total_evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

#second version, only some visual and readability, not performance improvement
#honestly i think is not posible
#O(n)
def goodVsEvil_v1(good, evil):
    good_list = good.split()    
    evil_list = evil.split()

    GOOD_WORTH = [1,2,3,3,4,10]
    EVIL_WORTH = [1,2,2,2,3,5,10]

    total_good = sum([int(GOOD_WORTH[ind]) * int(val) for ind, val in enumerate(good_list)])
    total_evil = sum([int(EVIL_WORTH[ind]) * int(val) for ind, val in enumerate(evil_list)])

    if total_good > total_evil:
        return "Battle Result: Good triumphs over Evil"
    elif total_good < total_evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

#inspired by codewars answers.
def goodVsEvil(good, evil):

    GOOD_WORTH = [1,2,3,3,4,10]
    EVIL_WORTH = [1,2,2,2,3,5,10]

    total_good = sum([int(val) * num for val, num in zip(good.split(), GOOD_WORTH)])
    total_evil = sum([int(val) * num for val, num in zip(evil.split(), EVIL_WORTH)])

    if total_good > total_evil:
        return "Battle Result: Good triumphs over Evil"
    elif total_good < total_evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

class test(unittest.TestCase):
    def test_0_v0(self):
        good = "1 1 1 1 1 1"
        evil = "1 1 1 1 1 1 1"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: Evil eradicates all trace of Good")

    def test_1_v0(self):
        good = "0 0 0 0 0 10"
        evil = "0 1 1 1 1 0 0"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: Good triumphs over Evil")

    def test_2_v0(self):
        good = "1 0 0 0 0 0"
        evil = "1 0 0 0 0 0 0"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: No victor on this battle field")

    def test_0_v1(self):
        good = "1 1 1 1 1 1"
        evil = "1 1 1 1 1 1 1"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: Evil eradicates all trace of Good")

    def test_1_v1(self):
        good = "0 0 0 0 0 10"
        evil = "0 1 1 1 1 0 0"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: Good triumphs over Evil")

    def test_1_v1(self):
        good = "1 0 0 0 0 0"
        evil = "1 0 0 0 0 0 0"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: No victor on this battle field")

    def test_0_codewars(self):
        good = "1 1 1 1 1 1"
        evil = "1 1 1 1 1 1 1"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: Evil eradicates all trace of Good")

    def test_1_codewars(self):
        good = "0 0 0 0 0 10"
        evil = "0 1 1 1 1 0 0"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: Good triumphs over Evil")

    def test_2_codewars(self):
        good = "1 0 0 0 0 0"
        evil = "1 0 0 0 0 0 0"
        res = goodVsEvil_v0(good, evil)
        self.assertEqual(res, "Battle Result: No victor on this battle field")

if __name__ == "__main__":
    unittest.main()