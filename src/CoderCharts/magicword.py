'''
Created on Oct 1, 2011

@author: sjoseph
'''
import sys
import re

def rotate(word):
    return (word + word)[1:1 + len(word)]

def scramble(word):
    if len(word) <= 3:
        return word
    else:
        return word[0:1] + rotate(word[1:-1]) + word[-1]
        
def magic_word(input):
    words = re.split('\s+', input)
    for word in words:    
        print(scramble(word))
        
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        magic_word('welcome to coder charts\nsijin is coding this')
    else:
        with open(sys.argv[1], 'r') as f:
            magic_word(f.read())
