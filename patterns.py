#########################
########## CANONICAL FORM:
########## THE LARGEST ELEMENT GOES AT THE END
#########################

import itertools
import more_itertools
import math


def is_pattern_3(perm, pattern): # works for patterns of length 3
    indices = []
    n = 3
    for i in range(len(perm)-n+1):
        for j in range(i+1, len(perm)-n+2):
            for k in range(j+1, len(perm)-n+3):
                indices += [[perm[i],perm[j],perm[k]]]
    for i in indices:
        for j in range(n):
            i[j] = (i[j], pattern[j])
        first = sorted(i, key=lambda t: t[1])
        second = sorted(i, key=lambda t: t[0])
        if first == second:
            return [a[0] for a in i]
    return False
    
def is_pattern_4(perm, pattern, startfixed=False): # works for patterns of length 4
    indices = []
    n = 4
    if startfixed:
        i = 0
        for j in range(i+1, len(perm)-n+2):
            for k in range(j+1, len(perm)-n+3):
                for l in range(k+1, len(perm)-n+4):
                    indices += [[perm[i],perm[j],perm[k],perm[l]]]
    else:
        for i in range(len(perm)-n+1):
            for j in range(i+1, len(perm)-n+2):
                for k in range(j+1, len(perm)-n+3):
                    for l in range(k+1, len(perm)-n+4):
                        indices += [[perm[i],perm[j],perm[k],perm[l]]]
    for i in indices:
        for j in range(n):
            i[j] = (i[j], pattern[j])
        first = sorted(i, key=lambda t: t[1])
        second = sorted(i, key=lambda t: t[0])
        if first == second:
            return [a[0] for a in i]
    return False
    

    
    
def is_pattern_3_c(perm, pattern):
    n = 3
    for i in range(n):
        temp = pattern.copy()
        temp = temp[i+1:] + temp[:i+1]
        p = is_pattern_3(perm, temp)
        if p:
            p =p[(n-i)+1:] + p[:(n-i)+1]
            return p
    return False
    
def is_pattern_4_c(perm, pattern):
    n = len(perm)
    for i in range(n):
        temp = perm.copy()
        temp = temp[i+1:] + temp[:i+1]
        p = is_pattern_4(temp, pattern, startfixed=True)
        if p:
            p =p[(n-i)+1:] + p[:(n-i)+1]
            return p
    return False
  
def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n = 9

print("Proposition 1")
count = 0
for i in itertools.permutations([i for i in range(1,n+1)]):
    if not is_pattern_3(list(i), [2,1,3]):
        if not is_pattern_3(list(i), [2,3,1]):
            count += 1
print(count)
print(2 ** (n-1))

print("Theorem 1")
count = 0
for i in itertools.permutations([i for i in range(1,n)]):
    if not is_pattern_4_c(list(i) + [n], [1,3,2,4]):
        count += 1
print(count)
print(Fibonacci(2*n-3+1))

print("Theorem 2")
count = 0
for i in itertools.permutations([i for i in range(1,n)]):
    if not is_pattern_4_c(list(i) + [n], [1,3,4,2]):
        count += 1
print(count)
print(2 ** (n-1) - (n-1))



print("Theorem 3")
count = 0
for i in itertools.permutations([i for i in range(1,n)]):
    if not is_pattern_4_c(list(i) + [n], [1,2,3,4]):
        count += 1
print(count)
print(2 ** (n) +1 - 2*n - math.comb(n, 3))
