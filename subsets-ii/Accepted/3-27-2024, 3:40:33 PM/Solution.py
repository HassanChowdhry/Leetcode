// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # init variables
        res = []
        nums.sort()
        
        # run an array adding a num, then calling func, then popping that num
        def backtrack(inner, curr_index, list_len):
            if inner not in res:
                res.append(inner.copy())

            for i in range(curr_index, list_len):
                inner.append(nums[i])
                backtrack(inner.copy(), i+1, list_len)
                inner.pop()

        backtrack([], 0, len(nums))
        return res