// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
                # declare
        prev1= 0
        prev2 = 0
        
        # max sum w/o adjacent elements
        for num in nums:
          temp = prev1
          prev1 = max(num + prev2, prev1)
          prev2 = temp
        
        # return
        return prev1