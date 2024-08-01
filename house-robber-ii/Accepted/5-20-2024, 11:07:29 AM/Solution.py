// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        m1, m2, rob1, rob2 = 0, 0, 0, 0

        for n in nums[:-1]:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        m1 = rob2
        
        rob1, rob2 = 0, 0
        for n in nums[1:]:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        m2 = rob2

        return max(m1, m2)