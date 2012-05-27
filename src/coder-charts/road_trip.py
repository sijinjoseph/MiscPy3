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
        adj[a].append((b, (d, (d * 60) / s)))
        adj[b].append((a, (d, (d * 60) / s)))
        
    g = dijikstra(Start, adj, N)
    print(g)
    number_of_queries = int(lines[P + 1])
    for i in range(number_of_queries):
        q = int(lines[P + 2 + i])
        print("{0:.2f}".format(g[q]["min_distance_time"] - g[q]["min_time"]))
              
def dijikstra(start, adj, N):
    q = []
    g = [{"min_distance": float("inf"), "vertex":i, "visited":False, "min_distance_time":0, "min_time":float("inf")} for i in range(N)]
    g[start]["min_distance"] = 0
    g[start]["min_time"] = 0
    q.append(g[start])
    while len(q) > 0:
        node = q.pop(0)
        if node["visited"] == True:
            continue
        else:
            node["visited"] = True
        for neighbor_index, wt in adj[node["vertex"]]:
            neighbor = g[neighbor_index]
            if node["min_distance"] + wt[0] < neighbor["min_distance"]:
                neighbor["min_distance"] = node["min_distance"] + wt[0]
                neighbor["min_distance_time"] = node["min_distance_time"] + wt[1]
            elif node["min_distance"] + wt[0] == neighbor["min_distance"]:
                neighbor["min_distance_time"] = min(neighbor["min_distance_time"], node["min_distance_time"] + wt[1])
            
            if node["min_time"] + wt[1] < neighbor["min_time"]:
                neighbor["min_time"] = node["min_time"] + wt[1]
              
            if neighbor["visited"] == False:
                q.append(neighbor)
    
    return g
        
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        road_trip('''6 8 0
0 1 19 10
1 2 20 10
2 3 20 10
0 4 20 20
4 5 20 20
5 3 20 20
3 5 10 100
3 0 10 100
1
3''')
    else:
        with open(sys.argv[1], 'r') as f:
            road_trip(f.read())