#Problem 6: Sum square difference
def sumSquareDifference(n):
    sum_of_the_squares = 0
    square_of_the_sum = 0
    diff = 0

    for i in range(1, n+1, 1):
        sum_of_the_squares += i**2
        square_of_the_sum += i

    square_of_the_sum = square_of_the_sum**2
    diff = square_of_the_sum - sum_of_the_squares

    return diff 


assert type(sumSquareDifference(10)) == int
assert sumSquareDifference(10) == 2640
assert sumSquareDifference(20) == 41230
assert sumSquareDifference(100) == 25164150