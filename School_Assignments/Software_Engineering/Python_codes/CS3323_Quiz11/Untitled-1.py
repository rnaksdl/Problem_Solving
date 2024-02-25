"""

USE RECURSION IN PYTHON TO WRITE A PROGRAM THAT GIVEN A POSITIVE INTEGER N, CALCULATES THE SUM OF THE
FIRST N CUBES. SO


SOFCU(1) = 1*1 = 1
SOFCU(2) = 1*1*1 + 2*2*2 = 9
SOFCU(3) = 1*1*1 + 2*2*2 + 3*3*3 = 36

"""

def SOFCU(n):
	if n == 1:
		return 1
	return  n * n * n + SOFCU(n - 1)

print(SOFCU(2))





"""


USE YIELD TO WRITE A PYTHON GENERATOR SOFSQ THAT PRODUCES ALL THE SUMS OF SQUARES. THE FIRST
THREE SOFSQ ARE
1*1(= 1), 1*1+2*2(= 5), 1*1+2*2+3*3(= 14)
YOU SHOULD WRITE ONLY ONE FUNCTION ( GENERATOR ), I.E. YOU SHOULD NOT USE HELPER FUNCTIONS.

"""

def SOFSQ():
	i = 1
	total = 0
	while True:
		yield total
		total += i * i
		i += 1

for i in range(5):
    print(SOFSQ)