'''
Created on Nov 10, 2009

@author: sjoseph
'''
import math

def is_prime(number):
    '''
    Checks if the given natural number is prime or not
    '''
    if(number < 1):
        raise ValueError("number must be natural")
    
    if(number == 1):
        return False
    
    if(number == 2):
        return True
    
    for factor in range(2, math.ceil(math.sqrt(number)) + 1):
        if (number % factor == 0):
            return False
    
    #No factors found
    return True

if __name__ == "__main__":
    for x in range(2, 100):
        print("{0} : {1}".format(x, is_prime(x))) 