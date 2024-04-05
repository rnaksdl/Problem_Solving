'''
This method is used to find max value without evaluating all contents of the array.
But it needs to know the length of the array

You give it the length of the array,
it will ask for the first 37% of the array
then it will simply confirm that the value greater than the max of the first 37% of the array is the best bet.

this method is really weirdly explained in a YouTube video.
I'm now sure how I can implement "reject 37% just to get a sense of what's out there" part..
'''


from cmath import infI
from typing import List


class Solution:
    def thirtyseven_percent(self, nums: List[int]) -> int:

        length = input("Enter length of the array:")
        counter = 0
        max = - inf 
        found = False
        while not found:
            if counter <= (length * 0.37):
                current_value = input("Enter more values:")
                if current_value > max:
                    max = current_value
            if counter > (length * 0.37):
                current_value = input("Enter more values:")
                if current_value > max:
                    print(current_value + " is your best bet")
                    return current_value
                
        return current_value