// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if num >= curr_sum:
                curr_sum = num
            
            if mx < curr_sum:
                mx = curr_sum
        
        return mx