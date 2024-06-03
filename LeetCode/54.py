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

        # init Left, Right pointers
        L = 0
        R = len(matrix[0])

        # init Top, Bottom pointers
        T = 0
        B = len(matrix)

        # init result list
        result = []

        # iterate like two-pointer problems
        while L < R and T < B:
            
            # sweping top most line
            for i in range(L, R):
                result.append(matrix[T][i])
            # then increment Top
            T += 1

            # sweeping right most line
            for i in range(T, B):
                result.append(matrix[i][R - 1])
            # decrement Right
            R -= 1

            # check if there are more rows, cols to sweep
            if not (L < R and T < B):
                break

            # sweping bottom most line
            for i in range(R - 1, L - 1, -1):
                result.append(matrix[B - 1][i])
            # decrement Bottom
            B -= 1

            # sweping left most line
            for i in range(B - 1, T - 1, -1):
                result.append(matrix[i][L])
            # then increment Left
            L += 1
            
        return result
        
'''
this problem was like two-pointer problem
'''