import unittest

def rgb(r, g, b):
    rgb = [r,g,b]
    rgb = [str(hex(i))[2:] for i in rgb]
    return "".join(rgb)

class test(unittest.TestCase):
    def test_rgb(self):
        pass


if __name__ == "__main__":
    print(rgb(0,0,0))
    print(rgb(255,255,300))

