class attempt1:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        if x < 10:
            return True
        
        num_of_digit = 0
        value_at_digit = 0
        digit = 1

        while(True):
            value_at_digit = x - digit
            if value_at_digit > digit:
                digit *= 10
                num_of_digit += 1
            else:
                break
        
        l_digit = 10**(num_of_digit)
        r_digit = 1
        
        while(l_digit > r_digit):
            if x // l_digit != x % (r_digit * 10):
                return False
            l_digit /= 10
            r_digit *= 10
            
        return True
'''
returns false on '313' ????
the algo is too messy
'''

class attempt2:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        if x < 10:
            return True
        
        num_of_digit = 0
        value_at_digit = 0
        digit = 1

        while(True):
            value_at_digit = x // digit
            if value_at_digit >= 10:
                digit *= 10
                num_of_digit += 1
            else:
                break
        
        l_digit = 10**(num_of_digit)
        r_digit = 1
        
        while(l_digit > r_digit):
            if x // l_digit != x % (r_digit * 10):
                return False
            l_digit /= 10
            r_digit *= 10
            
        return True

'''
returns false on '1001' ???
'''



class Solution1:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Single digit numbers are palindromes
        if x < 10:
            return True
        
        # Calculate the number of digits
        num_of_digit = 0
        temp_x = x
        while temp_x > 0:
            temp_x //= 10
            num_of_digit += 1
        
        # Initialize left and right digit positions
        l_digit = 10**(num_of_digit - 1)
        r_digit = 1
        
        # Compare digits from the left and right
        while l_digit > r_digit:
            left_digit = (x // l_digit) % 10
            right_digit = (x // r_digit) % 10
            
            if left_digit != right_digit:
                return False
            
            l_digit //= 10
            r_digit *= 10
        
        return True
'''
Got some help...
Runtime: 72 ms, faster than 5.08% of Python3 online submissions for Palindrome Number.
Memory Usage: 16.6 MB, less than 64.90% of Python3 online submissions for Palindrome Number.

Not very optimal
'''

class Solution2:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        if x < 10:
            return True
        
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return original == reversed_num
'''
much simpler....
I can't believe I didn't think of comparing original and reversed..
'''