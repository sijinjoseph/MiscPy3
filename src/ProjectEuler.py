'''
Created on Oct 16, 2009

@author: sjoseph
'''

import itertools
import MyUtils
import math
import collections
import functools
import queue
import operator 

def problem29(maxA, maxB):
    result = set()
    for x,y in itertools.product(range(2, maxA + 1), range(2, maxB + 1)):
        # print("{0},{1}".format(x,y))
        result.add(x ** y)
    print(len(result))   
    
def problem27(maxA, maxB):
    answer = -1;
    max_consecutive_primes = 0
    for a,b in itertools.product(range(-maxA, maxA + 1), range(-maxB, maxB + 1)):
        func = lambda n: n*n + a*n + b
        consecutive_primes = number_of_consecutive_primes(func)
        #print(consecutive_primes)
        if consecutive_primes > max_consecutive_primes:
            answer = a * b
            max_consecutive_primes = consecutive_primes
            
    print(answer)
    
def number_of_consecutive_primes(func):
    count = 0;
    for n in itertools.count():
        val = func(n)
        if(val != 0 and MyUtils.is_prime(abs(val))):
            count = count + 1
        else:
            break
    return count
        
def problem30():
    result = 0
    for x in range(11, (9 ** 5) * 6 + 1):
        if x == sum([int(n) ** 5 for n in str(x)]):
            result += x
            
    print(result)
    
def problem31():
    denominations = (1,2,5,10,20,50,100,200)
    result = 0
    for r in range(1, 201):
        for combination in itertools.combinations_with_replacement(denominations, r):
            print(combination)
            if(sum(combination) == 200):
                result += 1
        
    print(result)

def problem31DP():
    D = (1,2,5,10,20,50,100,200)
    M = [[1]*len(D) for _ in [0]*201]
    for x in range(1, 201):
        for y in range(0, len(D)):
            #print(x,y)
            M[x][y] = (M[x][y - 1] if y >= 1 else 0) + (M[x - D[y]][y] if x >= D[y] else 0)
        print(M[x])
        
    print(M[200][len(D) - 1])
    print(M[5][len(D) - 1])
    
    
