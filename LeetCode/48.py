'''
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

class Attempt:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix) - 1):

            # rotating corners
            if i == 0:
                temp = matrix[0][0]
                matrix[0][0] = matrix[-1][0]
                matrix[-1][0] = matrix[-1][-1]
                matrix[-1][-1] = matrix[0][-1]
                matrix[0][-1] = temp

            if i == 1:
                temp = matrix[0][-2]
                matrix[0][-2] = matrix[1][0]
                matrix[1][0] = matrix[-1][1]
                matrix[-1][1] = matrix[-2][-1]
                matrix[-2][-1] = temp
