'''
Created on Apr 12, 2011

@author: sjoseph
'''

from pprint import pprint
from itertools import product, combinations

def camel_and_bananas():
    total_distance = 1000
    banana_per_mile = 1
    max_load = 1000
    start_load = 3000
    
    def bananas_left(start_count, distance):
        number_of_trips = (start_count//max_load)
        return max(0, number_of_trips * max_load - (2*number_of_trips - 1) * distance * banana_per_mile)
    
    def print_path(index):
        if index > 0:
            print("{} bananas at mile {} starting with {} bananas at mile {}".format(M[index], index, M[index - W[index]], index - W[index]))
            print_path(index - W[index])
            
    M = [0] * (total_distance + 1)
    W = [0] * (total_distance + 1)
    M[0] = start_load
    
    for n in range(1, total_distance + 1):
        for k in range(n):
            if bananas_left(M[k], n-k) > M[n]:
                M[n] = bananas_left(M[k], n-k)
                W[n] = n-k
         
    #pprint(M)
    #pprint(W)
    print_path(total_distance)
    
#You have 40 bowls, all placed in a line at exact intervals of 1 meter. You also have 9 oranges.
#You wish to place all the oranges in the bowls, no more than one orange in each bowl,
#so that there are no three oranges A, B, and C such that the distance between A and B is equal to the distance between B and C.
#How many ways can you arrange the oranges in the bowls?.
def bittorrent_dev_challenge():
    number_of_bowls = 40
    number_of_oranges = 9
    
    def solve(state, oranges_left, solutions):
        print('+')
        if oranges_left == 0:
            solution = ''.join(state)
            pprint(solution)
            solutions.add(solution)
        
        print(''.join(state))
        len_state = len(state)
        for i in range(len_state):
            if state[i] == '0':
                new_state = list(state)
                new_state[i] = '1'
                #print(i)
                filled_bowls = list(filter(lambda i: new_state[i] == '1', range(len_state)))     
                distances = [abs(i - j) for i, j in combinations(filled_bowls, 2)]
                if len(distances) != len(set(distances)):
                    #pprint(filled_bowls)
                    #pprint(sorted(distances))
                    #print('Bad state => ', ''.join(state))
                    return
                else:
                    #print('Good state')
                    pass
                
                distances = set(distances) 
                for m, n in product(filled_bowls, distances):
                    if m - n >= 0 and new_state[m - n] == '0':
                        new_state[m - n] = 'x'
                    
                    if m + n < len_state and new_state[m + n] == '0':
                        new_state[m + n] = 'x'
                        
                solve(new_state, oranges_left - 1, solutions)
                
    solutions = set()
    solve(['0'] * number_of_bowls, number_of_oranges, solutions)
    print(len(solutions))
                        
    
def test_pass_by_ref():
    def changex(x):
        x = 10
        
    x = 5
    changex(x)
    print(x)
    
def score_predictors():
    data = [
            [1,1,1,1,1,0,0,0,0,0],
            [1,1,1,0,0,0,0,0,1,1],
            [1,0,1,0,1,0,1,0,1,0],
            [0,0,0,0,0,1,1,1,1,1],
            [0,0,0,0,0,0,1,1,1,1],
            [0,0,0,0,0,0,0,1,1,1],
            [1,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1]]
    
    for d in data:
        sum = 0
        for i in range(len(d)):
            sum += (d[i] * (i + 1))
        
        print("Score for {0} is {1}".format(d, sum / ((len(d) * (len(d) + 1)) / 2)))
    
    
if __name__ == '__main__':
    #camel_and_bananas()
    #test_pass_by_ref()
    #bittorrent_dev_challenge()
    score_predictors()