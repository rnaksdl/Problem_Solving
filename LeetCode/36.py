'''36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in sub_boxes[(row // 3, col // 3)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sub_boxes[(row // 3, col // 3)].add(board[row][col])
            
        return True

'''
collections.defaultdict(set) is hash set

sub_boxes keys are represented like this sub_boxes[(row // 3, col // 3)]
    since there are 3 rows of boxes and 3 cols of boxes
'''