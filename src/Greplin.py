'''
Created on Oct 13, 2010

@author: sjoseph
'''

import itertools
import math
import collections
import functools
import queue
import operator
import urllib.request
    
def problem1():
    u = urllib.request.urlopen('http://challenge.greplin.com/static/gettysburg.txt')
    input = u.read();
    #input = 'hello xxx'
    for l in range(len(input), 0, -1):
        for i in range(len(input) - l + 1):
            if(is_simple_palindrome(input[i:i+l+1])):
                print(input[i:i+l+1])
                return
            
def is_simple_palindrome(str):
    left, right = 0, len(str) - 1
    while left < right and str[left] == str[right]:
        left = left + 1
        right = right - 1
    
    if(left == right):
        return True
    else:
        return False
    
if __name__ == '__main__':
    problem1()