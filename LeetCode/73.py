'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''


class Attempt1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rowWithZero = set()
        colWithZero = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    print(i)
                    rowWithZero.add(i)
                    colWithZero.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rowWithZero and j in colWithZero:
                    matrix[i][j] = 0
'''
if i in rowWithZero and j in colWithZero:

in this line "and" should have been "or"
since we want to change the value when its lying at either row OR col with zero(s).
using "and" would be changing just the 0(s) to 0(s) again.
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # init 2 sets to store which row or col had zero(s)
        rowWithZero = set()
        colWithZero = set()

        # iterate through the whole matrix and find 0's
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                # when you find a 0, add the indeces of row and col to each sets
                if matrix[i][j] == 0:
                    rowWithZero.add(i)
                    colWithZero.add(j)

        # iterate throught the whole matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                # if you're at a row or col with zero, change the value to 0
                if i in rowWithZero or j in colWithZero:
                    matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        firstRow = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        firstRow = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
    
        if firstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
'''
only one extra variable to store info of whether firstRow shoud be zero or not
others are stored in first row or col.
[0][0] stores for the first col.
'''