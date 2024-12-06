#Problem 7: 10001st prime
def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def nthPrime(n):
    rankings = 0
    nth_prime = 0
    arbitrary_number = 1
    while rankings < n:
        if is_prime(arbitrary_number) == True:
            rankings += 1
            nth_prime = arbitrary_number
            arbitrary_number += 1
        else:
            arbitrary_number += 1
    
    return nth_prime

assert type(nthPrime(6)) == int
assert nthPrime(6) == 13
assert nthPrime(10) == 29
assert nthPrime(100) == 541
assert nthPrime(1000) == 7919
assert nthPrime(10001) == 104743