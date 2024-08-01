// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [float("inf")] * len(nums)
        min_jumps[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                if (i+j) < len(nums):
                    min_jumps[i] = min(min_jumps[i], min_jumps[i+j]+1)
        
        return min_jumps[0]