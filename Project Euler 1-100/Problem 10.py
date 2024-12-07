#Problem 10: Sumamtion of primes
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
        
    return True

def primeSummation(n):
    result = []
    for i in range(1, n):
        if is_prime(i) == True:
            result.append(i)

    summation = sum(j for j in result)
    return summation

assert type(primeSummation(17)) == int
assert primeSummation(17) == 41
assert primeSummation(2001) == 277050
assert primeSummation(140759) == 873608362
assert primeSummation(2000000) == 142913828922