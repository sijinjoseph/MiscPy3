'''
Created on Oct 1, 2011

@author: sjoseph
'''

import sys
l=open(sys.argv[1],'r').read().split('\n')
P=int(l[0].split(' ')[1])
s={}
for i in range(P):
    r=l[i+1].split(' ')
    s.setdefault(r[0], set()).add(r[1])
    s.setdefault(r[1], set()).add(r[0])
for i in range(int(l[P+1])):
    c=l[P+2+i]
    print(len({y for x in s[c] for y in s[x] if y not in s[c] and y!=c}))

#if __name__ == '__main__':
#    if len(sys.argv) <= 1:
#        eoe('''6 7
#frank bob
#bob marley
#bob john
#john frank
#jenny bob
#carol jenny
#carol frank
#3
#frank
#jenny
#bob''')
#    else:
#        with open(sys.argv[1], 'r') as f:
#            eoe(f.read())