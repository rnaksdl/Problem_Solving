'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
'''

'''
[1,2,3,4]
[5,6,7,8]
[1,2,3,4]
[5,6,7,8]
[5,6,7,8]
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        L = 0
        R = len(matrix[0])

        T = 0
        B = len(matrix)

        result = []

        while L < R and T < B:
            for i in range(L, R):
                result.append(matrix[T][i])
            T += 1

            for i in range(T, B):
                result.append(matrix[i][R - 1])
            R -= 1

            if not (L < R and T < B):
                break

            for i in range(R - 1, L - 1, -1):
                result.append(matrix[B - 1][i])
            B -= 1

            for i in range(B - 1, T - 1, -1):
                result.append(matrix[i][L])
            L += 1
            
        return result
        
