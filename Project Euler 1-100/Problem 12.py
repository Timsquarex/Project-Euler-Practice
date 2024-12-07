#Problem 12: Highly divisible triangular number
def check_divisor(number):
    divisor = 0
    for i in range(1, number+1):
        if number%i == 0:
            divisor += 1
    return divisor

def divisibleTriangleNumber(n):
    divisors = 0
    k = 0
    result = 0
    while divisors < n:
        k += 1
        result += k
        divisors = check_divisor(result) 
        
    return result

assert type(divisibleTriangleNumber(5)) == int
assert divisibleTriangleNumber(5) == 28
assert divisibleTriangleNumber(23) == 630
assert divisibleTriangleNumber(167) == 1385280
assert divisibleTriangleNumber(374) == 17907120
assert divisibleTriangleNumber(500) == 765766500