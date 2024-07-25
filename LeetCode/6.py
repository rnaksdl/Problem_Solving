'''
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # edge case where it's just one character
        if numRows == 1: return s

        # init res
        res = ""

        # iter each row
        for r in range(numRows):
            # 2:2, 3:4, 4:6
            increment = 2 * (numRows - 1)

            # iter from r to len(s)
            for i in range(r, len(s), increment):

                # add to result
                res += s[i]

                # for diagonals
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        
        return res
            

'''
I'm going to take a break.
NO screens what so ever.
'''