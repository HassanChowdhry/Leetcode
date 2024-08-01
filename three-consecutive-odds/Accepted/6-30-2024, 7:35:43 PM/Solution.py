// https://leetcode.com/problems/three-consecutive-odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = 0

        for num in arr:
            if num % 2:
                res += 1                
                if res == 3:
                    return True
            else:
                res = 0
        
        return False
            