import unittest
import string
#ROT13 is a simple letter substitution cipher that replaces a letter with 
# the letter 13 letters after it in the alphabet. ROT13 is an example of 
# the Caesar cipher.

#Create a function that takes a string and returns the string ciphered 
# with Rot13. If there are numbers or special characters included in 
# the string, they should be returned as they are. Only letters from 
# the latin/english alphabet should be shifted, like in the original 
# Rot13 "implementation".



#first and probably last attempt, has a good performance, redeability and i
#dont see much imporvement.
#O(n)
def rot13(message):
    message = list(message)
    for ind, val in enumerate(message):
        if val.isupper():
            top_limit = 90
            bottom_limit = 65
        else:
            top_limit = 122
            bottom_limit = 97
        
        if ord(val) in range(bottom_limit, top_limit + 1): 
            new_ascii = ord(val) + 13
            if new_ascii > top_limit:
                new_ascii -= 26
        else:
            new_ascii = ord(val)
                
        message[ind] = chr(new_ascii) 
    encrypted_message = "".join(message)

    return encrypted_message

if __name__ == "__main__":
    print(rot13("Test TWO"))