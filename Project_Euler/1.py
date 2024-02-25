'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.


I've solved it with cpp first
#include <iostream>
using namespace std;

int main() {
	int sum = 0;
	for(int i = 1; i < 1000; i++) {
		if(i % 3 == 0 || i % 5 == 0){
			sum += i;	
		}
	}

	cout << sum;

	return 0;
}
'''


from typing import List

class Solution:
	def mutiples_of(self, numbers: List[int], bound) -> int:
		sum = 0
		for i in range(bound):
			for num in numbers:
				if i % num == 0:
					sum += i
					break
		return sum
	
solution = Solution()
print(solution.mutiples_of([3,5], 1000))