import math
def is_prime(n):
    if (n<2): return False
    elif (n<4): return True
    elif (n % 2 == 0): return False
    m = int(math.sqrt(n))
    for i in range (3,m+1,2):
        if (n % i ==0): return False
    return True
for i in range (1,101):
    if (is_prime(i)): print(i, end=" ")