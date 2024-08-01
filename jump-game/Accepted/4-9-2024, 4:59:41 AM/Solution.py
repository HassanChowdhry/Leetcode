// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_len = len(nums)
        memo = {}

        @lru_cache(maxsize=None)
        def backtrack(num, idx):
            if idx >= num_len-1:
                return True
            if (num, idx) in memo:
                return memo[(num, idx)]
            
            canJump = False
            for i in range(num, 0, -1):
                if idx+i >= num_len:
                    return True

                curr = nums[idx+i]

                canJump = canJump or backtrack(curr, idx+i)

            memo[(num, idx)] = canJump
            return canJump
        
        return backtrack(nums[0], 0)