def problem42():
    f = open('c:/temp/words.txt', 'r')
    data = f.read()
    f.close()
    
    words = [w.strip('"') for w in str(data).split(',')]
    triange_numbers = [(n*(n+1))//2 for n in range(1, 25)]
    count = 0
    for word in words:
        s = sum([ord(x) - ord('A') + 1 for x in word])
        if s in triange_numbers:
            count += 1
    print(count)
        

def problem240():
    result = 0;
    dice_faces = 12
    total_dice = 20
    top_dice = 10
    sum_to_match = 70
    
    for x in itertools.combinations_with_replacement(range(1, dice_faces + 1), top_dice):
        if(sum(x) == sum_to_match):
            m = min(x)
            for y in itertools.combinations_with_replacement(range(1, m + 1), total_dice - top_dice):
                z = x + y
                #print(z)
                freqs = collections.defaultdict(lambda : 0)
                for k in z:
                    freqs[k] += 1
                
                product = functools.reduce(lambda x,y : x * math.factorial(y), freqs.values(), 1)                    
                result += (math.factorial(total_dice) // product)
    print(result)

def number_of_combinations_with_replacement_order_insignificant(n, r):
    #http://www.delphiforfun.org/Programs/SelectwithReplacment.htm
    return math.factorial(n + r - 1) // (math.factorial(n - 1) * math.factorial(r))

def problem244():
    def update_checksum(move, current_checksum):
        return (current_checksum * 243 + ord(move)) % 100000007
    
    def str_swap(input, i, j):
        l = list(input)
        l[i], l[j] = l[j], l[i]
        return "".join(l)

    def generate_new_states(state):
        config = state[0]
        current_checksum = state[1]
        posW = config.find('W')
        (posX, posY) = divmod(posW, 4)
        
        moves = []
        if posY > 0:
            move = 'R'
            moves.append([str_swap(config, posW, posW - 1)   , update_checksum(move, current_checksum)])
            
        if posY < 3:
            move = 'L'
            moves.append([str_swap(config, posW, posW + 1)   , update_checksum(move, current_checksum)])
            
        if posX > 0:
            move = 'D'
            moves.append([str_swap(config, posW, posW - 4)   , update_checksum(move, current_checksum)])
            
        if posX < 3:
            move = 'U'
            moves.append([str_swap(config, posW, posW + 4)   , update_checksum(move, current_checksum)])
            
        return moves
        
    start = ['WRBBRRBBRRBBRRBB', 0]
    target = 'WBRBBRBRRBRBBRBR'
    visited = set(start[0])
    paths_to_target = collections.defaultdict(list)
    q = queue.PriorityQueue()
    q.put((0, start))
    while q.empty() == False:
        (path_length, state) = q.get()
        new_states = generate_new_states(state)
        for new_state in new_states:
            config = new_state[0]
            if config == target:
                paths_to_target[path_length + 1].append(new_state)
            elif config not in visited:
                q.put((path_length + 1, new_state))
                visited.add(config)
            
    print(paths_to_target)
    min_length = min(paths_to_target.keys())
    print(sum((x[1] for x in paths_to_target[min_length])))
    

def problem34():
    ans = 0
    for num in range(10, 9*math.factorial(9) + 1):
        s = sum((math.factorial(int(x)) for x in str(num)))
        if (s == num):
            print(num)
            ans += num
    print(ans)
    
def problem36():
    ans = 0
    for num in range(1, 1000001):
        if str(num) == str(num)[::-1] and "{0:b}".format(num) == "{0:b}".format(num)[::-1]:
            ans += num
    print(ans)
    
def problem23():
    def is_abundant(num):
        print
        return sum([x for x in range(1, (num // 2) + 1) if num % x == 0]) > num
    
    abundants = [x for x in range(1, 28123 + 1) if is_abundant(x)]
    print(len(abundants))
    sum_of_two_abundants = set([sum(pair) for pair in itertools.combinations_with_replacement(abundants, 2)])
    
    ans = sum(x for x in range(1, 28123 + 1) if x not in sum_of_two_abundants)
    print(ans)        
    
def is_prime(num):
    if num < 2:
        raise ValueError("number cannot be less than two")
    
    if num == 2:
        return True
    
    for x in range(2, math.floor(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    
    return True

def problem50():
    limit = 1000000
    bit_primes = generate_primes(limit)
    primes = [i for i,v in enumerate(bit_primes) if v == 1]
    print(primes)
            
    max_index = 0
    for i, v in enumerate(primes):
        if v > limit // 2:
            max_index = i + 1
            break
    print(max_index)
    
    max_consecutive = 0
    max_prime = 0
    for start_index in range(max_index + 1):
        if max_index - start_index <= max_consecutive:
            break
        
        sum = 0
        for seq_length in range(1, max_index - start_index + 1):
            sum += primes[start_index + seq_length - 1]
            if sum >= limit:
                break
            
            if seq_length > max_consecutive and sum < limit and bit_primes[sum] == 1:
                max_consecutive = seq_length
                max_prime = sum
         
    print(max_consecutive, max_prime)

def problem26():
    def find_decimal_cycle(denominator):
        numerator = 1
        
        divmods = []
        while True:
            while numerator < denominator:
                numerator *= 10
            
            q, r = divmod(numerator, denominator)    
            divmods.append((q, r))
            #print(divmods)
            if r == 0:
                return 0
            
            for k in range(len(divmods) - 1):
                if divmods[k][1] == r:
                    return len(divmods) - 1
            
            numerator = r
        
    max_length = -1
    max_x = 0
    for x in range(1, 1000):
        len_cycle = find_decimal_cycle(x)
        if max_length < len_cycle:
            max_length = len_cycle
            max_x = x
        print("{}, {}".format(x, len_cycle))
        
    print(max_x, max_length)
                
def problem32():
    prod = 0
    processed = set()
    for p in itertools.permutations('123456789'):
        equal_pos = 5
        s = ''.join(p)
        # m1 * m2 = r
        for mul_pos in range(1, equal_pos):
            m1 = int(s[:mul_pos])
            m2 = int(s[mul_pos:equal_pos])
            r = int(s[equal_pos:])
            if m1 * m2 == r and r not in processed:
                prod += r
                processed.add(r)
                print("{} x {} = {}".format(m1, m2, r))
    print(prod)
    
def generate_primes(max):
    primes = [1] * max
    primes[0] = primes[1] = 0
    
    for x in range(2, len(primes)):
        if primes[x] == 1:
            for k in range(2, math.ceil(len(primes) / x)):
                primes[x * k] = 0
    
    return primes   

def rotations(iterable):
    i2 = iterable * 2
    l = len(iterable)
    for k in range(l):
        yield i2[k:k + l]
    
def problem35():
    limit = 1000000
    bit_primes = generate_primes(limit)
    count = 0
    for i in (k for k in range(len(bit_primes)) if bit_primes[k] == 1):     
        if all([bit_primes[int(r)] == 1 for r in rotations(str(i))]):
            print(i)
            count += 1
                
    print("Ans = {}".format(count))
            
def problem37():
    def truncations(s):
        for k in range(1, len(s)):
            yield s[k:]
            
        for k in range(1, len(s)):
            yield s[0:k]
        
    limit = 1000000
    bit_primes = generate_primes(limit)
    
    matches = []
    for x in range(10, len(bit_primes)):
        if bit_primes[x] == 0:
            continue
        
        if all([bit_primes[int(t)] == 1 for t in truncations(str(x))]) == True:
            matches.append(x)
            print(x)
        
        if len(matches) >= 11:
            break
    
    print("Ans = {}".format(sum(matches)))
                    
def problem38():
    def generate_products(num):
        s = str(num)
        for x in range(2, 10):
            s += str(num * x)
            yield s
    
    pandigitals = {''.join(x) for x in itertools.permutations('123456789')}
    max_pandigital = 0
    for num in range(1, 10000):
        for product in generate_products(num):
            if (len(product) == 9) and (product in pandigitals) and (int(product) > max_pandigital):
                print(product)
                max_pandigital = int(product)
    
    print("Ans = {}".format(max_pandigital))
    
def problem39():
    triplets = []
    limit = 1000
    for a in range(1, limit):
        for b in range(a, limit):
            for c in range(b, limit):
                if a + b + c < limit and a * a + b * b == c * c:
                    print(a,b,c)
                    triplets.append((a,b,c))
    
    perimeters = [sum(x) for x in triplets]
    counts = collections.Counter(perimeters)
    print(counts.most_common(1))
    
def problem41():
    digits = '987654321'
    for k in range(len(digits)):
        for p in itertools.permutations(digits[k:]):
            num = int(''.join(p))
            print(num)
            if is_prime(num):
                print("Ans = {}".format(num))
                return
        
def problem40():
    product = 1
    next_index_to_process = 1
    current_index = 0
    for x in range(1, 1000000):
        s = str(x)
        if next_index_to_process > current_index and next_index_to_process <= current_index + len(s):
            product *= int(s[next_index_to_process - current_index - 1])
            print(product)
            next_index_to_process *= 10
            if next_index_to_process > 1000000:
                return
        
        current_index += len(s)
            
def problem43():
    primes = [2,3,5,7,11,13,17]
    sum = 0

    for p in itertools.permutations('0123456789'):
        s = ''.join(p)
        if all([int(s[k:k+3]) % primes[k - 1] == 0 for k in range(1, 8)]):
            print(s)
            sum += int(s)
    
    print("Ans = {}".format(sum))
    
def problem28():
    limit = 1001
    M = [[0] * limit for _ in range(limit)] 
    c_row = limit // 2
    c_col = limit // 2
    M[c_row][c_col] = 1
    
    top, left, bottom, right = c_row, c_col, c_row, c_col
    next_num = 2
    while c_col < limit - 1:
        c_col += 1
        
        #expand grid
        top -= 1
        left -= 1
        bottom += 1
        right += 1
        
        for c_row in range(c_row, bottom + 1):
            M[c_row][c_col] = next_num
            next_num += 1
            
        for c_col in range(right - 1, left - 1, -1):
            M[c_row][c_col] = next_num
            next_num += 1
            
        for c_row in range(bottom - 1, top - 1, -1):
            M[c_row][c_col] = next_num
            next_num += 1
            
        for c_col in range(left + 1, right + 1):
            M[c_row][c_col] = next_num
            next_num += 1

    sum = 0
    for x,y in itertools.product(range(limit), range(limit)):
        if x == y or x + y == limit - 1:
            sum += M[x][y]
    
    print("Ans = {}".format(sum))
    
def problem81():
    f = open('c:\\temp\\matrix.txt')
    lines = f.readlines()
    f.close()
    
    I = []
    for line in lines:
        I.append([int(x) for x in line.strip().split(',')])

    M = [[0] * len(I) for _ in range(len(I))]
    M[0][0] = I[0][0]
    
    for row, col in itertools.product(range(len(I)), range(len(I))):
        if row == 0 and col > 0:
            M[row][col] = M[row][col - 1] + I[row][col]
        
        if col == 0 and row > 0:
            M[row][col] = M[row - 1][col] + I[row][col]
            
        if row > 0 and col > 0:
            M[row][col] = min(M[row][col - 1] + I[row][col], M[row - 1][col] + I[row][col]) 
            
    print(M[-1][-1])
    
def problem82():
    f = open('c:\\temp\\matrix.txt')
    lines = f.readlines()
    f.close()
    
    I = []
    for line in lines:
        I.append([int(x) for x in line.strip().split(',')])

    I = [
         [131,    673,    234,    103,    18],
         [201,    96,    342,    965,    150],
         [630,    803,    746,    422,    111],
         [537,    699,    497,    121,    956],
         [805,    732,    524,    37,    331]]
    
    ans = 0
    for start in range(len(I)):
        M = [[0] * len(I) for _ in range(len(I))]
        M[0][start] = I[0][start]
        
        for row, col in itertools.product(range(len(I)), range(len(I))):
            if row == 0 and col > 0:
                M[row][col] = M[row][col - 1] + I[row][col]
            
            if col == 0 and row > 0:
                M[row][col] = M[row - 1][col] + I[row][col]
                
            if row > 0 and col > 0:
                M[row][col] = min(M[row][col - 1] + I[row][col], M[row - 1][col] + I[row][col]) 
            
    print(ans)
    
def problem45():
    limit = 100000
    
    T = [(x*(x+1)) // 2 for x in range(1,limit)]
    P = {(x*(3*x-1)) // 2 for x in range(1,limit)}
    H = {(x*(2*x-1)) for x in range(1,limit)}

    for k in range(285, limit - 1):
        if (T[k] in P) and (T[k] in H):
            print(T[k])
            return
        
    print("Not found")
        
def problem51():
    def generate_numbers(str_num, indexes):
        #0 is not a valid choice for digit if any of the indexes is a leading one
        start_digit = 0
        if 0 in indexes:
            start_digit = 1
            
        for digit in range(start_digit, 10):
            s = list(str_num)
            for i in indexes:
                s[i] = str(digit)
                
            yield int(''.join(s))
            
    limit = 1000000
    target_family_length = 8
    bit_primes = generate_primes(limit)
    for p in range(11, len(bit_primes)):
        if bit_primes[p] == 0:
            continue
        
        s = str(p)
        for num_stars in range(1, len(s) - 1):
            for c in itertools.combinations(range(len(s)), num_stars):
                prime_family = [x for x in generate_numbers(s,c) if bit_primes[x] == 1]
                if(len(prime_family) == target_family_length):
                    print(prime_family)
                    return
                
    print("not found")
                    
    
def problem44():
    limit = 1000
    P = [(x*(3*x-1)) // 2 for x in range(1,limit)]
    D = []
    for j in range(len(P)):
        for k in range(j, len(P)):
            if P[k] + P[j] in P and P[k] - P[j] in P:
                print(P[k], P[j])
                D.append(P[k] - P[j])
    
    print(min(D))                      
    
def binary(N, padding):
    return "{{0:0{0}b}}".format(padding).format(N)

def problem265(N):   
    def search(state, current, sum):
        candidates = [k for k,v in state.items() if v == 0 and current.endswith(k[:-1])]
        max_index = max(state.values())
        if(len(candidates) == 0):
            if(max_index == len(state) and current.endswith(binary(0, N-1))):
                sorted_state = sorted(state.items(), key=operator.itemgetter(1))
                match = int(''.join([k[0] for k,v in sorted_state]), 2)
                print("Match = {0:b} : {0}".format(match))
                sum[0] += match
        else:  
            for candidate in candidates:
                new_state = state.copy()
                new_state[candidate] = max_index + 1
                search(new_state, candidate, sum)
                
    state = {}
    for i in range(2**N):
        state[binary(i, N)] = 0;
    
    state[binary(0, N)] = 1    
    sum = [0]
    search(state, binary(0, N), sum)
    print("S({0}) = {1}".format(N, sum[0]))

if __name__ == "__main__":
    problem265(5) 