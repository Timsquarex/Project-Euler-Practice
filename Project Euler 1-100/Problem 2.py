#Problem 2: Even Fibonacci Numbers
def fiboEvenSum(n):
    candidate = [1, 2]
    value = 0
    i = 0
    while value <= n:
        value = candidate[i] + candidate[i+1]
        candidate.append(value)
        i += 1

    candidate_2 = []
    for i in range(len(candidate)-1):
        if candidate[i] % 2 == 0:
            candidate_2.append(candidate[i])
    
    result = sum(candidate_2)
    return result

assert type(fiboEvenSum(10)) == int
assert fiboEvenSum(10) % 2 == 0
assert fiboEvenSum(8) == 10
assert fiboEvenSum(10) == 10
assert fiboEvenSum(34) == 44
assert fiboEvenSum(60) == 44
assert fiboEvenSum(1000) == 798
assert fiboEvenSum(100000) == 60696
assert fiboEvenSum(4000000) == 4613732
