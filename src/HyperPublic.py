from pprint import pprint

def problem1():
    influence = [] 
    from urllib import request
    (filename, _) = request.urlretrieve('http://hyperpublic.com/challenge2input.txt')
    with open(filename, 'r') as f:
        for line in f:
            influence.append(list(line))
     
    in_work_table = [-1 for _ in range(len(influence))]
    def get_user_influence(user_index):
        if in_work_table[user_index] < 0:
            user_influence = 0
            for k in range(len(influence)):
                user_influence += (get_user_influence(k) + 1 if influence[user_index][k] == 'X' else 0)
            in_work_table[user_index] = user_influence
            
        return in_work_table[user_index]      
    
    scores = sorted([get_user_influence(i) for i in range(len(influence))], reverse=True)
    print("".join([str(x) for x in scores[0:3]]))

def problem2():
    points = (2,3,17,23,42,98)
    targets = (2349, 2102, 2001, 1747)
    
    M = [10000000 for _ in range(max(targets) + 1)]
    M[0] = 0
    for i in range(1, len(M)):
        for point in points:
            if(i >= point):
                M[i] = min(M[i], M[i - point] + 1) 

    from functools import reduce
    print(reduce(lambda x,y: x * y, (M[t] for t in targets), 1))
    
if __name__ == "__main__":
    problem2();
