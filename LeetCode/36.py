'''36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [[set() for _  in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                if num in subgrids[i//3][j//3]:
                    return False
                subgrids[i//3][j//3].add(num)

        return True

  