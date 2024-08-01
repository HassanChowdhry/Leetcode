// https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, ceil(c ** (1/2))

        while left <= right:
            reach = (left ** 2) + (right ** 2)
            if reach == c:
                return True
            elif reach > c:
                right -= 1
            elif reach < c:
                left += 1
        
        return False
