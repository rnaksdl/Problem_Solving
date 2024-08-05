'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

class Solution1:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while True:
            n_str = str(n)
            result = 0
            for c in n_str:
                result += int(c) ** 2

            if result == 1:
                return True
            elif result in visited:
                return False
            
            visited.add(result)
            n = result
            
            
'''
I didn't add "n = result" and got a wrong solution but I fixed it right away.
But initially, I didin't want to use while true loop and was thinking about how to solve it without one.
I failed to do so though.
'''

class Solution2:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
    
