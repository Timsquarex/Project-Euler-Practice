#Problem 1: Multiples of 3 or 5
def multiplesOf3Or5(number):
    candidate = []
    number = number - 1
    while number != 0:
        if number % 3 == 0 or number % 5 == 0:
            candidate.append(number)
            number -= 1
        else: 
            number -= 1
    
    result = 0 
    for i in range(len(candidate)):
        result += candidate[i]
        
    return result

assert type(multiplesOf3Or5(10)) == int
assert multiplesOf3Or5(49) == 543
assert multiplesOf3Or5(1000) == 233168
assert multiplesOf3Or5(8456) == 16687353
assert multiplesOf3Or5(19564) == 89301183