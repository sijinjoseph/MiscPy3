'''
Created on May 3, 2011

@author: Sijin Joseph

Explore and learn about string matching algorithms
'''

import timeit
import random
import string
    
def generate_random_text(length):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])

def match_and_verify(pattern, text, func):
    matches = func(pattern, text)
    for match in matches:
        if text[match:match+len(pattern)] != pattern:
            raise Exception("{0} was not found in {1} at position {2}".format(pattern, text, match))
      
def str_find(pattern, text):
    matches = []
    start = 0
    match = text.find(pattern, start)
    while match >= 0:
        matches.append(match)
        start = match + 1
        match = text.find(pattern, start)
        
    return matches
      
def test_performance():
    functions = [str_find]
    for pattern_length in range(5, 1001, 100):
        for text_length in range(5, 1001, 100):
            pattern = generate_random_text(pattern_length)
            text = generate_random_text(text_length)
            for function in functions:
                stmt = "match_and_verify('{}','{}',{})".format(pattern, text, function.__name__)
                setup = "from __main__ import match_and_verify,{}".format(function.__name__)
                time = timeit.timeit(stmt, setup, number=10000)
                print(function.__name__, pattern_length, text_length, time)

if __name__ == '__main__':
    test_performance()