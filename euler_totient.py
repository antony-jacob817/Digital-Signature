import math

def euler_totient(n):
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result
