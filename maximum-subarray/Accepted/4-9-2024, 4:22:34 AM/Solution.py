// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')  
        cur = float('-inf')  

        # Iterate through each element in the array
        for n in nums:
            # Update cur to be the maximum of either cur + n or n
            cur = max(cur + n, n)
            # Update ans to be the maximum of ans and cur
            ans = max(ans, cur)
            
        return ans  # Return the maximum sum subarray