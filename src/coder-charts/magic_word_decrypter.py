'''
Created on Oct 1, 2011

@author: sjoseph
'''
import sys
import re
from collections import defaultdict

def magic_word_decrypter(str_encrypted, str_dictionary):
    encrypted_words = re.split('\s+', str_encrypted)
    dictionary = re.split('\s+', str_dictionary)
    
    def normalize(word):
        if len(word) <= 3:
            return word
        else:
            return word[0:1] + ''.join(sorted(word[1:-1])) + word[-1]
        
    normalized_table = defaultdict(list)
    for d_word in dictionary:
        normalized_table[normalize(d_word)].append(d_word)
    
    for e_word in encrypted_words:
        matching_words = normalized_table[normalize(e_word)]
        number_of_matches = len(matching_words)
        if number_of_matches == 0:
            raise Exception("No match found")
        elif number_of_matches == 1:
            print(matching_words[0], end = ' ')
        else:
            print(sorted(matching_words)[0], end = ' ')
        
        
if __name__ == '__main__':
    if len(sys.argv) <= 2:
        magic_word_decrypter('wlemoce to cdeor ctrhas werhe parremgmors utine', '''CHARS
CHARTS
CODED
CODER
PROGRAMMERS
SURELY
THIS
TO
UNITE
UNTIE
WELCOME
WERE
WHERE
YOU'''.lower())
    else:
        with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'r') as d:
            magic_word_decrypter(f.read(), d.read().lower())
