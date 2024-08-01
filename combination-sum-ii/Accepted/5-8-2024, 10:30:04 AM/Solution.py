// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # init
        nums = sorted(candidates)
        n = len(nums)
        res = []

        # backtrack - keep track of tot n subset and append when total == target
        def backtrack(subset, idx):
            total = sum(subset)
            if total == target:
                res.append(subset.copy())
                return
            if total > target or idx>=n:
                return
            
            subset.append(nums[idx])
            backtrack(subset, idx+1)
            subset.pop()

            while idx+1 < n and nums[idx]==nums[idx+1]:
                idx+=1

            backtrack(subset, idx+1)
        
        
        # backtrack([], 0, 0)
        backtrack([], 0)
        return res