// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # declare
        res = [[1]]

        # Main - use previus sum
        for row in range(1, rowIndex+1):
            curr_row = [1]

            # calculates for each position
            for i in range(1, row):
                num = res[row - 1][i-1] + res[row - 1][i]
                curr_row.append(num)
            
            curr_row.append(1)
            res.append(curr_row)
        
        # return
        return res[-1]