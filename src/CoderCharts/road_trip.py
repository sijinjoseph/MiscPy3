'''
Created on Oct 1, 2011

@author: sjoseph
'''
import sys
from collections import defaultdict

def road_trip(input):
    lines = input.split('\n')
    line0parts = lines[0].split(' ')
    N, P, Start = int(line0parts[0]), int(line0parts[1]), int(line0parts[2])
    adj = defaultdict(list)
    for i in range(1, P + 1):
       parts = lines[i].split(' ')
       a, b, d, s = int(parts[0]), int(parts[1]), float(parts[2]), float(parts[3])
       adj[a].append((b, d, s))
       adj[b].append((a, d, s))
    
    print(adj)
        
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        road_trip('''4 6 0
0 1 30 30
0 2 60 60
0 3 100 60
1 2 20 30
2 3 40 25
3 1 80 65
2
2
3''')
    else:
        with open(sys.argv[1], 'r') as f:
            road_trip(f.read())