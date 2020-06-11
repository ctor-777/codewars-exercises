import math

def playing_with_digits(n , p):
    list_n = list(str(n))
    list_n = [int(i) for i in list_n]

    digits = sum([list_n[i] ** (p + i)  for i in range(len(list_n))])
    print(digits, math.sqrt(digits))
    k = None
    for i in range(1, digits//2 ):
        if digits/i == n: return i
    if k == None: return -1




if __name__ =="__main__":
    x = playing_with_digits(10383,6)
    print(x)

    """ int(math.sqrt(digits))
    """