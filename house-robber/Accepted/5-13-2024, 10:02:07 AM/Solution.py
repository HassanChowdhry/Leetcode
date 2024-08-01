// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        res = [nums[0], nums[1]]

        for i in range(2, n):
            if i-3 < 0:
                curr = nums[i] + res[i-2]
            else:
                curr = nums[i] + max(res[i-2], res[i-3])
            res.append(curr)
        
        return max(res[-1], res[-2])