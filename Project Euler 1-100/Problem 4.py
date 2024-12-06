#Problem 4: Largest Palindrome Product
    #we need to find the product of two n-digit numbers
    #we need to check the product of the numbers are palindrome
    #we need to get the largest palindrom product

def palindrome(number):
    candidate = str(number)
    if candidate == candidate[::-1]:
        return True
    else:
        return False

def largestPalindromeProduct(n):
    #upper and lower bounds for n-digit numbers
    upper = 10**n - 1
    lower = 10**(n-1)

    max_palindrome = 0

    for i in range(upper, lower-1, -1): #we need to add step such that the i wil be 99, 98, ..., 10
        for j in range(i, lower-1, -1):
            product = i * j
            if palindrome(product) == True:
                if product > max_palindrome:
                    max_palindrome = product
    
    return max_palindrome

assert type(largestPalindromeProduct(2)) == int 
assert largestPalindromeProduct(2) == 9009
assert largestPalindromeProduct(3) == 906609



