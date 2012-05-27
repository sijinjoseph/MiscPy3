'''
Created on Oct 1, 2011

@author: sjoseph
'''
import sys
import re
from collections import defaultdict
import smtplib

def crab_fishermen(input):
    lines = re.split('\n', input)
    N = int(lines[0])
    points = []
    for i in range(N):
        point = re.split('\s+', lines[i+1])
        points.append((float(point[0]), float(point[1])))

    U = (-1 * N * sum((x*y for x,y in points)) + sum((x for x,_ in points))*sum((y for _,y in points)))/(N*sum((x*x for x,_ in points)) - pow(sum((x for x,_ in points)), 2))
    print(U, end =' ')
    print('1.0', end = ' ')
    V = (-1*sum((y for _,y in points)) - U*sum((x for x,_ in points))) / N
    print(V)
    
    print(pow(sum((pow((U*x) + (1.0*y) + V, 2) for x,y in points)), 0.5)) 
        
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        crab_fishermen('''10
-34.17 24.17
3.69 -3.57
-13.32 8.49
-49.70 35.97
39.24 -31.06
-1.48 -0.57
-21.05 14.40
33.74 -25.90
-7.93 4.87
-7.27 4.34''')
    else:
        with open(sys.argv[1], 'r') as f:
            crab_fishermen(f.read())
