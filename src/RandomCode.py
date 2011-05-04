'''
Created on Apr 12, 2011

@author: sjoseph
'''

from pprint import pprint

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
    
if __name__ == '__main__':
    camel_and_bananas()