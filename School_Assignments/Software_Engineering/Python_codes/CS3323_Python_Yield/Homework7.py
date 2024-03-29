"""
CS3323 Homework 7 - Python yield
Kyumin Lee 113591341
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def SQUARED_OF_PRIMES():
    num = 2
    while True:
        if is_prime(num):
            yield num ** 2
        num += 1

def S2SP(n):
    primes_squared = SQUARED_OF_PRIMES()
    found_S2SPs = set()
    squares_list = []

    while True:
        # Get the next square of a prime
        ps = next(primes_squared)

        # Temporary list to store new S2SP numbers found in this iteration
        new_S2SPs = []

        # Check combinations with all previously found squares of primes
        for other_ps in squares_list:
            S2SP_num = ps + other_ps
            if S2SP_num > n and S2SP_num not in found_S2SPs:
                new_S2SPs.append(S2SP_num)

        # Add the new S2SP numbers to the set after iteration is complete
        for new_S2SP in new_S2SPs:
            found_S2SPs.add(new_S2SP)
            yield new_S2SP

        squares_list.append(ps)
        
		
def find_20_consecutive_S2SP(start_id):
    S2SP_gen = S2SP(start_id)
    return [next(S2SP_gen) for i in range(20)]

"""
MY_STUDENT_ID = 113591341
print(find_20_consecutive_S2SP(MY_STUDENT_ID))

#OUTPUT:
[113673050, 113643050, 113763578, 113823890, 113673242, 113793770, 113854082, 113944610, 113643770, 113734010, 113824322, 113944850, 114005162, 114095690, 114125882, 113674010, 113764250, 113854562, 113975090, 114035402]
"""