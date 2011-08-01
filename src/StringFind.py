'''
Created on May 3, 2011

@author: Sijin Joseph

Explore and learn about string matching algorithms
'''

import timeit
import random
import string
import collections
import pprint
    
def generate_random_text(length):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])

def insert_pattern(pattern, text):
    insert_point = 0
    insert_full_match = False
    for _ in range(random.randint(0, 10)):
        if(insert_point >= len(text) - 1):
            break
        
        next_insert_point = random.randrange(insert_point + 1, len(text))
        if insert_full_match:
            text = text[0:next_insert_point] + pattern + text[next_insert_point + 1:]
        else:
            text = text[0:next_insert_point] + pattern[:random.randrange(len(pattern))] + text[next_insert_point + 1:]
        insert_full_match = not insert_full_match
        insert_point = next_insert_point
    return text

def match_and_verify(pattern, text, func):
    matches = func(pattern, text)
    known_matches = str_find(pattern, text)
    if matches != known_matches:
        print(pattern, text)
        pprint.pprint(matches)
        pprint.pprint(known_matches)
        raise Exception("Incorrect implementation")

      
def str_find(pattern, text):
    matches = []
    start = 0
    match = text.find(pattern, start)
    while match >= 0:
        matches.append(match)
        start = match + 1
        match = text.find(pattern, start)
        
    return matches
      
def brute_force(pattern, text):
    matches = []
    pattern_length = len(pattern)
    text_length = len(text)
    pp, tp, cmp = 0, 0, 0
    while tp < text_length:
        cmp += 1
        if pattern[pp] == text[tp]:
            pp += 1
            tp += 1
        else:
            tp = tp - pp + 1
            pp = 0
           
        if pp >= pattern_length:
            matches.append(tp - pp)
            pp = 0
            
    #print(cmp)
    return matches 

def karp_rabin(pattern, text):
    matches = []
    hp = hash(pattern)
    lp = len(pattern)

    for i in range(len(text) - len(pattern) + 1):
        if hp == hash(text[i:i+lp]):
            match = True
            for k in range(len(pattern)):
                if pattern[k] != text[i + k]:
                    match = False
                    break
            if match:
                matches.append(i)
    
    return matches

def preMP(pattern):
    pattern_length = len(pattern)
    mpNext = [-1] * (pattern_length + 1)

    i = 1
    while i < pattern_length + 1:
        mpNext[i] = mpNext[i-1] + 1 if (pattern[i-1] == pattern[mpNext[i-1]]) else 0
        i += 1
        
    return mpNext

def preKMP(pattern):
    pattern_length = len(pattern)
    mpNext = [-1] * (pattern_length + 1)

    for i in range(1, pattern_length + 1):
        mpNext[i] = mpNext[i-1] + 1 if (pattern[i-1] == pattern[mpNext[i-1]]) else 0
        
    return mpNext
        
def morris_pratt(pattern, text):
    pre = preMP(pattern)
    matches = []
    pattern_length = len(pattern)
    text_length = len(text)
    pp, tp, cmp = 0, 0, 0
    while tp < text_length:
        cmp += 1
        while pp > -1 and pattern[pp] != text[tp]:
            pp = pre[pp]
        tp+=1
        pp+=1
        
        if pp >= pattern_length:
            matches.append(tp - pp)
            pp = 0
    return matches 
        
def preBM_bad_character(pattern):
    pre = collections.defaultdict(lambda: -1)
    len_pattern = len(pattern) 
    for i in range(len_pattern):
        pre[pattern[i]] = i
        
    return pre

def boyer_moore(pattern, text):
    matches = []
    len_pattern = len(pattern)
    len_text = len(text)
    pre = preBM_bad_character(pattern)
    
    tp = 0
    pp = len_pattern - 1
    while tp <= len_text - len_pattern:
        #print(tp, pp, pre[text[tp + pp]])
        if pattern[pp] != text[tp + pp]:
            skip = max(1, pp - pre[text[tp + pp]])
            tp += skip
            pp = len_pattern - 1
        else:
            pp -=1
            
        if pp < 0:
            matches.append(tp)
            tp += 1
            pp = len_pattern - 1
    
    return matches
        
        
def test_performance():
    functions = [brute_force, morris_pratt, boyer_moore]
    start_length = 10
    step = 5
    number_data_points = 10
    
    for pattern_length in range(start_length, start_length + step*number_data_points+1, step):
        for text_length in range(pattern_length, step*number_data_points+1, step):
            pattern = generate_random_text(pattern_length)
            text = insert_pattern(pattern, generate_random_text(text_length))
            for function in functions:
                stmt = "match_and_verify('{}','{}',{})".format(pattern, text, function.__name__)
                setup = "from __main__ import match_and_verify,{}".format(function.__name__)
                time = timeit.timeit(stmt, setup, number=10)
                print(function.__name__, pattern_length, text_length, time)

if __name__ == '__main__':
    #print(preMP('gcagagag'))
    #test_performance()
    #print(boyer_moore('TIYeHZoAqw', 'tYfBjgSZTIYeHZoAeZSVoIXbUYTIYeHZoAqwPTIYeMChKffARTIYeHZoAqwPTIYeHZoAwypGnMBWCsik'))
    #exit(1)
    import cProfile
    cProfile.run('test_performance()')
    