# Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number. 
# Sieve of Eratosthenes

# Time complexity: O(nloglogn)

def sieve(n):
    prime = [True for _ in range(n + 1)]
    prime[0], prime[1] = False, False
    i = 2
    while(float(i * i) <= n):
        if prime[i]:
            for j in range(int(i * i), n + 1, i):
                prime[j] = False
        i += 1
    return prime

s = sieve(30)
for p in range(2, 31):
    if s[p]: print(p, sep = ' ')

