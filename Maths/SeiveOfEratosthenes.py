
from typing import List

def seive(n:int)->List[int]:

    if n < 2:
        return []

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i]]





def seive_optimized(n: int)->List[int]:

    if n < 2:
        return []

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, 2*i):
                is_prime[j] = False

    primes = [2] if n>=2 else []
    primes += [i for i in range(3, n+1, 2) if is_prime[i]]

    return primes


if __name__ == '__main__':
    n = 30
    print(seive(n))
    print(seive_optimized(n))
