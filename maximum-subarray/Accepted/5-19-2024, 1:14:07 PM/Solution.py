// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float("-inf")
        curr = 0

        for num in nums:
            curr += num
            if num > curr:
                curr = num
            if curr > m:
                m = curr
        
        return m