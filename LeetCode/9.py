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