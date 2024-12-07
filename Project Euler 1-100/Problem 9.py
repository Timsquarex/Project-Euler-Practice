#Problem 9: Special Pythagorean Triplet
def specialPythagoreanTriplet(n):
    for a in range(1, 1000):
        for b in range(a + 1, 1000): #for a < b < c
            c = n - a - b
            if a**2 + b**2 == c**2 and a+b+c == n:
                return a*b*c

assert type(specialPythagoreanTriplet(24)) == int
assert specialPythagoreanTriplet(24) == 480
assert specialPythagoreanTriplet(120) == 49920 or 55080 or 60000
assert specialPythagoreanTriplet(1000) == 31875000
