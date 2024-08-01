// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen1 = 0
        seen2 = 0

        for num in nums:
            seen1 = ~seen2 & (seen1 ^ num)
            seen2 = ~seen1 & (seen2 ^ num)
        
        return seen1