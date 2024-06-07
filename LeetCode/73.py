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
