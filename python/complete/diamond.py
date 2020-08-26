from math import floor, ceil

#You need to return a string that looks like a diamond shape when 
# printed on the screen, using asterisk (*) characters. Trailing 
# spaces should be removed, and every line must be terminated with 
# a newline character (\n).

#Return null/nil/None/... if the input is an even number or negative, as 
# it is not possible to print a diamond of even or negative size.

#in this challenge i will not do any test cases because is a visual challenge,
#not a logic one.

#first and probably last attempt, it's enought good.
def give_me_a_diamond(size):
    if size % 2 == 0 or size < 1:
        return None
    
    diamond = ""

    for i in range(size):
        if i < size/2:
            layer = " " * (int(size/ 2) - i) + ("*" + "**" * i) + "\n"
        else:
            temp = int(i - (size / 2)) + 1 
                #^^^^this part augment by 1 starting when the loop arrives 
                # to the center of the diamond, then in the next line we 
                # substract this to the size / 2, that gives a descendent 
                # counter, ideal for the bottom part of the diamond
            layer = " " * (i - int(size/2)) + ("*" + "**" * (int(size/2) - temp)) + "\n"

        diamond += layer
        
    return diamond

#right, here's another because i like the use of absolute value. 
# I have to admit it, is simpler than mine unu.
def diamond_codewars(n):
    if n < 0 or n % 2 == 0:
        return None
    diamond = ""
    for i in range(n):
        diamond += " " * int(abs(floor(n/2) - i))
        diamond += "*" * (n - abs((n-1) - 2 * i))
        diamond += "\n"
    return diamond

if __name__ == "__main__":
    print(give_me_a_diamond(7))
    print(diamond_codewars(7))