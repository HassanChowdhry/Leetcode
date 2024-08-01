// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # init
        nums = sorted(candidates)
        n = len(nums)
        res = []

        # backtrack - keep track of tot n subset and append when total == target
        def backtrack(subset, total, idx):
            if total == target:
                res.append(list(subset))
                return
            if total > target or idx>=n:
                return
            
            subset.append(nums[idx])
            backtrack(subset, total+nums[idx], idx+1)
            subset.pop()

            while idx+1 < n and nums[idx]==nums[idx+1]:
                idx+=1

            backtrack(subset, total, idx+1)
        
        
        backtrack([], 0, 0)
        return res