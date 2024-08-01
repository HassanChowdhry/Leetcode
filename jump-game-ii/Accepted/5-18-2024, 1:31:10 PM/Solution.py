// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        levelEnd = 0
        jump = 1
        maxReach = nums[0]
        goal = len(nums)-1
        
        while levelEnd <= goal:
            if maxReach >= goal:
                return jump

            start = levelEnd+1
            end = maxReach
            for i in range(start, end+1):
                if i+nums[i] >= maxReach:
                    maxReach = nums[i]+i

            jump += 1
            levelEnd = end
        
        return jump
