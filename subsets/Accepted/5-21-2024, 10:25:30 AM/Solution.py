// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init variables
        res = []
        n = len(nums)
        
        # run an array adding a num, then calling func, then popping that num
        def backtrack(inner, curr_index):
            res.append(inner)

            for i in range(curr_index, n):
                inner.append(nums[i])
                backtrack(inner.copy(), i+1)
                inner.pop()

        backtrack([], 0)
        return res