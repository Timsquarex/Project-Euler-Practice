#Problem 5: Smallest Multiple
    #there is a number could be evenly divisible by all of the numbers from (1 to n)
    #so test every possible numbers to see if a certain number could be divisible from 1 to n
    #stop the test when we find the multiple as we need the smallest multiple

    #solve this by using Least Common Multiple(LCM)
    #gcd ==> greatest common divisor

import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a,b)

def smallestMult(n):
    result = 1
    for i in range(1, n+1):
        result = lcm(result, i)
    return result

assert type(smallestMult(5)) == int
assert smallestMult(5) == 60
assert smallestMult(7) == 420
assert smallestMult(10) == 2520
assert smallestMult(13) == 360360
assert smallestMult(20) == 232792560