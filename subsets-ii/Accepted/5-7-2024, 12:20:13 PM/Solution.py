// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(curr, idx):
            if idx == n:
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtrack(curr, idx+1)
            curr.pop()

            while idx+1 < n and nums[idx]==nums[idx+1]:
                idx+=1
            backtrack(curr, idx+1)
        
        backtrack([], 0)
        return res
