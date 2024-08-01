// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        import math
        
        row = []
        for k in range(rowIndex+1):
            row.append(math.comb(rowIndex, k))
        
        return row