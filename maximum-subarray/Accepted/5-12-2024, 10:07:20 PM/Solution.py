// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum += num
            curr_sum = max(curr_sum, num)
            mx = max(mx, curr_sum)
        
        return mx