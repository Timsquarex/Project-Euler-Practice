#Problem 3: Largest Prime Factor
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def largestPrimeFactor(number):
    candidate = []
    for i in range(1, number+1):
        if number % i == 0:
            candidate.append(i)

    prime_factor = []
    for j in candidate:
        if is_prime(j):
            prime_factor.append(j)
            
    return max(prime_factor)

assert type(largestPrimeFactor(2)) == int
assert largestPrimeFactor(2) == 2
assert largestPrimeFactor(3) == 3
assert largestPrimeFactor(5) == 5
assert largestPrimeFactor(7) == 7
assert largestPrimeFactor(8) == 2
assert largestPrimeFactor(13195) == 29
assert largestPrimeFactor(600851475143) == 6857