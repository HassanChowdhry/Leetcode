// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float("-inf")
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            if total < nums[i]:
                total = nums[i]
            mx = max(total, mx)
        
        return mx