// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                in_row = board[i][j]
                in_col = board[j][i]
                
                if in_row in row_set or in_col in col_set:
                    return False

                if in_row.isdigit():
                    row_set.add(in_row)
                if in_col.isdigit():
                    col_set.add(in_col)
        
        for rep in range(3):
            start = rep*3
            b_one_set = set()
            b_two_set = set()
            b_three_set = set()
            for i in range(start, start + 3):
                for j in range(3):
                    b_one = board[i][j]
                    b_two = board[i][j+3]
                    b_three = board[i][j+6]

                    if b_one in b_one_set or b_two in b_two_set or b_three in b_three_set:
                        return False
                    
                    if b_one.isdigit():
                        b_one_set.add(b_one)
                    if b_two.isdigit():
                        b_two_set.add(b_two)
                    if b_three.isdigit():
                        b_three_set.add(b_three)
        
        return True